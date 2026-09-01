# 图像生成与编辑论文库索引

> 读者：要系统补齐 2021–2026 图像生成与编辑技术脉络的人
> 目标：按脉络挑论文，点进任意一篇能直接读完整深读笔记，不用再读原文
> 覆盖：195 项，2021-08 ～ 2026-08
> 最后核对：2026-09-01

[README](../README.md) 是一张按时间倒序（最新在最前）的平表，用来查。本页按技术脉络分组，用来读。
每篇的「一句话」摘自该篇 `解读.md` 第 1 节首句，依据是论文原文，不是另写的导读。
跨论文的结论在 [总结分析.md](总结分析.md)，笔记能信到什么程度在 [可信度与产出.md](可信度与产出.md)。

## 任务分布

一篇论文可以同时是生成和编辑，**27 篇就是这样**——这是本库按模态而不按任务划分的原因。

| 任务 | 篇数 |
| --- | ---: |
| 编辑 | 140 |
| 生成 | 82 |
| 两者都是 | 27 |

两者都是的 27 篇：MasaCtrl、SEED-X、OmniGen、UniReal、ACEpp、GoT、BAGEL、UniWorld-V1、FLUX-Kontext、OmniGen2、Ovis-U1、EditVerse、Seedream4、OpenGPT-4o-Image、Lumina-DiMOO、DreamOmni2、Emu3.5、Z-Image、nextflow、unireason、internvl-u、GPT-Image-2、Qwen-Image-2.0、sensenova-u1、arm-unified、hydra-x、qwen-image-rl

## 贡献类型

| 类型 | 篇数 |
| --- | ---: |
| 方法 | 107 |
| 模型 | 34 |
| 基准 | 30 |
| 数据集 | 12 |
| 奖励与 RL | 7 |
| 综述 | 5 |

## 17 条脉络

### 生成骨干：编辑方法赖以运行的底座（14 篇）

编辑方法跑在什么模型上。潜空间扩散、无分类器引导、整流流、各家开源与闭源旗舰——不读这条线，后面所有编辑方法的「在哪一层动手」都无从判断。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2021-12 | [Latent-Diffusion](../papers/2021-12_Latent-Diffusion/解读.md) | High-Resolution Image Synthesis with Latent Diffusion Models | 方法 | 生成 | 这篇论文提出 Latent Diffusion Models（LDMs，潜在扩散模型），核心做法是把扩散模型（Diffusion Models, DMs）的训练和推理从高维像素空间搬到一个预训练自编码器（autoencoder）产生的低维潜在空间。 |
| 2022-07 | [Classifier-Free-Guidance](../papers/2022-07_Classifier-Free-Guidance/解读.md) | Classifier-Free Diffusion Guidance | 方法 | 生成 | 这篇论文提出“无分类器引导”（classifier-free guidance，CFG），用于扩散模型的条件生成。 |
| 2023-07 | [SDXL](../papers/2023-07_SDXL/解读.md) | SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis | 模型 | 生成 | 这篇论文解决的是 Stable Diffusion 在高分辨率、多宽高比文本生成中质量不足、物体被意外裁剪、局部细节差的问题。 |
| 2023-09 | [PixArt-alpha](../papers/2023-09_PixArt-alpha/解读.md) | PixArt-$alpha$: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis | 方法 | 生成 | PixArt-α（PixArt-alpha）是一篇关于高效训练文本到图像（text-to-image, T2I）扩散 Transformer 的技术报告。 |
| 2024-03 | [SD3-RectifiedFlow](../papers/2024-03_SD3-RectifiedFlow/解读.md) | Scaling Rectified Flow Transformers for High-Resolution Image Synthesis | 方法 | 生成 | 这篇论文是 Stability AI 在 2024 年 3 月发布的 SD3 底层技术报告，标题为《Scaling Rectified Flow Transformers for High-Resolution Image Synthesis》。 |
| 2024-07 | [Kolors](../papers/2024-07_Kolors/解读.md) | Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis | 模型 | 生成 | 这篇论文要解决的是：如何训练一个能同时理解中英文、并生成高保真图像的文本到图像扩散模型。 |
| 2024-08 | [FLUX.1](../papers/2024-08_FLUX.1/解读.md) | FLUX.1 Model Family | 模型 | 生成 | — |
| 2024-10 | [REPA](../papers/2024-10_REPA/解读.md) | Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think | 方法 | 生成 | REPA解决扩散Transformer训练中内部表示学习慢、生成质量受限的问题：它在去噪网络早期层的隐藏状态后接一个可训练MLP投影头，把这些噪声输入的隐藏表示与外部预训练视觉编码器对干净图像提取的patch表示对齐。 |
| 2025-05 | [HiDream-I1](../papers/2025-05_HiDream-I1/解读.md) | HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer | 模型 | 生成 | HiDream-I1 是一个 17B（170 亿）参数的开源图像生成基础模型，核心卖点是在“秒级”生成的同时追求顶尖画质，而不是无限制地堆算力。 |
| 2025-06 | [FLUX-Kontext](../papers/2025-06_FLUX-Kontext/解读.md) | FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space | 模型 | 生成+编辑 | FLUX-Kontext 是 Black Forest Labs 在 2025 年 6 月提出的一个统一图像生成与编辑模型，论文全称《FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space》（arXiv:2506.15742）。 |
| 2025-08 | [Qwen-Image](../papers/2025-08_Qwen-Image/解读.md) | Qwen-Image Technical Report | 模型 | 生成 | Qwen-Image 是 Qwen 系列在 2025 年 8 月发布的开源图像生成基础模型。 |
| 2026-02 | [rethink-global-text](../papers/2026-02_rethink-global-text/解读.md) | Rethinking Global Text Conditioning in Diffusion Transformers | 方法 | 生成 | 这篇论文回答一个看似很小、但直接影响扩散 Transformer 设计的问题：**全局文本条件，也就是 CLIP 的 pooled embedding 通过调制层（modulation）注入模型，到底有没有用？** 作者先做系统分析，发现它在 FLUX schnell、HiDream-Fast、COSMOS、FLUX Kontext 等模型里影响很弱：FLUX schnel…… |
| 2026-04 | [tuna-2](../papers/2026-04_tuna-2/解读.md) | Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation | 模型 | 生成 | 《Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation》提出原生统一多模态模型 Tuna-2。 |
| 2026-05 | [masked-gen-transformer](../papers/2026-05_masked-gen-transformer/解读.md) | Masked Generative Transformer Is What You Need for Image Editing | 方法 | 编辑 | 这篇论文提出 **EditMGT**，一个基于掩码生成 Transformer（Masked Generative Transformer, MGT）的图像编辑框架。 |

### 少步与一步生成（2 篇）　**（2026-09 新增）**

把几十步采样压到一步。一致性模型把少步从技巧变成一类模型，分布匹配蒸馏是各家 Turbo / Lightning / Flash 的共同做法。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2023-03 | [Consistency Models](../papers/2023-03_Consistency-Models/解读.md) | Consistency Models | 方法 | 生成 | 这篇论文解决扩散模型生成太慢的问题，办法是提出一致性模型，把概率流常微分方程轨迹上任意带有噪声的点直接映射回轨迹起点，从而把采样压缩为一次网络前向；代价是训练时需要从预训练扩散模型蒸馏，或采用自洽训练目标，并引入指数滑动平均目标网络来稳定优化。 |
| 2023-11 | [DMD](../papers/2023-11_DMD/解读.md) | One-step Diffusion with Distribution Matching Distillation | 方法 | 生成 | 这篇论文解决扩散模型生成图像时需几十到几百次前向、难以实时交互的问题。 |

### 统一多模态：理解与生成同一个模型（22 篇）

一个骨干同时做理解、生成和编辑。离散 token、连续 token、扩散与自回归混合三条子路线都在这里。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2023-12 | [Emu2](../papers/2023-12_Emu2/解读.md) | Generative Multimodal Models are In-Context Learners | 模型 | 生成 | Emu2 是一个 37B 参数的生成式多模态基础模型，目标不是只回答问题或只生成图片，而是用同一个自回归模型同时处理文本、图像、视频的交错序列：看到序列中上一个文本 token 就预测下一个文本 token，看到视觉嵌入就预测下一个视觉嵌入。 |
| 2024-04 | [VAR](../papers/2024-04_VAR/解读.md) | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | 方法 | 生成 | VAR（Visual AutoRegressive Modeling）提出一种新的图像自回归生成范式：不再像 VQGAN、DALL-E、RQ-Transformer 那样，把图像离散 token 按“从左到右、从上到下”的扫描顺序逐 token 预测，而是按分辨率从粗到细做“下一尺度预测”。 |
| 2024-04 | [SEED-X](../papers/2024-04_SEED-X/解读.md) | SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation | 模型 | 生成+编辑 | SEED-X 是腾讯 AI Lab 与 ARC Lab 提出的多模态基础模型，作为 SEED-LLaMA 的后续工作，目标是让一个模型同时具备“任意尺寸/宽高比图像理解”和“多粒度图像生成”能力。 |
| 2024-05 | [Chameleon](../papers/2024-05_Chameleon/解读.md) | Chameleon: Mixed-Modal Early-Fusion Foundation Models | 模型 | 生成 | Chameleon 是 Meta FAIR 提出的“早融合、基于 token 的混合模态基础模型”家族，论文于 2024 年 5 月发布（arXiv:2405.09818）。 |
| 2024-06 | [MAR](../papers/2024-06_MAR/解读.md) | Autoregressive Image Generation without Vector Quantization | 方法 | 生成 | 这篇论文解决的是图像自回归生成是否必须依赖向量量化（VQ）离散 token 的问题。 |
| 2024-08 | [Transfusion](../papers/2024-08_Transfusion/解读.md) | Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model | 方法 | 生成 | 《Transfusion》提出一种训练单个 Transformer 同时处理离散文本与连续图像的方法。 |
| 2024-08 | [Show-o](../papers/2024-08_Show-o/解读.md) | Show-o: One Single Transformer to Unify Multimodal Understanding and Generation | 模型 | 生成 | 《Show-o》是一篇提出统一多模态 Transformer 的论文，目标是在一个模型里同时完成视觉理解与视觉生成。 |
| 2024-09 | [OmniGen](../papers/2024-09_OmniGen/解读.md) | OmniGen: Unified Image Generation | 模型 | 生成+编辑 | OmniGen 是一个面向“统一图像生成”的扩散模型：它把文生图、图像编辑、主体驱动生成、视觉条件生成和若干传统视觉任务塞进同一个 Transformer，不需要 ControlNet、人脸编码器、检测器或任何额外插件。 |
| 2024-09 | [Emu3](../papers/2024-09_Emu3/解读.md) | Emu3: Next-Token Prediction is All You Need | 模型 | 生成 | Emu3 是北京智源人工智能研究院（BAAI）提出的多模态模型系列，论文标题为《Emu3: Next-Token Prediction is All You Need》（arXiv:2409.18869）。 |
| 2024-12 | [Grok-Aurora](../papers/2024-12_Grok-Aurora/解读.md) | Grok (Aurora) | 模型 | 生成 | — |
| 2024-12 | [UniReal](../papers/2024-12_UniReal/解读.md) | UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics | 方法 | 生成+编辑 | UniReal 是 Adobe 与香港大学合作提出的一种统一图像生成与编辑框架，论文发表于 arXiv:2412.07774（2024/12/10），核心模型是一个 5B 参数的 Diffusion Transformer。 |
| 2025-01 | [Janus-Pro](../papers/2025-01_Janus-Pro/解读.md) | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | 模型 | 生成 | Janus-Pro 是 DeepSeek-AI 于 2025 年 1 月 29 日发布在 arXiv 的统一多模态模型，论文编号 2501.17811。 |
| 2025-04 | [MetaQuery](../papers/2025-04_MetaQuery/解读.md) | Transfer between Modalities with MetaQueries | 方法 | 生成 | 这篇论文提出一种名为 MetaQuery 的统一多模态建模方法，用来把“理解型”自回归多模态大模型（MLLM）和“生成型”扩散模型连接起来。 |
| 2025-05 | [BLIP3-o](../papers/2025-05_BLIP3-o/解读.md) | BLIP3-o: A Family of Fully Open Unified Multimodal Models-Architecture, Training and Dataset | 模型 | 生成 | BLIP3-o 是 Salesforce Research 等机构在 2025 年 5 月发布的统一多模态模型家族，论文系统研究了一件具体事：在“自回归大语言模型 + 扩散模型”的混合架构里，图像生成模块到底应该怎么设计。 |
| 2025-05 | [BAGEL](../papers/2025-05_BAGEL/解读.md) | Emerging Properties in Unified Multimodal Pretraining | 模型 | 生成+编辑 | BAGEL 是字节跳动 Seed 等机构在 2025 年 7 月发布的一个开源统一多模态基础模型，论文全称《Emerging Properties in Unified Multimodal Pretraining》（arXiv:2505.14683）。 |
| 2025-06 | [UniWorld-V1](../papers/2025-06_UniWorld-V1/解读.md) | UniWorld-V1: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation | 方法 | 生成+编辑 | UniWorld-V1 是一个统一多模态生成框架，核心主张是：用高分辨率语义编码器（SigLIP2-so400m/14）替代传统 VAE，作为参考图像的视觉控制信号，同时接入冻结的 Qwen2.5-VL-7B 提供高层理解 token，并把这些条件送入 FLUX 的 DiT 做流匹配生成。 |
| 2025-06 | [Show-o2](../papers/2025-06_Show-o2/解读.md) | Show-o2: Improved Native Unified Multimodal Models | 模型 | 生成 | Show-o2 是一个原生统一多模态模型（native unified multimodal model），目标是用单一模型同时完成多模态理解（看图、看视频回答问题）和多模态生成（文生图、文生视频、图生视频、图文交错生成）。 |
| 2025-06 | [OmniGen2](../papers/2025-06_OmniGen2/解读.md) | OmniGen2: Towards Instruction-Aligned Multimodal Generation | 方法 | 生成+编辑 | OmniGen2 是一个统一的多模态生成模型，目标不是单纯堆画质，而是让模型真正“听懂复杂指令”并在文本到图像（T2I）、图像编辑（Edit）、多图上下文生成（In-Context Generation，IC）三类任务上同时稳定工作。 |
| 2025-06 | [Ovis-U1](../papers/2025-06_Ovis-U1/解读.md) | Ovis-U1 Technical Report | 模型 | 生成+编辑 | Ovis-U1 是阿里 Ovis 团队在 2025 年 6 月提交的一个统一多模态模型技术报告（arXiv:2506.23044）。 |
| 2026-01 | [nextflow](../papers/2026-01_nextflow/解读.md) | NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation | 模型 | 生成+编辑 | NextFlow 是一个统一的多模态自回归 Transformer，只用一个 decoder-only 结构同时做图像理解、文本理解和图像生成。 |
| 2026-03 | [ug-fight-dpo](../papers/2026-03_ug-fight-dpo/解读.md) | Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models | 综述 | 生成 | 这篇论文回答一个直接问题：统一多模态模型（同时做图像理解和图像生成）能否用 DPO（直接偏好优化，Direct Preference Optimization）同时对齐两种能力？作者在 Janus-Pro 的 1B 和 7B 两个版本上，系统测试了 7 种训练策略和 2 种后处理方法，覆盖真实图 vs 生成图、模型自身 vs 模型自身两类偏好数据，以及 150–288 对偏…… |
| 2026-06 | [hydra-x](../papers/2026-06_hydra-x/解读.md) | HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers | 模型 | 生成+编辑 | HYDRA-X 是一个 7B 规模的原生统一多模态模型（Native Unified Multimodal Model, UMM），其核心不是更大的 LLM，而是一个称为 HYDRA-XTOK 的整体视觉 tokenizer。 |

### 训练-free 扩散编辑：靠注意力和反演改图（15 篇）

不训练，只在推理时动注意力图和噪声轨迹。这条线定义了图像编辑最初的问题形态。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2021-08 | [SDEdit](../papers/2021-08_SDEdit/解读.md) | SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations | 方法 | 编辑 | SDEdit（Stochastic Differential Editing）是一种基于随机微分方程（SDE）生成先验的图像引导合成与编辑方法。 |
| 2022-06 | [Blended-Latent-Diffusion](../papers/2022-06_Blended-Latent-Diffusion/解读.md) | Blended Latent Diffusion | 方法 | 编辑 | 本文解决的是“局部文本驱动编辑”：用户给出一张真实图像、一句文本提示（text prompt）和一个二值掩码（mask），要求只修改掩码内区域，使内容符合文本描述，同时保持掩码外区域与原图接近、过渡无缝（§4 开头）。 |
| 2022-08 | [Prompt-to-Prompt](../papers/2022-08_Prompt-to-Prompt/解读.md) | Prompt-to-Prompt Image Editing with Cross Attention Control | 方法 | 编辑 | 这篇论文要解决的核心矛盾是：在文本条件扩散模型里，只改一个词，整张图往往变成完全不同的布局和内容。 |
| 2022-10 | [Imagic](../papers/2022-10_Imagic/解读.md) | Imagic: Text-Based Real Image Editing with Diffusion Models | 方法 | 编辑 | Imagic 解决的是“对一张真实照片做复杂文本编辑”的问题。 |
| 2022-10 | [DiffEdit](../papers/2022-10_DiffEdit/解读.md) | DiffEdit: Diffusion-based semantic image editing with mask guidance | 方法 | 编辑 | DiffEdit 是 Meta AI 等机构于 2022 年提出的一种基于扩散模型的语义图像编辑方法（arXiv:2210.11427，§1）。 |
| 2022-11 | [Plug-and-Play](../papers/2022-11_Plug-and-Play/解读.md) | Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation | 方法 | 编辑 | Plug-and-Play（以下简称 PnP）解决的是一个具体任务：**给定一张真实或生成的“结构引导图”和一句目标文本提示**，在不重新训练模型的前提下，生成一张既保留引导图布局、又符合目标文本语义的新图像。 |
| 2023-02 | [pix2pix-zero](../papers/2023-02_pix2pix-zero/解读.md) | Zero-shot Image-to-Image Translation | 方法 | 编辑 | pix2pix-zero（arXiv:2302.03027，2023/02/06）解决的是“用预训练文本到图像扩散模型编辑真实图像”这一任务。 |
| 2023-04 | [MasaCtrl](../papers/2023-04_MasaCtrl/解读.md) | MasaCtrl: Tuning-Free Mutual Self-Attention Control for Consistent Image Synthesis and Editing | 方法 | 生成+编辑 | MasaCtrl 是一种“免微调”（tuning-free）的扩散模型控制方法，用于解决两件相关的事：一是生成多张内容一致但姿态/视角不同的图像，二是对真实图像做复杂的非刚性编辑（例如让坐着的狗跑起来、让鸟展开翅膀），同时保持物体纹理和身份不变。 |
| 2023-06 | [Self-Guidance](../papers/2023-06_Self-Guidance/解读.md) | Diffusion Self-Guidance for Controllable Image Generation | 方法 | 生成 | 这篇论文提出一种叫 **self-guidance（自引导）** 的方法，让预训练文本到图像扩散模型（text-to-image diffusion model）在生成过程中根据自身内部表征来“自我修正”，从而实现对物体位置、大小、形状、外观等属性的细粒度控制。 |
| 2023-11 | [Cross-Image-Attention](../papers/2023-11_Cross-Image-Attention/解读.md) | Cross-Image Attention for Zero-Shot Appearance Transfer | 方法 | 编辑 | 这篇论文解决的是“零样本外观迁移”（zero-shot appearance transfer）：给定两张图，一张提供结构（structure），一张提供外观（appearance），输出一张新图，保留结构图的物体形状、姿态和布局，但把外观图的纹理、颜色、材质或局部语义细节迁移上去。 |
| 2023-11 | [LEDITSpp](../papers/2023-11_LEDITSpp/解读.md) | LEDITS++: Limitless Image Editing using Text-to-Image Models | 方法 | 编辑 | LEDITS++ 是一种基于文本到图像扩散模型的真实图像编辑方法，全称 Limitless Edits with sde-dpm-solver++。 |
| 2023-12 | [StyleAligned](../papers/2023-12_StyleAligned/解读.md) | Style Aligned Image Generation via Shared Attention | 方法 | 生成 | 《StyleAligned》提出了一种免微调、免优化的零样本方法，用于让同一批生成图像在风格上保持一致。 |
| 2024-11 | [Add-it](../papers/2024-11_Add-it/解读.md) | Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models | 方法 | 编辑 | Add-it 是一个训练无关（training-free）的图像物体插入方法，目标是根据一句文本提示，把新物体自然地加到现有图像中，同时尽量保留原图的结构与细节。 |
| 2024-11 | [FlowChef](../papers/2024-12_FlowChef/解读.md) | FlowChef: Steering of Rectified Flow Models for Controlled Generations | 方法 | 编辑 | FlowChef 解决的是一个很具体的工程问题：手里已经有训练好的 Rectified Flow Model（RFM），现在想在**不重新训练模型、不改模型权重、也不把整条 ODE 轨迹展开做反向传播**的前提下，让生成结果满足一个测试时才给出的约束。 |
| 2026-03 | [editing-manifold](../papers/2026-03_editing-manifold/解读.md) | Editing on the Generative Manifold: A Theoretical and Empirical Study of General Diffusion-Based Image Editing Trade-offs | 综述 | 编辑 | 这篇论文不是提出一个新的图像编辑网络，而是把现有扩散式图像编辑方法放进一个统一框架里，用“在生成流形上做受引导传输”来解释它们共同面临的矛盾。 |

### 反演精度：真实图片怎么无损映回噪声（9 篇）

编辑真实照片的前提是先把它准确映回噪声。重建误差有多大，编辑就有多不可控。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2022-11 | [Null-text-Inversion](../papers/2022-11_Null-text-Inversion/解读.md) | Null-text Inversion for Editing Real Images using Guided Diffusion Models | 方法 | 编辑 | 这篇论文解决的是：如何把一张真实照片“喂回”文本引导扩散模型，使模型既能近乎原样重建它，又能继续用纯文本指令编辑它。 |
| 2022-11 | [EDICT](../papers/2022-11_EDICT/解读.md) | EDICT: Exact Diffusion Inversion via Coupled Transformations | 方法 | 编辑 | EDICT（Exact Diffusion Inversion via Coupled Transformations，通过耦合变换实现精确扩散反演）是一种用于扩散模型（Diffusion Models）的**图像反演与编辑方法**。 |
| 2023-12 | [InfEdit](../papers/2023-12_InfEdit/解读.md) | Inversion-Free Image Editing with Natural Language | 方法 | 编辑 | 这篇论文解决的是“基于扩散模型的真实图像文本编辑”里一个绕不开的工程瓶颈：现有主流方法几乎都需要先把原图做扩散反演（inversion），得到一条能将图像还原出来的隐变量轨迹，再在目标文本条件下沿这条轨迹去噪生成编辑结果。 |
| 2024-03 | [ReNoise](../papers/2024-03_ReNoise/解读.md) | ReNoise: Real Image Inversion Through Iterative Noising | 方法 | 编辑 | 这是一篇扩散模型反演方法论文，标题为《ReNoise: Real Image Inversion Through Iterative Noising》。 |
| 2024-08 | [TurboEdit](../papers/2024-08_TurboEdit/解读.md) | TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models | 方法 | 编辑 | TurboEdit 是一种把“少步扩散模型”直接用于真实图像文本编辑的方法。 |
| 2024-10 | [RF-Inversion](../papers/2024-10_RF-Inversion/解读.md) | Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations | 方法 | 编辑 | 《RF-Inversion》研究生成模型中的“反演”与“编辑”两个任务：给定一张真实图像，如何找到模型内部对应的结构化噪声，使模型从这个噪声出发能重建原图，并且能在新提示词下做语义编辑。 |
| 2024-11 | [RF-Solver-Edit](../papers/2024-11_RF-Solver-Edit/解读.md) | Taming Rectified Flow for Inversion and Editing | 方法 | 编辑 | 这是一篇关于“修正流模型反演与编辑”的论文，作者来自清华、腾讯 ARC Lab 与香港科技大学，发表于 ICML 2025。 |
| 2026-05 | [directedit](../papers/2026-05_directedit/解读.md) | DirectEdit: Step-Level Accurate Inversion for Flow-Based Image Editing | 方法 | 编辑 | DirectEdit 解决的是 Rectified Flow（整流流，RF）文生图模型中的免训练图像编辑问题。 |
| 2026-07 | [cfg-inversion-fail](../papers/2026-07_cfg-inversion-fail/解读.md) | When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt--Latent Interactions | 综述 | 编辑 | 这篇论文不提出新的通用图像编辑框架，而是在做一个诊断性研究：当一张图像是由高分类器自由引导（classifier-free guidance，CFG）的扩散轨迹生成时，这条轨迹什么时候能被成功反演？论文把问题放在一个受控的“生成—反演—重建”环境中：使用 Stable Diffusion v1.4，DDIM 采样器固定 50 步，CFG 尺度固定为 7。 |

### 指令式编辑：说人话改图，以及数据从哪来（21 篇）

从「描述目标图」转向「说要改什么」。这条线的瓶颈从头到尾是三元组数据，所以方法与数据集混在同一条线里。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2022-11 | [InstructPix2Pix](../papers/2022-11_InstructPix2Pix/解读.md) | InstructPix2Pix: Learning to Follow Image Editing Instructions | 数据集 | 编辑 | InstructPix2Pix 要解决的问题是：给一张真实图像和一句人类写的“编辑指令”，让模型直接输出编辑后的图像。 |
| 2023-03 | [HIVE](../papers/2023-03_HIVE/解读.md) | HIVE: Harnessing Human Feedback for Instructional Visual Editing | 方法 | 编辑 | HIVE（Harnessing Human Feedback for Instructional Visual Editing，arXiv:2303.09618）解决的是“指令式图像编辑”：给定一张原图和一句人类指令，例如“把植物颜色改成蓝色”，模型输出编辑后的图像。 |
| 2023-06 | [MagicBrush](../papers/2023-06_MagicBrush/解读.md) | MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | 数据集 | 编辑 | MagicBrush 是俄亥俄州立大学等机构提出的一个大规模、人工标注的指令引导真实图像编辑数据集，发表于 NeurIPS 2023 Datasets and Benchmarks track，论文版本为 arXiv 2306.10012。 |
| 2023-09 | [InstructDiffusion](../papers/2023-09_InstructDiffusion/解读.md) | InstructDiffusion: A Generalist Modeling Interface for Vision Tasks | 方法 | 编辑 | InstructDiffusion 是微软亚洲研究院 2023 年提出的通用视觉模型接口。 |
| 2023-09 | [MGIE](../papers/2023-09_MGIE/解读.md) | Guiding Instruction-based Image Editing via Multimodal Large Language Models | 方法 | 编辑 | 这篇论文提出 **MGIE**（Multimodal Large Language Model Guided Image Editing），解决“用一句简短的自然语言指令编辑图像”时，指令太模糊、编辑模型难以准确理解意图的问题。 |
| 2023-11 | [Emu-Edit](../papers/2023-11_Emu-Edit/解读.md) | Emu Edit: Precise Image Editing via Recognition and Generation Tasks | 方法 | 编辑 | Emu-Edit 是一个多任务图像编辑扩散模型，目标是根据自然语言指令精确修改输入图像。 |
| 2023-12 | [SmartEdit](../papers/2023-12_SmartEdit/解读.md) | SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models | 方法 | 编辑 | SmartEdit 是一篇面向复杂文本指令图像编辑的方法论文。 |
| 2024-01 | [Instruct-Imagen](../papers/2024-01_Instruct-Imagen/解读.md) | Instruct-Imagen: Image Generation with Multi-modal Instruction | 方法 | 生成 | 这篇论文提出 Instruct-Imagen，目标是让一个图像生成模型理解“多模态指令”（multi-modal instruction），并用同一套接口完成多种图像生成任务，而不是为每种控制信号单独设计模型。 |
| 2024-04 | [HQ-Edit](../papers/2024-04_HQ-Edit/解读.md) | HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing | 数据集 | 编辑 | 《HQ-Edit》是一篇关于**指令式图像编辑数据构造与评估**的论文，发表于 2024 年 4 月。 |
| 2024-05 | [SEED-Data-Edit](../papers/2024-05_SEED-Data-Edit/解读.md) | SEED-Data-Edit Technical Report: A Hybrid Dataset for Instructional Image Editing | 数据集 | 编辑 | 这篇论文是一个技术报告，核心贡献不是提出全新模型架构，而是发布一个名为 **SEED-Data-Edit** 的混合图像编辑指令数据集。 |
| 2024-07 | [UltraEdit](../papers/2024-07_UltraEdit/解读.md) | UltraEdit: Instruction-based Fine-Grained Image Editing at Scale | 数据集 | 编辑 | 本文提出并公开了一个大规模指令式图像编辑数据集 **UltraEdit**，包含约 410 万条编辑样本、75 万余条去重后的编辑指令。 |
| 2024-11 | [OmniEdit](../papers/2024-11_OmniEdit/解读.md) | OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision | 方法 | 编辑 | OmniEdit 是一个基于 Stable Diffusion 3 Medium（SD3）和本文提出的 EditNet 架构训练出来的指令式图像编辑通用模型。 |
| 2024-11 | [SeedEdit](../papers/2024-11_SeedEdit/解读.md) | SeedEdit: Align Image Re-Generation to Image Editing | 方法 | 编辑 | SeedEdit 解决的是“根据任意文本指令修改一张给定图像”的问题，也就是指令式图像编辑（instructional image editing）。 |
| 2024-11 | [AnyEdit](../papers/2024-11_AnyEdit/解读.md) | AnyEdit: Mastering Unified High-Quality Image Editing for Any Idea | 数据集 | 编辑 | AnyEdit 是一个面向“指令式图像编辑”（instruction-based image editing）的数据集与模型方案。 |
| 2025-03 | [FireEdit](../papers/2025-03_FireEdit/解读.md) | FireEdit: Fine-grained Instruction-based Image Editing via Region-aware Vision Language Model | 方法 | 编辑 | FireEdit 解决指令式图像编辑在复杂场景下定位不准、非编辑区域细节丢失、语义一致性差的问题；办法是用区域令牌（region tokens）增强视觉语言模型（Vision Language Model, VLM），再通过时间感知目标注入（Time-Aware Target Injection, TATI）和混合视觉交叉注意力（Hybrid Visual Cross At…… |
| 2025-04 | [Step1X-Edit](../papers/2025-04_Step1X-Edit/解读.md) | Step1X-Edit: A Practical Framework for General Image Editing | 方法 | 编辑 | Step1X-Edit 是 StepFun 团队提出的通用图像编辑框架，目标是用开放模型逼近 GPT-4o、Gemini 2 Flash、Doubao/SeedEdit 等闭源系统的指令式图像编辑能力。 |
| 2025-04 | [ICEdit](../papers/2025-04_ICEdit/解读.md) | In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer | 方法 | 编辑 | ICEdit 是浙江大学 ReLER 等机构提出的指令式图像编辑框架，发表于 NeurIPS 2025（arXiv:2504.20690）。 |
| 2025-05 | [DICE](../papers/2025-05_DICE/解读.md) | What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models | 方法 | 编辑 | — |
| 2025-06 | [RefEdit](../papers/2025-06_RefEdit/解读.md) | RefEdit: A Benchmark and Method for Improving Instruction-based Image Editing Model on Referring Expressions | 基准 | 编辑 | — |
| 2025-06 | [SeedEdit3](../papers/2025-06_SeedEdit3/解读.md) | SeedEdit 3.0: Fast and High-Quality Generative Image Editing | 模型 | 编辑 | SeedEdit 3.0（论文简称 SeedEdit3）是字节跳动 Seed 团队在 2025 年 6 月发布的生成式图像编辑模型，重点面向真实图像输入。 |
| 2026-07 | [implicit-preservation](../papers/2026-07_implicit-preservation/解读.md) | Making Implicit Preservation Intent Explicit in Conversational Image Editing | 方法 | 编辑 | 这篇论文讨论的核心问题是**多轮对话式图像编辑中的“时间性遮挡恢复”**：有些内容在某一轮被新加或变换的物体暂时盖住，但用户从未要求改变它；等这些遮挡物稍后被移除、移动、缩小或替换，被盖住的内容应当按历史状态忠实恢复，而不是被模型重新“合理生成”成别的样子。 |

### 条件控制：结构、身份、参考图怎么注入（15 篇）

除了文本，还能往模型里塞什么：边缘图、姿态、身份特征、参考图。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2023-02 | [ControlNet](../papers/2023-02_ControlNet/解读.md) | Adding Conditional Control to Text-to-Image Diffusion Models | 方法 | 生成 | ControlNet 解决的是“文本到图像扩散模型难以精确控制空间构图”的问题。 |
| 2023-02 | [T2I-Adapter](../papers/2023-02_T2I-Adapter/解读.md) | T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | 方法 | 生成 | 这篇论文解决的是：如何在不重新训练或微调 Stable Diffusion（稳定扩散，一种隐空间文本到图像扩散模型）的前提下，给已有的大模型增加图像生成的结构、颜色、姿态等细粒度控制。 |
| 2023-04 | [Rich-Text](../papers/2023-04_Rich-Text/解读.md) | Expressive Text-to-Image Generation with Rich Text | 方法 | 生成 | 《Rich-Text》是 Songwei Ge、Taesung Park、Jun-Yan Zhu 与 Jia-Bin Huang 提出的文生图控制方法，论文题为“Expressive Text-to-Image Generation with Rich Text”，arXiv 编号 2304.06720，2023 年 4 月 13 日首次提交。 |
| 2023-08 | [IP-Adapter](../papers/2023-08_IP-Adapter/解读.md) | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | 方法 | 生成 | 本文提出 IP-Adapter，一个轻量适配器（adapter），让预训练文本到图像扩散模型（text-to-image diffusion models）获得图像提示（image prompt）能力，同时保留文本提示能力。 |
| 2023-11 | [Concept-Sliders](../papers/2023-11_Concept-Sliders/解读.md) | Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models | 方法 | 生成 | 这篇论文提出一种叫“Concept Sliders”（概念滑块）的方法，核心是在扩散模型（如 Stable Diffusion XL，SDXL）的参数空间里，用低秩适配器（LoRA，Low-Rank Adaptation）学习一个低秩方向，专门控制某个视觉属性（比如年龄、天气、风格、表情），同时尽量减少对其他属性的干扰。 |
| 2023-12 | [PhotoMaker](../papers/2023-12_PhotoMaker/解读.md) | PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | 方法 | 生成 | PhotoMaker 是一个基于 SDXL 的个性化文本到图像生成方法，核心贡献是“堆叠身份嵌入”（Stacked ID Embedding）。 |
| 2024-01 | [InstantID](../papers/2024-01_InstantID/解读.md) | InstantID: Zero-shot Identity-Preserving Generation in Seconds | 方法 | 生成 | InstantID 是一篇面向“人脸身份保持生成”的论文，解决的是给一张参考人脸，让扩散模型生成不同姿势、风格或背景下仍像同一个人的图像。 |
| 2024-10 | [In-Context-LoRA](../papers/2024-10_In-Context-LoRA/解读.md) | In-Context LoRA for Diffusion Transformers | 方法 | 生成 | 这篇论文提出一个极简的任务无关图像生成框架，叫 **In-Context LoRA（IC-LoRA）**。 |
| 2024-11 | [OminiControl](../papers/2024-11_OminiControl/解读.md) | OminiControl: Minimal and Universal Control for Diffusion Transformer | 方法 | 编辑 | OminiControl 是一种面向 Diffusion Transformer（DiT，扩散 Transformer）图像生成模型的图像条件控制框架。 |
| 2025-01 | [ACEpp](../papers/2025-01_ACEpp/解读.md) | ACE++: Instruction-Based Image Creation and Editing via Context-Aware Content Filling | 方法 | 生成+编辑 | ACE++ 是通义实验室提出的一个基于指令的图像创建与编辑框架。 |
| 2025-03 | [EasyControl](../papers/2025-03_EasyControl/解读.md) | EasyControl: Adding Efficient and Flexible Control for Diffusion Transformer | 方法 | 生成 | EasyControl 是一套面向扩散 Transformer（Diffusion Transformer，DiT）的高效、灵活条件控制框架，基座模型选 FLUX.1 dev（§3）。 |
| 2025-04 | [UNO](../papers/2025-04_UNO/解读.md) | Less-to-More Generalization: Unlocking More Controllability by In-Context Generation | 方法 | 生成 | UNO 是一篇面向“主体驱动图像生成”（subject-driven generation）的方法论文，核心不是发明新架构，而是把现有 DiT（Diffusion Transformer）文本到图像模型逐步改造成一个可接受 1 张或多张参考图、并让生成结果保持参考主体外观一致性的“主体到图像”（S2I）模型。 |
| 2025-04 | [DreamO](../papers/2025-04_DreamO/解读.md) | DreamO: A Unified Framework for Image Customization | 方法 | 生成 | DreamO 是字节跳动智能创作团队与北京大学合作提出的统一图像定制框架（arXiv:2504.16915，2025年4月23日，接收于 SIGGRAPH Asia 2025）。 |
| 2026-03 | [care-edit](../papers/2026-03_care-edit/解读.md) | CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing | 方法 | 编辑 | CARE-Edit 是一篇关于上下文图像编辑的论文，核心问题是：当一个编辑任务同时接收文本、参考图像和用户掩码等多模态条件时，固定共享骨干的扩散模型容易产生任务干扰，比如颜色跨边界渗漏、参考身份漂移、多条件互相冲突。 |
| 2026-04 | [spatialfusion](../papers/2026-04_spatialfusion/解读.md) | SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness | 方法 | 生成 | SpatialFusion 是一篇研究如何让“统一图像生成模型”具备内在 3D 几何意识的方法论文。 |

### 个性化与主体保持（4 篇）

让模型记住一个特定的人或物，再把它放进新场景。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2022-08 | [Textual-Inversion](../papers/2022-08_Textual-Inversion/解读.md) | An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | 方法 | 生成 | 这篇论文提出 “Textual Inversion”（文本反转），任务是把用户给出的 3–5 张同主题图片，例如一个特定杯子、一只猫、一种风格，压缩成预训练文本到图像扩散模型词汇表中的一个“伪词”（pseudo-word），记为 S*。 |
| 2022-08 | [DreamBooth](../papers/2022-08_DreamBooth/解读.md) | DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | 方法 | 生成 | DreamBooth 是一篇 2022 年 Google Research 提出的方法，目标是“主体驱动生成”（subject-driven generation）。 |
| 2022-12 | [Custom-Diffusion](../papers/2022-12_Custom-Diffusion/解读.md) | Multi-Concept Customization of Text-to-Image Diffusion | 方法 | 生成 | Custom-Diffusion 是一种面向文本到图像扩散模型的少样本定制方法。 |
| 2026-05 | [decompose-subject](../papers/2026-05_decompose-subject/解读.md) | Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction | 方法 | 生成 | 本文题为《Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction》，作者 Hanzhong Guo 与 Yizhou Yu，来自香港大学计算与数据科学学院，arXiv 编号 2605.20807（v2 版本修订于 2026 年 7 月）。 |

### 局部与对象级：抠图、补全、搬物体（13 篇）

只改一块区域，或者把一个物体搬走、放进来。分割能力是这条线的前置条件。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2022-11 | [Paint-by-Example](../papers/2022-11_Paint-by-Example/解读.md) | Paint by Example: Exemplar-based Image Editing with Diffusion Models | 方法 | 编辑 | Paint-by-Example 提出一种“示例引导的图像编辑”（exemplar-based image editing）任务：给定一张源图像、一个可编辑区域掩码、一张参考图像，模型要在掩码内生成与参考图像语义相似、外观合理且与周围背景自然融合的内容，同时保持掩码外区域不变。 |
| 2022-12 | [Imagen-Editor-EditBench](../papers/2022-12_Imagen-Editor-EditBench/解读.md) | Imagen Editor and EditBench: Advancing and Evaluating Text-Guided Image Inpainting | 方法 | 编辑 | 这篇论文做的是文本引导图像修复（text-guided image inpainting）：用户给一张图、一个二值掩码区域、一句文本提示，模型只在掩码区域内生成新内容，既要符合文本，又要和未遮住的环境自然衔接。 |
| 2023-04 | [SAM](../papers/2023-04_SAM/解读.md) | Segment Anything | 方法 | 编辑 | SAM（Segment Anything Model）是 Meta AI 在 2023 年 4 月发布的图像分割基础模型，论文提出三个相互耦合的组件：**可提示分割任务**、**SAM 模型**和 **SA-1B 数据集**。 |
| 2023-04 | [Inpaint-Anything](../papers/2023-04_Inpaint-Anything/解读.md) | Inpaint Anything: Segment Anything Meets Image Inpainting | 方法 | 编辑 | 《Inpaint-Anything》是一篇工程组合型论文，不是提出新网络或新训练目标的模型论文。 |
| 2023-05 | [InstructEdit](../papers/2023-05_InstructEdit/解读.md) | InstructEdit: Improving Automatic Masks for Diffusion-based Image Editing With User Instructions | 方法 | 编辑 | 这篇论文提出一个名为 InstructEdit 的图像编辑框架，核心目标是把用户的一句自然语言指令，直接变成一张局部编辑后的图像，而不需要用户提供手工掩码或“输入描述 + 编辑描述”这类结构化文本。 |
| 2023-07 | [AnyDoor](../papers/2023-07_AnyDoor/解读.md) | AnyDoor: Zero-shot Object-level Image Customization | 方法 | 编辑 | AnyDoor（任意门）是一个基于扩散模型的“对象传送”生成器：输入一张目标对象图、一张场景图和一个目标位置框（可选形状掩码），输出该对象被放置到场景指定位置、并按指定形状与周围环境自然融合的新图像，形式上等价于“把目标物体从参考图传送到场景图的某个框里重新生成”。 |
| 2023-12 | [PowerPaint](../papers/2023-12_PowerPaint/解读.md) | A Task is Worth One Word: Learning with Task Prompts for High-Quality Versatile Image Inpainting | 方法 | 编辑 | PowerPaint 是一个基于 Stable Diffusion v1.5 的通用图像修复（image inpainting）模型。 |
| 2024-03 | [BrushNet](../papers/2024-03_BrushNet/解读.md) | BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion | 方法 | 编辑 | BrushNet 解决的是“文本引导的图像修复（text-guided image inpainting）”：给定一张部分区域被遮挡的图像、一个二值掩码（mask）和一句描述文本，模型需要在被遮挡区域生成与遮挡外区域和文本都协调的内容。 |
| 2024-06 | [MimicBrush](../papers/2024-06_MimicBrush/解读.md) | Zero-shot Image Editing with Reference Imitation | 方法 | 编辑 | MimicBrush 解决的是“模仿式编辑”（imitative editing）：用户给一张源图、一个要修改的白色区域掩码，再给一张参考图，但不需要在参考图上框出具体区域。 |
| 2024-11 | [MagicQuill](../papers/2024-11_MagicQuill/解读.md) | MagicQuill: An Intelligent Interactive Image Editing System | 模型 | 编辑 | MagicQuill 是一个交互式图像编辑系统，核心不是单一模型，而是三模块协同：Editing Processor 负责受控生成，Painting Assistor 负责从笔触猜测用户意图，Idea Collector 负责图形界面。 |
| 2025-04 | [Insert-Anything](../papers/2025-04_Insert-Anything/解读.md) | Insert Anything: Image Insertion via In-Context Editing in DiT | 方法 | 编辑 | 《Insert Anything》提出一个统一的参考图像插入框架，目标是把参考图中的特定元素（人、物体、服装）无缝插入到目标场景中，并支持掩码（mask）和文本两种控制方式。 |
| 2026-04 | [edit-where-you-mean](../papers/2026-04_edit-where-you-mean/解读.md) | Edit Where You Mean: Region-Aware Adapter Injection for Mask-Free Local Image Editing | 方法 | 编辑 | 这篇论文要解决的问题很具体：现有大规模扩散 Transformer（DiT）图像编辑器能听懂全局指令，但做“只把杯子改成红色”这类局部编辑时，修改会泄漏到背景、桌子甚至无关物体上。 |
| 2026-06 | [moebius-inpainting](../papers/2026-06_moebius-inpainting/解读.md) | Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance | 方法 | 编辑 | Moebius 是一个面向图像修复（image inpainting）的轻量级扩散模型框架，参数量只有 0.226B，但论文声称在自然场景和肖像场景的修复质量上可以匹敌甚至超过 11.9B 的工业级通用模型 FLUX.1-Fill-Dev。 |

### 拖拽与点控编辑（4 篇）

用鼠标拖一个点，让内容跟着动。交互形态与文本指令完全不同。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2023-05 | [DragGAN](../papers/2023-05_DragGAN/解读.md) | Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold | 方法 | 编辑 | 《Drag Your GAN》研究如何在 **GAN 生成图像**上，通过用户拖拽点实现精确、灵活、通用的图像编辑。 |
| 2023-06 | [DragDiffusion](../papers/2023-06_DragDiffusion/解读.md) | DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | 方法 | 编辑 | DragDiffusion 是一种基于扩散模型的交互式点拖拽图像编辑方法。 |
| 2023-07 | [DragonDiffusion](../papers/2023-07_DragonDiffusion/解读.md) | DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | 方法 | 编辑 | DragonDiffusion 是一种无需微调扩散模型的图像编辑方法，论文发表于 arXiv 2307.02421（2023/07/05）。 |
| 2024-02 | [DiffEditor](../papers/2024-02_DiffEditor/解读.md) | DiffEditor: Boosting Accuracy and Flexibility on Diffusion-based Image Editing | 方法 | 编辑 | DiffEditor 是一篇面向细粒度图像编辑的扩散模型方法论文，完整标题为《DiffEditor: Boosting Accuracy and Flexibility on Diffusion-based Image Editing》，arXiv 编号 2402.02583。 |

### 会推理再动手：think-then-edit（7 篇）

先想清楚要改什么、改到哪，再动手。把链式推理接到编辑上。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2025-10 | [ChronoEdit](../papers/2025-10_ChronoEdit/解读.md) | ChronoEdit: Towards Temporal Reasoning for Image Editing and World Simulation | 方法 | 编辑 | ChronoEdit 是 NVIDIA 与多伦多大学在 2025 年提出的一种图像编辑基础模型，核心目标不是简单提升视觉美观，而是让编辑结果在物理上自洽（physical consistency）。 |
| 2025-11 | [UniREditBench](../papers/2025-11_UniREditBench/解读.md) | UniREditBench: A Unified Reasoning-based Image Editing Benchmark | 基准 | 编辑 | 本文提出 **UniREditBench**，一个面向“基于推理的图像编辑”的统一评测基准。 |
| 2025-11 | [ReasonEdit](../papers/2025-11_ReasonEdit/解读.md) | ReasonEdit: Towards Reasoning-Enhanced Image Editing Models | 方法 | 编辑 | ReasonEdit 是一篇面向指令式图像编辑的推理增强方法论文。 |
| 2026-02 | [unireason](../papers/2026-02_unireason/解读.md) | UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing | 方法 | 生成+编辑 | 这篇论文提出 **UniReason**，一个统一的图像生成与图像编辑推理框架，论文标题为 *UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing*，arXiv 编号 2602.02437（2026/02/02）。 |
| 2026-03 | [coco-code-cot](../papers/2026-03_coco-code-cot/解读.md) | CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation | 方法 | 生成 | 这篇论文解决的核心问题是：统一多模态模型（Unified Multimodal Model, UMM）在生成结构化图像（如图表、数学图、带密集文字的海报）时，自然语言形式的思维链（Chain-of-Thought, CoT）太抽象，无法精确指定空间布局、文字内容和结构关系。 |
| 2026-04 | [meta-cot](../papers/2026-04_meta-cot/解读.md) | Meta-CoT: Enhancing Granularity and Generalization in Image Editing | 方法 | 编辑 | 这篇论文研究的是“用思维链（Chain-of-Thought，CoT）指导图像编辑”时，如何同时提高两件事：对编辑指令的理解粒度，以及对未见编辑任务的泛化能力。 |
| 2026-06 | [mind-the-gap](../papers/2026-06_mind-the-gap/解读.md) | Mind the Gap: Diagnosing Constraint Discovery Failures in Text-in-Image Editing | 综述 | 编辑 | 本文是一份诊断研究，不训练新模型，而是系统回答一个问题：多模态大模型（MLLM）拿到一张图片和一条文字编辑指令时，能否自发发现那些指令没有明说、但编辑后应当在图片里保持一致的区域？例如把海报上的“50% OFF”改成“30% OFF”，模型若只改折扣文字、不改价格标签“$50”，就漏掉了一个隐式约束。 |

### 2025H2–2026 的编辑与统一模型（19 篇）

这条不是技术脉络，是时间切片——2025 下半年之后的旗舰模型与统一模型，技术路线还没沉淀到能干净归类。留着这条比硬塞进别的线更诚实。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2025-08 | [VAREdit](../papers/2025-08_VAREdit/解读.md) | Visual Autoregressive Modeling for Instruction-Guided Image Editing | 方法 | 编辑 | VAREdit 是 ICLR 2026 接收的一种指令引导图像编辑框架。 |
| 2025-09 | [EditVerse](../papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | 方法 | 生成+编辑 | EditVerse 是 Adobe Research 与香港中文大学等机构联合提出的统一图像与视频生成/编辑框架。 |
| 2025-09 | [Seedream4](../papers/2025-09_Seedream4/解读.md) | Seedream 4.0: Toward Next-generation Multimodal Image Generation | 模型 | 生成+编辑 | Seedream 4.0 是字节跳动 Seed 团队提出的统一多模态图像生成系统。 |
| 2025-09 | [HunyuanImage3](../papers/2025-09_HunyuanImage3/解读.md) | HunyuanImage 3.0 Technical Report | 模型 | 生成 | HunyuanImage 3.0 是腾讯混元基础模型团队发布的一个原生多模态模型，论文全称为《HunyuanImage 3.0 Technical Report》。 |
| 2025-10 | [Lumina-DiMOO](../papers/2025-10_Lumina-DiMOO/解读.md) | Lumina-DiMOO: An Omni Diffusion Large Language Model for Multi-Modal Generation and Understanding | 模型 | 生成+编辑 | Lumina-DiMOO 是一个开源统一多模态基础模型，由上海 AI 实验室等机构提出，论文发布于 2025 年 10 月 7 日（arXiv:2510.06308）。 |
| 2025-10 | [DreamOmni2](../papers/2025-10_DreamOmni2/解读.md) | DreamOmni2: Multimodal Instruction-based Editing and Generation | 方法 | 生成+编辑 | DreamOmni2 是一篇 2025 年 10 月的工作论文，提出两个新任务：**多模态指令编辑**和**多模态指令生成**。 |
| 2025-10 | [InstructX](../papers/2025-10_InstructX/解读.md) | InstructX: Towards Unified Visual Editing with MLLM Guidance | 方法 | 编辑 | InstructX 是一个统一的图像与视频编辑框架，核心思想是把多模态大语言模型（Multimodal Large Language Model, MLLM）当作“理解器”，把扩散变换器（Diffusion Transformer, DiT）当作“生成器”，通过一组可学习查询（learnable queries）和一个小型多层感知机（Multi-Layer Perceptr…… |
| 2025-10 | [Kontinuous-Kontext](../papers/2025-10_Kontinuous-Kontext/解读.md) | Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing | 方法 | 编辑 | Kontinuous Kontext 解决的是“指令式图像编辑只能做离散前后对比，不能像调音量一样控制编辑强度”的问题。 |
| 2025-10 | [Emu3.5](../papers/2025-10_Emu3.5/解读.md) | Emu3.5: Native Multimodal Models are World Learners | 模型 | 生成+编辑 | Emu3.5 是北京智源人工智能研究院（BAAI）提出的大规模多模态世界模型，核心是用统一的“下一个 token 预测”（Next-Token Prediction, NTP）目标同时学习视觉和语言。 |
| 2025-11 | [Z-Image](../papers/2025-11_Z-Image/解读.md) | Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer | 模型 | 生成+编辑 | Z-Image 是阿里巴巴提出的 6B 参数高效图像生成基础模型，包含基础模型、8 步推理的 Z-Image-Turbo 和编辑模型 Z-Image-Edit。 |
| 2025-12 | [Qwen-Image-Edit-2511](../papers/2025-12_Qwen-Image-Edit-2511/解读.md) | Qwen-Image-Edit-2511 | 模型 | 编辑 | — |
| 2025-12 | [Qwen-Image-Layered](../papers/2025-12_Qwen-Image-Layered/解读.md) | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition | 方法 | 编辑 | 这篇论文解决的是图像编辑中“改了这里，别处也变了”的一致性问题。 |
| 2026-02 | [FireRed-Image-Edit](../papers/2026-02_FireRed-Image-Edit/解读.md) | FireRed-Image-Edit-1.0 Technical Report | 方法 | 编辑 | FireRed-Image-Edit 是小红书超级智能团队提出的指令式图像编辑扩散 Transformer（Diffusion Transformer, DiT）。 |
| 2026-02 | [ChordEdit](../papers/2026-02_ChordEdit/解读.md) | ChordEdit: One-Step Low-Energy Transport for Image Editing | 方法 | 编辑 | ChordEdit 是一篇面向“单步文生图模型”的图像编辑方法论文。 |
| 2026-03 | [internvl-u](../papers/2026-03_internvl-u/解读.md) | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | 模型 | 生成+编辑 | InternVL-U 是一个 4B 参数的统一多模态模型（Unified Multimodal Model，UMM），目标是在一个框架内同时完成图像理解、推理、生成与编辑。 |
| 2026-04 | [GPT-Image-2](../papers/2026-04_GPT-Image-2/解读.md) | GPT Image 2 | 模型 | 生成+编辑 | — |
| 2026-05 | [Qwen-Image-2.0](../papers/2026-05_Qwen-Image-2.0/解读.md) | Qwen-Image-2.0 Technical Report | 模型 | 生成+编辑 | Qwen-Image-2.0 是 Qwen 团队在 2026 年 5 月发布的一个图像生成基础模型，技术报告编号 arXiv:2605.10730。 |
| 2026-05 | [sensenova-u1](../papers/2026-05_sensenova-u1/解读.md) | SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture | 方法 | 生成+编辑 | SenseNova-U1 是一个统一多模态理解与生成的“原生”模型，论文提出两个变体：SenseNova-U1-8B-MoT 和 SenseNova-U1-A3B-MoT。 |
| 2026-06 | [arm-unified](../papers/2026-06_arm-unified/解读.md) | ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations | 模型 | 生成+编辑 | ARM 是一篇提出统一离散表示的自回归多模态大模型论文，核心目标是用一个 7B 的自回归 Transformer 同时完成图像理解、图像生成和指令式图像编辑，而不是像 Janus-Pro 或 Bagel 那样为理解和生成各配一套视觉编码器。 |

### 生成侧数据与重标注（1 篇）　**（2026-09 新增）**

生成侧的数据工程：用模型重写训练集的 caption。DALL·E 3 之后，每一份图像生成技术报告都有「重标注」这一节。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2023-10 | [DALL·E 3](../papers/2023-10_DALL-E-3/解读.md) | Improving Image Generation with Better Captions | 模型 | 生成 | 这篇论文解决的是文本到图像模型“提示跟随”（prompt following）能力弱的问题，即模型经常忽略词、词序或语义。 |

### 编辑数据工程：三元组从哪来（6 篇）

大规模编辑三元组的生产管线本身作为贡献。与「指令式编辑」里的数据集论文的区别是：这条线的论文主体就是数据管线，不附带新方法。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2025-07 | [NoHumansRequired](../papers/2025-07_NoHumansRequired/解读.md) | NoHumansRequired: Autonomous High-Quality Image Editing Triplet Mining | 数据集 | 编辑 | 这篇论文回答一个问题：**能否在不需要人类标注员的情况下，自动挖出高质量的图像编辑训练数据？** 作者来自 SALUTEDEV，论文发表于 arXiv（2507.14119，2025/07/18，v2 为 2025/09/25）。 |
| 2025-07 | [GPT-Image-Edit-1.5M](../papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset | 数据集 | 编辑 | 这篇论文的核心不是提出一个新的图像编辑模型，而是发布一个大规模、公开的图像编辑数据集：**GPT-Image-Edit-1.5M**，包含超过 150 万个高质量三元组 `{指令, 源图像, 编辑图像}`。 |
| 2025-08 | [X2Edit](../papers/2025-08_X2Edit/解读.md) | X2Edit: Revisiting Arbitrary-Instruction Image Editing through Self-Constructed Data and Task-Aware Representation Learning | 数据集 | 编辑 | 这篇论文同时做了两件事。 |
| 2025-09 | [OpenGPT-4o-Image](../papers/2025-09_OpenGPT-4o-Image/解读.md) | OpenGPT-4o-Image: A Comprehensive Dataset for Advanced Image Generation and Editing | 数据集 | 生成+编辑 | 《OpenGPT-4o-Image》是一篇数据集论文，发布于 arXiv:2509.24900。 |
| 2025-10 | [Pico-Banana-400K](../papers/2025-10_Pico-Banana-400K/解读.md) | Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing | 数据集 | 编辑 | 这是一篇数据集论文，不是模型论文。 |
| 2026-06 | [bootstrap-generator](../papers/2026-06_bootstrap-generator/解读.md) | Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching | 方法 | 编辑 | 这篇论文提出 ByG（Bootstrap Your Generator），目标是训练一个视觉编辑模型，但完全不使用“编辑前/编辑后”成对数据，也不使用外部奖励模型或视觉语言模型反馈。 |

### 奖励模型与在线 RL（2025H2 起）（9 篇）

编辑做得好不好，让奖励模型说；然后拿奖励去做在线 RL。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2025-09 | [EditScore](../papers/2025-09_EditScore/解读.md) | EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling | 奖励与 RL | 编辑 | 这篇论文解决的是：**图像编辑领域没有可用的奖励模型，导致在线强化学习（Online RL）很难跑起来**。 |
| 2025-09 | [EditReward](../papers/2025-09_EditReward/解读.md) | EditReward: A Human-Aligned Reward Model for Instruction-Guided Image Editing | 奖励与 RL | 编辑 | EditReward 是一个面向“指令引导图像编辑”任务的奖励模型（reward model）。 |
| 2025-10 | [Edit-R1-UniWorld-V2](../papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback | 方法 | 编辑 | 这篇论文提出一个叫 **Edit-R1** 的图像编辑后训练框架，不是新模型架构。 |
| 2026-01 | [ThinkRL-Edit](../papers/2026-01_ThinkRL-Edit/解读.md) | ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing | 方法 | 编辑 | 这篇论文解决的是“推理密集型图像编辑”（reasoning-centric image editing）：模型必须先理解指令和参考图像中的语义、常识、空间或规则约束，再执行编辑。 |
| 2026-01 | [reward-hacking-t2i](../papers/2026-01_reward-hacking-t2i/解读.md) | Understanding Reward Hacking in Text-to-Image Reinforcement Learning | 方法 | 编辑 | 这篇论文做的是文生图（Text-to-Image, T2I）强化学习后训练中的“奖励黑客”（reward hacking）问题。 |
| 2026-02 | [spatialreward-edit](../papers/2026-02_spatialreward-edit/解读.md) | SpatialReward: Bridging the Perception Gap in Online RL for Image Editing via Explicit Spatial Reasoning | 奖励与 RL | 编辑 | 这篇论文解决的是图像编辑领域中“奖励模型不可靠”的问题，具体落脚在在线强化学习（Online RL）训练编辑模型时，反馈信号需要同时具备细粒度、跨图比较和绝对打分能力。 |
| 2026-06 | [qwen-image-rl](../papers/2026-06_qwen-image-rl/解读.md) | Qwen-Image-2.0-RL Technical Report | 奖励与 RL | 生成+编辑 | 本文是 Qwen-Image-2.0-RL 的技术报告，介绍一种后训练流程，把强化学习人类反馈（RLHF）和在线策略蒸馏（On-Policy Distillation，OPD）应用到 Qwen-Image-2.0 扩散模型上。 |
| 2026-07 | [read-it-back](../papers/2026-07_read-it-back/解读.md) | Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation | 奖励与 RL | 编辑 | 这篇论文提出 **SpectraReward**，一种面向文生图强化学习的免训练奖励函数。 |
| 2026-08 | [rl-no-edit-rewards](../papers/2026-08_rl-no-edit-rewards/解读.md) | Can We Perform Online RL for Image Editing without Editing Rewards? | 奖励与 RL | 编辑 | 这篇论文回答一个直接的问题：**能不能不做图像编辑专用奖励，只用文生图（T2I）奖励来在线强化学习微调图像编辑模型？** 作者的核心判断是：图像编辑的三个质量维度——纯图像质量、指令执行、参考一致性——都可以被“语义投影”到 T2I 奖励空间。 |

### 推理、强化学习与评测（15 篇）

推理链、策略优化，以及 2025 上半年那批评测基准。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2023-10 | [GenEval](../papers/2023-10_GenEval/解读.md) | GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment | 基准 | 生成 | 这篇论文解决的是文本到图像（T2I）模型组合性对齐评估缺乏细粒度自动方法的问题：现有指标如FID只看图像质量、CLIPScore只给整体图文对齐分数，无法指出模型在“对象共现、计数、颜色、相对位置、属性绑定”上具体错在哪。 |
| 2024-08 | [I2EBench](../papers/2024-08_I2EBench/解读.md) | I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing | 基准 | 编辑 | — |
| 2025-03 | [GoT](../papers/2025-03_GoT/解读.md) | GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing | 方法 | 生成+编辑 | 这篇论文提出一种叫 Generation Chain-of-Thought（GoT）的视觉生成与编辑范式。 |
| 2025-04 | [RISEBench](../papers/2025-04_RISEBench/解读.md) | Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing | 基准 | 编辑 | 这篇论文提出 **RISEBench**，一个专门评测“推理引导视觉编辑”（Reasoning-Informed Visual Editing，简称 RISE）的基准。 |
| 2025-04 | [Complex-Edit](../papers/2025-04_Complex-Edit/解读.md) | $texttt{Complex-Edit}$: CoT-Like Instruction Generation for Complexity-Controllable Image Editing Benchmark | 基准 | 编辑 | Complex-Edit 是 2025 年 4 月 17 日提交到 arXiv（2504.13143）的一个图像编辑基准，由 UCSC、爱丁堡大学和 Google 合作提出。 |
| 2025-05 | [T2I-R1](../papers/2025-05_T2I-R1/解读.md) | T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT | 方法 | 生成 | T2I-R1 是一篇 2025 年 5 月发布（arXiv:2505.00703，v2 版本更新于 2025 年 7 月）的论文，研究如何在文本到图像生成（text-to-image generation）中引入类似大语言模型“思维链”（Chain-of-Thought, CoT）的推理过程。 |
| 2025-05 | [Flow-GRPO](../papers/2025-05_Flow-GRPO/解读.md) | Flow-GRPO: Training Flow Matching Models via Online RL | 奖励与 RL | 生成 | Flow-GRPO 是本论文提出的方法，首次把在线策略梯度强化学习（online policy gradient RL）中的 GRPO（Group Relative Policy Optimization，组相对策略优化）引入流匹配（Flow Matching）文生图模型训练。 |
| 2025-05 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | 方法 | 生成 | 这篇论文提出一个叫 **DanceGRPO** 的框架，把大语言模型（LLM）里已经有效的 **Group Relative Policy Optimization（GRPO，群组相对策略优化）** 用于视觉生成模型的对齐。 |
| 2025-05 | [GIE-Bench](../papers/2025-05_GIE-Bench/解读.md) | GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing | 基准 | 编辑 | — |
| 2025-05 | [Everyday-Image-Editing](../papers/2025-05_Everyday-Image-Editing/解读.md) | Understanding Generative AI Capabilities in Everyday Image Editing Tasks | 基准 | 编辑 | ### 1.1 论文要解决的问题 |
| 2025-05 | [KRIS-Bench](../papers/2025-05_KRIS-Bench/解读.md) | KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models | 基准 | 编辑 | KRIS-Bench 是一个诊断型基准，不是新的图像编辑模型。 |
| 2025-05 | [ImgEdit](../papers/2025-05_ImgEdit/解读.md) | ImgEdit: A Unified Image Editing Dataset and Benchmark | 基准 | 编辑 | ImgEdit 是一个面向指令式图像编辑的统一框架，包含四部分：自动化数据构建流水线、120 万对高质量编辑数据集、一个验证性编辑模型 ImgEdit-E1、以及一个分层基准 ImgEdit-Bench。 |
| 2025-06 | [BPM](../papers/2025-06_BPM/解读.md) | Balancing Preservation and Modification: A Region and Semantic Aware Metric for Instruction-Based Image Editing | 基准 | 编辑 | — |
| 2025-07 | [LMM4Edit](../papers/2025-07_LMM4Edit/解读.md) | LMM4Edit: Benchmarking and Evaluating Multimodal Image Editing with LMMs | 基准 | 编辑 | — |
| 2025-11 | [WiseEdit](../papers/2025-12_WiseEdit/解读.md) | WiseEdit: Benchmarking Cognition- and Creativity-Informed Image Editing | 基准 | 编辑 | — |

### 新一代评测：物理合理性与多轮（19 篇）

2025 下半年之后的评测：不只看指令有没有照做，还看物理是否合理、多轮编辑会不会崩。

| 时间 | 简称 | 论文标题 | 类型 | 任务 | 一句话 |
| --- | --- | --- | --- | --- | --- |
| 2025-05 | [HATIE](../papers/2025-05_HATIE/解读.md) | Towards Scalable Human-aligned Benchmark for Text-guided Image Editing | 基准 | 编辑 | HATIE（Human-Aligned benchmark for Text-guided Image Editing）是一个面向文本引导图像编辑任务的基准与评估框架。 |
| 2025-06 | [ComplexBench-Edit](../papers/2025-06_ComplexBench-Edit/解读.md) | ComplexBench-Edit: Benchmarking Complex Instruction-Driven Image Editing via Compositional Dependencies | 基准 | 编辑 | — |
| 2025-09 | [EdiVal-Agent](../papers/2025-09_EdiVal-Agent/解读.md) | EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing | 基准 | 编辑 | 《EdiVal-Agent》是发表在 ICLR 2026 的一篇评估方法论文，提出一个面向对象中心、全自动、细粒度的多轮图像编辑评估框架。 |
| 2025-10 | [PICABench](../papers/2025-10_PICABench/解读.md) | PICABench: How Far Are We from Physically Realistic Image Editing? | 基准 | 编辑 | PICABench 是一个面向“物理真实图像编辑”的诊断基准与数据方案。 |
| 2025-12 | [I2I-Bench](../papers/2025-12_I2I-Bench/解读.md) | I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models | 基准 | 编辑 | 《I2I-Bench》是一套面向图像到图像编辑模型的综合评估基准，而不是一个新的编辑模型。 |
| 2026-02 | [VIBE](../papers/2026-02_VIBE/解读.md) | How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing | 基准 | 编辑 | — |
| 2026-02 | [reasoning-to-pixels](../papers/2026-02_reasoning-to-pixels/解读.md) | From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models | 基准 | 生成 | 这篇论文提出 UReason，一个用于诊断统一多模态模型（Unified Multimodal Models, UMMs）跨模态对齐差距的基准测试。 |
| 2026-03 | [Omni-IIE-Bench](../papers/2026-03_Omni-IIE-Bench/解读.md) | Omni IIE Bench: Benchmarking the Practical Capabilities of Image Editing Models | 基准 | 编辑 | — |
| 2026-03 | [TIEdit-EditProbe](../papers/2026-03_TIEdit-EditProbe/解读.md) | Evaluating Image Editing with LLMs: A Comprehensive Benchmark and Intermediate-Layer Probing Approach | 基准 | 编辑 | — |
| 2026-03 | [GEditBench-v2](../papers/2026-03_GEditBench-v2/解读.md) | GEditBench v2: A Human-Aligned Benchmark for General Image Editing | 基准 | 编辑 | — |
| 2026-04 | [banana100](../papers/2026-04_banana100/解读.md) | Banana100: Breaking NR-IQA Metrics by 100 Iterative Image Replications with Nano Banana Pro | 数据集 | 编辑 | Banana100 是一个专门记录“迭代图像编辑持续退化”的数据集：作者用 Nano Banana Pro 对 13 张高质量初始图像做 100 轮逐轮编辑/复制，得到 28,000 张输出图像，构建成本超过 $4,000（Section 2）。 |
| 2026-04 | [GSI-Bench](../papers/2026-04_GSI-Bench/解读.md) | Exploring Spatial Intelligence from a Generative Perspective | 基准 | 编辑 | — |
| 2026-04 | [beyond-accuracy](../papers/2026-04_beyond-accuracy/解读.md) | Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models | 基准 | 生成 | 这篇论文不训练新模型，而是提出一个评测基准 XTC-Bench，用来检查“统一多模态模型”（Unified Multimodal Models, uMM）在“看图说话/回答”和“文生图”这两件事之间，是否共享同一套语义理解。 |
| 2026-05 | [edit-compass](../papers/2026-05_edit-compass/解读.md) | Edit-Compass &amp; EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling | 基准 | 编辑 | 这篇论文提出并测评了一套双生基准：**Edit-Compass**（图像编辑能力评测）和 **EditReward-Compass**（图像编辑奖励模型评测）。 |
| 2026-05 | [PaintBench](../papers/2026-05_PaintBench/解读.md) | PaintBench: Deterministic Evaluation of Precise Visual Editing | 基准 | 编辑 | — |
| 2026-06 | [Inter-Edit](../papers/2026-06_Inter-Edit/解读.md) | Inter-Edit: First Benchmark for Interactive Instruction-Based Image Editing | 基准 | 编辑 | — |
| 2026-06 | [lighting-edit-bench](../papers/2026-06_lighting-edit-bench/解读.md) | Do Image Editing Models Understand Lighting? | 基准 | 编辑 | 这篇论文做的是一个叫 **3D-anchored Light Probe（3DLP）** 的基准，用来回答一个问题：**图像编辑模型真的“懂”现实光照和光传输吗？** 论文没有提出新的编辑模型，而是造了一套带真实物理真值的数据集和两个新指标。 |
| 2026-07 | [IIE-Survey](../papers/2026-07_IIE-Survey/解读.md) | Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications | 综述 | 编辑 | 这是一篇对“指令式图像编辑”（Instruction-based Image Editing, IIE）的系统综述与基准论文。 |
| 2026-08 | [CPI-Bench](../papers/2026-08_CPI-Bench/解读.md) | CPI-Bench: A Comprehensive, Practical and Intelligent Benchmark for Real-World Image Editing | 基准 | 编辑 | — |

## 按时间的全量清单

带发表、机构、原文直链的完整版在 [README](../README.md#全量清单)。

**这张表按时间倒序，最新的在最前**，跟 README 的全量清单同向——它们是同一类查询表。
上面 17 条脉络里的表是**时间升序**，从早到晚读才讲得通，两者方向不同不是 bug。

| 时间 | 简称 | 脉络 | 类型 | 任务 | 解读字数 |
| --- | --- | --- | --- | --- | ---: |
| 2026-08-24 | [rl-no-edit-rewards](../papers/2026-08_rl-no-edit-rewards/解读.md) | 奖励模型与在线 RL（2025H2 起） | 奖励与 RL | 编辑 | 7,117 |
| 2026-08-14 | [CPI-Bench](../papers/2026-08_CPI-Bench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 2,517 |
| 2026-07-28 | [IIE-Survey](../papers/2026-07_IIE-Survey/解读.md) | 新一代评测：物理合理性与多轮 | 综述 | 编辑 | 8,309 |
| 2026-07-13 | [read-it-back](../papers/2026-07_read-it-back/解读.md) | 奖励模型与在线 RL（2025H2 起） | 奖励与 RL | 编辑 | 6,611 |
| 2026-07-08 | [implicit-preservation](../papers/2026-07_implicit-preservation/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 6,823 |
| 2026-07-06 | [cfg-inversion-fail](../papers/2026-07_cfg-inversion-fail/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 综述 | 编辑 | 6,682 |
| 2026-06-25 | [lighting-edit-bench](../papers/2026-06_lighting-edit-bench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 6,897 |
| 2026-06-25 | [qwen-image-rl](../papers/2026-06_qwen-image-rl/解读.md) | 奖励模型与在线 RL（2025H2 起） | 奖励与 RL | 生成+编辑 | 8,108 |
| 2026-06-17 | [moebius-inpainting](../papers/2026-06_moebius-inpainting/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 6,843 |
| 2026-06-14 | [mind-the-gap](../papers/2026-06_mind-the-gap/解读.md) | 会推理再动手：think-then-edit | 综述 | 编辑 | 6,741 |
| 2026-06-11 | [hydra-x](../papers/2026-06_hydra-x/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成+编辑 | 6,583 |
| 2026-06-09 | [arm-unified](../papers/2026-06_arm-unified/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 7,433 |
| 2026-06-02 | [bootstrap-generator](../papers/2026-06_bootstrap-generator/解读.md) | 编辑数据工程：三元组从哪来 | 方法 | 编辑 | 7,686 |
| 2026-06-01 | [Inter-Edit](../papers/2026-06_Inter-Edit/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 2,661 |
| 2026-05-29 | [PaintBench](../papers/2026-05_PaintBench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 3,038 |
| 2026-05-20 | [decompose-subject](../papers/2026-05_decompose-subject/解读.md) | 个性化与主体保持 | 方法 | 生成 | 7,064 |
| 2026-05-13 | [edit-compass](../papers/2026-05_edit-compass/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 6,567 |
| 2026-05-12 | [sensenova-u1](../papers/2026-05_sensenova-u1/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 生成+编辑 | 6,907 |
| 2026-05-11 | [Qwen-Image-2.0](../papers/2026-05_Qwen-Image-2.0/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 8,086 |
| 2026-05-11 | [masked-gen-transformer](../papers/2026-05_masked-gen-transformer/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 编辑 | 6,797 |
| 2026-05-04 | [directedit](../papers/2026-05_directedit/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 7,200 |
| 2026-04-29 | [spatialfusion](../papers/2026-04_spatialfusion/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 6,812 |
| 2026-04-27 | [beyond-accuracy](../papers/2026-04_beyond-accuracy/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 生成 | 7,280 |
| 2026-04-27 | [meta-cot](../papers/2026-04_meta-cot/解读.md) | 会推理再动手：think-then-edit | 方法 | 编辑 | 6,900 |
| 2026-04-27 | [tuna-2](../papers/2026-04_tuna-2/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成 | 6,618 |
| 2026-04-26 | [edit-where-you-mean](../papers/2026-04_edit-where-you-mean/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 6,989 |
| 2026-04-22 | [GSI-Bench](../papers/2026-04_GSI-Bench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 2,510 |
| 2026-04-21 | [GPT-Image-2](../papers/2026-04_GPT-Image-2/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 732 |
| 2026-04-03 | [banana100](../papers/2026-04_banana100/解读.md) | 新一代评测：物理合理性与多轮 | 数据集 | 编辑 | 8,186 |
| 2026-03-31 | [editing-manifold](../papers/2026-03_editing-manifold/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 综述 | 编辑 | 7,110 |
| 2026-03-30 | [GEditBench-v2](../papers/2026-03_GEditBench-v2/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 3,755 |
| 2026-03-20 | [TIEdit-EditProbe](../papers/2026-03_TIEdit-EditProbe/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 2,864 |
| 2026-03-17 | [ug-fight-dpo](../papers/2026-03_ug-fight-dpo/解读.md) | 统一多模态：理解与生成同一个模型 | 综述 | 生成 | 6,969 |
| 2026-03-16 | [Omni-IIE-Bench](../papers/2026-03_Omni-IIE-Bench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 3,225 |
| 2026-03-10 | [internvl-u](../papers/2026-03_internvl-u/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 6,642 |
| 2026-03-09 | [care-edit](../papers/2026-03_care-edit/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 编辑 | 6,830 |
| 2026-03-09 | [coco-code-cot](../papers/2026-03_coco-code-cot/解读.md) | 会推理再动手：think-then-edit | 方法 | 生成 | 6,950 |
| 2026-02-22 | [ChordEdit](../papers/2026-02_ChordEdit/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 编辑 | 7,579 |
| 2026-02-12 | [FireRed-Image-Edit](../papers/2026-02_FireRed-Image-Edit/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 编辑 | 7,206 |
| 2026-02-09 | [reasoning-to-pixels](../papers/2026-02_reasoning-to-pixels/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 生成 | 6,985 |
| 2026-02-09 | [rethink-global-text](../papers/2026-02_rethink-global-text/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 生成 | 7,486 |
| 2026-02-07 | [spatialreward-edit](../papers/2026-02_spatialreward-edit/解读.md) | 奖励模型与在线 RL（2025H2 起） | 奖励与 RL | 编辑 | 7,019 |
| 2026-02-02 | [VIBE](../papers/2026-02_VIBE/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 2,564 |
| 2026-02-02 | [unireason](../papers/2026-02_unireason/解读.md) | 会推理再动手：think-then-edit | 方法 | 生成+编辑 | 7,070 |
| 2026-01-06 | [ThinkRL-Edit](../papers/2026-01_ThinkRL-Edit/解读.md) | 奖励模型与在线 RL（2025H2 起） | 方法 | 编辑 | 7,196 |
| 2026-01-06 | [reward-hacking-t2i](../papers/2026-01_reward-hacking-t2i/解读.md) | 奖励模型与在线 RL（2025H2 起） | 方法 | 编辑 | 7,524 |
| 2026-01-05 | [nextflow](../papers/2026-01_nextflow/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成+编辑 | 7,320 |
| 2025-12-17 | [Qwen-Image-Edit-2511](../papers/2025-12_Qwen-Image-Edit-2511/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 编辑 | 666 |
| 2025-12-17 | [Qwen-Image-Layered](../papers/2025-12_Qwen-Image-Layered/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 编辑 | 7,109 |
| 2025-12-04 | [I2I-Bench](../papers/2025-12_I2I-Bench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 7,049 |
| 2025-11-29 | [WiseEdit](../papers/2025-12_WiseEdit/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 2,593 |
| 2025-11-27 | [ReasonEdit](../papers/2025-11_ReasonEdit/解读.md) | 会推理再动手：think-then-edit | 方法 | 编辑 | 7,349 |
| 2025-11-27 | [Z-Image](../papers/2025-11_Z-Image/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 6,667 |
| 2025-11-03 | [UniREditBench](../papers/2025-11_UniREditBench/解读.md) | 会推理再动手：think-then-edit | 基准 | 编辑 | 7,321 |
| 2025-10-30 | [Emu3.5](../papers/2025-10_Emu3.5/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 7,580 |
| 2025-10-22 | [Pico-Banana-400K](../papers/2025-10_Pico-Banana-400K/解读.md) | 编辑数据工程：三元组从哪来 | 数据集 | 编辑 | 7,750 |
| 2025-10-20 | [PICABench](../papers/2025-10_PICABench/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 7,739 |
| 2025-10-19 | [Edit-R1-UniWorld-V2](../papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | 奖励模型与在线 RL（2025H2 起） | 方法 | 编辑 | 6,542 |
| 2025-10-09 | [InstructX](../papers/2025-10_InstructX/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 编辑 | 6,671 |
| 2025-10-09 | [Kontinuous-Kontext](../papers/2025-10_Kontinuous-Kontext/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 编辑 | 8,551 |
| 2025-10-08 | [DreamOmni2](../papers/2025-10_DreamOmni2/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 生成+编辑 | 6,564 |
| 2025-10-07 | [Lumina-DiMOO](../papers/2025-10_Lumina-DiMOO/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 7,291 |
| 2025-10-05 | [ChronoEdit](../papers/2025-10_ChronoEdit/解读.md) | 会推理再动手：think-then-edit | 方法 | 编辑 | 6,825 |
| 2025-09-30 | [EditReward](../papers/2025-09_EditReward/解读.md) | 奖励模型与在线 RL（2025H2 起） | 奖励与 RL | 编辑 | 7,572 |
| 2025-09-29 | [OpenGPT-4o-Image](../papers/2025-09_OpenGPT-4o-Image/解读.md) | 编辑数据工程：三元组从哪来 | 数据集 | 生成+编辑 | 7,651 |
| 2025-09-28 | [EditScore](../papers/2025-09_EditScore/解读.md) | 奖励模型与在线 RL（2025H2 起） | 奖励与 RL | 编辑 | 6,719 |
| 2025-09-28 | [HunyuanImage3](../papers/2025-09_HunyuanImage3/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成 | 6,546 |
| 2025-09-24 | [EditVerse](../papers/2025-09_EditVerse/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 生成+编辑 | 7,231 |
| 2025-09-24 | [Seedream4](../papers/2025-09_Seedream4/解读.md) | 2025H2–2026 的编辑与统一模型 | 模型 | 生成+编辑 | 6,611 |
| 2025-09-16 | [EdiVal-Agent](../papers/2025-09_EdiVal-Agent/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 6,599 |
| 2025-08-21 | [VAREdit](../papers/2025-08_VAREdit/解读.md) | 2025H2–2026 的编辑与统一模型 | 方法 | 编辑 | 7,076 |
| 2025-08-11 | [X2Edit](../papers/2025-08_X2Edit/解读.md) | 编辑数据工程：三元组从哪来 | 数据集 | 编辑 | 6,789 |
| 2025-08-04 | [Qwen-Image](../papers/2025-08_Qwen-Image/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成 | 7,310 |
| 2025-07-28 | [GPT-Image-Edit-1.5M](../papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | 编辑数据工程：三元组从哪来 | 数据集 | 编辑 | 6,615 |
| 2025-07-22 | [LMM4Edit](../papers/2025-07_LMM4Edit/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 2,544 |
| 2025-07-18 | [NoHumansRequired](../papers/2025-07_NoHumansRequired/解读.md) | 编辑数据工程：三元组从哪来 | 数据集 | 编辑 | 6,730 |
| 2025-06-29 | [Ovis-U1](../papers/2025-06_Ovis-U1/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成+编辑 | 6,716 |
| 2025-06-23 | [OmniGen2](../papers/2025-06_OmniGen2/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成+编辑 | 6,695 |
| 2025-06-18 | [Show-o2](../papers/2025-06_Show-o2/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 6,918 |
| 2025-06-17 | [FLUX-Kontext](../papers/2025-06_FLUX-Kontext/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成+编辑 | 8,679 |
| 2025-06-15 | [BPM](../papers/2025-06_BPM/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 2,528 |
| 2025-06-15 | [ComplexBench-Edit](../papers/2025-06_ComplexBench-Edit/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 2,534 |
| 2025-06-05 | [SeedEdit3](../papers/2025-06_SeedEdit3/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 模型 | 编辑 | 7,643 |
| 2025-06-03 | [RefEdit](../papers/2025-06_RefEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 基准 | 编辑 | 2,516 |
| 2025-06-03 | [UniWorld-V1](../papers/2025-06_UniWorld-V1/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成+编辑 | 6,657 |
| 2025-05-28 | [HiDream-I1](../papers/2025-05_HiDream-I1/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成 | 7,337 |
| 2025-05-26 | [DICE](../papers/2025-05_DICE/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 3,306 |
| 2025-05-26 | [ImgEdit](../papers/2025-05_ImgEdit/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 7,451 |
| 2025-05-22 | [Everyday-Image-Editing](../papers/2025-05_Everyday-Image-Editing/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 2,986 |
| 2025-05-22 | [KRIS-Bench](../papers/2025-05_KRIS-Bench/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 7,494 |
| 2025-05-20 | [BAGEL](../papers/2025-05_BAGEL/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成+编辑 | 7,170 |
| 2025-05-16 | [GIE-Bench](../papers/2025-05_GIE-Bench/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 2,670 |
| 2025-05-14 | [BLIP3-o](../papers/2025-05_BLIP3-o/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 6,887 |
| 2025-05-12 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | 推理、强化学习与评测 | 方法 | 生成 | 7,294 |
| 2025-05-08 | [Flow-GRPO](../papers/2025-05_Flow-GRPO/解读.md) | 推理、强化学习与评测 | 奖励与 RL | 生成 | 6,502 |
| 2025-05-01 | [HATIE](../papers/2025-05_HATIE/解读.md) | 新一代评测：物理合理性与多轮 | 基准 | 编辑 | 6,842 |
| 2025-05-01 | [T2I-R1](../papers/2025-05_T2I-R1/解读.md) | 推理、强化学习与评测 | 方法 | 生成 | 6,876 |
| 2025-04-29 | [ICEdit](../papers/2025-04_ICEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 6,865 |
| 2025-04-24 | [Step1X-Edit](../papers/2025-04_Step1X-Edit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 7,396 |
| 2025-04-23 | [DreamO](../papers/2025-04_DreamO/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,727 |
| 2025-04-21 | [Insert-Anything](../papers/2025-04_Insert-Anything/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 6,580 |
| 2025-04-17 | [Complex-Edit](../papers/2025-04_Complex-Edit/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 8,329 |
| 2025-04-08 | [MetaQuery](../papers/2025-04_MetaQuery/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成 | 7,502 |
| 2025-04-03 | [RISEBench](../papers/2025-04_RISEBench/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 7,917 |
| 2025-04-02 | [UNO](../papers/2025-04_UNO/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,202 |
| 2025-03-25 | [FireEdit](../papers/2025-03_FireEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 3,066 |
| 2025-03-13 | [GoT](../papers/2025-03_GoT/解读.md) | 推理、强化学习与评测 | 方法 | 生成+编辑 | 7,356 |
| 2025-03-10 | [EasyControl](../papers/2025-03_EasyControl/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,188 |
| 2025-01-29 | [Janus-Pro](../papers/2025-01_Janus-Pro/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 8,116 |
| 2025-01-05 | [ACEpp](../papers/2025-01_ACEpp/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成+编辑 | 7,487 |
| 2024-12-10 | [UniReal](../papers/2024-12_UniReal/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成+编辑 | 6,953 |
| 2024-12 | [Grok-Aurora](../papers/2024-12_Grok-Aurora/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 330 |
| 2024-11-27 | [FlowChef](../papers/2024-12_FlowChef/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 4,314 |
| 2024-11-24 | [AnyEdit](../papers/2024-11_AnyEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 数据集 | 编辑 | 7,500 |
| 2024-11-22 | [OminiControl](../papers/2024-11_OminiControl/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 编辑 | 6,543 |
| 2024-11-14 | [MagicQuill](../papers/2024-11_MagicQuill/解读.md) | 局部与对象级：抠图、补全、搬物体 | 模型 | 编辑 | 7,389 |
| 2024-11-11 | [Add-it](../papers/2024-11_Add-it/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,033 |
| 2024-11-11 | [OmniEdit](../papers/2024-11_OmniEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 7,402 |
| 2024-11-11 | [SeedEdit](../papers/2024-11_SeedEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 7,623 |
| 2024-11-07 | [RF-Solver-Edit](../papers/2024-11_RF-Solver-Edit/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 7,204 |
| 2024-10-31 | [In-Context-LoRA](../papers/2024-10_In-Context-LoRA/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 6,951 |
| 2024-10-14 | [RF-Inversion](../papers/2024-10_RF-Inversion/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 7,312 |
| 2024-10-09 | [REPA](../papers/2024-10_REPA/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 生成 | 3,143 |
| 2024-09-27 | [Emu3](../papers/2024-09_Emu3/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 7,382 |
| 2024-09-17 | [OmniGen](../papers/2024-09_OmniGen/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成+编辑 | 8,139 |
| 2024-08-26 | [I2EBench](../papers/2024-08_I2EBench/解读.md) | 推理、强化学习与评测 | 基准 | 编辑 | 2,518 |
| 2024-08-22 | [Show-o](../papers/2024-08_Show-o/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 7,514 |
| 2024-08-20 | [Transfusion](../papers/2024-08_Transfusion/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成 | 7,019 |
| 2024-08-01 | [FLUX.1](../papers/2024-08_FLUX.1/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成 | 634 |
| 2024-08-01 | [TurboEdit](../papers/2024-08_TurboEdit/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 6,973 |
| 2024-07-07 | [UltraEdit](../papers/2024-07_UltraEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 数据集 | 编辑 | 7,074 |
| 2024-07-05 | [Kolors](../papers/2024-07_Kolors/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成 | 3,470 |
| 2024-06-17 | [MAR](../papers/2024-06_MAR/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成 | 3,458 |
| 2024-06-11 | [MimicBrush](../papers/2024-06_MimicBrush/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 8,536 |
| 2024-05-16 | [Chameleon](../papers/2024-05_Chameleon/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 8,109 |
| 2024-05-07 | [SEED-Data-Edit](../papers/2024-05_SEED-Data-Edit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 数据集 | 编辑 | 6,626 |
| 2024-04-22 | [SEED-X](../papers/2024-04_SEED-X/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成+编辑 | 6,648 |
| 2024-04-15 | [HQ-Edit](../papers/2024-04_HQ-Edit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 数据集 | 编辑 | 7,232 |
| 2024-04-03 | [VAR](../papers/2024-04_VAR/解读.md) | 统一多模态：理解与生成同一个模型 | 方法 | 生成 | 8,136 |
| 2024-03-21 | [ReNoise](../papers/2024-03_ReNoise/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 6,706 |
| 2024-03-11 | [BrushNet](../papers/2024-03_BrushNet/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 6,745 |
| 2024-03-05 | [SD3-RectifiedFlow](../papers/2024-03_SD3-RectifiedFlow/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 生成 | 6,564 |
| 2024-02-04 | [DiffEditor](../papers/2024-02_DiffEditor/解读.md) | 拖拽与点控编辑 | 方法 | 编辑 | 7,254 |
| 2024-01-15 | [InstantID](../papers/2024-01_InstantID/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 6,825 |
| 2024-01-03 | [Instruct-Imagen](../papers/2024-01_Instruct-Imagen/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 生成 | 7,210 |
| 2023-12-20 | [Emu2](../papers/2023-12_Emu2/解读.md) | 统一多模态：理解与生成同一个模型 | 模型 | 生成 | 6,701 |
| 2023-12-11 | [SmartEdit](../papers/2023-12_SmartEdit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 6,742 |
| 2023-12-07 | [InfEdit](../papers/2023-12_InfEdit/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 6,814 |
| 2023-12-07 | [PhotoMaker](../papers/2023-12_PhotoMaker/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,001 |
| 2023-12-06 | [PowerPaint](../papers/2023-12_PowerPaint/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 7,204 |
| 2023-12-04 | [StyleAligned](../papers/2023-12_StyleAligned/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 生成 | 7,216 |
| 2023-11-30 | [DMD](../papers/2023-11_DMD/解读.md) | 少步与一步生成 | 方法 | 生成 | 3,540 |
| 2023-11-28 | [LEDITSpp](../papers/2023-11_LEDITSpp/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 6,869 |
| 2023-11-20 | [Concept-Sliders](../papers/2023-11_Concept-Sliders/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,827 |
| 2023-11-16 | [Emu-Edit](../papers/2023-11_Emu-Edit/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 6,854 |
| 2023-11-06 | [Cross-Image-Attention](../papers/2023-11_Cross-Image-Attention/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,423 |
| 2023-10-19 | [DALL·E 3](../papers/2023-10_DALL-E-3/解读.md) | 生成侧数据与重标注 | 模型 | 生成 | 3,183 |
| 2023-10-17 | [GenEval](../papers/2023-10_GenEval/解读.md) | 推理、强化学习与评测 | 基准 | 生成 | 3,290 |
| 2023-09-30 | [PixArt-alpha](../papers/2023-09_PixArt-alpha/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 生成 | 6,861 |
| 2023-09-29 | [MGIE](../papers/2023-09_MGIE/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 8,943 |
| 2023-09-07 | [InstructDiffusion](../papers/2023-09_InstructDiffusion/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 6,804 |
| 2023-08-13 | [IP-Adapter](../papers/2023-08_IP-Adapter/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,379 |
| 2023-07-18 | [AnyDoor](../papers/2023-07_AnyDoor/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 7,129 |
| 2023-07-05 | [DragonDiffusion](../papers/2023-07_DragonDiffusion/解读.md) | 拖拽与点控编辑 | 方法 | 编辑 | 7,518 |
| 2023-07-04 | [SDXL](../papers/2023-07_SDXL/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 模型 | 生成 | 3,051 |
| 2023-06-26 | [DragDiffusion](../papers/2023-06_DragDiffusion/解读.md) | 拖拽与点控编辑 | 方法 | 编辑 | 7,065 |
| 2023-06-16 | [MagicBrush](../papers/2023-06_MagicBrush/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 数据集 | 编辑 | 7,080 |
| 2023-06-01 | [Self-Guidance](../papers/2023-06_Self-Guidance/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 生成 | 7,259 |
| 2023-05-29 | [InstructEdit](../papers/2023-05_InstructEdit/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 6,897 |
| 2023-05-18 | [DragGAN](../papers/2023-05_DragGAN/解读.md) | 拖拽与点控编辑 | 方法 | 编辑 | 7,007 |
| 2023-04-17 | [MasaCtrl](../papers/2023-04_MasaCtrl/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 生成+编辑 | 6,562 |
| 2023-04-13 | [Inpaint-Anything](../papers/2023-04_Inpaint-Anything/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 8,149 |
| 2023-04-13 | [Rich-Text](../papers/2023-04_Rich-Text/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 6,817 |
| 2023-04-05 | [SAM](../papers/2023-04_SAM/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 6,768 |
| 2023-03-16 | [HIVE](../papers/2023-03_HIVE/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 方法 | 编辑 | 7,788 |
| 2023-03-02 | [Consistency Models](../papers/2023-03_Consistency-Models/解读.md) | 少步与一步生成 | 方法 | 生成 | 3,194 |
| 2023-02-16 | [T2I-Adapter](../papers/2023-02_T2I-Adapter/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,127 |
| 2023-02-10 | [ControlNet](../papers/2023-02_ControlNet/解读.md) | 条件控制：结构、身份、参考图怎么注入 | 方法 | 生成 | 7,943 |
| 2023-02-06 | [pix2pix-zero](../papers/2023-02_pix2pix-zero/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 6,692 |
| 2022-12-13 | [Imagen-Editor-EditBench](../papers/2022-12_Imagen-Editor-EditBench/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 8,394 |
| 2022-12-08 | [Custom-Diffusion](../papers/2022-12_Custom-Diffusion/解读.md) | 个性化与主体保持 | 方法 | 生成 | 7,128 |
| 2022-11-23 | [Paint-by-Example](../papers/2022-11_Paint-by-Example/解读.md) | 局部与对象级：抠图、补全、搬物体 | 方法 | 编辑 | 7,577 |
| 2022-11-22 | [EDICT](../papers/2022-11_EDICT/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 6,614 |
| 2022-11-22 | [Plug-and-Play](../papers/2022-11_Plug-and-Play/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,284 |
| 2022-11-17 | [InstructPix2Pix](../papers/2022-11_InstructPix2Pix/解读.md) | 指令式编辑：说人话改图，以及数据从哪来 | 数据集 | 编辑 | 7,603 |
| 2022-11-17 | [Null-text-Inversion](../papers/2022-11_Null-text-Inversion/解读.md) | 反演精度：真实图片怎么无损映回噪声 | 方法 | 编辑 | 7,202 |
| 2022-10-20 | [DiffEdit](../papers/2022-10_DiffEdit/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,215 |
| 2022-10-17 | [Imagic](../papers/2022-10_Imagic/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,136 |
| 2022-08-25 | [DreamBooth](../papers/2022-08_DreamBooth/解读.md) | 个性化与主体保持 | 方法 | 生成 | 6,553 |
| 2022-08-02 | [Prompt-to-Prompt](../papers/2022-08_Prompt-to-Prompt/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,138 |
| 2022-08-02 | [Textual-Inversion](../papers/2022-08_Textual-Inversion/解读.md) | 个性化与主体保持 | 方法 | 生成 | 6,900 |
| 2022-07-26 | [Classifier-Free-Guidance](../papers/2022-07_Classifier-Free-Guidance/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 生成 | 6,581 |
| 2022-06-06 | [Blended-Latent-Diffusion](../papers/2022-06_Blended-Latent-Diffusion/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 6,702 |
| 2021-12-20 | [Latent-Diffusion](../papers/2021-12_Latent-Diffusion/解读.md) | 生成骨干：编辑方法赖以运行的底座 | 方法 | 生成 | 7,160 |
| 2021-08-02 | [SDEdit](../papers/2021-08_SDEdit/解读.md) | 训练-free 扩散编辑：靠注意力和反演改图 | 方法 | 编辑 | 7,249 |

## 可信度边界

⚠️ 下面这段是人写的，不由脚本生成。

**笔记正文全部由模型生成，未逐句人工复核。** 图里的信息模型读不到，公式符号会在 PDF
抽取时丢失。数字与结论以原文为准。做过哪些机器校验、哪些地方已知会出错，见
[可信度与产出.md](可信度与产出.md)。

**三种写作规范并存**，是分批产出留下的，旧的不回炉重写：最初 160 篇是 11 节深读
（6,502–8,943 汉字）；2026-08-29 那轮补的 26 项是决策型短笔记（8～9 节），其中 4 项没有
独立论文、只记录官方资料与核验边界；2026-09 起新增的走 v2 规范（8 节 / 3,000–5,000 字）。
结构上 158 篇是标准 11 节，Complex-Edit 与 KRIS-Bench 各有 19 个二级标题——11 节之后
接了 benchmark 那套格式的 6 个无编号小节，再补 §12 决策意义、§13 一手来源。

**2026 年那批的选文不是人挑的。** 38 篇里有 33 篇是模型从 1,123 篇候选里筛出来的，
人工只定了标准。详见 [总结分析.md §5](总结分析.md)，用之前先看那一节。

**[总结分析.md](总结分析.md) 的覆盖范围是最初 160 篇 / 15 条脉络。**
2026-09 并入生成侧论文时新增的两条脉络（少步与一步生成、生成侧数据与重标注）
和那 8 篇论文，还没进那份分析。

**脉络归属怎么定的**：最初 160 篇是人工归的，本次一篇都没动。其余篇目由模型读该篇
`解读.md` 第 1 节判定，只允许从已有脉络清单里选，不许新造；判定结果按本库既有约定
做过一轮归位（基准与综述类归到两条评测脉络，分界取 2025-09，依据是那两条线现有成员的
时间分布）。逐条的判定来源记在 `papers.json` 的 `tag_source`。

