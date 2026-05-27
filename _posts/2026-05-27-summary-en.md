---
layout: default
title: "Horizon Summary: 2026-05-27 (EN)"
date: 2026-05-27
lang: en
---

> From 28 items, 17 important content pieces were selected

---

1. [Curl Project Overwhelmed by AI-Assisted Security Reports](#item-1) ⭐️ 9.0/10
2. [WAVE: A Portable GPU ISA for Cross-Vendor Kernels](#item-2) ⭐️ 9.0/10
3. [Stripe Accused of Inadequate Response to Friendly Fraud](#item-3) ⭐️ 8.0/10
4. [Wikimedia Layoffs Spark Editor Strikes and Debate](#item-4) ⭐️ 8.0/10
5. [Microsoft Copilot Cowork Vulnerable to Prompt Injection Data Theft](#item-5) ⭐️ 8.0/10
6. [Pope Leo XIV's AI Encyclical Offers Clear Ethical Guidance](#item-6) ⭐️ 8.0/10
7. [EAMS: Equivariant Mesh Network for Robust Anatomical Segmentation](#item-7) ⭐️ 8.0/10
8. [METR AI Time Horizons Graph Critiqued as Flawed](#item-8) ⭐️ 8.0/10
9. [DCGAN with 12.6M params runs on RISC-V MCU in pure C](#item-9) ⭐️ 8.0/10
10. [Chemistry Behind the Garden Grove Chemical Tank Incident](#item-10) ⭐️ 7.0/10
11. [Modern Pixel Fonts Showcase with Retro Display Insights](#item-11) ⭐️ 7.0/10
12. [Dropbox CEO Drew Houston Steps Down](#item-12) ⭐️ 7.0/10
13. [Spice: Open-Source Decision Layer Decouples Planning from Execution](#item-13) ⭐️ 7.0/10
14. [Erin Brockovich Launches Data Center Tracking Map](#item-14) ⭐️ 6.0/10
15. [Spain blocks Polymarket, Kalshi over gambling license issue](#item-15) ⭐️ 6.0/10
16. [Paul Graham Slams AI-Generated Emails from Founders](#item-16) ⭐️ 6.0/10
17. [2nd Workshop on Efficient Reasoning at COLM 2026](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Curl Project Overwhelmed by AI-Assisted Security Reports](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 9.0/10

Daniel Stenberg, the maintainer of the curl project, reports that the rate of incoming AI-assisted security reports has surged to over one per day, 4-5 times higher than in 2024 and double the rate of 2025. The reports are of much higher quality and detail, placing unprecedented pressure on the curl team. This highlights a growing challenge for open-source projects: AI tools can generate a flood of credible vulnerability reports, straining maintainers and risking burnout. As curl is a critical internet infrastructure, this threatens the sustainability of essential open-source software. Despite the high volume, the vulnerabilities found are mostly LOW or MEDIUM severity; the last HIGH severity CVE was in October 2023. Stenberg notes that his wife has voiced concerns about his work hours, indicating severe maintainer burnout.

rss · Simon Willison · May 26, 23:48

**Background**: curl is a widely used open-source command-line tool and library for transferring data with URLs. It is maintained by a small team of volunteers and is a critical component of countless systems. AI-assisted vulnerability reporting uses large language models to automatically find and describe potential security flaws, which can produce many plausible but sometimes false reports.

<details><summary>References</summary>
<ul>
<li><a href="https://curl.se/">curl</a></li>
<li><a href="https://en.wikipedia.org/wiki/CURL">cURL - Wikipedia</a></li>
<li><a href="https://socket.dev/blog/django-joins-curl-in-pushing-back-on-ai-slop-security-reports">Django Joins curl in Pushing Back on AI Slop Security Report ...</a></li>

</ul>
</details>

**Discussion**: The Lobste.rs discussion likely expresses sympathy for Stenberg and concern about the sustainability of open-source maintenance under AI-generated report floods. Some may debate the value of AI-assisted security research versus the burden it creates.

**Tags**: `#open-source`, `#security`, `#AI`, `#curl`, `#maintainer burnout`

---

<a id="item-2"></a>
## [WAVE: A Portable GPU ISA for Cross-Vendor Kernels](https://www.reddit.com/r/MachineLearning/comments/1to76tv/p_built_a_portable_gpu_isa_after_reading_too_many/) ⭐️ 9.0/10

WAVE is a new portable GPU ISA and toolchain that compiles a single kernel into a portable binary, which can then be translated to run on NVIDIA, AMD, Intel, and Apple GPUs, with verified identical training results across all backends. This project significantly simplifies cross-platform GPU programming by abstracting vendor-specific ISAs into a common intermediate representation, potentially reducing development effort and enabling broader hardware compatibility for machine learning and GPU computing. WAVE supports four backends: Metal (Apple), PTX (NVIDIA), HIP (AMD), and SYCL (Intel), and includes a built-in CPU emulator for development without a GPU. The project is open-source on GitHub and available via pip install wave-gpu.

reddit · r/MachineLearning · /u/not-your-typical-cs · May 26, 13:36

**Background**: GPU programming typically requires vendor-specific languages and tools, such as CUDA for NVIDIA, ROCm for AMD, and Metal for Apple, making cross-platform development cumbersome. WAVE addresses this by providing a unified ISA that abstracts common GPU operations, inspired by the author's analysis of over 5,000 pages of architecture documentation across 16 microarchitectures.

<details><summary>References</summary>
<ul>
<li><a href="https://wave.ojima.me/">WAVE - The Universal GPU ISA</a></li>

</ul>
</details>

**Tags**: `#GPU`, `#ISA`, `#portability`, `#compiler`, `#machine learning`

---

<a id="item-3"></a>
## [Stripe Accused of Inadequate Response to Friendly Fraud](https://www.gingerlime.com/2026/stripe-seem-friendly-to-friendly-fraud/) ⭐️ 8.0/10

A detailed blog post by a Stripe user recounts how Stripe failed to adequately handle a friendly fraud chargeback, revealing that Stripe does not use cross-merchant fraud signals or take action against the customer's card or email for other merchants. This highlights a significant gap in Stripe's fraud prevention, potentially costing merchants billions annually, and underscores the need for better chargeback protection and cross-merchant fraud detection. Stripe confirmed they do not share chargeback abuse evidence across merchants, and the author suggests that Stripe's support responses are carefully noncommittal. The post includes community advice such as banning customers by card, email, and fingerprint after a chargeback.

hackernews · gingerlime · May 27, 00:40 · [Discussion](https://news.ycombinator.com/item?id=48287982)

**Background**: Friendly fraud, also known as chargeback fraud, occurs when a consumer makes a purchase with their own credit card and then requests a chargeback after receiving the goods or services. It accounts for about 80% of chargeback losses for merchants, costing over $132 billion annually. Stripe is a major payment processor that handles disputes and chargebacks on behalf of merchants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Friendly_fraud">Friendly fraud - Wikipedia</a></li>
<li><a href="https://stripe.com/resources/more/what-is-friendly-fraud">What is friendly fraud? Chargeback fraud explained | Stripe</a></li>
<li><a href="https://docs.stripe.com/disputes">Disputes | Stripe Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters suggest banning specific regions to cut 80% of fraud, and recommend completely banning the customer from the database after a chargeback. One commenter notes that Stripe likely records data for Visa Compelling Evidence 3.0, while another argues Stripe is not to blame for the customer's fraud.

**Tags**: `#fraud`, `#Stripe`, `#payment processing`, `#chargebacks`, `#SaaS`

---

<a id="item-4"></a>
## [Wikimedia Layoffs Spark Editor Strikes and Debate](https://medium.com/@jakeorlowitz/wikipedia-is-doing-the-capitalist-thing-56a393232943) ⭐️ 8.0/10

The Wikimedia Foundation laid off key MediaWiki developers and its entire Community Tech team, prompting English Wikipedia editors to go on strike in protest. This move threatens the volunteer-driven tooling and governance of Wikipedia, highlighting growing corporate influence and labor tensions within the open-source ecosystem. The layoffs included Brooke, one of MediaWiki's original developers, and the Community Tech team that maintained the Community Wishlist, a key channel for editor feature requests.

hackernews · cdrnsf · May 26, 20:33 · [Discussion](https://news.ycombinator.com/item?id=48285592)

**Background**: MediaWiki is the open-source software that powers Wikipedia and other Wikimedia projects. The Community Tech team was responsible for developing tools requested by volunteer editors, many of whom rely on custom tooling to edit efficiently. The Wikimedia Foundation has over 17 months of operating reserves, leading critics to argue the layoffs were unnecessary.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MediaWiki">MediaWiki</a></li>
<li><a href="https://meta.wikimedia.org/wiki/Community_Tech/Tool_Labs_support">Community Tech /Tool Labs support - Meta- Wiki</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock at the firing of a key MediaWiki developer and noted that the Community Tech team's removal undermines editor productivity. Some defended the Foundation's financial prudence, while others saw it as a betrayal of the community.

**Tags**: `#Wikipedia`, `#Open Source`, `#Tech Labor`, `#Layoffs`, `#Community`

---

<a id="item-5"></a>
## [Microsoft Copilot Cowork Vulnerable to Prompt Injection Data Theft](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

Microsoft Copilot Cowork agents can be exploited via prompt injection to exfiltrate files by sending emails with external images that trigger data-leaking network requests when opened. This vulnerability highlights a critical security challenge in agentic AI systems, where autonomous agents can be manipulated to leak sensitive data, affecting millions of Microsoft 365 users and raising concerns about the safety of AI-driven automation. The attack leverages the fact that Copilot Cowork can send emails to the user's own inbox without approval, and those emails can contain external images that trigger network requests, enabling data exfiltration via pre-authenticated OneDrive download links.

rss · Simon Willison · May 26, 15:36

**Background**: Prompt injection is a type of attack where malicious instructions are embedded in input to an AI model, causing it to perform unintended actions. Agentic systems like Copilot Cowork are designed to autonomously execute tasks, but this autonomy can be exploited if proper guardrails are not in place. Data exfiltration via external images is a known technique where an attacker embeds a URL that leaks data when the image is loaded.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/09/copilot-cowork-a-new-way-of-getting-work-done/">Copilot Cowork: A new way of getting work done | Microsoft ...</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#data exfiltration`, `#Microsoft Copilot`, `#agentic systems`

---

<a id="item-6"></a>
## [Pope Leo XIV's AI Encyclical Offers Clear Ethical Guidance](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 8.0/10

Pope Leo XIV released his first encyclical, 'Magnifica Humanitas', on May 15, 2026, addressing the ethical integration of artificial intelligence into society, drawing parallels to Pope Leo XIII's 1891 encyclical on the industrial revolution. This encyclical provides a clear, authoritative ethical framework from a major global religious institution, potentially influencing AI policy and discourse worldwide, especially on human dignity, labor, and justice. The encyclical highlights the interpretability problem of AI systems, describing them as 'cultivated' rather than 'built', and emphasizes that true development must place people at the center, not wealth accumulation.

rss · Simon Willison · May 25, 23:58

**Background**: An encyclical is a formal papal letter addressing important issues for the Catholic Church and the world. Pope Leo XIV chose his name to honor Pope Leo XIII, whose 1891 encyclical 'Rerum novarum' addressed the social question during the first industrial revolution. This new encyclical applies similar principles to the AI revolution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_humanitas">Magnifica Humanitas - Wikipedia</a></li>
<li><a href="https://www.ncregister.com/cna/full-text-magnifica-humanitas">Full Text of ‘Magnifica Humanitas’: Read Pope Leo XIV’s First ...</a></li>
<li><a href="https://www.humandevelopment.va/en/magnifica-humanitas.html">Magnifica Humanitas - Dicastery for Promoting Integral Human ...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#Vatican`, `#encyclical`, `#technology and society`, `#Pope Leo XIV`

---

<a id="item-7"></a>
## [EAMS: Equivariant Mesh Network for Robust Anatomical Segmentation](https://www.reddit.com/r/MachineLearning/comments/1tobtmu/augmented_equivariant_mesh_networks_for/) ⭐️ 8.0/10

The paper introduces EAMS, an Equivariant Anatomical Mesh Segmentor built on Equivariant Mesh Neural Networks (EMNN), which achieves robust anatomical mesh segmentation across varying patient poses and mesh resolutions, with improvements of 25-26 IoU points under geometric perturbations. This work unifies segmentation across diverse anatomical tasks (vertex-, edge-, and face-level) with a single lightweight architecture (<2M parameters), demonstrating that equivariant networks can be both robust and practical for clinical applications. EAMS combines intrinsic mesh descriptors (HKS) with anatomy-aware priors using PCA-derived frames for dental arches and liver surfaces, and augments message passing with lightweight global context. The paper also reveals a trade-off: strict equivariance can hurt performance on subtle asymmetric features like liver creases.

reddit · r/MachineLearning · /u/m0ronovich · May 26, 16:18

**Background**: Anatomical mesh segmentation involves labeling vertices, edges, or faces of 3D surface meshes from medical scans. Equivariant neural networks are designed to be robust to rotations and translations, which is important for handling varying patient poses. Prior methods were often task-specific and not equivariant, leading to performance drops under pose changes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2402.04821">[2402.04821] E (3)-Equivariant Mesh Neural Networks - arXiv.org</a></li>
<li><a href="https://arxiv.org/abs/2605.08172">[2605.08172] Augmented Equivariant Mesh Networks for ... PCA Retargeting: Encoding Linear Shape Models as ... GitHub - ellthompson/pca-body-model-param: Full body mesh ... Tutorial: PCA Meshes — Morphic 0.1 documentation Automatic construction of statistical shape models using ...</a></li>
<li><a href="https://proceedings.mlr.press/v238/anh-trang24a.html">E (3)-Equivariant Mesh Neural Networks - PMLR</a></li>

</ul>
</details>

**Tags**: `#equivariant neural networks`, `#mesh segmentation`, `#medical imaging`, `#ICML 2026`

---

<a id="item-8"></a>
## [METR AI Time Horizons Graph Critiqued as Flawed](https://www.reddit.com/r/MachineLearning/comments/1tnhnh5/the_famous_metr_ai_time_horizons_graph_contains/) ⭐️ 8.0/10

Nathan Witkin published a detailed critique exposing severe methodological errors in METR's influential AI time horizons graph, arguing it cannot be salvaged. The critique highlights issues such as unmeasured human baselines, biased sampling, and train-test contamination. The METR graph is widely cited to argue that AI is rapidly approaching human-level capabilities, so these flaws undermine a key piece of evidence in AI progress debates. If the graph is invalid, it could mislead policymakers, researchers, and the public about the true pace of AI advancement. Key errors include human baseline data being guesstimated rather than measured, hourly payment incentivizing slower human performance, and a biased sample of METR employees' acquaintances. Additionally, some tasks had published solutions online, leading to train-test contamination.

reddit · r/MachineLearning · /u/common_yarrow · May 25, 18:30

**Background**: METR (Model Evaluation and Threat Research) created a graph showing the time horizon over which AI agents can complete tasks, suggesting rapid progress toward human-level performance. The graph has been widely shared and discussed in AI safety and capability communities. The critique comes from a research writer at NYU Stern's Tech and Society Lab and is supported by additional analysis from cognitive scientist Gary Marcus.

<details><summary>References</summary>
<ul>
<li><a href="https://metr.org/time-horizons/">Task-Completion Time Horizons of Frontier AI Models - METR</a></li>
<li><a href="https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/">This is the most misunderstood graph in AI | MIT Technology ...</a></li>
<li><a href="https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/">Measuring AI Ability to Complete Long Tasks - METR</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion largely agrees with the critique, with commenters noting that the graph's flaws are severe and that it should not be used for policy decisions. Some users point out that the graph was already controversial and that this analysis confirms their suspicions.

**Tags**: `#AI benchmarks`, `#METR`, `#AI progress`, `#critique`, `#machine learning`

---

<a id="item-9"></a>
## [DCGAN with 12.6M params runs on RISC-V MCU in pure C](https://www.reddit.com/r/MachineLearning/comments/1tnhfxp/dcgan_inference_on_a_microcontroller_126m/) ⭐️ 8.0/10

A DCGAN with 12.6 million parameters has been successfully run on a RISC-V microcontroller (CH32H417) using a pure C inference engine, generating 64x64 cat faces in 26 seconds. This demonstrates that large generative models can run on extremely resource-constrained devices without external libraries, opening possibilities for on-device AI art and TinyML applications on open-source RISC-V hardware. The model uses int8 per-channel quantization, streams weights from an SD card via double buffering, and stores intermediate activations in 512KB SRAM. The latent vector is seeded with quantum random data from ANU QRNG.

reddit · r/MachineLearning · /u/Separate-Choice · May 25, 18:22

**Background**: DCGAN (Deep Convolutional Generative Adversarial Network) is a class of neural networks that generate images from random noise. Microcontrollers like the CH32H417 have very limited memory (typically kilobytes) and no operating system, making deep learning inference challenging. RISC-V is an open-standard instruction set architecture, and the CH32H417 is a dual-core RISC-V MCU with 896KB SRAM and 960KB Flash.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openwch/ch32h417">GitHub - openwch/ch32h417: A high-performance RISC-V dual ...</a></li>
<li><a href="https://www.wch-ic.com/products/CH32H417.html">SuperSpeed USB3.0 Dual-core Interconnect MCU CH32H417</a></li>
<li><a href="https://en.wikipedia.org/wiki/Box-Muller_transform">Box-Muller transform</a></li>

</ul>
</details>

**Tags**: `#DCGAN`, `#microcontroller`, `#RISC-V`, `#edge inference`, `#quantum random`

---

<a id="item-10"></a>
## [Chemistry Behind the Garden Grove Chemical Tank Incident](https://www.science.org/content/blog-post/methyl-methacrylate-tank) ⭐️ 7.0/10

An analysis of a methyl methacrylate tank incident in Garden Grove highlights the risks of uncontrolled polymerization, where the monomer can spontaneously polymerize if the inhibitor is depleted or if exposed to heat or UV radiation. This incident underscores the critical need for robust safety measures in chemical storage, as polymerization can generate heat and gases that may rupture tanks, leading to potential fires or explosions. Methyl methacrylate (MMA) is a monomer used to produce polymethyl methacrylate (PMMA), and its polymerization is highly exothermic and can accelerate if not properly controlled. The incident likely involved a loss of inhibitor or an external trigger such as heat or UV light.

hackernews · nooks · May 26, 19:25 · [Discussion](https://news.ycombinator.com/item?id=48284712)

**Background**: Methyl methacrylate is a flammable liquid that can undergo free-radical polymerization. To prevent uncontrolled polymerization, inhibitors are added, but they can be consumed over time or under certain conditions. If polymerization initiates, it produces heat and gases, increasing pressure inside the tank, which can lead to catastrophic failure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0040603123001892">Thermal safety and overall kinetics for methyl methacrylate ...</a></li>
<li><a href="https://www.cdph.ca.gov/Programs/OPA/Pages/CAHAN/Information-On-Methyl-Methacrylate.aspx">Information-On-Methyl-Methacrylate - California Department of ...</a></li>
<li><a href="https://download.basf.com/p1/000000000030041969_SDS_GEN_US/en_US/METHYLMETHACR._30041969_SDS_GEN_US_en_4-0.pdf">Safety Data Sheet METHYL METHACRYLATE - BASF</a></li>

</ul>
</details>

**Discussion**: Commenters shared links to postmortem analyses of similar incidents involving styrene and butyl acrylate, providing additional technical depth. Some questioned why passive protection systems are not standard, drawing parallels to earthquake safety. A tangential comment noted a Sublime song titled 'Garden Grove'.

**Tags**: `#chemistry`, `#industrial safety`, `#chemical engineering`, `#hazard analysis`

---

<a id="item-11"></a>
## [Modern Pixel Fonts Showcase with Retro Display Insights](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/) ⭐️ 7.0/10

A curated article showcases several modern pixel fonts, highlighting their design and historical context, with community comments adding technical depth on CRT display constraints and pixel ratios. This discussion matters for typography and retro computing enthusiasts as it bridges modern font design with the technical realities of vintage displays, influencing how pixel fonts are created and appreciated today. Community comments note that most modern pixel fonts assume 1:1 square pixels, but many 1980s displays had non-square pixels (e.g., finer horizontal resolution), which affects font appearance on original hardware.

hackernews · zdw · May 25, 20:41 · [Discussion](https://news.ycombinator.com/item?id=48271448)

**Background**: Pixel fonts originated in the 1980s with early computer graphics and video games, designed for low-resolution displays. CRT monitors often had non-square pixels, unlike modern LCDs, which affects how pixel fonts render. The article and comments explore these historical constraints and their relevance to contemporary font design.

<details><summary>References</summary>
<ul>
<li><a href="https://fonts.google.com/specimen/Pixelify+Sans">Pixelify Sans - Google Fonts</a></li>
<li><a href="https://www.reddit.com/r/identifythisfont/comments/1cjjetg/font_designed_for_crt_monitors/">Font designed for crt monitors : r/identifythisfont - Reddit</a></li>

</ul>
</details>

**Discussion**: Commenters highlight that many old displays had non-square pixels, a fact often overlooked by modern pixel font designers. They also share additional font resources like Departure Mono and Unscii, and critique some fonts for poor adaptation to pixel grids.

**Tags**: `#typography`, `#pixel fonts`, `#retro computing`, `#font design`, `#CRT displays`

---

<a id="item-12"></a>
## [Dropbox CEO Drew Houston Steps Down](https://www.cnbc.com/2026/05/26/dropbox-ceo-drew-houston-ashraf-alkarmi.html) ⭐️ 7.0/10

Dropbox CEO Drew Houston has announced he is stepping down, with Ashraf Alkarmi named as his replacement. This leadership change marks a pivotal moment for Dropbox as it navigates increasing competition from integrated cloud storage by Apple, Google, and Microsoft, and the need to innovate beyond file sync. Houston will remain on the board, and Alkarmi previously served as Dropbox's chief operating officer. The transition comes as Dropbox faces slowing growth and a shift toward AI-focused products.

hackernews · aghuang · May 26, 13:18 · [Discussion](https://news.ycombinator.com/item?id=48279453)

**Background**: Dropbox is a cloud storage company founded in 2007 that popularized file syncing across devices. In recent years, it has struggled to differentiate as competitors like iCloud, Google Drive, and OneDrive offer similar features integrated into their ecosystems.

**Discussion**: Community members expressed respect for Houston's leadership and the engineering culture he built, but also noted that Dropbox has introduced few meaningful features since 2011 and faces structural challenges as cloud-native apps reduce reliance on file sync.

**Tags**: `#Dropbox`, `#CEO transition`, `#tech leadership`, `#cloud storage`

---

<a id="item-13"></a>
## [Spice: Open-Source Decision Layer Decouples Planning from Execution](https://www.reddit.com/r/MachineLearning/comments/1tnfxsc/reconstructing_the_agent_methodology_decoupling/) ⭐️ 7.0/10

Spice, an open-source decision layer runtime, has been released to sit above AI agents and explicitly handle decision-making before execution, decoupling planning from execution. It records observations, options considered, trade-offs, and approval needs via Decision Cards. Current agent systems excel at execution but lack a transparent decision layer, making agent behavior a black box. Spice addresses this gap by making the reasoning process explicit, which could improve reliability, auditability, and trust in autonomous agents. Spice is installed via pip, configured with an LLM provider, and runs in the terminal; it can hand off approved execution to external agents like Claude Code or Codex. The project is early-stage but already supports Decision Cards and approval workflows.

reddit · r/MachineLearning · /u/Alarming_Rou_3841 · May 25, 17:29

**Background**: AI agents typically combine planning and execution in a single loop (e.g., ReAct), which can lead to short-sighted decisions or brittle plans. Decoupling planning from execution is a known architectural pattern that improves reliability by separating high-level reasoning from step-by-step action. Spice implements this pattern as a dedicated decision layer.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Dyalwayshappy/Spice">GitHub - Dyalwayshappy/Spice: A decision brain for agentic ...</a></li>
<li><a href="https://baguaai.com/beyond-execution-spice-introduces-an-open-source-decision-layer-to-solve-agentic-drift/">Beyond Execution: Spice Introduces an Open-Source Decision ...</a></li>
<li><a href="https://pypi.org/project/spice-runtime/">spice-runtime · PyPI</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#decision-making`, `#open source`, `#agent architecture`

---

<a id="item-14"></a>
## [Erin Brockovich Launches Data Center Tracking Map](https://www.niemanlab.org/2026/05/erin-brockovich-made-a-map-to-track-data-centers-around-the-country/) ⭐️ 6.0/10

Environmental activist Erin Brockovich has created an interactive map that tracks operational and planned hyperscale AI data centers across the United States, along with a form for community members to report local impacts. This map raises public awareness about the environmental footprint of the rapidly growing data center industry, particularly water consumption and ecosystem impacts, and empowers communities to voice concerns. The map overlays data center locations with community-submitted reports, but some critics note that similar resources like datacentermap.com already exist, and the tool's accuracy and novelty have been questioned.

hackernews · cratermoon · May 27, 00:36 · [Discussion](https://news.ycombinator.com/item?id=48287952)

**Background**: Data centers consume significant amounts of water for cooling servers, especially those using evaporative cooling. The water footprint includes on-site usage, power plant water use, and chip manufacturing. As AI and cloud computing drive data center expansion, environmental concerns have grown.

<details><summary>References</summary>
<ul>
<li><a href="https://www.niemanlab.org/2026/05/erin-brockovich-made-a-map-to-track-data-centers-around-the-country/">Erin Brockovich made a map to track data centers around the ...</a></li>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>
<li><a href="https://gizmodo.com/erin-brockovich-targets-ai-industry-with-new-data-center-map-2000763638">Erin Brockovich Targets AI Industry With New Data Center Map</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some question the novelty, pointing to existing maps like datacentermap.com, while others criticize the focus on water consumption as a canard. There is also skepticism about the tool being built with AI and a sentiment that the topic is populist.

**Tags**: `#data centers`, `#environment`, `#map`, `#water consumption`

---

<a id="item-15"></a>
## [Spain blocks Polymarket, Kalshi over gambling license issue](https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/) ⭐️ 6.0/10

Spain has blocked access to prediction markets Polymarket and Kalshi, citing their lack of required gambling licenses. The regulatory action was reported on May 26, 2026. This decision highlights the growing regulatory scrutiny on prediction markets, which operate in a legal gray area between gambling and financial trading. It could set a precedent for other countries considering similar restrictions. Polymarket is a cryptocurrency-based prediction market, while Kalshi is a regulated exchange for event contracts. Both platforms allow users to bet on outcomes of real-world events such as elections, sports, and conflicts.

hackernews · thm · May 26, 13:08 · [Discussion](https://news.ycombinator.com/item?id=48279316)

**Background**: Prediction markets are platforms where individuals can place bets on future events, often using cryptocurrencies or fiat money. They have faced criticism for potentially incentivizing manipulation of real-world events and for resembling gambling. Spain's action aligns with its strict gambling regulations, which require operators to obtain a license.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polymarket">Polymarket - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prediction_market">Prediction market - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments are overwhelmingly critical of prediction markets, with users arguing they incentivize harmful behavior such as manipulation of events and even murder. Some compare them to casinos or worse, calling for global bans. A few express surprise that such platforms are advertised to the general public.

**Tags**: `#prediction markets`, `#regulation`, `#gambling`, `#tech policy`

---

<a id="item-16"></a>
## [Paul Graham Slams AI-Generated Emails from Founders](https://simonwillison.net/2026/May/26/paul-graham/#atom-everything) ⭐️ 6.0/10

Paul Graham, a prominent startup investor and Y Combinator co-founder, publicly criticized founders for using AI to write emails, stating that it feels like deception and makes him think less of the author. This highlights a growing tension between AI-assisted writing and authenticity in professional communication, especially in the startup ecosystem where personal effort and sincerity are highly valued. Graham noted that AI-generated emails often adopt a 'hard-hitting journalistic style' that no founder used before, and he has never knowingly finished reading such an email. He equated using AI to write emails with an attempt to trick the recipient.

rss · Simon Willison · May 26, 15:02

**Background**: Paul Graham is a well-known figure in the startup world, co-founding Y Combinator, a startup accelerator that has funded thousands of companies. His opinions often carry weight among entrepreneurs. The use of large language models (LLMs) like GPT-4 for writing has become widespread, raising questions about authenticity and effort in communication.

**Tags**: `#AI`, `#writing`, `#ethics`, `#startups`

---

<a id="item-17"></a>
## [2nd Workshop on Efficient Reasoning at COLM 2026](https://www.reddit.com/r/MachineLearning/comments/1tncfx9/call_for_papers_workshop_on_efficient_reasoning/) ⭐️ 6.0/10

The 2nd Workshop on Efficient Reasoning (ER) at COLM 2026 has issued a call for papers, with submissions due July 12, 2026, and the workshop taking place on October 9, 2026. This workshop addresses the critical need for efficient reasoning in large language models, covering topics like fast inference, KV-cache tricks, and long chain-of-thought reasoning, which are essential for deploying AI in resource-constrained environments. Topics include multimodal reasoning, efficient training and RL fine-tuning, pruning, compression, progressive generation, and real-time applications in healthcare, robotics, and autonomy. Submissions are accepted via OpenReview.

reddit · r/MachineLearning · /u/Mediocre-Ad5059 · May 25, 15:25

**Background**: Efficient reasoning aims to reduce the computational cost of inference in large language models while maintaining accuracy. Techniques such as KV caching, chain-of-thought prompting, and model compression are key areas of research. COLM (Conference on Language Modeling) is a leading venue for language modeling research, and this workshop is part of its 2026 edition.

<details><summary>References</summary>
<ul>
<li><a href="https://colmweb.org/plenary.html">COLM 2026</a></li>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>
<li><a href="https://arxiv.org/abs/2503.09567">Towards Reasoning Era: A Survey of Long Chain-of-Thought for ... Towards Reasoning Era: A Survey of Long Chain-of-Thought Unlocking General Long Chain-of-Thought Reasoning ... Demystifying Long Chain-of-Thought Reasoning Demystifying Long Chain-of-Thought Reasoning in LLMs Images What is chain of thought (CoT) prompting? - IBM Demystifying Long Chain-of-Thought Reasoning - OpenReview</a></li>

</ul>
</details>

**Tags**: `#efficient reasoning`, `#workshop`, `#COLM 2026`, `#call for papers`, `#machine learning`

---