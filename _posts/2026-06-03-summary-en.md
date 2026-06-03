---
layout: default
title: "Horizon Summary: 2026-06-03 (EN)"
date: 2026-06-03
lang: en
---

> From 51 items, 17 important content pieces were selected

---

1. [Hackers Exploit Meta AI Bot to Hijack Instagram Accounts](#item-1) ⭐️ 9.0/10
2. [AI beats law professors in Stanford study](#item-2) ⭐️ 8.0/10
3. [Trump Signs Scaled-Back AI Executive Order](#item-3) ⭐️ 8.0/10
4. [Microsoft Unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs](#item-4) ⭐️ 8.0/10
5. [MiniMax Introduces Sparse Attention for 1M Context](#item-5) ⭐️ 8.0/10
6. [Backprop destroys V1 brain alignment in one epoch](#item-6) ⭐️ 8.0/10
7. [Top LightGBM Feature by Importance Degrades Performance](#item-7) ⭐️ 8.0/10
8. [MLE-Bench Gains Largely from Better Models, Not Algorithms](#item-8) ⭐️ 8.0/10
9. [Use Nvidia GPU VRAM as swap on Linux](#item-9) ⭐️ 7.0/10
10. [CT Scans Reveal BYD's Build Quality and Vertical Integration](#item-10) ⭐️ 7.0/10
11. [User leaves Gmail over intrusive AI features](#item-11) ⭐️ 7.0/10
12. [Hugging Face Revives PapersWithCode for CVPR 2026](#item-12) ⭐️ 7.0/10
13. [Routing-Based Real-Time Multilingual ASR with Rolling Buffers](#item-13) ⭐️ 7.0/10
14. [Seattle Surveillance Walking Tour Sparks Privacy Debate](#item-14) ⭐️ 6.0/10
15. [HP Revives Classic HP-16C Programmer's Calculator](#item-15) ⭐️ 6.0/10
16. [Datasette Agent MicroPython Sandbox Alpha Released](#item-16) ⭐️ 6.0/10
17. [SFT vs RL for Fine-Tuning Reasoning LLMs](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Hackers Exploit Meta AI Bot to Hijack Instagram Accounts](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/#atom-everything) ⭐️ 9.0/10

Hackers successfully took over high-profile Instagram accounts by simply asking Meta's AI support chatbot to change the linked email address, bypassing standard account recovery procedures. This incident exposes a critical design flaw in integrating AI chatbots with sensitive account management functions, highlighting the urgent need for robust guardrails to prevent prompt injection and unauthorized actions. The hackers used VPNs to mask their locations and asked the bot to link a new email to the target account, providing the username and attacker's email. The bot complied without requiring additional verification, enabling one-shot account takeovers.

rss · Simon Willison · Jun 1, 21:14

**Background**: Prompt injection is a cybersecurity attack where malicious inputs trick AI models into ignoring instructions or performing unintended actions. In this case, Meta's AI support bot was given direct access to account recovery tools, allowing it to change email addresses without proper authentication checks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/">Hackers Simply Asked Meta AI to Give Them Access to High-Profile Instagram Accounts. It Worked</a></li>
<li><a href="https://www.engadget.com/2185225/meta-ai-support-chatbot-made-it-ridiculously-easy-for-hackers-to-take-over-instagram-accounts/">Meta's AI support chatbot made it ridiculously easy for hackers to take over Instagram accounts - Engadget</a></li>
<li><a href="https://arstechnica.com/ai/2026/06/meta-ai-support-chatbot-gave-hackers-access-to-notable-instagram-accounts/">Hackers duped Meta AI support chatbot to steal celebrity Instagram accounts - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#Meta`, `#account takeover`, `#prompt injection`

---

<a id="item-2"></a>
## [AI beats law professors in Stanford study](https://law.stanford.edu/press/ai-outperforms-law-professors-in-stanford-law-study/) ⭐️ 8.0/10

A Stanford Law study found that AI-generated answers to first-year contracts-law questions were preferred by law professors over their own colleagues' answers. This suggests AI could serve as an effective tutor for law students, potentially lowering the cost of legal education, while also raising questions about AI's role in legal practice. The study involved only 16 professors, leading to high variance and concerns about statistical power, as noted by community commenters.

hackernews · berlianta · Jun 2, 23:43 · [Discussion](https://news.ycombinator.com/item?id=48377761)

**Background**: Large language models (LLMs) like GPT-4 have shown promise in legal reasoning tasks, but their ability to handle nuanced legal questions has been debated. This study specifically tested LLMs as tutors for law students, not as replacements for lawyers.

<details><summary>References</summary>
<ul>
<li><a href="https://practicesource.com/ai-outperforms-law-professors-in-new-stanford-law-study-by-law-professor-julian-nyarko/">AI Outperforms Law Professors in new Stanford Law Study by Law ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48377761">AI Outperforms Law Professors in Stanford Law Study | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters raised methodological concerns, including small sample size and high variance, and noted that the study focused on tutoring rather than replacing lawyers. Some questioned whether students can effectively prompt LLMs without domain knowledge.

**Tags**: `#AI`, `#legal`, `#education`, `#LLM`, `#research`

---

<a id="item-3"></a>
## [Trump Signs Scaled-Back AI Executive Order](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389) ⭐️ 8.0/10

On June 2, 2026, President Trump signed an executive order requiring AI companies to voluntarily submit powerful new models for government review 30 days before public release. This order represents a significant but cautious step in federal AI regulation, potentially shaping how the U.S. government oversees advanced AI development while balancing industry concerns. The review period was reduced from an earlier draft's 90 days to 30 days, and the order also directs the Justice Department to pursue criminal cases against individuals who misuse AI.

hackernews · _alternator_ · Jun 2, 16:40 · [Discussion](https://news.ycombinator.com/item?id=48372628)

**Background**: The executive order, titled 'Promoting Advanced Artificial Intelligence Innovation and Security,' aims to unify AI oversight at the federal level and reduce patchwork state regulations. It follows weeks of reversals and negotiations with industry officials who had called earlier provisions too onerous.

<details><summary>References</summary>
<ul>
<li><a href="https://www.opb.org/article/2026/06/02/trumps-new-ai-safety-order-seeks-voluntary-review-of-new-models/">Trump signs AI safety order seeking voluntary review of new ...</a></li>
<li><a href="https://deadline.com/2026/06/trump-ai-executive-order-1236938859/">Trump Signs AI Executive Order That Includes Review Period ...</a></li>
<li><a href="https://www.usatoday.com/story/news/politics/2026/06/02/trump-ai-order-artificial-intelligence-technology/90370746007/">Trump signs AI order that seeks access to new models before ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the voluntary nature of the review, with some viewing it as a step toward mandatory restrictions. Others noted the reduction from 90 to 30 days as a concession to industry, while still questioning the effectiveness of voluntary compliance.

**Tags**: `#AI regulation`, `#executive order`, `#government policy`, `#AI safety`, `#tech industry`

---

<a id="item-4"></a>
## [Microsoft Unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 8.0/10

Microsoft announced two new text LLMs: MAI-Thinking-1, a 1-trillion-parameter reasoning model with 35 billion active parameters, and MAI-Code-1-Flash, a 137-billion-parameter code model with 5 billion active parameters, rolling out to GitHub Copilot in VS Code. These models represent Microsoft's push to develop competitive in-house AI without relying on OpenAI, with claims that MAI-Thinking-1 is preferred over Anthropic's Sonnet 4.6 in blind evaluations, potentially reshaping the AI model landscape. Both models use a Mixture-of-Experts (MoE) architecture, with MAI-Thinking-1 having a 256,000-token context window. Microsoft states they were trained on clean, commercially licensed data without distillation from third-party models, though the technical paper reveals the training data includes a proprietary web crawl and Common Crawl.

rss · Simon Willison · Jun 2, 22:21

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate human-like text. Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling high performance with lower computational cost. GitHub Copilot is Microsoft's AI-powered code completion tool integrated into VS Code.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">Introducing MAI - Thinking - 1 | Microsoft AI</a></li>
<li><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">Introducing MAI-Code-1-Flash | Microsoft AI</a></li>
<li><a href="https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm">Microsoft Build 2026: MAI - Thinking - 1 Is First In-House Reasoning...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the models' performance, noting that MAI-Code-1-Flash's SWE-bench score (51%) is only slightly better than the much smaller Qwen3.6-35B-A3B (49.5%). Some criticized Microsoft for comparing against the outdated Claude Haiku rather than stronger models like Sonnet or Opus.

**Tags**: `#LLM`, `#Microsoft`, `#AI`, `#reasoning`, `#code generation`

---

<a id="item-5"></a>
## [MiniMax Introduces Sparse Attention for 1M Context](https://www.reddit.com/r/MachineLearning/comments/1tvameq/minimax_dropped_a_new_attention_architecture_n/) ⭐️ 8.0/10

MiniMax has released the M3 model featuring a novel attention architecture called MiniMax Sparse Attention (MSA), which uses a KV outer gather Q approach to efficiently scale context windows to 1 million tokens. This breakthrough addresses the quadratic complexity bottleneck of standard attention, enabling long-context models with significantly lower compute cost, which could accelerate research and applications in areas like long-document understanding and multi-turn agents. MSA achieves 4× faster execution than Flash-Sparse-Attention, reduces per-token compute to 1/20th at full 1M context, and delivers 9× prefilling and 15× decoding speedups. The M3 model is also the first open-weight model combining frontier coding, 1M context, and native multimodality.

reddit · r/MachineLearning · /u/superintelligence03 · Jun 3, 01:26

**Background**: Standard transformer attention has O(n²) memory and compute complexity with respect to sequence length, making long contexts prohibitively expensive. Sparse attention methods reduce this cost by only attending to a subset of tokens, but often sacrifice recall or hardware efficiency. MSA restructures memory access patterns to keep reads contiguous and fetch each KV block exactly once, achieving hardware-efficient sparse attention.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/minimax-m3-complete-guide/">MiniMax M3: Complete Guide to the Open-Weight Frontier Model ...</a></li>
<li><a href="https://lushbinary.com/blog/minimax-m3-developer-guide-benchmarks-pricing-msa-architecture/">MiniMax M3 Developer Guide: Benchmarks & Pricing | Lushbinary</a></li>
<li><a href="https://felloai.com/minimax-m3/">MiniMax M3 Specs, Benchmarks, and Pricing (2026)</a></li>

</ul>
</details>

**Discussion**: The Reddit community is impressed by the technical details and performance gains, with many noting the clever hardware-level optimization. Some users are eager to see the open-weight release and technical report promised within ten days, while others question how MSA compares to other sparse attention methods in practice.

**Tags**: `#attention mechanism`, `#long context`, `#efficiency`, `#transformer`, `#MiniMax`

---

<a id="item-6"></a>
## [Backprop destroys V1 brain alignment in one epoch](https://www.reddit.com/r/MachineLearning/comments/1tupu9z/backpropagation_destroys_v1_brain_alignment_in/) ⭐️ 8.0/10

A new study shows that backpropagation reduces V1 brain alignment by 90% after just one epoch of training on CIFAR-10, while predictive coding and STDP preserve alignment much better. This reveals a fundamental trade-off between global error signals and neural alignment, suggesting that biologically plausible learning rules may be necessary for building brain-like representations in early visual cortex. The study tracked RSA alignment at 8 checkpoints across 5 seeds, finding that backprop drops V1 alignment from r=0.102 to 0.011 (p=0.031), while predictive coding and STDP only drop 25-31% and stabilize. Cohen's d > 5 for PC/STDP vs BP.

reddit · r/MachineLearning · /u/ConfusionSpiritual19 · Jun 2, 12:43

**Background**: Representational Similarity Analysis (RSA) measures how similarly a neural network and the brain represent stimuli. V1 is the primary visual cortex, the earliest stage of visual processing. Backpropagation uses global error signals, while predictive coding and STDP rely on local learning rules thought to be more biologically plausible.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30556">Supervised Training Rapidly Degrades Early Visual Cortex Alignment ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Predictive_coding">Predictive coding - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity">Spike-timing-dependent plasticity - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights the rigor of the study (multiple seeds, checkpoints, Cohen's d > 5) and the trade-off between global error and early-layer alignment. Some commenters wonder if deeper architectures show the same pattern more slowly.

**Tags**: `#backpropagation`, `#brain alignment`, `#predictive coding`, `#STDP`, `#neuroscience`

---

<a id="item-7"></a>
## [Top LightGBM Feature by Importance Degrades Performance](https://www.reddit.com/r/MachineLearning/comments/1tu0y14/why_our_1_lightgbm_feature_by_importance_made/) ⭐️ 8.0/10

A case study from Flyback shows that LightGBM's top feature by importance, a Bayesian target encoder, actually increased test MAPE by 0.28 percentage points and failed to generalize due to overfitting on irreducible label variance. This highlights a common pitfall in gradient boosting where high feature importance does not guarantee improved generalization, emphasizing the need for rigorous ablation studies to validate feature engineering. The ablation used 4 seeds × 3 variants, and the between-variant delta was 7 times the within-variant standard deviation, confirming the feature's negative impact was statistically significant.

reddit · r/MachineLearning · /u/Nj-yeti · Jun 1, 18:20

**Background**: Feature importance in tree-based models like LightGBM measures how often a feature is used for splitting. However, a feature can rank high by importance while actually hurting generalization if it captures noise or label variance that does not generalize to new data. Ablation studies, where features are removed to measure their impact, help detect such issues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datasciencebase.com/supervised-ml/algorithms/gradient-boosting/LightGBM/common-mistakes/">Common Mistakes & Best Practices for LightGBM - DataScienceBase</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ablation_(artificial_intelligence)">Ablation (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://mattmotoki.github.io/blog/beta-target-encoding/">Beta Target Encoding | Matt Motoki</a></li>

</ul>
</details>

**Tags**: `#LightGBM`, `#feature importance`, `#overfitting`, `#gradient boosting`, `#ablation study`

---

<a id="item-8"></a>
## [MLE-Bench Gains Largely from Better Models, Not Algorithms](https://www.reddit.com/r/MachineLearning/comments/1ttu47l/how_much_of_mlebenchs_gains_are_the_algorithm_vs/) ⭐️ 8.0/10

A controlled study using the new FML-Bench benchmark shows that the dramatic performance gains on MLE-Bench (from 30% to 80% over two years) are mostly due to better base models and increased search budget, not algorithmic improvements. When controlling for these factors, the older AIDE algorithm matches modern agent systems. This finding challenges the perceived rapid algorithmic progress in ML agent benchmarks, suggesting that reported gains may be inflated by confounding factors. It underscores the need for controlled evaluations to separate model improvements from algorithmic innovations. FML-Bench unifies code editing agents, step definitions, and validation/test splits to isolate algorithmic efficiency. The study used the same step budget and models to compare AIDE (two years old) with modern agents, finding no significant difference in performance on novel tasks.

reddit · r/MachineLearning · /u/Educational_Strain_3 · Jun 1, 14:34

**Background**: MLE-Bench is a benchmark from OpenAI that evaluates AI agents on 75 Kaggle-style machine learning engineering tasks. Over the past two years, reported scores have risen sharply, but it was unclear whether this reflected true algorithmic progress or improvements in underlying models and evaluation methodology. FML-Bench is a new benchmark designed to control for these factors by focusing on fundamental ML research tasks and using a unified evaluation framework.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/mle-bench">GitHub - openai/mle-bench: MLE-bench is a benchmark for measuring how well AI agents perform at machine learning engineering · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2410.07095">[2410.07095] MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering</a></li>
<li><a href="https://arxiv.org/abs/2510.10472">[2510.10472] FML-bench: Benchmarking Machine Learning Agents ... Images GitHub - qrzou/FML-bench: FML-bench FML-bench: A Benchmark for Automatic ML Research Agents ... qrzou/FML-bench | DeepWiki A Benchmark for Automatic ML Research Agents Highlighting the... FML-bench: Automated ML Research Benchmark FML-bench Tests AI Agents on Real ML Research ... - Medium</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion largely agrees with the analysis, with many commenters noting that overfitting to MLE-Bench is a real concern. Some suggest that the field should adopt more rigorous controlled experiments like FML-Bench to avoid conflating model scaling with algorithmic progress.

**Tags**: `#machine learning`, `#benchmarking`, `#AI research`, `#evaluation`

---

<a id="item-9"></a>
## [Use Nvidia GPU VRAM as swap on Linux](https://github.com/c0dejedi/nbd-vram) ⭐️ 7.0/10

A developer released a tool called nbd-vram that allows Linux users to repurpose Nvidia GPU VRAM as swap space, effectively using idle VRAM to relieve memory pressure. This is particularly useful for laptops with soldered RAM and no upgrade path, as it can triple addressable memory on systems with limited RAM. It also provides a novel way to utilize idle GPU VRAM, which is often underutilized when not running AI models. The tool uses a daemon that allocates VRAM via the CUDA driver API and serves it as a block device using the NBD (Network Block Device) protocol over a Unix socket. Sequential throughput is about 1.3 GB/s on an RTX 3070 Laptop GPU, which is slower than NVMe swap but may have lower latency.

hackernews · tanelpoder · Jun 2, 22:55 · [Discussion](https://news.ycombinator.com/item?id=48377404)

**Background**: Swap space on Linux is used to extend available memory by moving less frequently used data to a storage device, typically a disk or SSD. GPU VRAM is high-bandwidth memory primarily used for graphics and compute tasks, but often sits idle when not running demanding applications. This tool bridges the gap by treating VRAM as a fast swap device.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/c0dejedi/nbd-vram">GitHub - c0deJedi/nbd- vram : Use your NVIDIA GPU 's VRAM as swap ...</a></li>
<li><a href="https://wiki.archlinux.org/title/Swap_on_video_RAM">Swap on video RAM - ArchWiki</a></li>
<li><a href="https://wpnews.pro/news/use-your-nvidia-gpu-s-vram-as-swap-space-on-linux">Use your Nvidia GPU 's VRAM as swap space on Linux — Web Pulse</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights mixed sentiment: some see it as a niche but useful idea for laptops with soldered RAM, while others point out performance trade-offs, noting that NVMe swap can be faster. Concerns about VRAM backpressure and potential crashes under Wayland were also raised, along with historical references to similar approaches using phram or OpenCL.

**Tags**: `#Linux`, `#GPU`, `#swap`, `#VRAM`, `#performance`

---

<a id="item-10"></a>
## [CT Scans Reveal BYD's Build Quality and Vertical Integration](https://www.lumafield.com/scan-of-the-month/byd) ⭐️ 7.0/10

Lumafield published CT scans of BYD car parts, including a key fob, control arm, and battery pack, revealing detailed internal structures and build quality. The analysis highlights BYD's extensive vertical integration, from lithium mining to finished vehicles. This analysis challenges negative perceptions of Chinese manufacturing by demonstrating BYD's high-quality components and cost control through vertical integration. It provides rare technical insight into a rapidly growing EV maker that now rivals Tesla and Ford in scale. The CT scans show that BYD produces approximately 75% of its components in-house, compared to Ford's 25%. The key fob contains a mechanical backup key that pulls out, not hinged as initially described, and the control arms and subframes appear heavy-duty and well-engineered.

hackernews · viasfo · Jun 2, 20:30 · [Discussion](https://news.ycombinator.com/item?id=48375824)

**Background**: Industrial CT scanning uses X-rays to create 3D images of objects' internal structures, commonly used in automotive and aerospace for quality control. BYD is a Chinese EV manufacturer known for its vertical integration strategy, producing batteries, motors, and electronics in-house, which helps reduce costs and ensure supply chain control.

<details><summary>References</summary>
<ul>
<li><a href="https://evboosters.com/ev-charging-news/the-blueprint-of-an-ev-empire-how-byd-built-global-dominance-through-vertical-integration/">The blueprint of an EV empire: how BYD built global dominance ...</a></li>
<li><a href="https://news.gm.com/home.detail.html/Pages/topic/us/en/2025/jul/0715-GM-CT-scanning-vehicle-manufacturing-quality.html">How GM uses CT scanning to boost vehicle manufacturing quality</a></li>
<li><a href="https://www.nelpretech.com/blog/10-frequently-asked-questions-about-industrial-ct-scanning">Industrial CT Scanning FAQs: Capabilities, Limitations & Applications</a></li>

</ul>
</details>

**Discussion**: Commenters generally praised BYD's build quality, with one automotive technician noting that components like control arms and subframes are 'heavy duty' and contradict the 'Chinese car bad' narrative. A BYD owner corrected a detail about the key fob's mechanical backup key, while others compared BYD's vertical integration to Ford and Tesla, and shared links to related teardown videos.

**Tags**: `#BYD`, `#EV`, `#manufacturing`, `#CT scan`, `#automotive`

---

<a id="item-11"></a>
## [User leaves Gmail over intrusive AI features](https://moddedbear.com/gmail-thinks-im-stupid-so-i-left) ⭐️ 7.0/10

A user announced they left Gmail due to intrusive AI features like smart replies and email summarization, and switched to Fastmail. The post sparked a large discussion on Hacker News with 681 points and 411 comments. This reflects growing user frustration with AI overreach in email services and a desire for more control and privacy. It highlights the demand for alternatives like Fastmail that offer similar features without intrusive AI. The user criticized Gmail's AI suggestions for being too large and unnecessary, such as a full point-by-point response that didn't fit in the preview box. Fastmail was praised for its speed, privacy features like masked emails, and instant performance.

hackernews · speckx · Jun 2, 19:27 · [Discussion](https://news.ycombinator.com/item?id=48375016)

**Background**: Gmail's Smart Reply uses AI to suggest short replies based on email context, while newer features like AI summarization generate longer responses. Fastmail is a paid email service known for privacy, speed, and features like masked emails that protect user identity. Many users are seeking alternatives as AI becomes more pervasive in everyday tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fastmail">Fastmail - Wikipedia</a></li>
<li><a href="https://www.fastmail.com/features/">Better features - Fastmail</a></li>
<li><a href="https://workspace.google.com/features/smart-reply/">Smart Reply for Email Messages in Gmail | Google Workspace</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with the sentiment, criticizing AI-generated email replies as unnecessary for native speakers and praising Fastmail's speed and privacy. Some noted that even useful features like one-click simple replies are acceptable, but full AI-generated responses feel intrusive.

**Tags**: `#email`, `#AI`, `#privacy`, `#user experience`, `#Fastmail`

---

<a id="item-12"></a>
## [Hugging Face Revives PapersWithCode for CVPR 2026](https://www.reddit.com/r/MachineLearning/comments/1tukrf4/browse_cvpr_2026_papers_on_paperswithcode_p/) ⭐️ 7.0/10

Hugging Face's open-source team has revived PapersWithCode as paperswithcode.co, now adding conference support to browse CVPR 2026 papers with associated code, GitHub links, and Hugging Face artifacts. This revival restores a critical resource for the AI community after Meta retired the original PapersWithCode in July 2025, enabling researchers to easily find and reproduce state-of-the-art results from top conferences. The platform indexes all CVPR 2026 papers with arXiv IDs, categorizes them by task, and tags them with linked GitHub repositories, project pages, Hugging Face models, and evaluation results. It also supports browsing Oral and Spotlight papers.

reddit · r/MachineLearning · /u/NielsRogge · Jun 2, 08:32

**Background**: PapersWithCode was a widely-used platform that linked research papers to code implementations and benchmark leaderboards. Meta retired the original site in July 2025, leaving a gap that Hugging Face's community-driven revival aims to fill.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/spaces/huggingface/paperswithcode">Paperswithcode - a Hugging Face Space by huggingface</a></li>
<li><a href="https://www.codesota.com/papers-with-code">Papers With Code Alternative: SOTA Leaderboards and Archived ...</a></li>

</ul>
</details>

**Discussion**: The Reddit community expressed strong support for the revival, praising the quick addition of conference features and the platform's utility. Some users requested support for additional conferences and improved search functionality.

**Tags**: `#CVPR`, `#PapersWithCode`, `#Hugging Face`, `#Computer Vision`, `#Open Source`

---

<a id="item-13"></a>
## [Routing-Based Real-Time Multilingual ASR with Rolling Buffers](https://www.reddit.com/r/MachineLearning/comments/1ttwfuy/realtime_multilingual_asr_using_rolling_buffers/) ⭐️ 7.0/10

Researchers at Gladia have developed a routing-based system for real-time multilingual ASR that uses small monolingual models (~100M parameters each) instead of a single large multilingual model, achieving ~13% WER on inter-utterance code-switching benchmarks. This approach offers a practical alternative to large multilingual models, enabling real-time transcription on local hardware with lower latency and competitive accuracy, which is crucial for applications like live captioning and voice assistants. The system uses Zipformer for streaming transcription, Silero VAD for speech boundary detection, and SpeechBrain for language identification, with a rolling buffer that rolls back to the last speech boundary upon language switch detection.

reddit · r/MachineLearning · /u/JeanMichelRanu · Jun 1, 15:53

**Background**: Multilingual automatic speech recognition (ASR) typically relies on large models that cover many languages, but these models are often too large for real-time local deployment and struggle with code-switching. This work proposes routing audio segments to smaller monolingual models based on language identification, reducing model size and improving latency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2310.11230">Zipformer : A faster and better encoder for automatic speech recognition</a></li>
<li><a href="https://dev.to/jlq/building-real-time-multilingual-asr-with-code-switching-3561">Building real-time multilingual ASR with code-switching</a></li>

</ul>
</details>

**Tags**: `#ASR`, `#multilingual`, `#real-time`, `#machine learning`, `#speech recognition`

---

<a id="item-14"></a>
## [Seattle Surveillance Walking Tour Sparks Privacy Debate](https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/) ⭐️ 6.0/10

A 2020 article titled 'A walking tour of surveillance infrastructure in Seattle' provides a detailed exploration of the city's surveillance cameras and their social implications, sparking debate on privacy and policing. This analysis highlights the growing ubiquity of surveillance in urban environments and raises critical questions about privacy, social control, and the balance between safety and civil liberties. The article describes various types of cameras and their capabilities, including those that can detect 'abnormal' behavior, and critiques the language used to describe surveillance, which some commenters found overly academic.

hackernews · eustoria · Jun 2, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48369980)

**Background**: Surveillance infrastructure in cities like Seattle includes public and private cameras used for law enforcement and traffic monitoring. The debate often centers on the trade-off between security and privacy, especially as technology enables more advanced monitoring.

**Discussion**: Commenters expressed mixed views: some argued surveillance is necessary for public safety, citing cases where video evidence is required for prosecution, while others criticized the erosion of privacy and the academic jargon used in the article.

**Tags**: `#surveillance`, `#privacy`, `#Seattle`, `#urban technology`

---

<a id="item-15"></a>
## [HP Revives Classic HP-16C Programmer's Calculator](https://hpcalcs.com/product/hp-16c-collectors-edition/) ⭐️ 6.0/10

HP has re-released the HP-16C Computer Scientist calculator as a Collector's Edition, bringing back the iconic programmer's tool with a classic design and modern programming functions. This revival caters to retro computing enthusiasts and programmers who value the HP-16C's specialized bit-manipulation capabilities, preserving a niche tool that remains useful for low-level debugging and binary arithmetic. The HP-16C Collector's Edition is part of the Voyager series and includes features like AND, OR, NOT, shifts, rotates, and complements, originally designed for computer programmers. It is available for purchase on hpcalcs.com.

hackernews · dm319 · Jun 2, 19:02 · [Discussion](https://news.ycombinator.com/item?id=48374685)

**Background**: The original HP-16C was produced from 1982 to 1989 and was specifically designed for computer programmers to assist in debugging. It is a member of the HP Voyager series of programmable calculators, known for their compact size and RPN (Reverse Polish Notation) input. The Collector's Edition follows a similar revival of the HP-15C scientific calculator.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HP-16C">HP-16C - Wikipedia</a></li>
<li><a href="https://hpcalcs.com/product/hp-16c-collectors-edition/">HP 16c Collector's Edition - HP Calc</a></li>

</ul>
</details>

**Discussion**: Community comments are generally positive, with many users expressing nostalgia and praising the original's durability. However, some users question the build quality compared to the original and suggest alternatives like SwissMicros DM16L, which offer similar functionality with modern construction.

**Tags**: `#retro computing`, `#HP calculators`, `#hardware`, `#programmer tools`

---

<a id="item-16"></a>
## [Datasette Agent MicroPython Sandbox Alpha Released](https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/#atom-everything) ⭐️ 6.0/10

Simon Willison released datasette-agent-micropython 0.1a0, an alpha plugin that allows Datasette Agent to safely generate and execute Python code using a MicroPython sandbox compiled to WebAssembly and run via wasmtime. This enables AI agents in Datasette to run user-generated Python code without security risks, expanding the capabilities of data exploration and analysis while maintaining safety. It represents a novel approach to sandboxing for LLM-driven code execution. The plugin bundles a lightly customized WASM build of MicroPython with a wrapper to execute code via wasmtime. The author notes that GPT-5.5 has so far failed to break out of the sandbox, indicating promising security.

rss · Simon Willison · Jun 2, 19:28

**Background**: Datasette Agent is an extensible AI assistant for Datasette, an open-source tool for exploring and publishing data. MicroPython is a lean implementation of Python 3 designed for microcontrollers, but it can also run in WebAssembly, providing a sandboxed environment. WebAssembly's security model isolates modules from the host system, making it suitable for running untrusted code.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent</a></li>
<li><a href="https://webassembly.org/docs/security/">Security - WebAssembly</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#python`, `#sandboxing`, `#webassembly`, `#ai-agents`

---

<a id="item-17"></a>
## [SFT vs RL for Fine-Tuning Reasoning LLMs](https://www.reddit.com/r/MachineLearning/comments/1ttxcm5/finetuning_a_reasoning_llm_with_supervised_or/) ⭐️ 6.0/10

A Reddit user seeks advice on whether supervised fine-tuning (SFT) or reinforcement learning (RL) is better for fine-tuning small LLMs on conversational data that includes reasoning traces and tool-calling decisions. This question is central to building effective AI agents that can reason and use tools, a rapidly growing area in LLM development. The answer can guide practitioners in choosing the right training paradigm for complex multi-step tasks. The user proposes splitting multi-turn conversations into samples with cumulative history and masking loss on non-assistant tokens. They also ask about incorporating RL after SFT, specifically how to design reward functions for tool-calling decisions.

reddit · r/MachineLearning · /u/zdeneklapes · Jun 1, 16:23

**Background**: Supervised fine-tuning (SFT) trains a model on labeled data to mimic desired outputs, while reinforcement learning (RL) optimizes a reward signal to encourage desirable behaviors like correct tool use. For reasoning tasks, RL with verifiable rewards (RLVR) has been used in models like DeepSeek-R1 to teach the model to produce effective reasoning traces. Tool-calling fine-tuning can adapt even non-native function-calling models to use tools through simple SFT.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2504.09762v2">Stop Anthropomorphizing Intermediate Tokens as Reasoning /Thinking...</a></li>
<li><a href="https://outcomeschool.com/blog/large-reasoning-models">Large Reasoning Models (LRMs)</a></li>
<li><a href="https://kyrylai.com/2025/04/01/fine-tune-llm-agent-tool-use-huggingface/">Fine - Tune LLM Agent for Tool Use with Hugging Face | Kyryl Opens ML</a></li>

</ul>
</details>

**Tags**: `#fine-tuning`, `#LLM`, `#reasoning`, `#reinforcement learning`, `#supervised learning`

---