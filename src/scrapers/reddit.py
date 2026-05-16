"""Reddit scraper implementation."""

import asyncio
import logging
import os
import re
from datetime import datetime, timezone
from typing import Any, List, Optional

import feedparser
import httpx

from .base import BaseScraper
from ..models import ContentItem, RedditConfig, RedditSubredditConfig, RedditUserConfig, SourceType

logger = logging.getLogger(__name__)

REDDIT_BASE = "https://www.reddit.com"
REDDIT_OAUTH_BASE = "https://oauth.reddit.com"
REDDIT_RSS_BASE = "https://www.reddit.com/r"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0.0.0 Safari/537.36"
)
REDDIT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": f"{REDDIT_BASE}/",
}
MAX_COMMENT_CONCURRENCY = 2


class RedditScraper(BaseScraper):
    """Scraper for Reddit posts and comments."""

    def __init__(self, config: RedditConfig, http_client: httpx.AsyncClient):
        super().__init__(config.model_dump(), http_client)
        self.reddit_config = config
        self._comment_semaphore = asyncio.Semaphore(MAX_COMMENT_CONCURRENCY)
        self._oauth_token: Optional[str] = None
        self._use_rss = False

    async def _ensure_oauth(self) -> bool:
        if self._oauth_token:
            return True
        client_id = os.getenv(self.reddit_config.client_id_env) if self.reddit_config.client_id_env else ""
        client_secret = os.getenv(self.reddit_config.client_secret_env) if self.reddit_config.client_secret_env else ""
        if not client_id or not client_secret:
            return False
        try:
            resp = await self.client.post(
                "https://www.reddit.com/api/v1/access_token",
                auth=(client_id, client_secret),
                data={"grant_type": "client_credentials"},
                headers={"User-Agent": self.reddit_config.user_agent},
            )
            resp.raise_for_status()
            self._oauth_token = resp.json().get("access_token")
            if self._oauth_token:
                logger.info("Reddit OAuth token acquired")
                return True
        except Exception as e:
            logger.warning("Reddit OAuth failed: %s", e)
        return False

    def _get_headers(self) -> dict:
        if self._oauth_token:
            return {
                "Authorization": f"Bearer {self._oauth_token}",
                "User-Agent": self.reddit_config.user_agent,
            }
        return REDDIT_HEADERS

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.get("enabled", True):
            return []

        if not await self._ensure_oauth():
            self._use_rss = True
            logger.info("Reddit: no OAuth credentials, falling back to RSS feeds")

        tasks = []
        for sub_cfg in self.reddit_config.subreddits:
            if sub_cfg.enabled:
                tasks.append(self._fetch_subreddit(sub_cfg, since))
        for user_cfg in self.reddit_config.users:
            if user_cfg.enabled:
                tasks.append(self._fetch_user(user_cfg, since))

        if not tasks:
            return []

        results = await asyncio.gather(*tasks, return_exceptions=True)
        items = []
        for result in results:
            if isinstance(result, Exception):
                logger.warning("Error fetching Reddit source: %s", result)
            elif isinstance(result, list):
                items.extend(result)
        return items

    def _base_url(self) -> str:
        return REDDIT_OAUTH_BASE if self._oauth_token else REDDIT_BASE

    async def _fetch_subreddit(self, cfg: RedditSubredditConfig, since: datetime) -> List[ContentItem]:
        if self._use_rss:
            return await self._fetch_subreddit_rss(cfg, since)
        return await self._fetch_subreddit_api(cfg, since)

    async def _fetch_user(self, cfg: RedditUserConfig, since: datetime) -> List[ContentItem]:
        if self._use_rss:
            logger.info("Reddit: user feed not available via RSS, skipping %s", cfg.username)
            return []
        return await self._fetch_user_api(cfg, since)

    async def _fetch_subreddit_rss(self, cfg: RedditSubredditConfig, since: datetime) -> List[ContentItem]:
        url = f"{REDDIT_RSS_BASE}/{cfg.subreddit}/.rss"
        try:
            resp = await self.client.get(url, headers=REDDIT_HEADERS, follow_redirects=True, timeout=15)
            resp.raise_for_status()
            feed = feedparser.parse(resp.text)
        except Exception as e:
            logger.warning("Reddit RSS failed for r/%s: %s", cfg.subreddit, e)
            return []

        items = []
        for entry in feed.entries[:cfg.fetch_limit]:
            published = entry.get("published_parsed") or entry.get("updated_parsed")
            if not published:
                continue
            created = datetime(*published[:6], tzinfo=timezone.utc)
            if created < since:
                continue

            link = entry.get("link", "")
            content = entry.get("summary", entry.get("description", ""))
            items.append(ContentItem(
                id=self._generate_id("reddit", "subreddit", entry.get("id", link)),
                source_type=SourceType.REDDIT,
                title=entry.get("title", ""),
                url=link,
                content=content,
                author=entry.get("author", "unknown"),
                published_at=created,
                metadata={"subreddit": cfg.subreddit, "score": 0, "num_comments": 0},
            ))
        logger.info("Reddit RSS: fetched %d items from r/%s", len(items), cfg.subreddit)
        return items

    async def _fetch_subreddit_api(self, cfg: RedditSubredditConfig, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.fetch_limit, 100), "raw_json": 1}
        if cfg.sort in ("top", "controversial"):
            params["t"] = cfg.time_filter
        if self._oauth_token:
            params["sr_detail"] = "true"

        url = f"{REDDIT_BASE}/r/{cfg.subreddit}/{cfg.sort}.json"
        data = await self._reddit_get(url, params)
        if not data:
            return []

        posts = [child["data"] for child in data.get("data", {}).get("children", [])
                 if child.get("kind") == "t3"]
        return await self._process_posts(
            posts, since, "subreddit", cfg.subreddit, cfg.min_score
        )

    async def _fetch_user_api(self, cfg: RedditUserConfig, since: datetime) -> List[ContentItem]:
        params = {"limit": min(cfg.fetch_limit, 100), "sort": cfg.sort, "raw_json": 1}
        url = f"{REDDIT_BASE}/user/{cfg.username}/submitted.json"
        data = await self._reddit_get(url, params)
        if not data:
            return []

        posts = [child["data"] for child in data.get("data", {}).get("children", [])
                 if child.get("kind") == "t3"]
        return await self._process_posts(
            posts, since, "user", cfg.username, min_score=0
        )

    async def _process_posts(
        self,
        posts: list,
        since: datetime,
        subtype: str,
        source_name: str,
        min_score: int,
    ) -> List[ContentItem]:
        valid_posts = []
        comment_tasks = []
        fetch_comments = self.reddit_config.fetch_comments

        for post in posts:
            created = datetime.fromtimestamp(post.get("created_utc", 0), tz=timezone.utc)
            if created < since:
                continue
            if post.get("score", 0) < min_score:
                continue
            valid_posts.append(post)
            if fetch_comments > 0:
                comment_tasks.append(
                    self._fetch_comments(post.get("subreddit", ""), post["id"])
                )
            else:
                comment_tasks.append(self._empty_comments())

        if not valid_posts:
            return []

        all_comments = await asyncio.gather(*comment_tasks, return_exceptions=True)

        items = []
        for post, comments in zip(valid_posts, all_comments):
            if isinstance(comments, Exception):
                comments = []
            item = self._parse_post(post, comments, subtype)
            if item:
                items.append(item)
        return items

    @staticmethod
    async def _empty_comments() -> List[dict]:
        return []

    async def _fetch_comments(self, subreddit: str, post_id: str) -> List[dict]:
        fetch_limit = self.reddit_config.fetch_comments
        url = f"{self._base_url()}/r/{subreddit}/comments/{post_id}"
        params = {"limit": fetch_limit, "depth": 1, "sort": "top", "raw_json": 1}

        async with self._comment_semaphore:
            data = await self._reddit_get(url, params)
        if not data or not isinstance(data, list) or len(data) < 2:
            return []

        comments = []
        for child in data[1].get("data", {}).get("children", []):
            if child.get("kind") != "t1":
                continue
            c = child["data"]
            if c.get("body") and not c.get("distinguished") == "moderator":
                comments.append(c)

        comments.sort(key=lambda c: c.get("score", 0), reverse=True)
        return comments[:fetch_limit]

    def _parse_post(self, post: dict, comments: List[dict], subtype: str) -> Optional[ContentItem]:
        post_id = post["id"]
        title = post.get("title", "")
        is_self = post.get("is_self", False)
        subreddit = post.get("subreddit", "")
        discussion_url = f"https://www.reddit.com{post.get('permalink', '')}"

        # For link posts, use the external URL; for self posts, use the discussion URL
        url = discussion_url if is_self else post.get("url", discussion_url)

        author = post.get("author", "unknown")
        created = datetime.fromtimestamp(post.get("created_utc", 0), tz=timezone.utc)

        # Build content
        parts = []
        if post.get("selftext"):
            text = post["selftext"]
            if len(text) > 1500:
                text = text[:1497] + "..."
            parts.append(text)

        if comments:
            parts.append("\n--- Top Comments ---")
            for c in comments:
                commenter = c.get("author", "anon")
                body = c.get("body", "")
                body = body.strip()
                if len(body) > 500:
                    body = body[:497] + "..."
                score = c.get("score", 0)
                parts.append(f"[{commenter} ({score} pts)]: {body}")

        content = "\n\n".join(parts)

        return ContentItem(
            id=self._generate_id("reddit", subtype, post_id),
            source_type=SourceType.REDDIT,
            title=title,
            url=url,
            content=content,
            author=author,
            published_at=created,
            metadata={
                "score": post.get("score", 0),
                "upvote_ratio": post.get("upvote_ratio"),
                "num_comments": post.get("num_comments", 0),
                "subreddit": subreddit,
                "is_self": is_self,
                "flair": post.get("link_flair_text"),
                "discussion_url": discussion_url,
            },
        )

    async def _reddit_get(self, url: str, params: dict) -> Optional[Any]:
        try:
            headers = self._get_headers()
            response = await self.client.get(
                url,
                params=params,
                headers=headers,
                follow_redirects=True,
            )
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 5))
                logger.warning("Reddit rate limited, retrying after %ds", retry_after)
                await asyncio.sleep(retry_after)
                response = await self.client.get(
                    url,
                    params=params,
                    headers=headers,
                    follow_redirects=True,
                )
            if response.status_code == 403:
                logger.warning("Reddit blocked request for %s (403). Try adding Reddit OAuth credentials (client_id/client_secret) in config.", url)
                return None
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.warning("Reddit request failed for %s: %s", url, e)
            return None
