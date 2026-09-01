# 图像生成与编辑论文库 2021–2026

[![papers](https://img.shields.io/badge/papers-195-2b7489)](#全量清单)
[![notes](https://img.shields.io/badge/notes-1.26M_CJK_chars-4c9a2a)](#全量清单)
[![coverage](https://img.shields.io/badge/coverage-2021.08_--_2026.08-e07b39)](#全量清单)
[![links](https://img.shields.io/badge/source_links-191%2F195_byte--verified-1f883d)](docs/可信度与产出.md#2-原文直链是怎么核的)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**195 篇图像生成与编辑论文，每篇一份中文深读笔记，外加一条核验过的原文直链。**
时间跨度 2021-08 → 2026-08，笔记合计 1,261,285 个汉字。

*195 image generation & editing papers, each with an in-depth Chinese reading note and a verified link to the original source. Aug 2021 – Aug 2026.*

> **维护者** [@ManagerYu10](https://github.com/ManagerYu10) · **授权** [CC BY 4.0](LICENSE)（署名即可转载、改写、商用） · **最后核对** 2026-09-01
>
> ⚠️ **笔记正文由 DeepSeek V4 Pro 依据原文抽取的文字生成**，人定标准、做机器校验、逐条抽查。
> 图里的信息模型读不到，公式符号会在 PDF 抽取时丢失。哪些能直接当依据、哪些必须回原文，
> 见 [可信度与产出.md](docs/可信度与产出.md)。

---

## 这个库收什么

**按模态划分，不按生成/编辑划分。** 图像生成与图像编辑在同一个库里，因为这条边界在论文
层面本来就不成立：编辑方法长在生成骨干上（本库的 Latent-Diffusion、Classifier-Free-Guidance、
SD3、FLUX.1 都是生成侧论文），而 2025 年之后的主线是统一模型——BAGEL、OmniGen2、
UniWorld、Emu3.5 同时是生成和编辑。硬按任务拆仓库，这批论文只能任意归到一边，
或者被复制成两份笔记。

所以任务是 `scripts/papers.json` 里的一个**可多值**字段，不是目录边界：

| 任务 | 篇数 |
| --- | ---: |
| 编辑 | 140 |
| 生成 | 82 |
| 两者都是（统一模型） | 27 |

视频侧在另一个库：[video-gen-edit-papers](https://github.com/ManagerYu10/video-gen-edit-papers)。

按贡献类型分：方法 107、模型 34、基准 30、数据集 12、奖励与 RL 7、综述 5。

## 怎么用

直接拉到本页最后的[全量清单](#全量清单)，195 行按时间**倒序**排，最新的在最前，浏览器里 `Ctrl/Cmd + F` 搜简称或标题。每行两列可以点：

| 这一列 | 点开是什么 |
| --- | --- |
| **简称** | 这篇的 `解读.md`，中文深读笔记，就在本仓库里 |
| **原文** | 论文本身。191 行标 `PDF` 的过了字节级核验，4 行标 `官方来源` 的确实没有独立论文 |

按技术脉络分组的视图在 [docs/INDEX.md](docs/INDEX.md)，跨论文的结论在 [docs/总结分析.md](docs/总结分析.md)。

**解读的定位是替代第一次完整泛读**，不替代精读——要抠实现细节仍然得回 PDF。三种规范并存，
是分批产出留下的，旧的不回炉重写：

| 规范 | 篇数 | 说明 |
| --- | ---: | --- |
| 11 节深读（6,502–8,943 字） | 160 | 最初那批的规范。结构上 158 篇是标准 11 节，Complex-Edit 与 KRIS-Bench 在 11 节之后又接了 benchmark 那套格式的 6 个无编号小节，再补决策意义与一手来源两节 |
| 决策型短笔记（8～9 节） | 26 | 2026-08-29 那轮核验补进来的，以 benchmark 和评测指标为主；其中 4 项没有独立论文，只记录官方资料与核验边界 |
| v2 / 8 节 / 3,000–5,000 字 | 9 | 2026-09 起的新增篇目，含本次并入的 8 篇生成侧论文。8 节齐全、3,000–5,000 汉字、证据表至少 4 行，由脚本硬校验，不达标自动重生成 |

规范正文见 [docs/prompt.md](docs/prompt.md)（v2）与 [docs/LARK论文短版解读_PROMPT.md](docs/LARK论文短版解读_PROMPT.md)（短版）。

**要原文 PDF**：不在仓库里，合计 3.4 GB。单篇点表里的链接就行，批量拉到本地：

```bash
python3 scripts/fetch_pdfs.py                    # 补齐所有缺的
python3 scripts/fetch_pdfs.py --list             # 只列缺什么，不下载
python3 scripts/fetch_pdfs.py 2024-11_OmniEdit   # 只下一篇
```

只用标准库，按 arXiv 要求节流到每 3 秒一份，断了重跑只补没下成的。

## 技术脉络

| 脉络 | 篇数 |
| --- | ---: |
| 统一多模态：理解与生成同一个模型 | 22 |
| 指令式编辑：说人话改图，以及数据从哪来 | 21 |
| 新一代评测：物理合理性与多轮 | 19 |
| 2025H2–2026 的编辑与统一模型 | 19 |
| 条件控制：结构、身份、参考图怎么注入 | 15 |
| 训练-free 扩散编辑：靠注意力和反演改图 | 15 |
| 推理、强化学习与评测 | 15 |
| 生成骨干：编辑方法赖以运行的底座 | 14 |
| 局部与对象级：抠图、补全、搬物体 | 13 |
| 奖励模型与在线 RL（2025H2 起） | 9 |
| 反演精度：真实图片怎么无损映回噪声 | 9 |
| 会推理再动手：think-then-edit | 7 |
| 编辑数据工程：三元组从哪来 | 6 |
| 个性化与主体保持 | 4 |
| 拖拽与点控编辑 | 4 |
| 少步与一步生成 | 2 |
| 生成侧数据与重标注 | 1 |

逐篇归入哪条、每条怎么串起来，见 [docs/INDEX.md](docs/INDEX.md)。

## 全量清单

195 行按时间**倒序**排，`#1` 是最新的一篇，`#195` 是最早的一篇。**解读字数**是当场从 `解读.md` 数的（U+4E00–U+9FFF），不读 `meta.json`。

| # | 时间 | 简称（→ 解读） | 论文标题 | 发表 | 机构 | 任务 | 原文 | 解读字数 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| 1 | 2026-08-24 | [rl-no-edit-rewards](papers/2026-08_rl-no-edit-rewards/解读.md) | Can We Perform Online RL for Image Editing without Editing Rewards? | arXiv 预印本 | 北京大学 | 编辑 | [PDF](https://arxiv.org/pdf/2608.22780) | 7,117 |
| 2 | 2026-08-14 | [CPI-Bench](papers/2026-08_CPI-Bench/解读.md) | CPI-Bench: A Comprehensive, Practical and Intelligent Benchmark for Real-World Image Editing | arXiv 预印本 | 阿里巴巴 | 编辑 | [PDF](https://arxiv.org/pdf/2608.14546) | 2,517 |
| 3 | 2026-07-28 | [IIE-Survey](papers/2026-07_IIE-Survey/解读.md) | Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications | Vicinagearth 3, Article 3 (2026) | 中国电信人工智能研究院（TeleAI） | 编辑 | [PDF](https://arxiv.org/pdf/2607.25642) | 8,309 |
| 4 | 2026-07-13 | [read-it-back](papers/2026-07_read-it-back/解读.md) | Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation | arXiv 预印本 | 香港大学 / 字节跳动 Seed 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2607.11886) | 6,611 |
| 5 | 2026-07-08 | [implicit-preservation](papers/2026-07_implicit-preservation/解读.md) | Making Implicit Preservation Intent Explicit in Conversational Image Editing | arXiv 预印本 | 西江大学 / 高丽大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2607.07051) | 6,823 |
| 6 | 2026-07-06 | [cfg-inversion-fail](papers/2026-07_cfg-inversion-fail/解读.md) | When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt--Latent Interactions | arXiv 预印本 | 东北大学信息科学研究科 / 理化学研究所AIP中心 | 编辑 | [PDF](https://arxiv.org/pdf/2607.04731) | 6,682 |
| 7 | 2026-06-25 | [lighting-edit-bench](papers/2026-06_lighting-edit-bench/解读.md) | Do Image Editing Models Understand Lighting? | arXiv 预印本 | 海德堡大学 / 慕尼黑工业大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2606.26738) | 6,897 |
| 8 | 2026-06-25 | [qwen-image-rl](papers/2026-06_qwen-image-rl/解读.md) | Qwen-Image-2.0-RL Technical Report | arXiv 预印本 | 阿里巴巴通义千问团队 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2606.27608) | 8,108 |
| 9 | 2026-06-17 | [moebius-inpainting](papers/2026-06_moebius-inpainting/解读.md) | Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance | arXiv 预印本 | 华中科技大学 / vivo AI Lab | 编辑 | [PDF](https://arxiv.org/pdf/2606.19195) | 6,843 |
| 10 | 2026-06-14 | [mind-the-gap](papers/2026-06_mind-the-gap/解读.md) | Mind the Gap: Diagnosing Constraint Discovery Failures in Text-in-Image Editing | arXiv 预印本 | 中南大学 | 编辑 | [PDF](https://arxiv.org/pdf/2606.15982) | 6,741 |
| 11 | 2026-06-11 | [hydra-x](papers/2026-06_hydra-x/解读.md) | HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers | arXiv 预印本 | 南京大学 / 中国科学院自动化研究所 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2606.13289) | 6,583 |
| 12 | 2026-06-09 | [arm-unified](papers/2026-06_arm-unified/解读.md) | ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations | arXiv 预印本 | 复旦大学 / 字节跳动 等 3 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2606.11188) | 7,433 |
| 13 | 2026-06-02 | [bootstrap-generator](papers/2026-06_bootstrap-generator/解读.md) | Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching | ICML 2026 | 英伟达 / 特拉维夫大学 | 编辑 | [PDF](https://arxiv.org/pdf/2606.03911) | 7,686 |
| 14 | 2026-06-01 | [Inter-Edit](papers/2026-06_Inter-Edit/解读.md) | Inter-Edit: First Benchmark for Interactive Instruction-Based Image Editing | CVPR 2026 | 北京邮电大学 / 北京航空航天大学 等 5 家 | 编辑 | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Inter-Edit_First_Benchmark_for_Interactive_Instruction-Based_Image_Editing_CVPR_2026_paper.pdf) | 2,661 |
| 15 | 2026-05-29 | [PaintBench](papers/2026-05_PaintBench/解读.md) | PaintBench: Deterministic Evaluation of Precise Visual Editing | arXiv 预印本 | 纽约大学 | 编辑 | [PDF](https://arxiv.org/pdf/2606.00188) | 3,038 |
| 16 | 2026-05-20 | [decompose-subject](papers/2026-05_decompose-subject/解读.md) | Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction | arXiv 预印本 | 香港大学 | 生成 | [PDF](https://arxiv.org/pdf/2605.20807) | 7,064 |
| 17 | 2026-05-13 | [edit-compass](papers/2026-05_edit-compass/解读.md) | Edit-Compass &amp; EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling | arXiv 预印本 | 杭州电子科技大学 / 北京大学 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2605.13062) | 6,567 |
| 18 | 2026-05-12 | [sensenova-u1](papers/2026-05_sensenova-u1/解读.md) | SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture | 商汤技术报告 | 商汤科技 SenseNova 团队 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2605.12500) | 6,907 |
| 19 | 2026-05-11 | [Qwen-Image-2.0](papers/2026-05_Qwen-Image-2.0/解读.md) | Qwen-Image-2.0 Technical Report | 阿里巴巴通义千问技术报告 | 阿里巴巴通义千问团队 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2605.10730) | 8,086 |
| 20 | 2026-05-11 | [masked-gen-transformer](papers/2026-05_masked-gen-transformer/解读.md) | Masked Generative Transformer Is What You Need for Image Editing | CVPR 2026 HiGen Workshop | 字节跳动 / 新加坡国立大学 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2605.10859) | 6,797 |
| 21 | 2026-05-04 | [directedit](papers/2026-05_directedit/解读.md) | DirectEdit: Step-Level Accurate Inversion for Flow-Based Image Editing | ICML 2026 | 武汉大学计算机学院多媒体软件国家工程研究中心 | 编辑 | [PDF](https://arxiv.org/pdf/2605.02417) | 7,200 |
| 22 | 2026-04-29 | [spatialfusion](papers/2026-04_spatialfusion/解读.md) | SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness | arXiv 预印本 | 浙江大学 / HiThink Research | 生成 | [PDF](https://arxiv.org/pdf/2604.26341) | 6,812 |
| 23 | 2026-04-27 | [beyond-accuracy](papers/2026-04_beyond-accuracy/解读.md) | Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models | arXiv 预印本 | Hasso Plattner Institute / 波茨坦大学 | 生成 | [PDF](https://arxiv.org/pdf/2604.25072) | 7,280 |
| 24 | 2026-04-27 | [meta-cot](papers/2026-04_meta-cot/解读.md) | Meta-CoT: Enhancing Granularity and Generalization in Image Editing | CVPR2026 | 清华大学深圳国际研究生院 / 腾讯混元 | 编辑 | [PDF](https://arxiv.org/pdf/2604.24625) | 6,900 |
| 25 | 2026-04-27 | [tuna-2](papers/2026-04_tuna-2/解读.md) | Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation | arXiv 预印本 | Meta AI / 香港大学 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2604.24763) | 6,618 |
| 26 | 2026-04-26 | [edit-where-you-mean](papers/2026-04_edit-where-you-mean/解读.md) | Edit Where You Mean: Region-Aware Adapter Injection for Mask-Free Local Image Editing | arXiv 预印本 | 香港中文大学（深圳） / 北京航空航天大学 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2604.23763) | 6,989 |
| 27 | 2026-04-22 | [GSI-Bench](papers/2026-04_GSI-Bench/解读.md) | Exploring Spatial Intelligence from a Generative Perspective | CVPR 2026 | 浙江大学 / 蚂蚁集团 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2604.20570) | 2,510 |
| 28 | 2026-04-21 | [GPT-Image-2](papers/2026-04_GPT-Image-2/解读.md) | GPT Image 2 | OpenAI official model documentation | OpenAI | 生成+编辑 | [官方来源](https://developers.openai.com/api/docs/models/gpt-image-2) | 732 |
| 29 | 2026-04-03 | [banana100](papers/2026-04_banana100/解读.md) | Banana100: Breaking NR-IQA Metrics by 100 Iterative Image Replications with Nano Banana Pro | CVPR 2026 Workshop on Agentic AI for Visual Media | 加州大学圣巴巴拉分校 | 编辑 | [PDF](https://arxiv.org/pdf/2604.03400) | 8,186 |
| 30 | 2026-03-31 | [editing-manifold](papers/2026-03_editing-manifold/解读.md) | Editing on the Generative Manifold: A Theoretical and Empirical Study of General Diffusion-Based Image Editing Trade-offs | arXiv 预印本 | 西安电子科技大学 | 编辑 | [PDF](https://arxiv.org/pdf/2603.29736) | 7,110 |
| 31 | 2026-03-30 | [GEditBench-v2](papers/2026-03_GEditBench-v2/解读.md) | GEditBench v2: A Human-Aligned Benchmark for General Image Editing | arXiv 预印本 | 南洋理工大学 / StepFun 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2603.28547) | 3,755 |
| 32 | 2026-03-20 | [TIEdit-EditProbe](papers/2026-03_TIEdit-EditProbe/解读.md) | Evaluating Image Editing with LLMs: A Comprehensive Benchmark and Intermediate-Layer Probing Approach | Displays 94 (2026), 103494 | 上海交通大学图像通信与网络工程研究所 | 编辑 | [PDF](https://arxiv.org/pdf/2603.19775) | 2,864 |
| 33 | 2026-03-17 | [ug-fight-dpo](papers/2026-03_ug-fight-dpo/解读.md) | Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models | arXiv 预印本 | **未核** | 生成 | [PDF](https://arxiv.org/pdf/2603.17044v1) | 6,969 |
| 34 | 2026-03-16 | [Omni-IIE-Bench](papers/2026-03_Omni-IIE-Bench/解读.md) | Omni IIE Bench: Benchmarking the Practical Capabilities of Image Editing Models | CVPR 2026 | 中国科学院大学 / 腾讯 | 编辑 | [PDF](https://arxiv.org/pdf/2603.16944) | 3,225 |
| 35 | 2026-03-10 | [internvl-u](papers/2026-03_internvl-u/解读.md) | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | arXiv 预印本 | 上海人工智能实验室 / 香港中文大学多媒体实验室 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2603.09877) | 6,642 |
| 36 | 2026-03-09 | [care-edit](papers/2026-03_care-edit/解读.md) | CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing | CVPR 2026 | 香港科技大学 | 编辑 | [PDF](https://arxiv.org/pdf/2603.08589) | 6,830 |
| 37 | 2026-03-09 | [coco-code-cot](papers/2026-03_coco-code-cot/解读.md) | CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation | ECCV 2026 | 香港中文大学 / 华南理工大学 等 4 家 | 生成 | [PDF](https://arxiv.org/pdf/2603.08652) | 6,950 |
| 38 | 2026-02-22 | [ChordEdit](papers/2026-02_ChordEdit/解读.md) | ChordEdit: One-Step Low-Energy Transport for Image Editing | CVPR 2026 | 广东工业大学 / 惠州学院 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2602.19083) | 7,579 |
| 39 | 2026-02-12 | [FireRed-Image-Edit](papers/2026-02_FireRed-Image-Edit/解读.md) | FireRed-Image-Edit-1.0 Technical Report | arXiv 预印本 | 小红书 | 编辑 | [PDF](https://arxiv.org/pdf/2602.13344) | 7,206 |
| 40 | 2026-02-09 | [reasoning-to-pixels](papers/2026-02_reasoning-to-pixels/解读.md) | From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models | arXiv 预印本 | 加州大学圣迭戈分校 / 南加州大学 等 4 家 | 生成 | [PDF](https://arxiv.org/pdf/2602.08336) | 6,985 |
| 41 | 2026-02-09 | [rethink-global-text](papers/2026-02_rethink-global-text/解读.md) | Rethinking Global Text Conditioning in Diffusion Transformers | ICLR26 | Yandex Research / Adobe Research | 生成 | [PDF](https://arxiv.org/pdf/2602.09268) | 7,486 |
| 42 | 2026-02-07 | [spatialreward-edit](papers/2026-02_spatialreward-edit/解读.md) | SpatialReward: Bridging the Perception Gap in Online RL for Image Editing via Explicit Spatial Reasoning | 43rd International Conference on Machine Learning (ICML 2026) | 哈尔滨工业大学（深圳） / 清华大学深圳国际研究生院 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2602.07458) | 7,019 |
| 43 | 2026-02-02 | [VIBE](papers/2026-02_VIBE/解读.md) | How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing | arXiv 预印本 | 中国科学院大学人工智能学院 / 中国科学院自动化研究所 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2602.01851) | 2,564 |
| 44 | 2026-02-02 | [unireason](papers/2026-02_unireason/解读.md) | UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing | arXiv 预印本 | 复旦大学 / 上海创新研究院 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2602.02437) | 7,070 |
| 45 | 2026-01-06 | [ThinkRL-Edit](papers/2026-01_ThinkRL-Edit/解读.md) | ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing | arXiv 预印本 | 浙江大学 / 字节跳动 | 编辑 | [PDF](https://arxiv.org/pdf/2601.03467) | 7,196 |
| 46 | 2026-01-06 | [reward-hacking-t2i](papers/2026-01_reward-hacking-t2i/解读.md) | Understanding Reward Hacking in Text-to-Image Reinforcement Learning | arXiv 预印本 | 加州大学洛杉矶分校 | 编辑 | [PDF](https://arxiv.org/pdf/2601.03468) | 7,524 |
| 47 | 2026-01-05 | [nextflow](papers/2026-01_nextflow/解读.md) | NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation | arXiv 预印本 | 字节跳动 / 清华大学 等 3 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2601.02204) | 7,320 |
| 48 | 2025-12-17 | [Qwen-Image-Edit-2511](papers/2025-12_Qwen-Image-Edit-2511/解读.md) | Qwen-Image-Edit-2511 | Qwen official model card | 阿里巴巴通义千问团队 | 编辑 | [官方来源](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | 666 |
| 49 | 2025-12-17 | [Qwen-Image-Layered](papers/2025-12_Qwen-Image-Layered/解读.md) | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition | arXiv 预印本 | 香港科技大学（广州） / 阿里巴巴 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2512.15603) | 7,109 |
| 50 | 2025-12-04 | [I2I-Bench](papers/2025-12_I2I-Bench/解读.md) | I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models | CVPR 2026 | 上海交通大学图像通信与网络工程研究所 | 编辑 | [PDF](https://arxiv.org/pdf/2512.04660) | 7,049 |
| 51 | 2025-11-29 | [WiseEdit](papers/2025-12_WiseEdit/解读.md) | WiseEdit: Benchmarking Cognition- and Creativity-Informed Image Editing | arXiv 预印本 | 浙江大学 / 上海人工智能实验室 | 编辑 | [PDF](https://arxiv.org/pdf/2512.00387) | 2,593 |
| 52 | 2025-11-27 | [ReasonEdit](papers/2025-11_ReasonEdit/解读.md) | ReasonEdit: Towards Reasoning-Enhanced Image Editing Models | arXiv 预印本 | 阶跃星辰 | 编辑 | [PDF](https://arxiv.org/pdf/2511.22625) | 7,349 |
| 53 | 2025-11-27 | [Z-Image](papers/2025-11_Z-Image/解读.md) | Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer | 阿里巴巴通义技术报告 | 阿里巴巴 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2511.22699) | 6,667 |
| 54 | 2025-11-03 | [UniREditBench](papers/2025-11_UniREditBench/解读.md) | UniREditBench: A Unified Reasoning-based Image Editing Benchmark | arXiv 预印本 | 复旦大学 / 上海创新研究院 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2511.01295) | 7,321 |
| 55 | 2025-10-30 | [Emu3.5](papers/2025-10_Emu3.5/解读.md) | Emu3.5: Native Multimodal Models are World Learners | arXiv 预印本 | 北京智源人工智能研究院 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2510.26583) | 7,580 |
| 56 | 2025-10-22 | [Pico-Banana-400K](papers/2025-10_Pico-Banana-400K/解读.md) | Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing | arXiv 预印本 | 苹果公司 | 编辑 | [PDF](https://arxiv.org/pdf/2510.19808) | 7,750 |
| 57 | 2025-10-20 | [PICABench](papers/2025-10_PICABench/解读.md) | PICABench: How Far Are We from Physically Realistic Image Editing? | arXiv 预印本 | 上海交通大学 / 上海人工智能实验室 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2510.17681) | 7,739 |
| 58 | 2025-10-19 | [Edit-R1-UniWorld-V2](papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback | arXiv 预印本 | 北京大学深圳研究生院 / Rabbitpre AI | 编辑 | [PDF](https://arxiv.org/pdf/2510.16888) | 6,542 |
| 59 | 2025-10-09 | [InstructX](papers/2025-10_InstructX/解读.md) | InstructX: Towards Unified Visual Editing with MLLM Guidance | arXiv 预印本 | 字节跳动智能创作团队 | 编辑 | [PDF](https://arxiv.org/pdf/2510.08485) | 6,671 |
| 60 | 2025-10-09 | [Kontinuous-Kontext](papers/2025-10_Kontinuous-Kontext/解读.md) | Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing | CVPR 2026 | Snap Research / 特拉维夫大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2510.08532) | 8,551 |
| 61 | 2025-10-08 | [DreamOmni2](papers/2025-10_DreamOmni2/解读.md) | DreamOmni2: Multimodal Instruction-based Editing and Generation | arXiv 预印本 | 香港中文大学 / 香港科技大学 等 4 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2510.06679) | 6,564 |
| 62 | 2025-10-07 | [Lumina-DiMOO](papers/2025-10_Lumina-DiMOO/解读.md) | Lumina-DiMOO: An Omni Diffusion Large Language Model for Multi-Modal Generation and Understanding | arXiv 预印本 | 上海人工智能实验室 / Shanghai Innovation Institute 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2510.06308) | 7,291 |
| 63 | 2025-10-05 | [ChronoEdit](papers/2025-10_ChronoEdit/解读.md) | ChronoEdit: Towards Temporal Reasoning for Image Editing and World Simulation | arXiv 预印本 | 英伟达 / 多伦多大学 | 编辑 | [PDF](https://arxiv.org/pdf/2510.04290) | 6,825 |
| 64 | 2025-09-30 | [EditReward](papers/2025-09_EditReward/解读.md) | EditReward: A Human-Aligned Reward Model for Instruction-Guided Image Editing | ICLR 2026 | 滑铁卢大学 / 清华大学 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2509.26346) | 7,572 |
| 65 | 2025-09-29 | [OpenGPT-4o-Image](papers/2025-09_OpenGPT-4o-Image/解读.md) | OpenGPT-4o-Image: A Comprehensive Dataset for Advanced Image Generation and Editing | arXiv 预印本 | 中国科学技术大学 / 北京大学 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2509.24900) | 7,651 |
| 66 | 2025-09-28 | [EditScore](papers/2025-09_EditScore/解读.md) | EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling | ICLR 2026 | 中国科学技术大学 / 中国科学院自动化研究所 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2509.23909) | 6,719 |
| 67 | 2025-09-28 | [HunyuanImage3](papers/2025-09_HunyuanImage3/解读.md) | HunyuanImage 3.0 Technical Report | 腾讯混元技术报告 | 腾讯混元基础模型团队 | 生成 | [PDF](https://arxiv.org/pdf/2509.23951) | 6,546 |
| 68 | 2025-09-24 | [EditVerse](papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | arXiv 预印本 | Adobe Research / 香港中文大学 等 4 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2509.20360) | 7,231 |
| 69 | 2025-09-24 | [Seedream4](papers/2025-09_Seedream4/解读.md) | Seedream 4.0: Toward Next-generation Multimodal Image Generation | 字节跳动 Seed 技术报告 | 字节跳动 Seed | 生成+编辑 | [PDF](https://arxiv.org/pdf/2509.20427) | 6,611 |
| 70 | 2025-09-16 | [EdiVal-Agent](papers/2025-09_EdiVal-Agent/解读.md) | EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing | ICLR 2026 | 得克萨斯大学奥斯汀分校 / 加州大学洛杉矶分校 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2509.13399) | 6,599 |
| 71 | 2025-08-21 | [VAREdit](papers/2025-08_VAREdit/解读.md) | Visual Autoregressive Modeling for Instruction-Guided Image Editing | ICLR 2026 | 中国科学技术大学 / HiDream.ai Inc. | 编辑 | [PDF](https://arxiv.org/pdf/2508.15772) | 7,076 |
| 72 | 2025-08-11 | [X2Edit](papers/2025-08_X2Edit/解读.md) | X2Edit: Revisiting Arbitrary-Instruction Image Editing through Self-Constructed Data and Task-Aware Representation Learning | AAAI 2026 | OPPO AI 中心 / 中山大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2508.07607) | 6,789 |
| 73 | 2025-08-04 | [Qwen-Image](papers/2025-08_Qwen-Image/解读.md) | Qwen-Image Technical Report | 阿里巴巴通义千问技术报告 | 阿里巴巴通义千问团队 | 生成 | [PDF](https://arxiv.org/pdf/2508.02324) | 7,310 |
| 74 | 2025-07-28 | [GPT-Image-Edit-1.5M](papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset | arXiv 预印本 | 加州大学圣克鲁兹分校 / 爱丁堡大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2507.21033) | 6,615 |
| 75 | 2025-07-22 | [LMM4Edit](papers/2025-07_LMM4Edit/解读.md) | LMM4Edit: Benchmarking and Evaluating Multimodal Image Editing with LMMs | ACM Multimedia 2025 | 上海交通大学 / 电子科技大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2507.16193) | 2,544 |
| 76 | 2025-07-18 | [NoHumansRequired](papers/2025-07_NoHumansRequired/解读.md) | NoHumansRequired: Autonomous High-Quality Image Editing Triplet Mining | WACV（年份未核） | SALUTEDEV | 编辑 | [PDF](https://arxiv.org/pdf/2507.14119) | 6,730 |
| 77 | 2025-06-29 | [Ovis-U1](papers/2025-06_Ovis-U1/解读.md) | Ovis-U1 Technical Report | arXiv 预印本 | 阿里巴巴 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2506.23044) | 6,716 |
| 78 | 2025-06-23 | [OmniGen2](papers/2025-06_OmniGen2/解读.md) | OmniGen2: Towards Instruction-Aligned Multimodal Generation | arXiv 预印本 | 北京智源人工智能研究院 / 中国科学技术大学 等 4 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2506.18871) | 6,695 |
| 79 | 2025-06-18 | [Show-o2](papers/2025-06_Show-o2/解读.md) | Show-o2: Improved Native Unified Multimodal Models | NeurIPS 2025 | 新加坡国立大学 / 字节跳动 | 生成 | [PDF](https://arxiv.org/pdf/2506.15564) | 6,918 |
| 80 | 2025-06-17 | [FLUX-Kontext](papers/2025-06_FLUX-Kontext/解读.md) | FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space | arXiv 预印本 | 黑森林实验室 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2506.15742) | 8,679 |
| 81 | 2025-06-15 | [BPM](papers/2025-06_BPM/解读.md) | Balancing Preservation and Modification: A Region and Semantic Aware Metric for Instruction-Based Image Editing | ICML 2025 / PMLR 267 | 北京大学王选计算机技术研究所 | 编辑 | [PDF](https://arxiv.org/pdf/2506.13827) | 2,528 |
| 82 | 2025-06-15 | [ComplexBench-Edit](papers/2025-06_ComplexBench-Edit/解读.md) | ComplexBench-Edit: Benchmarking Complex Instruction-Driven Image Editing via Compositional Dependencies | ACM Multimedia 2025 | 华东师范大学 / 澳门大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2506.12830) | 2,534 |
| 83 | 2025-06-05 | [SeedEdit3](papers/2025-06_SeedEdit3/解读.md) | SeedEdit 3.0: Fast and High-Quality Generative Image Editing | arXiv 预印本 | 字节跳动 Seed | 编辑 | [PDF](https://arxiv.org/pdf/2506.05083) | 7,643 |
| 84 | 2025-06-03 | [RefEdit](papers/2025-06_RefEdit/解读.md) | RefEdit: A Benchmark and Method for Improving Instruction-based Image Editing Model on Referring Expressions | ICCV 2025 | 亚利桑那州立大学 | 编辑 | [PDF](https://arxiv.org/pdf/2506.03448) | 2,516 |
| 85 | 2025-06-03 | [UniWorld-V1](papers/2025-06_UniWorld-V1/解读.md) | UniWorld-V1: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation | arXiv 预印本 | 北京大学深圳研究生院 / 鹏城实验室 等 3 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2506.03147) | 6,657 |
| 86 | 2025-05-28 | [HiDream-I1](papers/2025-05_HiDream-I1/解读.md) | HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer | arXiv 预印本 | HiDream.ai | 生成 | [PDF](https://arxiv.org/pdf/2505.22705) | 7,337 |
| 87 | 2025-05-26 | [DICE](papers/2025-05_DICE/解读.md) | What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models | ICCV 2025 | 摩德纳和雷焦艾米利亚大学 / 比萨大学 等 4 家 | 编辑 | [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Baraldi_What_Changed_Detecting_and_Evaluating_Instruction-Guided_Image_Edits_with_Multimodal_ICCV_2025_paper.pdf) | 3,306 |
| 88 | 2025-05-26 | [ImgEdit](papers/2025-05_ImgEdit/解读.md) | ImgEdit: A Unified Image Editing Dataset and Benchmark | NeurIPS 2025 D&B | 北京大学深圳研究生院 / 鹏城实验室 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2505.20275) | 7,451 |
| 89 | 2025-05-22 | [Everyday-Image-Editing](papers/2025-05_Everyday-Image-Editing/解读.md) | Understanding Generative AI Capabilities in Everyday Image Editing Tasks | WACV 2026 | 阿尔伯塔大学 / 奥本大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2505.16181) | 2,986 |
| 90 | 2025-05-22 | [KRIS-Bench](papers/2025-05_KRIS-Bench/解读.md) | KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models | NeurIPS 2025 Datasets & Benchmarks | 东南大学 / 马克斯·普朗克信息学研究所 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2505.16707) | 7,494 |
| 91 | 2025-05-20 | [BAGEL](papers/2025-05_BAGEL/解读.md) | Emerging Properties in Unified Multimodal Pretraining | arXiv 预印本 | 字节跳动 Seed / 深圳先进技术研究院 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2505.14683) | 7,170 |
| 92 | 2025-05-16 | [GIE-Bench](papers/2025-05_GIE-Bench/解读.md) | GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing | ICLR 2026 投稿，未找到正式接收记录 | 苹果 / Meta | 编辑 | [PDF](https://arxiv.org/pdf/2505.11493) | 2,670 |
| 93 | 2025-05-14 | [BLIP3-o](papers/2025-05_BLIP3-o/解读.md) | BLIP3-o: A Family of Fully Open Unified Multimodal Models-Architecture, Training and Dataset | arXiv 预印本 | Salesforce Research / 马里兰大学 等 5 家 | 生成 | [PDF](https://arxiv.org/pdf/2505.09568) | 6,887 |
| 94 | 2025-05-12 | [DanceGRPO](papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | arXiv 预印本 | 字节跳动 Seed / 香港大学 | 生成 | [PDF](https://arxiv.org/pdf/2505.07818) | 7,294 |
| 95 | 2025-05-08 | [Flow-GRPO](papers/2025-05_Flow-GRPO/解读.md) | Flow-GRPO: Training Flow Matching Models via Online RL | NeurIPS（年份未核） | 香港中文大学多媒体实验室 / 清华大学 等 5 家 | 生成 | [PDF](https://arxiv.org/pdf/2505.05470) | 6,502 |
| 96 | 2025-05-01 | [HATIE](papers/2025-05_HATIE/解读.md) | Towards Scalable Human-aligned Benchmark for Text-guided Image Editing | CVPR 2025 Highlight | 首尔大学数据科学研究生院 | 编辑 | [PDF](https://arxiv.org/pdf/2505.00502) | 6,842 |
| 97 | 2025-05-01 | [T2I-R1](papers/2025-05_T2I-R1/解读.md) | T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT | NeurIPS（年份未核） | 香港中文大学MMLab / 香港中文大学MiuLar Lab 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2505.00703) | 6,876 |
| 98 | 2025-04-29 | [ICEdit](papers/2025-04_ICEdit/解读.md) | In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer | NeurIPS 2025 | 浙江大学 / 哈佛大学 | 编辑 | [PDF](https://arxiv.org/pdf/2504.20690) | 6,865 |
| 99 | 2025-04-24 | [Step1X-Edit](papers/2025-04_Step1X-Edit/解读.md) | Step1X-Edit: A Practical Framework for General Image Editing | arXiv 预印本 | 阶跃星辰 | 编辑 | [PDF](https://arxiv.org/pdf/2504.17761) | 7,396 |
| 100 | 2025-04-23 | [DreamO](papers/2025-04_DreamO/解读.md) | DreamO: A Unified Framework for Image Customization | SIGGRAPH（年份未核） | 字节跳动智能创作团队 / 北京大学 | 生成 | [PDF](https://arxiv.org/pdf/2504.16915) | 7,727 |
| 101 | 2025-04-21 | [Insert-Anything](papers/2025-04_Insert-Anything/解读.md) | Insert Anything: Image Insertion via In-Context Editing in DiT | arXiv 预印本 | 浙江大学 / 哈佛大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2504.15009) | 6,580 |
| 102 | 2025-04-17 | [Complex-Edit](papers/2025-04_Complex-Edit/解读.md) | $texttt{Complex-Edit}$: CoT-Like Instruction Generation for Complexity-Controllable Image Editing Benchmark | TMLR | 加州大学圣克鲁兹分校 / 爱丁堡大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2504.13143) | 8,329 |
| 103 | 2025-04-08 | [MetaQuery](papers/2025-04_MetaQuery/解读.md) | Transfer between Modalities with MetaQueries | arXiv 预印本 | Meta / 纽约大学 | 生成 | [PDF](https://arxiv.org/pdf/2504.06256) | 7,502 |
| 104 | 2025-04-03 | [RISEBench](papers/2025-04_RISEBench/解读.md) | Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing | NeurIPS（年份未核） | 上海交通大学 / 上海人工智能实验室 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2504.02826) | 7,917 |
| 105 | 2025-04-02 | [UNO](papers/2025-04_UNO/解读.md) | Less-to-More Generalization: Unlocking More Controllability by In-Context Generation | ICCV（年份未核） | 字节跳动智能创作团队 | 生成 | [PDF](https://arxiv.org/pdf/2504.02160) | 7,202 |
| 106 | 2025-03-25 | [FireEdit](papers/2025-03_FireEdit/解读.md) | FireEdit: Fine-grained Instruction-based Image Editing via Region-aware Vision Language Model | CVPR 2025 | 中山大学深圳校区 / 腾讯混元 等 4 家 | 编辑 | [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_FireEdit_Fine-grained_Instruction-based_Image_Editing_via_Region-aware_Vision_Language_Model_CVPR_2025_paper.pdf) | 3,066 |
| 107 | 2025-03-13 | [GoT](papers/2025-03_GoT/解读.md) | GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing | arXiv 预印本 | 香港中文大学MMLab / 香港大学 等 5 家 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2503.10639) | 7,356 |
| 108 | 2025-03-10 | [EasyControl](papers/2025-03_EasyControl/解读.md) | EasyControl: Adding Efficient and Flexible Control for Diffusion Transformer | ICCV（年份未核） | Tiamat AI / 上海科技大学 等 4 家 | 生成 | [PDF](https://arxiv.org/pdf/2503.07027) | 7,188 |
| 109 | 2025-01-29 | [Janus-Pro](papers/2025-01_Janus-Pro/解读.md) | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | arXiv 预印本 | 深度求索 | 生成 | [PDF](https://arxiv.org/pdf/2501.17811) | 8,116 |
| 110 | 2025-01-05 | [ACEpp](papers/2025-01_ACEpp/解读.md) | ACE++: Instruction-Based Image Creation and Editing via Context-Aware Content Filling | ICCV Workshops 2025 | 通义实验室 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2501.02487) | 7,487 |
| 111 | 2024-12-10 | [UniReal](papers/2024-12_UniReal/解读.md) | UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics | CVPR（年份未核） | 香港大学 / Adobe | 生成+编辑 | [PDF](https://arxiv.org/pdf/2412.07774) | 6,953 |
| 112 | 2024-12 | [Grok-Aurora](papers/2024-12_Grok-Aurora/解读.md) | Grok (Aurora) | 官方资料（无独立论文） | xAI | 生成 | [官方来源](https://docs.x.ai/docs/models) | 330 |
| 113 | 2024-11-27 | [FlowChef](papers/2024-12_FlowChef/解读.md) | FlowChef: Steering of Rectified Flow Models for Controlled Generations | ICCV 2025 | 亚利桑那州立大学 / 罗格斯大学 | 编辑 | [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Patel_FlowChef_Steering_of_Rectified_Flow_Models_for_Controlled_Generations_ICCV_2025_paper.pdf) | 4,314 |
| 114 | 2024-11-24 | [AnyEdit](papers/2024-11_AnyEdit/解读.md) | AnyEdit: Mastering Unified High-Quality Image Editing for Any Idea | CVPR 2025 | 浙江大学 / 南洋理工大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2411.15738) | 7,500 |
| 115 | 2024-11-22 | [OminiControl](papers/2024-11_OminiControl/解读.md) | OminiControl: Minimal and Universal Control for Diffusion Transformer | ICCV 2025 | 新加坡国立大学 | 编辑 | [PDF](https://arxiv.org/pdf/2411.15098) | 6,543 |
| 116 | 2024-11-14 | [MagicQuill](papers/2024-11_MagicQuill/解读.md) | MagicQuill: An Intelligent Interactive Image Editing System | CVPR 2025 | 香港科技大学 / 蚂蚁集团 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2411.09703) | 7,389 |
| 117 | 2024-11-11 | [Add-it](papers/2024-11_Add-it/解读.md) | Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models | ICLR（年份未核） | 英伟达 / 特拉维夫大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2411.07232) | 7,033 |
| 118 | 2024-11-11 | [OmniEdit](papers/2024-11_OmniEdit/解读.md) | OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision | ICLR（年份未核） | 滑铁卢大学 / 威斯康星大学麦迪逊分校 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2411.07199) | 7,402 |
| 119 | 2024-11-11 | [SeedEdit](papers/2024-11_SeedEdit/解读.md) | SeedEdit: Align Image Re-Generation to Image Editing | arXiv 预印本 | 字节跳动 Seed 团队 | 编辑 | [PDF](https://arxiv.org/pdf/2411.06686) | 7,623 |
| 120 | 2024-11-07 | [RF-Solver-Edit](papers/2024-11_RF-Solver-Edit/解读.md) | Taming Rectified Flow for Inversion and Editing | ICML 2025 | 清华大学 / 腾讯PCG ARC Lab 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2411.04746) | 7,204 |
| 121 | 2024-10-31 | [In-Context-LoRA](papers/2024-10_In-Context-LoRA/解读.md) | In-Context LoRA for Diffusion Transformers | arXiv 预印本 | 通义实验室 / 浙江大学 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2410.23775) | 6,951 |
| 122 | 2024-10-14 | [RF-Inversion](papers/2024-10_RF-Inversion/解读.md) | Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations | ICLR（年份未核） | 谷歌 / 德克萨斯大学奥斯汀分校 | 编辑 | [PDF](https://arxiv.org/pdf/2410.10792) | 7,312 |
| 123 | 2024-10-09 | [REPA](papers/2024-10_REPA/解读.md) | Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think | ICLR（年份未核） | 韩国科学技术院 / 高丽大学 等 4 家 | 生成 | [PDF](https://arxiv.org/pdf/2410.06940) | 3,143 |
| 124 | 2024-09-27 | [Emu3](papers/2024-09_Emu3/解读.md) | Emu3: Next-Token Prediction is All You Need | arXiv 预印本 | 北京智源人工智能研究院 | 生成 | [PDF](https://arxiv.org/pdf/2409.18869) | 7,382 |
| 125 | 2024-09-17 | [OmniGen](papers/2024-09_OmniGen/解读.md) | OmniGen: Unified Image Generation | CVPR（年份未核） | 北京智源人工智能研究院 | 生成+编辑 | [PDF](https://arxiv.org/pdf/2409.11340) | 8,139 |
| 126 | 2024-08-26 | [I2EBench](papers/2024-08_I2EBench/解读.md) | I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing | NeurIPS 2024 Main | 厦门大学 | 编辑 | [PDF](https://arxiv.org/pdf/2408.14180) | 2,518 |
| 127 | 2024-08-22 | [Show-o](papers/2024-08_Show-o/解读.md) | Show-o: One Single Transformer to Unify Multimodal Understanding and Generation | ICLR 2025 | 新加坡国立大学 Show Lab / 字节跳动 | 生成 | [PDF](https://arxiv.org/pdf/2408.12528) | 7,514 |
| 128 | 2024-08-20 | [Transfusion](papers/2024-08_Transfusion/解读.md) | Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model | arXiv 预印本 | Meta / Waymo 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2408.11039) | 7,019 |
| 129 | 2024-08-01 | [FLUX.1](papers/2024-08_FLUX.1/解读.md) | FLUX.1 Model Family | Black Forest Labs official launch blog/model card | Black Forest Labs | 生成 | [官方来源](https://bfl.ai/blog/24-08-01-bfl) | 634 |
| 130 | 2024-08-01 | [TurboEdit](papers/2024-08_TurboEdit/解读.md) | TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models | SIGGRAPH（年份未核） | 特拉维夫大学 / 英伟达 | 编辑 | [PDF](https://arxiv.org/pdf/2408.00735) | 6,973 |
| 131 | 2024-07-07 | [UltraEdit](papers/2024-07_UltraEdit/解读.md) | UltraEdit: Instruction-based Fine-Grained Image Editing at Scale | NeurIPS 2024 | 北京大学多媒体信息处理全国重点实验室 / 北京通用人工智能研究院 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2407.05282) | 7,074 |
| 132 | 2024-07-05 | [Kolors](papers/2024-07_Kolors/解读.md) | Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis | 快手可图技术报告 | 快手 | 生成 | [PDF](https://raw.githubusercontent.com/Kwai-Kolors/Kolors/master/imgs/Kolors_paper.pdf) | 3,470 |
| 133 | 2024-06-17 | [MAR](papers/2024-06_MAR/解读.md) | Autoregressive Image Generation without Vector Quantization | NeurIPS（年份未核） | 麻省理工学院计算机科学与人工智能实验室 / 谷歌 DeepMind 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2406.11838) | 3,458 |
| 134 | 2024-06-11 | [MimicBrush](papers/2024-06_MimicBrush/解读.md) | Zero-shot Image Editing with Reference Imitation | NeurIPS（年份未核） | 香港大学 / 阿里巴巴 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2406.07547) | 8,536 |
| 135 | 2024-05-16 | [Chameleon](papers/2024-05_Chameleon/解读.md) | Chameleon: Mixed-Modal Early-Fusion Foundation Models | arXiv 预印本 | FAIR at Meta | 生成 | [PDF](https://arxiv.org/pdf/2405.09818) | 8,109 |
| 136 | 2024-05-07 | [SEED-Data-Edit](papers/2024-05_SEED-Data-Edit/解读.md) | SEED-Data-Edit Technical Report: A Hybrid Dataset for Instructional Image Editing | arXiv 预印本 | 腾讯 AI Lab / 腾讯 PCG ARC Lab | 编辑 | [PDF](https://arxiv.org/pdf/2405.04007) | 6,626 |
| 137 | 2024-04-22 | [SEED-X](papers/2024-04_SEED-X/解读.md) | SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation | arXiv 预印本 | 腾讯 AI Lab / ARC Lab, 腾讯 PCG | 生成+编辑 | [PDF](https://arxiv.org/pdf/2404.14396) | 6,648 |
| 138 | 2024-04-15 | [HQ-Edit](papers/2024-04_HQ-Edit/解读.md) | HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing | ICLR 2025 | 加州大学圣克鲁兹分校 | 编辑 | [PDF](https://arxiv.org/pdf/2404.09990) | 7,232 |
| 139 | 2024-04-03 | [VAR](papers/2024-04_VAR/解读.md) | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | NeurIPS（年份未核） | 北京大学 / 字节跳动 | 生成 | [PDF](https://arxiv.org/pdf/2404.02905) | 8,136 |
| 140 | 2024-03-21 | [ReNoise](papers/2024-03_ReNoise/解读.md) | ReNoise: Real Image Inversion Through Iterative Noising | ECCV（年份未核） | 特拉维夫大学 / 谷歌研究院 | 编辑 | [PDF](https://arxiv.org/pdf/2403.14602) | 6,706 |
| 141 | 2024-03-11 | [BrushNet](papers/2024-03_BrushNet/解读.md) | BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion | ECCV（年份未核） | 腾讯PCG ARC Lab / 香港中文大学 | 编辑 | [PDF](https://arxiv.org/pdf/2403.06976) | 6,745 |
| 142 | 2024-03-05 | [SD3-RectifiedFlow](papers/2024-03_SD3-RectifiedFlow/解读.md) | Scaling Rectified Flow Transformers for High-Resolution Image Synthesis | ICML（年份未核） | Stability AI | 生成 | [PDF](https://arxiv.org/pdf/2403.03206) | 6,564 |
| 143 | 2024-02-04 | [DiffEditor](papers/2024-02_DiffEditor/解读.md) | DiffEditor: Boosting Accuracy and Flexibility on Diffusion-based Image Editing | CVPR（年份未核） | 北京大学深圳研究生院电子与计算机工程学院 / 腾讯PCG ARC Lab | 编辑 | [PDF](https://arxiv.org/pdf/2402.02583) | 7,254 |
| 144 | 2024-01-15 | [InstantID](papers/2024-01_InstantID/解读.md) | InstantID: Zero-shot Identity-Preserving Generation in Seconds | arXiv 预印本 | InstantX Team / 小红书 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2401.07519) | 6,825 |
| 145 | 2024-01-03 | [Instruct-Imagen](papers/2024-01_Instruct-Imagen/解读.md) | Instruct-Imagen: Image Generation with Multi-modal Instruction | CVPR（年份未核） | 谷歌DeepMind / 谷歌研究院 | 生成 | [PDF](https://arxiv.org/pdf/2401.01952) | 7,210 |
| 146 | 2023-12-20 | [Emu2](papers/2023-12_Emu2/解读.md) | Generative Multimodal Models are In-Context Learners | CVPR 2024 | 北京智源人工智能研究院 / 清华大学 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2312.13286) | 6,701 |
| 147 | 2023-12-11 | [SmartEdit](papers/2023-12_SmartEdit/解读.md) | SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models | CVPR（年份未核） | 香港中文大学（深圳）数据科学学院，深圳市大数据研究院 / 腾讯PCG ARC实验室 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2312.06739) | 6,742 |
| 148 | 2023-12-07 | [InfEdit](papers/2023-12_InfEdit/解读.md) | Inversion-Free Image Editing with Natural Language | arXiv 预印本 | 密歇根大学 / 加州大学伯克利分校 | 编辑 | [PDF](https://arxiv.org/pdf/2312.04965) | 6,814 |
| 149 | 2023-12-07 | [PhotoMaker](papers/2023-12_PhotoMaker/解读.md) | PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | CVPR（年份未核） | 南开大学 / 腾讯PCG ARC Lab 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2312.04461) | 7,001 |
| 150 | 2023-12-06 | [PowerPaint](papers/2023-12_PowerPaint/解读.md) | A Task is Worth One Word: Learning with Task Prompts for High-Quality Versatile Image Inpainting | ECCV（年份未核） | 清华大学深圳国际研究生院 / 上海人工智能实验室 | 编辑 | [PDF](https://arxiv.org/pdf/2312.03594) | 7,204 |
| 151 | 2023-12-04 | [StyleAligned](papers/2023-12_StyleAligned/解读.md) | Style Aligned Image Generation via Shared Attention | CVPR（年份未核） | 谷歌研究院 / 特拉维夫大学 | 生成 | [PDF](https://arxiv.org/pdf/2312.02133) | 7,216 |
| 152 | 2023-11-30 | [DMD](papers/2023-11_DMD/解读.md) | One-step Diffusion with Distribution Matching Distillation | CVPR（年份未核） | 麻省理工学院 / Adobe Research | 生成 | [PDF](https://arxiv.org/pdf/2311.18828) | 3,540 |
| 153 | 2023-11-28 | [LEDITSpp](papers/2023-11_LEDITSpp/解读.md) | LEDITS++: Limitless Image Editing using Text-to-Image Models | 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (C | 达姆施塔特工业大学 / 德国人工智能研究中心 等 4 家 | 编辑 | [PDF](https://arxiv.org/pdf/2311.16711) | 6,869 |
| 154 | 2023-11-20 | [Concept-Sliders](papers/2023-11_Concept-Sliders/解读.md) | Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models | ECCV（年份未核） | 东北大学 / 麻省理工学院 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2311.12092) | 7,827 |
| 155 | 2023-11-16 | [Emu-Edit](papers/2023-11_Emu-Edit/解读.md) | Emu Edit: Precise Image Editing via Recognition and Generation Tasks | CVPR 2024 | GenAI, Meta | 编辑 | [PDF](https://arxiv.org/pdf/2311.10089) | 6,854 |
| 156 | 2023-11-06 | [Cross-Image-Attention](papers/2023-11_Cross-Image-Attention/解读.md) | Cross-Image Attention for Zero-Shot Appearance Transfer | arXiv 预印本 | 特拉维夫大学 | 编辑 | [PDF](https://arxiv.org/pdf/2311.03335) | 7,423 |
| 157 | 2023-10-19 | [DALL·E 3](papers/2023-10_DALL-E-3/解读.md) | Improving Image Generation with Better Captions | OpenAI 报告 | OpenAI / 微软 | 生成 | [PDF](https://cdn.openai.com/papers/dall-e-3.pdf) | 3,183 |
| 158 | 2023-10-17 | [GenEval](papers/2023-10_GenEval/解读.md) | GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment | NeurIPS（年份未核） | 华盛顿大学 / 艾伦人工智能研究所 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2310.11513) | 3,290 |
| 159 | 2023-09-30 | [PixArt-alpha](papers/2023-09_PixArt-alpha/解读.md) | PixArt-$alpha$: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis | ICLR（年份未核） | 华为诺亚方舟实验室 / 大连理工大学 等 4 家 | 生成 | [PDF](https://arxiv.org/pdf/2310.00426) | 6,861 |
| 160 | 2023-09-29 | [MGIE](papers/2023-09_MGIE/解读.md) | Guiding Instruction-based Image Editing via Multimodal Large Language Models | ICLR 2024 | 加州大学圣塔芭芭拉分校 / 苹果 | 编辑 | [PDF](https://arxiv.org/pdf/2309.17102) | 8,943 |
| 161 | 2023-09-07 | [InstructDiffusion](papers/2023-09_InstructDiffusion/解读.md) | InstructDiffusion: A Generalist Modeling Interface for Vision Tasks | CVPR（年份未核） | 微软亚洲研究院 | 编辑 | [PDF](https://arxiv.org/pdf/2309.03895) | 6,804 |
| 162 | 2023-08-13 | [IP-Adapter](papers/2023-08_IP-Adapter/解读.md) | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | arXiv 预印本 | 腾讯 AI Lab | 生成 | [PDF](https://arxiv.org/pdf/2308.06721) | 7,379 |
| 163 | 2023-07-18 | [AnyDoor](papers/2023-07_AnyDoor/解读.md) | AnyDoor: Zero-shot Object-level Image Customization | CVPR2024 | 香港大学 / 阿里巴巴 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2307.09481) | 7,129 |
| 164 | 2023-07-05 | [DragonDiffusion](papers/2023-07_DragonDiffusion/解读.md) | DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | ICLR（年份未核） | 北京大学深圳研究生院电子与计算机工程学院 / 腾讯 PCG ARC Lab | 编辑 | [PDF](https://arxiv.org/pdf/2307.02421) | 7,518 |
| 165 | 2023-07-04 | [SDXL](papers/2023-07_SDXL/解读.md) | SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis | ICLR（年份未核） | Stability AI, Applied Research | 生成 | [PDF](https://arxiv.org/pdf/2307.01952) | 3,051 |
| 166 | 2023-06-26 | [DragDiffusion](papers/2023-06_DragDiffusion/解读.md) | DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | CVPR（年份未核） | 新加坡国立大学 / 字节跳动 | 编辑 | [PDF](https://arxiv.org/pdf/2306.14435) | 7,065 |
| 167 | 2023-06-16 | [MagicBrush](papers/2023-06_MagicBrush/解读.md) | MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | NeurIPS 2023 Datasets and Benchmarks | 俄亥俄州立大学 / 滑铁卢大学 | 编辑 | [PDF](https://arxiv.org/pdf/2306.10012) | 7,080 |
| 168 | 2023-06-01 | [Self-Guidance](papers/2023-06_Self-Guidance/解读.md) | Diffusion Self-Guidance for Controllable Image Generation | NeurIPS（年份未核） | 加州大学伯克利分校 / 谷歌研究院 | 生成 | [PDF](https://arxiv.org/pdf/2306.00986) | 7,259 |
| 169 | 2023-05-29 | [InstructEdit](papers/2023-05_InstructEdit/解读.md) | InstructEdit: Improving Automatic Masks for Diffusion-based Image Editing With User Instructions | arXiv 预印本 | 阿卜杜拉国王科技大学 | 编辑 | [PDF](https://arxiv.org/pdf/2305.18047) | 6,897 |
| 170 | 2023-05-18 | [DragGAN](papers/2023-05_DragGAN/解读.md) | Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold | SIGGRAPH 2023 | 马克斯·普朗克信息学研究所 / Saarbrücken Research Center for Visual Computing, Interaction and AI 等 5 家 | 编辑 | [PDF](https://arxiv.org/pdf/2305.10973) | 7,007 |
| 171 | 2023-04-17 | [MasaCtrl](papers/2023-04_MasaCtrl/解读.md) | MasaCtrl: Tuning-Free Mutual Self-Attention Control for Consistent Image Synthesis and Editing | ICCV（年份未核） | 东京大学 / 腾讯PCG ARC Lab | 生成+编辑 | [PDF](https://arxiv.org/pdf/2304.08465) | 6,562 |
| 172 | 2023-04-13 | [Inpaint-Anything](papers/2023-04_Inpaint-Anything/解读.md) | Inpaint Anything: Segment Anything Meets Image Inpainting | arXiv 预印本 | 中国科学技术大学 / 东方理工高等研究院 | 编辑 | [PDF](https://arxiv.org/pdf/2304.06790) | 8,149 |
| 173 | 2023-04-13 | [Rich-Text](papers/2023-04_Rich-Text/解读.md) | Expressive Text-to-Image Generation with Rich Text | ICCV 2023；正式题名为 *Expressive Text-to-Image Generation with Rich Text* | **未核** | 生成 | [PDF](https://arxiv.org/pdf/2304.06720) | 6,817 |
| 174 | 2023-04-05 | [SAM](papers/2023-04_SAM/解读.md) | Segment Anything | ICCV（年份未核） | Meta AI Research, FAIR | 编辑 | [PDF](https://arxiv.org/pdf/2304.02643) | 6,768 |
| 175 | 2023-03-16 | [HIVE](papers/2023-03_HIVE/解读.md) | HIVE: Harnessing Human Feedback for Instructional Visual Editing | CVPR（年份未核） | Salesforce AI Research / 斯坦福大学 | 编辑 | [PDF](https://arxiv.org/pdf/2303.09618) | 7,788 |
| 176 | 2023-03-02 | [Consistency Models](papers/2023-03_Consistency-Models/解读.md) | Consistency Models | ICML（年份未核） | OpenAI | 生成 | [PDF](https://arxiv.org/pdf/2303.01469) | 3,194 |
| 177 | 2023-02-16 | [T2I-Adapter](papers/2023-02_T2I-Adapter/解读.md) | T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | AAAI（年份未核） | 北京大学深圳研究生院 / 腾讯PCG ARC Lab 等 4 家 | 生成 | [PDF](https://arxiv.org/pdf/2302.08453) | 7,127 |
| 178 | 2023-02-10 | [ControlNet](papers/2023-02_ControlNet/解读.md) | Adding Conditional Control to Text-to-Image Diffusion Models | ICCV 2023 | 斯坦福大学 | 生成 | [PDF](https://arxiv.org/pdf/2302.05543) | 7,943 |
| 179 | 2023-02-06 | [pix2pix-zero](papers/2023-02_pix2pix-zero/解读.md) | Zero-shot Image-to-Image Translation | arXiv 预印本 | 卡内基梅隆大学 / Adobe Research | 编辑 | [PDF](https://arxiv.org/pdf/2302.03027) | 6,692 |
| 180 | 2022-12-13 | [Imagen-Editor-EditBench](papers/2022-12_Imagen-Editor-EditBench/解读.md) | Imagen Editor and EditBench: Advancing and Evaluating Text-Guided Image Inpainting | CVPR 2023 Camera Ready | 谷歌研究院 | 编辑 | [PDF](https://arxiv.org/pdf/2212.06909) | 8,394 |
| 181 | 2022-12-08 | [Custom-Diffusion](papers/2022-12_Custom-Diffusion/解读.md) | Multi-Concept Customization of Text-to-Image Diffusion | CVPR（年份未核） | 卡内基梅隆大学 / 清华大学 等 3 家 | 生成 | [PDF](https://arxiv.org/pdf/2212.04488) | 7,128 |
| 182 | 2022-11-23 | [Paint-by-Example](papers/2022-11_Paint-by-Example/解读.md) | Paint by Example: Exemplar-based Image Editing with Diffusion Models | CVPR 2023 | 中国科学技术大学 / 微软亚洲研究院 | 编辑 | [PDF](https://arxiv.org/pdf/2211.13227) | 7,577 |
| 183 | 2022-11-22 | [EDICT](papers/2022-11_EDICT/解读.md) | EDICT: Exact Diffusion Inversion via Coupled Transformations | CVPR（年份未核） | 赛富时研究院 | 编辑 | [PDF](https://arxiv.org/pdf/2211.12446) | 6,614 |
| 184 | 2022-11-22 | [Plug-and-Play](papers/2022-11_Plug-and-Play/解读.md) | Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation | CVPR 2023 | 魏茨曼科学研究所 | 编辑 | [PDF](https://arxiv.org/pdf/2211.12572) | 7,284 |
| 185 | 2022-11-17 | [InstructPix2Pix](papers/2022-11_InstructPix2Pix/解读.md) | InstructPix2Pix: Learning to Follow Image Editing Instructions | CVPR 2023 | 加州大学伯克利分校 | 编辑 | [PDF](https://arxiv.org/pdf/2211.09800) | 7,603 |
| 186 | 2022-11-17 | [Null-text-Inversion](papers/2022-11_Null-text-Inversion/解读.md) | Null-text Inversion for Editing Real Images using Guided Diffusion Models | CVPR 2023 | 谷歌研究院 / 特拉维夫大学布拉瓦特尼克计算机科学学院 | 编辑 | [PDF](https://arxiv.org/pdf/2211.09794) | 7,202 |
| 187 | 2022-10-20 | [DiffEdit](papers/2022-10_DiffEdit/解读.md) | DiffEdit: Diffusion-based semantic image editing with mask guidance | ICLR（年份未核） | Meta AI / 索邦大学 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2210.11427) | 7,215 |
| 188 | 2022-10-17 | [Imagic](papers/2022-10_Imagic/解读.md) | Imagic: Text-Based Real Image Editing with Diffusion Models | CVPR（年份未核） | 谷歌研究院 / 以色列理工学院 等 3 家 | 编辑 | [PDF](https://arxiv.org/pdf/2210.09276) | 7,136 |
| 189 | 2022-08-25 | [DreamBooth](papers/2022-08_DreamBooth/解读.md) | DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | CVPR 2023 | 谷歌研究院 / 波士顿大学 | 生成 | [PDF](https://arxiv.org/pdf/2208.12242) | 6,553 |
| 190 | 2022-08-02 | [Prompt-to-Prompt](papers/2022-08_Prompt-to-Prompt/解读.md) | Prompt-to-Prompt Image Editing with Cross Attention Control | ICLR（年份未核） | 谷歌研究院 / 特拉维夫大学 | 编辑 | [PDF](https://arxiv.org/pdf/2208.01626) | 7,138 |
| 191 | 2022-08-02 | [Textual-Inversion](papers/2022-08_Textual-Inversion/解读.md) | An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | ICLR（年份未核） | 特拉维夫大学 / 英伟达 | 生成 | [PDF](https://arxiv.org/pdf/2208.01618) | 6,900 |
| 192 | 2022-07-26 | [Classifier-Free-Guidance](papers/2022-07_Classifier-Free-Guidance/解读.md) | Classifier-Free Diffusion Guidance | arXiv 预印本 | 谷歌大脑 | 生成 | [PDF](https://arxiv.org/pdf/2207.12598) | 6,581 |
| 193 | 2022-06-06 | [Blended-Latent-Diffusion](papers/2022-06_Blended-Latent-Diffusion/解读.md) | Blended Latent Diffusion | SIGGRAPH 2023 | 耶路撒冷希伯来大学 / 赖希曼大学 | 编辑 | [PDF](https://arxiv.org/pdf/2206.02779) | 6,702 |
| 194 | 2021-12-20 | [Latent-Diffusion](papers/2021-12_Latent-Diffusion/解读.md) | High-Resolution Image Synthesis with Latent Diffusion Models | CVPR 2022 | 慕尼黑大学 & 海德堡大学 IWR / Runway ML | 生成 | [PDF](https://arxiv.org/pdf/2112.10752) | 7,160 |
| 195 | 2021-08-02 | [SDEdit](papers/2021-08_SDEdit/解读.md) | SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations | ICLR（年份未核） | 斯坦福大学 / 卡内基梅隆大学 | 编辑 | [PDF](https://arxiv.org/pdf/2108.01073) | 7,249 |

## 仓库长什么样

```
image-gen-edit-papers/
├── README.md                       ← 本文件。收什么 + 怎么用 + 195 项全量清单
├── LICENSE                         ← CC BY 4.0
├── papers/                         ← 195 个论文目录，名字就是 YYYY-MM_简称
│   └── YYYY-MM_简称/
│       ├── 解读.md                  ← 中文笔记（唯一正文）
│       ├── meta.json               ← 单篇元数据 + 核验记录
│       └── paper.pdf               ← 不在仓库里，跑 scripts/fetch_pdfs.py 下载
├── docs/
│   ├── INDEX.md                     ← 按技术脉络与任务分组的索引
│   ├── 总结分析.md                   ← 跨论文结论（覆盖最初 160 篇 / 15 条脉络）
│   ├── 可信度与产出.md                ← 做过哪些校验、哪些地方已知会出错
│   ├── prompt.md                     ← v2 深读规范（原样作为 system prompt）
│   ├── LARK论文短版解读_PROMPT.md      ← 短版解读规范
│   ├── 影响力口径.md                  ← 生成侧选文判据：Hub 落地 + 引用速率
│   ├── 备选池.md                     ← 生成侧候选池是怎么筛出来的
│   └── review/                       ← 人工核验产出：4 份 manifest + 4 份错误报告
├── scripts/
│   ├── papers.json                  ← 元数据唯一事实来源，README 与 INDEX 由它生成
│   ├── gen_readme.py                ← 渲染本文件
│   ├── build_index.py               ← 渲染 docs/INDEX.md
│   ├── fetch_pdfs.py                ← 按 meta.json 把 arXiv / CVF 原文拉回本地
│   ├── pdf_sources.py               ← 直链推导规则 + 默认规则会取错的例外
│   ├── verify_pdf_links.py          ← 逐条比对远端与本地字节数
│   └── （生成侧管线）discover_hf.py / fetch_cites.py / hub_signals.py / rank.py …
└── _work/                          ← 生产管线脚本（只提交 .py，日志和中间产物不进仓库）
```

## 已知没核到的

| 项 | 状态 |
| --- | --- |
| 机构标 **未核** 的 2 篇 | ug-fight-dpo、Rich-Text。这几篇 PDF 首页的抽取文本里确实没有作者机构，不编 |
| 机构一列的来源 | 只认 PDF 首页作者块（模型抽取，人抽查）。**没用 OpenAlex 补**——它对 arXiv 预印本几乎没有机构字段，且已知会误配 |
| 发表信息 | 优先用 `docs/review/` 四份人工核验 manifest；其次 arXiv `journal_ref`；再次 arXiv `comment` 里明确写「已接收」的。**只认接收，不认投稿**——写「submitted to」的一律记作预印本。逐条来源记在 `papers.json` 的 `venue_source` |
| 引用量 | 快照，非实时。provider 混用（人工核验轮用 Semantic Scholar，补齐用 OpenAlex），**不同 provider 的数字不做严格横向排名**。逐条记在 `cites_source` |
| 没有独立论文的 4 项 | GPT-Image-2、Qwen-Image-Edit-2511、Grok-Aurora、FLUX.1。笔记只记录官方资料和核验边界，不能用来反推架构、训练数据或身份保持机制 |
| 2026 年那批的选文 | 38 篇里有 33 篇是模型从 1,123 篇候选里筛出来的，**人工只定了标准**。详见 [总结分析.md §5](docs/总结分析.md) |
| 跨论文结论的覆盖范围 | [总结分析.md](docs/总结分析.md) 写的是最初 160 篇 / 15 条脉络。2026-09 并入的生成侧论文和新增的 2 条脉络还没进那份分析 |
| 解读正文 | 机器生成，未逐句人工复核。数字与结论以原文为准 |
