# 图像编辑论文库索引

> 读者：要系统补齐 2022–2026 图像编辑技术脉络的人
> 目标：按脉络挑论文，点进任意一篇能直接读完整深读笔记，不用再读原文
> 覆盖：186 项，2021-08 ～ 2026-08（160 篇 11 节深读 + 26 项决策型笔记，见 §4）
> 最后核对：2026-08-30

## 0. 先说这个库怎么用

每篇论文一个文件夹，里面是 `解读.md`（中文笔记）和 `meta.json`（arXiv ID、日期、字数、venue、引用量）。
`paper.pdf` 不在仓库里（182 份合计 3.3 GB），跑 `python3 scripts/fetch_pdfs.py` 拉回本地。
仓库怎么用、笔记能信到什么程度，见 [README.md](../README.md)。解读按 [prompt.md](prompt.md) 的规范写：
先定位问题，再画数据流，然后拆公式、训练、推理、实验、选型、工程风险。
**它的定位是替代第一次泛读**，不是替代精读——要抠实现细节仍然得回 PDF。

所有 arXiv ID 都实抓 `arxiv.org/abs` 比对过标题与日期，不是凭记忆写的。

## 1. 15 条脉络

### 训练-free 扩散编辑：靠注意力和反演改图

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2021-08 | [SDEdit](../papers/2021-08_SDEdit/解读.md) | SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations | SDEdit（Stochastic Differential Editing）是一种基于随机微分方程（SDE）生成先验的图像引导合成与编辑方法。 |
| 2022-06 | [Blended-Latent-Diffusion](../papers/2022-06_Blended-Latent-Diffusion/解读.md) | Blended Latent Diffusion | 本文解决的是“局部文本驱动编辑”：用户给出一张真实图像、一句文本提示（text prompt）和一个二值掩码（mask），要求只修改掩码内区域，使内容符合文本描述…… |
| 2022-08 | [Prompt-to-Prompt](../papers/2022-08_Prompt-to-Prompt/解读.md) | Prompt-to-Prompt Image Editing with Cross Attention Control | 这篇论文要解决的核心矛盾是：在文本条件扩散模型里，只改一个词，整张图往往变成完全不同的布局和内容。 |
| 2022-10 | [Imagic](../papers/2022-10_Imagic/解读.md) | Imagic: Text-Based Real Image Editing with Diffusion Models | Imagic 解决的是“对一张真实照片做复杂文本编辑”的问题。 |
| 2022-10 | [DiffEdit](../papers/2022-10_DiffEdit/解读.md) | DiffEdit: Diffusion-based semantic image editing with mask guidance | DiffEdit 是 Meta AI 等机构于 2022 年提出的一种基于扩散模型的语义图像编辑方法（arXiv:2210.11427，§1）。 |
| 2022-11 | [Plug-and-Play](../papers/2022-11_Plug-and-Play/解读.md) | Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation | Plug-and-Play（以下简称 PnP）解决的是一个具体任务：给定一张真实或生成的“结构引导图”和一句目标文本提示，在不重新训练模型的前提下…… |
| 2023-02 | [pix2pix-zero](../papers/2023-02_pix2pix-zero/解读.md) | Zero-shot Image-to-Image Translation | pix2pix-zero（arXiv:2302.03027，2023/02/06）解决的是“用预训练文本到图像扩散模型编辑真实图像”这一任务。 |
| 2023-04 | [MasaCtrl](../papers/2023-04_MasaCtrl/解读.md) | MasaCtrl: Tuning-Free Mutual Self-Attention Control for Consistent Image Synthesis and Editing | MasaCtrl 是一种“免微调”（tuning-free）的扩散模型控制方法，用于解决两件相关的事：一是生成多张内容一致但姿态/视角不同的图像…… |
| 2023-06 | [Self-Guidance](../papers/2023-06_Self-Guidance/解读.md) | Diffusion Self-Guidance for Controllable Image Generation | 这篇论文提出一种叫 self-guidance（自引导） 的方法，让预训练文本到图像扩散模型（text-to-image diffusion model）在生成过程中根据自身内部表征来“自…… |
| 2023-11 | [Cross-Image-Attention](../papers/2023-11_Cross-Image-Attention/解读.md) | Cross-Image Attention for Zero-Shot Appearance Transfer | 这篇论文解决的是“零样本外观迁移”（zero-shot appearance transfer）：给定两张图，一张提供结构（structure），一张提供外观（appearance）…… |
| 2023-11 | [LEDITSpp](../papers/2023-11_LEDITSpp/解读.md) | LEDITS++: Limitless Image Editing using Text-to-Image Models | LEDITS++ 是一种基于文本到图像扩散模型的真实图像编辑方法，全称 Limitless Edits with sde-dpm-solver++。 |
| 2023-12 | [StyleAligned](../papers/2023-12_StyleAligned/解读.md) | Style Aligned Image Generation via Shared Attention | 《StyleAligned》提出了一种免微调、免优化的零样本方法，用于让同一批生成图像在风格上保持一致。 |
| 2024-11 | [Add-it](../papers/2024-11_Add-it/解读.md) | Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models | Add-it 是一个训练无关（training-free）的图像物体插入方法，目标是根据一句文本提示，把新物体自然地加到现有图像中，同时尽量保留原图的结构与细节。 |
| 2026-03 | [editing-manifold](../papers/2026-03_editing-manifold/解读.md) | Editing on the Generative Manifold: A Theoretical and Empirical Study of General Diffusion-Based Image Editing Trade-offs | 这篇论文不是提出一个新的图像编辑网络，而是把现有扩散式图像编辑方法放进一个统一框架里，用“在生成流形上做受引导传输”来解释它们共同面临的矛盾。 |

### 反演精度：真实图片怎么无损映回噪声

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2022-11 | [Null-text-Inversion](../papers/2022-11_Null-text-Inversion/解读.md) | Null-text Inversion for Editing Real Images using Guided Diffusion Models | 这篇论文解决的是：如何把一张真实照片“喂回”文本引导扩散模型，使模型既能近乎原样重建它，又能继续用纯文本指令编辑它。 |
| 2022-11 | [EDICT](../papers/2022-11_EDICT/解读.md) | EDICT: Exact Diffusion Inversion via Coupled Transformations | EDICT（Exact Diffusion Inversion via Coupled Transformations…… |
| 2023-12 | [InfEdit](../papers/2023-12_InfEdit/解读.md) | Inversion-Free Image Editing with Natural Language | 这篇论文解决的是“基于扩散模型的真实图像文本编辑”里一个绕不开的工程瓶颈：现有主流方法几乎都需要先把原图做扩散反演（inversion），得到一条能将图像还原出来的隐变量轨迹…… |
| 2024-03 | [ReNoise](../papers/2024-03_ReNoise/解读.md) | ReNoise: Real Image Inversion Through Iterative Noising | 这是一篇扩散模型反演方法论文，标题为《ReNoise: Real Image Inversion Through Iterative Noising》。 |
| 2024-08 | [TurboEdit](../papers/2024-08_TurboEdit/解读.md) | TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models | TurboEdit 是一种把“少步扩散模型”直接用于真实图像文本编辑的方法。 |
| 2024-10 | [RF-Inversion](../papers/2024-10_RF-Inversion/解读.md) | Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations | 《RF-Inversion》研究生成模型中的“反演”与“编辑”两个任务：给定一张真实图像，如何找到模型内部对应的结构化噪声，使模型从这个噪声出发能重建原图，并且能在新提示词下做语义编辑。 |
| 2024-11 | [RF-Solver-Edit](../papers/2024-11_RF-Solver-Edit/解读.md) | Taming Rectified Flow for Inversion and Editing | 这是一篇关于“修正流模型反演与编辑”的论文，作者来自清华、腾讯 ARC Lab 与香港科技大学，发表于 ICML 2025。 |
| 2026-05 | [directedit](../papers/2026-05_directedit/解读.md) | DirectEdit: Step-Level Accurate Inversion for Flow-Based Image Editing | DirectEdit 解决的是 Rectified Flow（整流流，RF）文生图模型中的免训练图像编辑问题。 |
| 2026-07 | [cfg-inversion-fail](../papers/2026-07_cfg-inversion-fail/解读.md) | When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt--Latent Interactions | 这篇论文不提出新的通用图像编辑框架，而是在做一个诊断性研究：当一张图像是由高分类器自由引导（classifier-free guidance，CFG）的扩散轨迹生成时…… |

### 指令式编辑：说人话改图，以及数据从哪来

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2022-11 | [InstructPix2Pix](../papers/2022-11_InstructPix2Pix/解读.md) | InstructPix2Pix: Learning to Follow Image Editing Instructions | InstructPix2Pix 要解决的问题是：给一张真实图像和一句人类写的“编辑指令”，让模型直接输出编辑后的图像。 |
| 2023-03 | [HIVE](../papers/2023-03_HIVE/解读.md) | HIVE: Harnessing Human Feedback for Instructional Visual Editing | HIVE（Harnessing Human Feedback for Instructional Visual Editing…… |
| 2023-06 | [MagicBrush](../papers/2023-06_MagicBrush/解读.md) | MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | MagicBrush 是俄亥俄州立大学等机构提出的一个大规模、人工标注的指令引导真实图像编辑数据集…… |
| 2023-09 | [InstructDiffusion](../papers/2023-09_InstructDiffusion/解读.md) | InstructDiffusion: A Generalist Modeling Interface for Vision Tasks | InstructDiffusion 是微软亚洲研究院 2023 年提出的通用视觉模型接口。 |
| 2023-09 | [MGIE](../papers/2023-09_MGIE/解读.md) | Guiding Instruction-based Image Editing via Multimodal Large Language Models | 这篇论文提出 MGIE（Multimodal Large Language Model Guided Image Editing），解决“用一句简短的自然语言指令编辑图像”时…… |
| 2023-11 | [Emu-Edit](../papers/2023-11_Emu-Edit/解读.md) | Emu Edit: Precise Image Editing via Recognition and Generation Tasks | Emu-Edit 是一个多任务图像编辑扩散模型，目标是根据自然语言指令精确修改输入图像。 |
| 2023-12 | [SmartEdit](../papers/2023-12_SmartEdit/解读.md) | SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models | SmartEdit 是一篇面向复杂文本指令图像编辑的方法论文。 |
| 2024-01 | [Instruct-Imagen](../papers/2024-01_Instruct-Imagen/解读.md) | Instruct-Imagen: Image Generation with Multi-modal Instruction | 这篇论文提出 Instruct-Imagen，目标是让一个图像生成模型理解“多模态指令”（multi-modal instruction），并用同一套接口完成多种图像生成任务…… |
| 2024-04 | [HQ-Edit](../papers/2024-04_HQ-Edit/解读.md) | HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing | 《HQ-Edit》是一篇关于指令式图像编辑数据构造与评估的论文，发表于 2024 年 4 月。 |
| 2024-05 | [SEED-Data-Edit](../papers/2024-05_SEED-Data-Edit/解读.md) | SEED-Data-Edit Technical Report: A Hybrid Dataset for Instructional Image Editing | 这篇论文是一个技术报告，核心贡献不是提出全新模型架构，而是发布一个名为 SEED-Data-Edit 的混合图像编辑指令数据集。 |
| 2024-07 | [UltraEdit](../papers/2024-07_UltraEdit/解读.md) | UltraEdit: Instruction-based Fine-Grained Image Editing at Scale | 本文提出并公开了一个大规模指令式图像编辑数据集 UltraEdit，包含约 410 万条编辑样本、75 万余条去重后的编辑指令。 |
| 2024-11 | [OmniEdit](../papers/2024-11_OmniEdit/解读.md) | OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision | OmniEdit 是一个基于 Stable Diffusion 3 Medium（SD3）和本文提出的 EditNet 架构训练出来的指令式图像编辑通用模型。 |
| 2024-11 | [SeedEdit](../papers/2024-11_SeedEdit/解读.md) | SeedEdit: Align Image Re-Generation to Image Editing | SeedEdit 解决的是“根据任意文本指令修改一张给定图像”的问题，也就是指令式图像编辑（instructional image editing）。 |
| 2024-11 | [AnyEdit](../papers/2024-11_AnyEdit/解读.md) | AnyEdit: Mastering Unified High-Quality Image Editing for Any Idea | AnyEdit 是一个面向“指令式图像编辑”（instruction-based image editing）的数据集与模型方案。 |
| 2025-04 | [Step1X-Edit](../papers/2025-04_Step1X-Edit/解读.md) | Step1X-Edit: A Practical Framework for General Image Editing | Step1X-Edit 是 StepFun 团队提出的通用图像编辑框架，目标是用开放模型逼近 GPT-4o、Gemini 2 Flash、Doubao/SeedEdit 等闭源系统的指令式…… |
| 2025-04 | [ICEdit](../papers/2025-04_ICEdit/解读.md) | In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer | ICEdit 是浙江大学 ReLER 等机构提出的指令式图像编辑框架，发表于 NeurIPS 2025（arXiv:2504.20690）。 |
| 2025-06 | [SeedEdit3](../papers/2025-06_SeedEdit3/解读.md) | SeedEdit 3.0: Fast and High-Quality Generative Image Editing | SeedEdit 3.0（论文简称 SeedEdit3）是字节跳动 Seed 团队在 2025 年 6 月发布的生成式图像编辑模型，重点面向真实图像输入。 |
| 2026-07 | [implicit-preservation](../papers/2026-07_implicit-preservation/解读.md) | Making Implicit Preservation Intent Explicit in Conversational Image Editing | 这篇论文讨论的核心问题是多轮对话式图像编辑中的“时间性遮挡恢复”：有些内容在某一轮被新加或变换的物体暂时盖住，但用户从未要求改变它；等这些遮挡物稍后被移除、移动、缩小或替换…… |

### 条件控制：结构、身份、参考图怎么注入

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2023-02 | [ControlNet](../papers/2023-02_ControlNet/解读.md) | Adding Conditional Control to Text-to-Image Diffusion Models | ControlNet 解决的是“文本到图像扩散模型难以精确控制空间构图”的问题。 |
| 2023-02 | [T2I-Adapter](../papers/2023-02_T2I-Adapter/解读.md) | T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | 这篇论文解决的是：如何在不重新训练或微调 Stable Diffusion（稳定扩散，一种隐空间文本到图像扩散模型）的前提下，给已有的大模型增加图像生成的结构、颜色、姿态等细粒度控制。 |
| 2023-08 | [IP-Adapter](../papers/2023-08_IP-Adapter/解读.md) | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | 本文提出 IP-Adapter，一个轻量适配器（adapter），让预训练文本到图像扩散模型（text-to-image diffusion models）获得图像提示（image pro…… |
| 2023-11 | [Concept-Sliders](../papers/2023-11_Concept-Sliders/解读.md) | Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models | 这篇论文提出一种叫“Concept Sliders”（概念滑块）的方法，核心是在扩散模型（如 Stable Diffusion XL，SDXL）的参数空间里，用低秩适配器（LoRA…… |
| 2023-12 | [PhotoMaker](../papers/2023-12_PhotoMaker/解读.md) | PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | PhotoMaker 是一个基于 SDXL 的个性化文本到图像生成方法，核心贡献是“堆叠身份嵌入”（Stacked ID Embedding）。 |
| 2024-01 | [InstantID](../papers/2024-01_InstantID/解读.md) | InstantID: Zero-shot Identity-Preserving Generation in Seconds | InstantID 是一篇面向“人脸身份保持生成”的论文，解决的是给一张参考人脸，让扩散模型生成不同姿势、风格或背景下仍像同一个人的图像。 |
| 2024-10 | [In-Context-LoRA](../papers/2024-10_In-Context-LoRA/解读.md) | In-Context LoRA for Diffusion Transformers | 这篇论文提出一个极简的任务无关图像生成框架，叫 In-Context LoRA（IC-LoRA）。 |
| 2024-11 | [OminiControl](../papers/2024-11_OminiControl/解读.md) | OminiControl: Minimal and Universal Control for Diffusion Transformer | OminiControl 是一种面向 Diffusion Transformer（DiT，扩散 Transformer）图像生成模型的图像条件控制框架。 |
| 2025-01 | [ACEpp](../papers/2025-01_ACEpp/解读.md) | ACE++: Instruction-Based Image Creation and Editing via Context-Aware Content Filling | ACE++ 是通义实验室提出的一个基于指令的图像创建与编辑框架。 |
| 2025-03 | [EasyControl](../papers/2025-03_EasyControl/解读.md) | EasyControl: Adding Efficient and Flexible Control for Diffusion Transformer | EasyControl 是一套面向扩散 Transformer（Diffusion Transformer，DiT）的高效、灵活条件控制框架，基座模型选 FLUX.1 dev（§3）。 |
| 2025-04 | [UNO](../papers/2025-04_UNO/解读.md) | Less-to-More Generalization: Unlocking More Controllability by In-Context Generation | UNO 是一篇面向“主体驱动图像生成”（subject-driven generation）的方法论文，核心不是发明新架构…… |
| 2025-04 | [DreamO](../papers/2025-04_DreamO/解读.md) | DreamO: A Unified Framework for Image Customization | DreamO 是字节跳动智能创作团队与北京大学合作提出的统一图像定制框架（arXiv:2504.16915，2025年4月23日，接收于 SIGGRAPH Asia 2025）。 |
| 2026-03 | [care-edit](../papers/2026-03_care-edit/解读.md) | CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing | CARE-Edit 是一篇关于上下文图像编辑的论文，核心问题是：当一个编辑任务同时接收文本、参考图像和用户掩码等多模态条件时，固定共享骨干的扩散模型容易产生任务干扰…… |
| 2026-04 | [spatialfusion](../papers/2026-04_spatialfusion/解读.md) | SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness | SpatialFusion 是一篇研究如何让“统一图像生成模型”具备内在 3D 几何意识的方法论文。 |

### 个性化与主体保持

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2022-08 | [Textual-Inversion](../papers/2022-08_Textual-Inversion/解读.md) | An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | 这篇论文提出 “Textual Inversion”（文本反转），任务是把用户给出的 3–5 张同主题图片，例如一个特定杯子、一只猫、一种风格…… |
| 2022-08 | [DreamBooth](../papers/2022-08_DreamBooth/解读.md) | DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | DreamBooth 是一篇 2022 年 Google Research 提出的方法，目标是“主体驱动生成”（subject-driven generation）。 |
| 2022-12 | [Custom-Diffusion](../papers/2022-12_Custom-Diffusion/解读.md) | Multi-Concept Customization of Text-to-Image Diffusion | Custom-Diffusion 是一种面向文本到图像扩散模型的少样本定制方法。 |
| 2026-05 | [decompose-subject](../papers/2026-05_decompose-subject/解读.md) | Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction | 本文题为《Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction》…… |

### 局部与对象级：抠图、补全、搬物体

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2022-11 | [Paint-by-Example](../papers/2022-11_Paint-by-Example/解读.md) | Paint by Example: Exemplar-based Image Editing with Diffusion Models | Paint-by-Example 提出一种“示例引导的图像编辑”（exemplar-based image editing）任务：给定一张源图像、一个可编辑区域掩码、一张参考图像…… |
| 2022-12 | [Imagen-Editor-EditBench](../papers/2022-12_Imagen-Editor-EditBench/解读.md) | Imagen Editor and EditBench: Advancing and Evaluating Text-Guided Image Inpainting | 这篇论文做的是文本引导图像修复（text-guided image inpainting）：用户给一张图、一个二值掩码区域、一句文本提示，模型只在掩码区域内生成新内容，既要符合文本…… |
| 2023-04 | [SAM](../papers/2023-04_SAM/解读.md) | Segment Anything | SAM（Segment Anything Model）是 Meta AI 在 2023 年 4 月发布的图像分割基础模型，论文提出三个相互耦合的组件…… |
| 2023-04 | [Inpaint-Anything](../papers/2023-04_Inpaint-Anything/解读.md) | Inpaint Anything: Segment Anything Meets Image Inpainting | 《Inpaint-Anything》是一篇工程组合型论文，不是提出新网络或新训练目标的模型论文。 |
| 2023-07 | [AnyDoor](../papers/2023-07_AnyDoor/解读.md) | AnyDoor: Zero-shot Object-level Image Customization | AnyDoor（任意门）是一个基于扩散模型的“对象传送”生成器：输入一张目标对象图、一张场景图和一个目标位置框（可选形状掩码）…… |
| 2023-12 | [PowerPaint](../papers/2023-12_PowerPaint/解读.md) | A Task is Worth One Word: Learning with Task Prompts for High-Quality Versatile Image Inpainting | PowerPaint 是一个基于 Stable Diffusion v1.5 的通用图像修复（image inpainting）模型。 |
| 2024-03 | [BrushNet](../papers/2024-03_BrushNet/解读.md) | BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion | BrushNet 解决的是“文本引导的图像修复（text-guided image inpainting）”：给定一张部分区域被遮挡的图像、一个二值掩码（mask）和一句描述文本…… |
| 2024-06 | [MimicBrush](../papers/2024-06_MimicBrush/解读.md) | Zero-shot Image Editing with Reference Imitation | MimicBrush 解决的是“模仿式编辑”（imitative editing）：用户给一张源图、一个要修改的白色区域掩码，再给一张参考图，但不需要在参考图上框出具体区域。 |
| 2024-11 | [MagicQuill](../papers/2024-11_MagicQuill/解读.md) | MagicQuill: An Intelligent Interactive Image Editing System | MagicQuill 是一个交互式图像编辑系统，核心不是单一模型，而是三模块协同：Editing Processor 负责受控生成…… |
| 2025-04 | [Insert-Anything](../papers/2025-04_Insert-Anything/解读.md) | Insert Anything: Image Insertion via In-Context Editing in DiT | 《Insert Anything》提出一个统一的参考图像插入框架，目标是把参考图中的特定元素（人、物体、服装）无缝插入到目标场景中，并支持掩码（mask）和文本两种控制方式。 |
| 2026-04 | [edit-where-you-mean](../papers/2026-04_edit-where-you-mean/解读.md) | Edit Where You Mean: Region-Aware Adapter Injection for Mask-Free Local Image Editing | 这篇论文要解决的问题很具体：现有大规模扩散 Transformer（DiT）图像编辑器能听懂全局指令，但做“只把杯子改成红色”这类局部编辑时，修改会泄漏到背景、桌子甚至无关物体上。 |
| 2026-06 | [moebius-inpainting](../papers/2026-06_moebius-inpainting/解读.md) | Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance | Moebius 是一个面向图像修复（image inpainting）的轻量级扩散模型框架，参数量只有 0.226B…… |

### 拖拽与点控编辑

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2023-05 | [DragGAN](../papers/2023-05_DragGAN/解读.md) | Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold | 《Drag Your GAN》研究如何在 GAN 生成图像上，通过用户拖拽点实现精确、灵活、通用的图像编辑。 |
| 2023-06 | [DragDiffusion](../papers/2023-06_DragDiffusion/解读.md) | DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | DragDiffusion 是一种基于扩散模型的交互式点拖拽图像编辑方法。 |
| 2023-07 | [DragonDiffusion](../papers/2023-07_DragonDiffusion/解读.md) | DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | DragonDiffusion 是一种无需微调扩散模型的图像编辑方法，论文发表于 arXiv 2307.02421（2023/07/05）。 |
| 2024-02 | [DiffEditor](../papers/2024-02_DiffEditor/解读.md) | DiffEditor: Boosting Accuracy and Flexibility on Diffusion-based Image Editing | DiffEditor 是一篇面向细粒度图像编辑的扩散模型方法论文，完整标题为《DiffEditor: Boosting Accuracy and Flexibility on Diffus…… |

### 统一多模态：理解与生成同一个模型

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2023-12 | [Emu2](../papers/2023-12_Emu2/解读.md) | Generative Multimodal Models are In-Context Learners | Emu2 是一个 37B 参数的生成式多模态基础模型，目标不是只回答问题或只生成图片，而是用同一个自回归模型同时处理文本、图像、视频的交错序列…… |
| 2024-04 | [VAR](../papers/2024-04_VAR/解读.md) | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | VAR（Visual AutoRegressive Modeling）提出一种新的图像自回归生成范式：不再像 VQGAN、DALL-E、RQ-Transformer 那样…… |
| 2024-04 | [SEED-X](../papers/2024-04_SEED-X/解读.md) | SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation | SEED-X 是腾讯 AI Lab 与 ARC Lab 提出的多模态基础模型，作为 SEED-LLaMA 的后续工作…… |
| 2024-05 | [Chameleon](../papers/2024-05_Chameleon/解读.md) | Chameleon: Mixed-Modal Early-Fusion Foundation Models | Chameleon 是 Meta FAIR 提出的“早融合、基于 token 的混合模态基础模型”家族，论文于 2024 年 5 月发布（arXiv:2405.09818）。 |
| 2024-08 | [Transfusion](../papers/2024-08_Transfusion/解读.md) | Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model | 《Transfusion》提出一种训练单个 Transformer 同时处理离散文本与连续图像的方法。 |
| 2024-08 | [Show-o](../papers/2024-08_Show-o/解读.md) | Show-o: One Single Transformer to Unify Multimodal Understanding and Generation | 《Show-o》是一篇提出统一多模态 Transformer 的论文，目标是在一个模型里同时完成视觉理解与视觉生成。 |
| 2024-09 | [OmniGen](../papers/2024-09_OmniGen/解读.md) | OmniGen: Unified Image Generation | OmniGen 是一个面向“统一图像生成”的扩散模型：它把文生图、图像编辑、主体驱动生成、视觉条件生成和若干传统视觉任务塞进同一个 Transformer…… |
| 2024-09 | [Emu3](../papers/2024-09_Emu3/解读.md) | Emu3: Next-Token Prediction is All You Need | Emu3 是北京智源人工智能研究院（BAAI）提出的多模态模型系列，论文标题为《Emu3: Next-Token Prediction is All You Need》（arXiv:240…… |
| 2024-12 | [UniReal](../papers/2024-12_UniReal/解读.md) | UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics | UniReal 是 Adobe 与香港大学合作提出的一种统一图像生成与编辑框架，论文发表于 arXiv:2412.07774（2024/12/10）…… |
| 2025-01 | [Janus-Pro](../papers/2025-01_Janus-Pro/解读.md) | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | Janus-Pro 是 DeepSeek-AI 于 2025 年 1 月 29 日发布在 arXiv 的统一多模态模型，论文编号 2501.17811。 |
| 2025-04 | [MetaQuery](../papers/2025-04_MetaQuery/解读.md) | Transfer between Modalities with MetaQueries | 这篇论文提出一种名为 MetaQuery 的统一多模态建模方法，用来把“理解型”自回归多模态大模型（MLLM）和“生成型”扩散模型连接起来。 |
| 2025-05 | [BLIP3-o](../papers/2025-05_BLIP3-o/解读.md) | BLIP3-o: A Family of Fully Open Unified Multimodal Models-Architecture, Training and Dataset | BLIP3-o 是 Salesforce Research 等机构在 2025 年 5 月发布的统一多模态模型家族，论文系统研究了一件具体事…… |
| 2025-05 | [BAGEL](../papers/2025-05_BAGEL/解读.md) | Emerging Properties in Unified Multimodal Pretraining | BAGEL 是字节跳动 Seed 等机构在 2025 年 7 月发布的一个开源统一多模态基础模型…… |
| 2025-06 | [UniWorld-V1](../papers/2025-06_UniWorld-V1/解读.md) | UniWorld-V1: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation | UniWorld-V1 是一个统一多模态生成框架，核心主张是：用高分辨率语义编码器（SigLIP2-so400m/14）替代传统 VAE，作为参考图像的视觉控制信号…… |
| 2025-06 | [Show-o2](../papers/2025-06_Show-o2/解读.md) | Show-o2: Improved Native Unified Multimodal Models | Show-o2 是一个原生统一多模态模型（native unified multimodal model）…… |
| 2025-06 | [OmniGen2](../papers/2025-06_OmniGen2/解读.md) | OmniGen2: Towards Instruction-Aligned Multimodal Generation | OmniGen2 是一个统一的多模态生成模型，目标不是单纯堆画质，而是让模型真正“听懂复杂指令”并在文本到图像（T2I）、图像编辑（Edit）、多图上下文生成（In-Context Gen…… |
| 2025-06 | [Ovis-U1](../papers/2025-06_Ovis-U1/解读.md) | Ovis-U1 Technical Report | Ovis-U1 是阿里 Ovis 团队在 2025 年 6 月提交的一个统一多模态模型技术报告（arXiv:2506.23044）。 |
| 2026-01 | [nextflow](../papers/2026-01_nextflow/解读.md) | NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation | NextFlow 是一个统一的多模态自回归 Transformer，只用一个 decoder-only 结构同时做图像理解、文本理解和图像生成。 |
| 2026-03 | [ug-fight-dpo](../papers/2026-03_ug-fight-dpo/解读.md) | Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models | 这篇论文回答一个直接问题：统一多模态模型（同时做图像理解和图像生成）能否用 DPO（直接偏好优化，Direct Preference Optimization）同时对齐两种能力？ |
| 2026-06 | [hydra-x](../papers/2026-06_hydra-x/解读.md) | HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers | HYDRA-X 是一个 7B 规模的原生统一多模态模型（Native Unified Multimodal Model, UMM），其核心不是更大的 LLM…… |

### 生成骨干：编辑方法赖以运行的底座

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2021-12 | [Latent-Diffusion](../papers/2021-12_Latent-Diffusion/解读.md) | High-Resolution Image Synthesis with Latent Diffusion Models | 这篇论文提出 Latent Diffusion Models（LDMs，潜在扩散模型）…… |
| 2022-07 | [Classifier-Free-Guidance](../papers/2022-07_Classifier-Free-Guidance/解读.md) | Classifier-Free Diffusion Guidance | 这篇论文提出“无分类器引导”（classifier-free guidance，CFG），用于扩散模型的条件生成。 |
| 2023-09 | [PixArt-alpha](../papers/2023-09_PixArt-alpha/解读.md) | PixArt-alpha: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis | PixArt-α（PixArt-alpha）是一篇关于高效训练文本到图像（text-to-image, T2I）扩散 Transformer 的技术报告。 |
| 2024-03 | [SD3-RectifiedFlow](../papers/2024-03_SD3-RectifiedFlow/解读.md) | Scaling Rectified Flow Transformers for High-Resolution Image Synthesis | 这篇论文是 Stability AI 在 2024 年 3 月发布的 SD3 底层技术报告…… |
| 2025-05 | [HiDream-I1](../papers/2025-05_HiDream-I1/解读.md) | HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer | HiDream-I1 是一个 17B（170 亿）参数的开源图像生成基础模型，核心卖点是在“秒级”生成的同时追求顶尖画质，而不是无限制地堆算力。 |
| 2025-06 | [FLUX-Kontext](../papers/2025-06_FLUX-Kontext/解读.md) | FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space | FLUX-Kontext 是 Black Forest Labs 在 2025 年 6 月提出的一个统一图像生成与编辑模型…… |
| 2025-08 | [Qwen-Image](../papers/2025-08_Qwen-Image/解读.md) | Qwen-Image Technical Report | Qwen-Image 是 Qwen 系列在 2025 年 8 月发布的开源图像生成基础模型。 |
| 2026-02 | [rethink-global-text](../papers/2026-02_rethink-global-text/解读.md) | Rethinking Global Text Conditioning in Diffusion Transformers | 这篇论文回答一个看似很小、但直接影响扩散 Transformer 设计的问题：全局文本条件…… |
| 2026-04 | [tuna-2](../papers/2026-04_tuna-2/解读.md) | Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation | 《Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation》提出原…… |
| 2026-05 | [masked-gen-transformer](../papers/2026-05_masked-gen-transformer/解读.md) | Masked Generative Transformer Is What You Need for Image Editing | 这篇论文提出 EditMGT，一个基于掩码生成 Transformer（Masked Generative Transformer, MGT）的图像编辑框架。 |

### 推理、强化学习与评测

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2025-03 | [GoT](../papers/2025-03_GoT/解读.md) | GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing | 这篇论文提出一种叫 Generation Chain-of-Thought（GoT）的视觉生成与编辑范式。 |
| 2025-04 | [RISEBench](../papers/2025-04_RISEBench/解读.md) | Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing | 这篇论文提出 RISEBench，一个专门评测“推理引导视觉编辑”（Reasoning-Informed Visual Editing，简称 RISE）的基准。 |
| 2025-04 | [Complex-Edit](../papers/2025-04_Complex-Edit/解读.md) | texttt{Complex-Edit}: CoT-Like Instruction Generation for Complexity-Controllable Image Editing Benchmark | Complex-Edit 是 2025 年 4 月 17 日提交到 arXiv（2504.13143）的一个图像编辑基准，由 UCSC、爱丁堡大学和 Google 合作提出。 |
| 2025-05 | [T2I-R1](../papers/2025-05_T2I-R1/解读.md) | T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT | T2I-R1 是一篇 2025 年 5 月发布（arXiv:2505.00703，v2 版本更新于 2025 年 7 月）的论文…… |
| 2025-05 | [Flow-GRPO](../papers/2025-05_Flow-GRPO/解读.md) | Flow-GRPO: Training Flow Matching Models via Online RL | Flow-GRPO 是本论文提出的方法，首次把在线策略梯度强化学习（online policy gradient RL）中的 GRPO（Group Relative Policy Opti…… |
| 2025-05 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | 这篇论文提出一个叫 DanceGRPO 的框架，把大语言模型（LLM）里已经有效的 Group Relative Policy Optimization（GRPO…… |
| 2025-05 | [KRIS-Bench](../papers/2025-05_KRIS-Bench/解读.md) | KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models | KRIS-Bench 是一个诊断型基准，不是新的图像编辑模型。 |
| 2025-05 | [ImgEdit](../papers/2025-05_ImgEdit/解读.md) | ImgEdit: A Unified Image Editing Dataset and Benchmark | ImgEdit 是一个面向指令式图像编辑的统一框架，包含四部分：自动化数据构建流水线、120 万对高质量编辑数据集、一个验证性编辑模型 ImgEdit-E1、以及一个分层基准 ImgEdi…… |

### 奖励模型与在线 RL（2025H2 起）

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2025-09 | [EditScore](../papers/2025-09_EditScore/解读.md) | EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling | 这篇论文解决的是：图像编辑领域没有可用的奖励模型，导致在线强化学习（Online RL）很难跑起来。 |
| 2025-09 | [EditReward](../papers/2025-09_EditReward/解读.md) | EditReward: A Human-Aligned Reward Model for Instruction-Guided Image Editing | EditReward 是一个面向“指令引导图像编辑”任务的奖励模型（reward model）。 |
| 2025-10 | [Edit-R1-UniWorld-V2](../papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback | 这篇论文提出一个叫 Edit-R1 的图像编辑后训练框架，不是新模型架构。 |
| 2026-01 | [ThinkRL-Edit](../papers/2026-01_ThinkRL-Edit/解读.md) | ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing | 这篇论文解决的是“推理密集型图像编辑”（reasoning-centric image editing）：模型必须先理解指令和参考图像中的语义、常识、空间或规则约束，再执行编辑。 |
| 2026-01 | [reward-hacking-t2i](../papers/2026-01_reward-hacking-t2i/解读.md) | Understanding Reward Hacking in Text-to-Image Reinforcement Learning | 这篇论文做的是文生图（Text-to-Image, T2I）强化学习后训练中的“奖励黑客”（reward hacking）问题。 |
| 2026-02 | [spatialreward-edit](../papers/2026-02_spatialreward-edit/解读.md) | SpatialReward: Bridging the Perception Gap in Online RL for Image Editing via Explicit Spatial Reasoning | 这篇论文解决的是图像编辑领域中“奖励模型不可靠”的问题，具体落脚在在线强化学习（Online RL）训练编辑模型时，反馈信号需要同时具备细粒度、跨图比较和绝对打分能力。 |
| 2026-06 | [qwen-image-rl](../papers/2026-06_qwen-image-rl/解读.md) | Qwen-Image-2.0-RL Technical Report | 本文是 Qwen-Image-2.0-RL 的技术报告，介绍一种后训练流程，把强化学习人类反馈（RLHF）和在线策略蒸馏（On-Policy Distillation…… |
| 2026-07 | [read-it-back](../papers/2026-07_read-it-back/解读.md) | Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation | 这篇论文提出 SpectraReward，一种面向文生图强化学习的免训练奖励函数。 |
| 2026-08 | [rl-no-edit-rewards](../papers/2026-08_rl-no-edit-rewards/解读.md) | Can We Perform Online RL for Image Editing without Editing Rewards? | 这篇论文回答一个直接的问题：能不能不做图像编辑专用奖励，只用文生图（T2I）奖励来在线强化学习微调图像编辑模型？ |

### 会推理再动手：think-then-edit

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2025-10 | [ChronoEdit](../papers/2025-10_ChronoEdit/解读.md) | ChronoEdit: Towards Temporal Reasoning for Image Editing and World Simulation | ChronoEdit 是 NVIDIA 与多伦多大学在 2025 年提出的一种图像编辑基础模型，核心目标不是简单提升视觉美观…… |
| 2025-11 | [UniREditBench](../papers/2025-11_UniREditBench/解读.md) | UniREditBench: A Unified Reasoning-based Image Editing Benchmark | 本文提出 UniREditBench，一个面向“基于推理的图像编辑”的统一评测基准。 |
| 2025-11 | [ReasonEdit](../papers/2025-11_ReasonEdit/解读.md) | ReasonEdit: Towards Reasoning-Enhanced Image Editing Models | ReasonEdit 是一篇面向指令式图像编辑的推理增强方法论文。 |
| 2026-02 | [unireason](../papers/2026-02_unireason/解读.md) | UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing | 这篇论文提出 UniReason，一个统一的图像生成与图像编辑推理框架，论文标题为 UniReason 1.0: A Unified Reasoning Framework for Wor…… |
| 2026-03 | [coco-code-cot](../papers/2026-03_coco-code-cot/解读.md) | CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation | 这篇论文解决的核心问题是：统一多模态模型（Unified Multimodal Model, UMM）在生成结构化图像（如图表、数学图、带密集文字的海报）时…… |
| 2026-04 | [meta-cot](../papers/2026-04_meta-cot/解读.md) | Meta-CoT: Enhancing Granularity and Generalization in Image Editing | 这篇论文研究的是“用思维链（Chain-of-Thought，CoT）指导图像编辑”时，如何同时提高两件事：对编辑指令的理解粒度，以及对未见编辑任务的泛化能力。 |
| 2026-06 | [mind-the-gap](../papers/2026-06_mind-the-gap/解读.md) | Mind the Gap: Diagnosing Constraint Discovery Failures in Text-in-Image Editing | 本文是一份诊断研究，不训练新模型，而是系统回答一个问题：多模态大模型（MLLM）拿到一张图片和一条文字编辑指令时，能否自发发现那些指令没有明说、但编辑后应当在图片里保持一致的区域？ |

### 编辑数据工程：三元组从哪来

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2025-07 | [NoHumansRequired](../papers/2025-07_NoHumansRequired/解读.md) | NoHumansRequired: Autonomous High-Quality Image Editing Triplet Mining | 这篇论文回答一个问题：能否在不需要人类标注员的情况下，自动挖出高质量的图像编辑训练数据？ |
| 2025-07 | [GPT-Image-Edit-1.5M](../papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset | 这篇论文的核心不是提出一个新的图像编辑模型，而是发布一个大规模、公开的图像编辑数据集：GPT-Image-Edit-1.5M…… |
| 2025-08 | [X2Edit](../papers/2025-08_X2Edit/解读.md) | X2Edit: Revisiting Arbitrary-Instruction Image Editing through Self-Constructed Data and Task-Aware Representation Learning | 这篇论文同时做了两件事。 |
| 2025-09 | [OpenGPT-4o-Image](../papers/2025-09_OpenGPT-4o-Image/解读.md) | OpenGPT-4o-Image: A Comprehensive Dataset for Advanced Image Generation and Editing | 《OpenGPT-4o-Image》是一篇数据集论文，发布于 arXiv:2509.24900。 |
| 2025-10 | [Pico-Banana-400K](../papers/2025-10_Pico-Banana-400K/解读.md) | Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing | 这是一篇数据集论文，不是模型论文。 |
| 2026-06 | [bootstrap-generator](../papers/2026-06_bootstrap-generator/解读.md) | Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching | 这篇论文提出 ByG（Bootstrap Your Generator），目标是训练一个视觉编辑模型，但完全不使用“编辑前/编辑后”成对数据，也不使用外部奖励模型或视觉语言模型反馈。 |

### 2025H2–2026 的编辑与统一模型

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2025-08 | [VAREdit](../papers/2025-08_VAREdit/解读.md) | Visual Autoregressive Modeling for Instruction-Guided Image Editing | VAREdit 是 ICLR 2026 接收的一种指令引导图像编辑框架。 |
| 2025-09 | [Seedream4](../papers/2025-09_Seedream4/解读.md) | Seedream 4.0: Toward Next-generation Multimodal Image Generation | Seedream 4.0 是字节跳动 Seed 团队提出的统一多模态图像生成系统。 |
| 2025-09 | [EditVerse](../papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | EditVerse 是 Adobe Research 与香港中文大学等机构联合提出的统一图像与视频生成/编辑框架。 |
| 2025-09 | [HunyuanImage3](../papers/2025-09_HunyuanImage3/解读.md) | HunyuanImage 3.0 Technical Report | HunyuanImage 3.0 是腾讯混元基础模型团队发布的一个原生多模态模型，论文全称为《HunyuanImage 3.0 Technical Report》。 |
| 2025-10 | [Lumina-DiMOO](../papers/2025-10_Lumina-DiMOO/解读.md) | Lumina-DiMOO: An Omni Diffusion Large Language Model for Multi-Modal Generation and Understanding | Lumina-DiMOO 是一个开源统一多模态基础模型，由上海 AI 实验室等机构提出，论文发布于 2025 年 10 月 7 日（arXiv:2510.06308）。 |
| 2025-10 | [DreamOmni2](../papers/2025-10_DreamOmni2/解读.md) | DreamOmni2: Multimodal Instruction-based Editing and Generation | DreamOmni2 是一篇 2025 年 10 月的工作论文，提出两个新任务：多模态指令编辑和多模态指令生成。 |
| 2025-10 | [InstructX](../papers/2025-10_InstructX/解读.md) | InstructX: Towards Unified Visual Editing with MLLM Guidance | InstructX 是一个统一的图像与视频编辑框架，核心思想是把多模态大语言模型（Multimodal Large Language Model, MLLM）当作“理解器”…… |
| 2025-10 | [Kontinuous-Kontext](../papers/2025-10_Kontinuous-Kontext/解读.md) | Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing | Kontinuous Kontext 解决的是“指令式图像编辑只能做离散前后对比，不能像调音量一样控制编辑强度”的问题。 |
| 2025-10 | [Emu3.5](../papers/2025-10_Emu3.5/解读.md) | Emu3.5: Native Multimodal Models are World Learners | Emu3.5 是北京智源人工智能研究院（BAAI）提出的大规模多模态世界模型，核心是用统一的“下一个 token 预测”（Next-Token Prediction, NTP）目标同时学习…… |
| 2025-11 | [Z-Image](../papers/2025-11_Z-Image/解读.md) | Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer | Z-Image 是阿里巴巴提出的 6B 参数高效图像生成基础模型，包含基础模型、8 步推理的 Z-Image-Turbo 和编辑模型 Z-Image-Edit。 |
| 2025-12 | [Qwen-Image-Layered](../papers/2025-12_Qwen-Image-Layered/解读.md) | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition | 这篇论文解决的是图像编辑中“改了这里，别处也变了”的一致性问题。 |
| 2026-02 | [FireRed-Image-Edit](../papers/2026-02_FireRed-Image-Edit/解读.md) | FireRed-Image-Edit-1.0 Technical Report | FireRed-Image-Edit 是小红书超级智能团队提出的指令式图像编辑扩散 Transformer（Diffusion Transformer, DiT）。 |
| 2026-02 | [ChordEdit](../papers/2026-02_ChordEdit/解读.md) | ChordEdit: One-Step Low-Energy Transport for Image Editing | ChordEdit 是一篇面向“单步文生图模型”的图像编辑方法论文。 |
| 2026-03 | [internvl-u](../papers/2026-03_internvl-u/解读.md) | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | InternVL-U 是一个 4B 参数的统一多模态模型（Unified Multimodal Model，UMM），目标是在一个框架内同时完成图像理解、推理、生成与编辑。 |
| 2026-05 | [Qwen-Image-2.0](../papers/2026-05_Qwen-Image-2.0/解读.md) | Qwen-Image-2.0 Technical Report | Qwen-Image-2.0 是 Qwen 团队在 2026 年 5 月发布的一个图像生成基础模型，技术报告编号 arXiv:2605.10730。 |
| 2026-05 | [sensenova-u1](../papers/2026-05_sensenova-u1/解读.md) | SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture | SenseNova-U1 是一个统一多模态理解与生成的“原生”模型，论文提出两个变体：SenseNova-U1-8B-MoT 和 SenseNova-U1-A3B-MoT。 |
| 2026-06 | [arm-unified](../papers/2026-06_arm-unified/解读.md) | ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations | ARM 是一篇提出统一离散表示的自回归多模态大模型论文，核心目标是用一个 7B 的自回归 Transformer 同时完成图像理解、图像生成和指令式图像编辑…… |

### 新一代评测：物理合理性与多轮

| 时间 | 简称 | 论文标题 | 一句话 |
| --- | --- | --- | --- |
| 2025-09 | [EdiVal-Agent](../papers/2025-09_EdiVal-Agent/解读.md) | EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing | 《EdiVal-Agent》是发表在 ICLR 2026 的一篇评估方法论文，提出一个面向对象中心、全自动、细粒度的多轮图像编辑评估框架。 |
| 2025-10 | [PICABench](../papers/2025-10_PICABench/解读.md) | PICABench: How Far Are We from Physically Realistic Image Editing? | PICABench 是一个面向“物理真实图像编辑”的诊断基准与数据方案。 |
| 2026-02 | [reasoning-to-pixels](../papers/2026-02_reasoning-to-pixels/解读.md) | From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models | 这篇论文提出 UReason，一个用于诊断统一多模态模型（Unified Multimodal Models, UMMs）跨模态对齐差距的基准测试。 |
| 2026-04 | [banana100](../papers/2026-04_banana100/解读.md) | Banana100: Breaking NR-IQA Metrics by 100 Iterative Image Replications with Nano Banana Pro | Banana100 是一个专门记录“迭代图像编辑持续退化”的数据集：作者用 Nano Banana Pro 对 13 张高质量初始图像做 100 轮逐轮编辑/复制…… |
| 2026-04 | [beyond-accuracy](../papers/2026-04_beyond-accuracy/解读.md) | Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models | 这篇论文不训练新模型，而是提出一个评测基准 XTC-Bench，用来检查“统一多模态模型”（Unified Multimodal Models, uMM）在“看图说话/回答”和“文生图”这…… |
| 2026-05 | [edit-compass](../papers/2026-05_edit-compass/解读.md) | Edit-Compass &amp; EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling | 这篇论文提出并测评了一套双生基准：Edit-Compass（图像编辑能力评测）和 EditReward-Compass（图像编辑奖励模型评测）。 |
| 2026-06 | [lighting-edit-bench](../papers/2026-06_lighting-edit-bench/解读.md) | Do Image Editing Models Understand Lighting? | 这篇论文做的是一个叫 3D-anchored Light Probe（3DLP） 的基准，用来回答一个问题：图像编辑模型真的“懂”现实光照和光传输吗？ |
| 2026-07 | [IIE-Survey](../papers/2026-07_IIE-Survey/解读.md) | Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications | 这是一篇对“指令式图像编辑”（Instruction-based Image Editing, IIE）的系统综述与基准论文。 |

## 2. 可信度边界

下面这段只针对 §1 和 §3 里的 **160 篇标准深读**；§4 那 26 项走的是另一套验收口径。

160 个 arXiv ID 全部实抓 `arxiv.org/abs` 比对过标题与日期；160 篇 PDF 全部可解析，篇幅全部达标。
篇幅区间 6502–8943 汉字（2026-08-30 全量重数，口径 U+4E00–U+9FFF）。
结构上 158 篇是标准 11 节；Complex-Edit 和 KRIS-Bench 这两篇 benchmark 各有 19 个二级标题——
标准 11 节之后接了第二批那套 benchmark 格式的 6 个无编号小节（一句话结论 / 问题与动机 / 方法与数据构造 /
评测设计与指标 / 关键结果 / 局限），再补 §12 决策意义、§13 一手来源。
**但 2026 的 38 篇里有 33 篇是模型从 1123 篇候选里筛出来的，人工只定了标准**，还有图表信息丢失、公式失真等已知问题——
详见 [总结分析.md](总结分析.md) 第 5 节，用之前先看那一节。

## 3. 按时间的全量清单

| 时间 | 简称 | arXiv | 解读字数 |
| --- | --- | --- | --- |
| 2021-08-02 | [SDEdit](../papers/2021-08_SDEdit/解读.md) | [2108.01073](https://arxiv.org/abs/2108.01073) | 7249 |
| 2021-12-20 | [Latent-Diffusion](../papers/2021-12_Latent-Diffusion/解读.md) | [2112.10752](https://arxiv.org/abs/2112.10752) | 7160 |
| 2022-06-06 | [Blended-Latent-Diffusion](../papers/2022-06_Blended-Latent-Diffusion/解读.md) | [2206.02779](https://arxiv.org/abs/2206.02779) | 6702 |
| 2022-07-26 | [Classifier-Free-Guidance](../papers/2022-07_Classifier-Free-Guidance/解读.md) | [2207.12598](https://arxiv.org/abs/2207.12598) | 6581 |
| 2022-08-02 | [Prompt-to-Prompt](../papers/2022-08_Prompt-to-Prompt/解读.md) | [2208.01626](https://arxiv.org/abs/2208.01626) | 7138 |
| 2022-08-02 | [Textual-Inversion](../papers/2022-08_Textual-Inversion/解读.md) | [2208.01618](https://arxiv.org/abs/2208.01618) | 6900 |
| 2022-08-25 | [DreamBooth](../papers/2022-08_DreamBooth/解读.md) | [2208.12242](https://arxiv.org/abs/2208.12242) | 6553 |
| 2022-10-17 | [Imagic](../papers/2022-10_Imagic/解读.md) | [2210.09276](https://arxiv.org/abs/2210.09276) | 7136 |
| 2022-10-20 | [DiffEdit](../papers/2022-10_DiffEdit/解读.md) | [2210.11427](https://arxiv.org/abs/2210.11427) | 7215 |
| 2022-11-17 | [InstructPix2Pix](../papers/2022-11_InstructPix2Pix/解读.md) | [2211.09800](https://arxiv.org/abs/2211.09800) | 7603 |
| 2022-11-17 | [Null-text-Inversion](../papers/2022-11_Null-text-Inversion/解读.md) | [2211.09794](https://arxiv.org/abs/2211.09794) | 7202 |
| 2022-11-22 | [EDICT](../papers/2022-11_EDICT/解读.md) | [2211.12446](https://arxiv.org/abs/2211.12446) | 6614 |
| 2022-11-22 | [Plug-and-Play](../papers/2022-11_Plug-and-Play/解读.md) | [2211.12572](https://arxiv.org/abs/2211.12572) | 7284 |
| 2022-11-23 | [Paint-by-Example](../papers/2022-11_Paint-by-Example/解读.md) | [2211.13227](https://arxiv.org/abs/2211.13227) | 7577 |
| 2022-12-08 | [Custom-Diffusion](../papers/2022-12_Custom-Diffusion/解读.md) | [2212.04488](https://arxiv.org/abs/2212.04488) | 7128 |
| 2022-12-13 | [Imagen-Editor-EditBench](../papers/2022-12_Imagen-Editor-EditBench/解读.md) | [2212.06909](https://arxiv.org/abs/2212.06909) | 8394 |
| 2023-02-06 | [pix2pix-zero](../papers/2023-02_pix2pix-zero/解读.md) | [2302.03027](https://arxiv.org/abs/2302.03027) | 6692 |
| 2023-02-10 | [ControlNet](../papers/2023-02_ControlNet/解读.md) | [2302.05543](https://arxiv.org/abs/2302.05543) | 7943 |
| 2023-02-16 | [T2I-Adapter](../papers/2023-02_T2I-Adapter/解读.md) | [2302.08453](https://arxiv.org/abs/2302.08453) | 7127 |
| 2023-03-16 | [HIVE](../papers/2023-03_HIVE/解读.md) | [2303.09618](https://arxiv.org/abs/2303.09618) | 7788 |
| 2023-04-05 | [SAM](../papers/2023-04_SAM/解读.md) | [2304.02643](https://arxiv.org/abs/2304.02643) | 6768 |
| 2023-04-13 | [Inpaint-Anything](../papers/2023-04_Inpaint-Anything/解读.md) | [2304.06790](https://arxiv.org/abs/2304.06790) | 8149 |
| 2023-04-17 | [MasaCtrl](../papers/2023-04_MasaCtrl/解读.md) | [2304.08465](https://arxiv.org/abs/2304.08465) | 6562 |
| 2023-05-18 | [DragGAN](../papers/2023-05_DragGAN/解读.md) | [2305.10973](https://arxiv.org/abs/2305.10973) | 7007 |
| 2023-06-01 | [Self-Guidance](../papers/2023-06_Self-Guidance/解读.md) | [2306.00986](https://arxiv.org/abs/2306.00986) | 7259 |
| 2023-06-16 | [MagicBrush](../papers/2023-06_MagicBrush/解读.md) | [2306.10012](https://arxiv.org/abs/2306.10012) | 7080 |
| 2023-06-26 | [DragDiffusion](../papers/2023-06_DragDiffusion/解读.md) | [2306.14435](https://arxiv.org/abs/2306.14435) | 7065 |
| 2023-07-05 | [DragonDiffusion](../papers/2023-07_DragonDiffusion/解读.md) | [2307.02421](https://arxiv.org/abs/2307.02421) | 7518 |
| 2023-07-18 | [AnyDoor](../papers/2023-07_AnyDoor/解读.md) | [2307.09481](https://arxiv.org/abs/2307.09481) | 7129 |
| 2023-08-13 | [IP-Adapter](../papers/2023-08_IP-Adapter/解读.md) | [2308.06721](https://arxiv.org/abs/2308.06721) | 7379 |
| 2023-09-07 | [InstructDiffusion](../papers/2023-09_InstructDiffusion/解读.md) | [2309.03895](https://arxiv.org/abs/2309.03895) | 6804 |
| 2023-09-29 | [MGIE](../papers/2023-09_MGIE/解读.md) | [2309.17102](https://arxiv.org/abs/2309.17102) | 8943 |
| 2023-09-30 | [PixArt-alpha](../papers/2023-09_PixArt-alpha/解读.md) | [2310.00426](https://arxiv.org/abs/2310.00426) | 6861 |
| 2023-11-06 | [Cross-Image-Attention](../papers/2023-11_Cross-Image-Attention/解读.md) | [2311.03335](https://arxiv.org/abs/2311.03335) | 7423 |
| 2023-11-16 | [Emu-Edit](../papers/2023-11_Emu-Edit/解读.md) | [2311.10089](https://arxiv.org/abs/2311.10089) | 6854 |
| 2023-11-20 | [Concept-Sliders](../papers/2023-11_Concept-Sliders/解读.md) | [2311.12092](https://arxiv.org/abs/2311.12092) | 7827 |
| 2023-11-28 | [LEDITSpp](../papers/2023-11_LEDITSpp/解读.md) | [2311.16711](https://arxiv.org/abs/2311.16711) | 6869 |
| 2023-12-04 | [StyleAligned](../papers/2023-12_StyleAligned/解读.md) | [2312.02133](https://arxiv.org/abs/2312.02133) | 7216 |
| 2023-12-06 | [PowerPaint](../papers/2023-12_PowerPaint/解读.md) | [2312.03594](https://arxiv.org/abs/2312.03594) | 7204 |
| 2023-12-07 | [InfEdit](../papers/2023-12_InfEdit/解读.md) | [2312.04965](https://arxiv.org/abs/2312.04965) | 6814 |
| 2023-12-07 | [PhotoMaker](../papers/2023-12_PhotoMaker/解读.md) | [2312.04461](https://arxiv.org/abs/2312.04461) | 7001 |
| 2023-12-11 | [SmartEdit](../papers/2023-12_SmartEdit/解读.md) | [2312.06739](https://arxiv.org/abs/2312.06739) | 6742 |
| 2023-12-20 | [Emu2](../papers/2023-12_Emu2/解读.md) | [2312.13286](https://arxiv.org/abs/2312.13286) | 6701 |
| 2024-01-03 | [Instruct-Imagen](../papers/2024-01_Instruct-Imagen/解读.md) | [2401.01952](https://arxiv.org/abs/2401.01952) | 7210 |
| 2024-01-15 | [InstantID](../papers/2024-01_InstantID/解读.md) | [2401.07519](https://arxiv.org/abs/2401.07519) | 6825 |
| 2024-02-04 | [DiffEditor](../papers/2024-02_DiffEditor/解读.md) | [2402.02583](https://arxiv.org/abs/2402.02583) | 7254 |
| 2024-03-05 | [SD3-RectifiedFlow](../papers/2024-03_SD3-RectifiedFlow/解读.md) | [2403.03206](https://arxiv.org/abs/2403.03206) | 6564 |
| 2024-03-11 | [BrushNet](../papers/2024-03_BrushNet/解读.md) | [2403.06976](https://arxiv.org/abs/2403.06976) | 6745 |
| 2024-03-21 | [ReNoise](../papers/2024-03_ReNoise/解读.md) | [2403.14602](https://arxiv.org/abs/2403.14602) | 6706 |
| 2024-04-03 | [VAR](../papers/2024-04_VAR/解读.md) | [2404.02905](https://arxiv.org/abs/2404.02905) | 8136 |
| 2024-04-15 | [HQ-Edit](../papers/2024-04_HQ-Edit/解读.md) | [2404.09990](https://arxiv.org/abs/2404.09990) | 7232 |
| 2024-04-22 | [SEED-X](../papers/2024-04_SEED-X/解读.md) | [2404.14396](https://arxiv.org/abs/2404.14396) | 6648 |
| 2024-05-07 | [SEED-Data-Edit](../papers/2024-05_SEED-Data-Edit/解读.md) | [2405.04007](https://arxiv.org/abs/2405.04007) | 6626 |
| 2024-05-16 | [Chameleon](../papers/2024-05_Chameleon/解读.md) | [2405.09818](https://arxiv.org/abs/2405.09818) | 8109 |
| 2024-06-11 | [MimicBrush](../papers/2024-06_MimicBrush/解读.md) | [2406.07547](https://arxiv.org/abs/2406.07547) | 8536 |
| 2024-07-07 | [UltraEdit](../papers/2024-07_UltraEdit/解读.md) | [2407.05282](https://arxiv.org/abs/2407.05282) | 7074 |
| 2024-08-01 | [TurboEdit](../papers/2024-08_TurboEdit/解读.md) | [2408.00735](https://arxiv.org/abs/2408.00735) | 6973 |
| 2024-08-20 | [Transfusion](../papers/2024-08_Transfusion/解读.md) | [2408.11039](https://arxiv.org/abs/2408.11039) | 7019 |
| 2024-08-22 | [Show-o](../papers/2024-08_Show-o/解读.md) | [2408.12528](https://arxiv.org/abs/2408.12528) | 7514 |
| 2024-09-17 | [OmniGen](../papers/2024-09_OmniGen/解读.md) | [2409.11340](https://arxiv.org/abs/2409.11340) | 8139 |
| 2024-09-27 | [Emu3](../papers/2024-09_Emu3/解读.md) | [2409.18869](https://arxiv.org/abs/2409.18869) | 7382 |
| 2024-10-14 | [RF-Inversion](../papers/2024-10_RF-Inversion/解读.md) | [2410.10792](https://arxiv.org/abs/2410.10792) | 7312 |
| 2024-10-31 | [In-Context-LoRA](../papers/2024-10_In-Context-LoRA/解读.md) | [2410.23775](https://arxiv.org/abs/2410.23775) | 6951 |
| 2024-11-07 | [RF-Solver-Edit](../papers/2024-11_RF-Solver-Edit/解读.md) | [2411.04746](https://arxiv.org/abs/2411.04746) | 7204 |
| 2024-11-11 | [Add-it](../papers/2024-11_Add-it/解读.md) | [2411.07232](https://arxiv.org/abs/2411.07232) | 7033 |
| 2024-11-11 | [OmniEdit](../papers/2024-11_OmniEdit/解读.md) | [2411.07199](https://arxiv.org/abs/2411.07199) | 7402 |
| 2024-11-11 | [SeedEdit](../papers/2024-11_SeedEdit/解读.md) | [2411.06686](https://arxiv.org/abs/2411.06686) | 7623 |
| 2024-11-14 | [MagicQuill](../papers/2024-11_MagicQuill/解读.md) | [2411.09703](https://arxiv.org/abs/2411.09703) | 7389 |
| 2024-11-22 | [OminiControl](../papers/2024-11_OminiControl/解读.md) | [2411.15098](https://arxiv.org/abs/2411.15098) | 6543 |
| 2024-11-24 | [AnyEdit](../papers/2024-11_AnyEdit/解读.md) | [2411.15738](https://arxiv.org/abs/2411.15738) | 7500 |
| 2024-12-10 | [UniReal](../papers/2024-12_UniReal/解读.md) | [2412.07774](https://arxiv.org/abs/2412.07774) | 6953 |
| 2025-01-05 | [ACEpp](../papers/2025-01_ACEpp/解读.md) | [2501.02487](https://arxiv.org/abs/2501.02487) | 7487 |
| 2025-01-29 | [Janus-Pro](../papers/2025-01_Janus-Pro/解读.md) | [2501.17811](https://arxiv.org/abs/2501.17811) | 8116 |
| 2025-03-10 | [EasyControl](../papers/2025-03_EasyControl/解读.md) | [2503.07027](https://arxiv.org/abs/2503.07027) | 7188 |
| 2025-03-13 | [GoT](../papers/2025-03_GoT/解读.md) | [2503.10639](https://arxiv.org/abs/2503.10639) | 7356 |
| 2025-04-02 | [UNO](../papers/2025-04_UNO/解读.md) | [2504.02160](https://arxiv.org/abs/2504.02160) | 7202 |
| 2025-04-03 | [RISEBench](../papers/2025-04_RISEBench/解读.md) | [2504.02826](https://arxiv.org/abs/2504.02826) | 7917 |
| 2025-04-08 | [MetaQuery](../papers/2025-04_MetaQuery/解读.md) | [2504.06256](https://arxiv.org/abs/2504.06256) | 7502 |
| 2025-04-17 | [Complex-Edit](../papers/2025-04_Complex-Edit/解读.md) | [2504.13143](https://arxiv.org/abs/2504.13143) | 8329 |
| 2025-04-21 | [Insert-Anything](../papers/2025-04_Insert-Anything/解读.md) | [2504.15009](https://arxiv.org/abs/2504.15009) | 6580 |
| 2025-04-23 | [DreamO](../papers/2025-04_DreamO/解读.md) | [2504.16915](https://arxiv.org/abs/2504.16915) | 7727 |
| 2025-04-24 | [Step1X-Edit](../papers/2025-04_Step1X-Edit/解读.md) | [2504.17761](https://arxiv.org/abs/2504.17761) | 7396 |
| 2025-04-29 | [ICEdit](../papers/2025-04_ICEdit/解读.md) | [2504.20690](https://arxiv.org/abs/2504.20690) | 6865 |
| 2025-05-01 | [T2I-R1](../papers/2025-05_T2I-R1/解读.md) | [2505.00703](https://arxiv.org/abs/2505.00703) | 6876 |
| 2025-05-08 | [Flow-GRPO](../papers/2025-05_Flow-GRPO/解读.md) | [2505.05470](https://arxiv.org/abs/2505.05470) | 6502 |
| 2025-05-12 | [DanceGRPO](../papers/2025-05_DanceGRPO/解读.md) | [2505.07818](https://arxiv.org/abs/2505.07818) | 7294 |
| 2025-05-14 | [BLIP3-o](../papers/2025-05_BLIP3-o/解读.md) | [2505.09568](https://arxiv.org/abs/2505.09568) | 6887 |
| 2025-05-20 | [BAGEL](../papers/2025-05_BAGEL/解读.md) | [2505.14683](https://arxiv.org/abs/2505.14683) | 7170 |
| 2025-05-22 | [KRIS-Bench](../papers/2025-05_KRIS-Bench/解读.md) | [2505.16707](https://arxiv.org/abs/2505.16707) | 7494 |
| 2025-05-26 | [ImgEdit](../papers/2025-05_ImgEdit/解读.md) | [2505.20275](https://arxiv.org/abs/2505.20275) | 7451 |
| 2025-05-28 | [HiDream-I1](../papers/2025-05_HiDream-I1/解读.md) | [2505.22705](https://arxiv.org/abs/2505.22705) | 7337 |
| 2025-06-03 | [UniWorld-V1](../papers/2025-06_UniWorld-V1/解读.md) | [2506.03147](https://arxiv.org/abs/2506.03147) | 6657 |
| 2025-06-05 | [SeedEdit3](../papers/2025-06_SeedEdit3/解读.md) | [2506.05083](https://arxiv.org/abs/2506.05083) | 7643 |
| 2025-06-17 | [FLUX-Kontext](../papers/2025-06_FLUX-Kontext/解读.md) | [2506.15742](https://arxiv.org/abs/2506.15742) | 8679 |
| 2025-06-18 | [Show-o2](../papers/2025-06_Show-o2/解读.md) | [2506.15564](https://arxiv.org/abs/2506.15564) | 6918 |
| 2025-06-23 | [OmniGen2](../papers/2025-06_OmniGen2/解读.md) | [2506.18871](https://arxiv.org/abs/2506.18871) | 6695 |
| 2025-06-29 | [Ovis-U1](../papers/2025-06_Ovis-U1/解读.md) | [2506.23044](https://arxiv.org/abs/2506.23044) | 6716 |
| 2025-07-18 | [NoHumansRequired](../papers/2025-07_NoHumansRequired/解读.md) | [2507.14119](https://arxiv.org/abs/2507.14119) | 6730 |
| 2025-07-28 | [GPT-Image-Edit-1.5M](../papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | [2507.21033](https://arxiv.org/abs/2507.21033) | 6615 |
| 2025-08-04 | [Qwen-Image](../papers/2025-08_Qwen-Image/解读.md) | [2508.02324](https://arxiv.org/abs/2508.02324) | 7310 |
| 2025-08-11 | [X2Edit](../papers/2025-08_X2Edit/解读.md) | [2508.07607](https://arxiv.org/abs/2508.07607) | 6789 |
| 2025-08-21 | [VAREdit](../papers/2025-08_VAREdit/解读.md) | [2508.15772](https://arxiv.org/abs/2508.15772) | 7076 |
| 2025-09-16 | [EdiVal-Agent](../papers/2025-09_EdiVal-Agent/解读.md) | [2509.13399](https://arxiv.org/abs/2509.13399) | 6599 |
| 2025-09-24 | [EditVerse](../papers/2025-09_EditVerse/解读.md) | [2509.20360](https://arxiv.org/abs/2509.20360) | 7231 |
| 2025-09-24 | [Seedream4](../papers/2025-09_Seedream4/解读.md) | [2509.20427](https://arxiv.org/abs/2509.20427) | 6611 |
| 2025-09-28 | [EditScore](../papers/2025-09_EditScore/解读.md) | [2509.23909](https://arxiv.org/abs/2509.23909) | 6719 |
| 2025-09-28 | [HunyuanImage3](../papers/2025-09_HunyuanImage3/解读.md) | [2509.23951](https://arxiv.org/abs/2509.23951) | 6546 |
| 2025-09-29 | [OpenGPT-4o-Image](../papers/2025-09_OpenGPT-4o-Image/解读.md) | [2509.24900](https://arxiv.org/abs/2509.24900) | 7651 |
| 2025-09-30 | [EditReward](../papers/2025-09_EditReward/解读.md) | [2509.26346](https://arxiv.org/abs/2509.26346) | 7572 |
| 2025-10-05 | [ChronoEdit](../papers/2025-10_ChronoEdit/解读.md) | [2510.04290](https://arxiv.org/abs/2510.04290) | 6825 |
| 2025-10-07 | [Lumina-DiMOO](../papers/2025-10_Lumina-DiMOO/解读.md) | [2510.06308](https://arxiv.org/abs/2510.06308) | 7291 |
| 2025-10-08 | [DreamOmni2](../papers/2025-10_DreamOmni2/解读.md) | [2510.06679](https://arxiv.org/abs/2510.06679) | 6564 |
| 2025-10-09 | [InstructX](../papers/2025-10_InstructX/解读.md) | [2510.08485](https://arxiv.org/abs/2510.08485) | 6671 |
| 2025-10-09 | [Kontinuous-Kontext](../papers/2025-10_Kontinuous-Kontext/解读.md) | [2510.08532](https://arxiv.org/abs/2510.08532) | 8551 |
| 2025-10-19 | [Edit-R1-UniWorld-V2](../papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | [2510.16888](https://arxiv.org/abs/2510.16888) | 6542 |
| 2025-10-20 | [PICABench](../papers/2025-10_PICABench/解读.md) | [2510.17681](https://arxiv.org/abs/2510.17681) | 7739 |
| 2025-10-22 | [Pico-Banana-400K](../papers/2025-10_Pico-Banana-400K/解读.md) | [2510.19808](https://arxiv.org/abs/2510.19808) | 7750 |
| 2025-10-30 | [Emu3.5](../papers/2025-10_Emu3.5/解读.md) | [2510.26583](https://arxiv.org/abs/2510.26583) | 7580 |
| 2025-11-03 | [UniREditBench](../papers/2025-11_UniREditBench/解读.md) | [2511.01295](https://arxiv.org/abs/2511.01295) | 7321 |
| 2025-11-27 | [ReasonEdit](../papers/2025-11_ReasonEdit/解读.md) | [2511.22625](https://arxiv.org/abs/2511.22625) | 7349 |
| 2025-11-27 | [Z-Image](../papers/2025-11_Z-Image/解读.md) | [2511.22699](https://arxiv.org/abs/2511.22699) | 6667 |
| 2025-12-17 | [Qwen-Image-Layered](../papers/2025-12_Qwen-Image-Layered/解读.md) | [2512.15603](https://arxiv.org/abs/2512.15603) | 7109 |
| 2026-01-05 | [nextflow](../papers/2026-01_nextflow/解读.md) | [2601.02204](https://arxiv.org/abs/2601.02204) | 7320 |
| 2026-01-06 | [ThinkRL-Edit](../papers/2026-01_ThinkRL-Edit/解读.md) | [2601.03467](https://arxiv.org/abs/2601.03467) | 7196 |
| 2026-01-06 | [reward-hacking-t2i](../papers/2026-01_reward-hacking-t2i/解读.md) | [2601.03468](https://arxiv.org/abs/2601.03468) | 7524 |
| 2026-02-02 | [unireason](../papers/2026-02_unireason/解读.md) | [2602.02437](https://arxiv.org/abs/2602.02437) | 7070 |
| 2026-02-07 | [spatialreward-edit](../papers/2026-02_spatialreward-edit/解读.md) | [2602.07458](https://arxiv.org/abs/2602.07458) | 7019 |
| 2026-02-09 | [reasoning-to-pixels](../papers/2026-02_reasoning-to-pixels/解读.md) | [2602.08336](https://arxiv.org/abs/2602.08336) | 6985 |
| 2026-02-09 | [rethink-global-text](../papers/2026-02_rethink-global-text/解读.md) | [2602.09268](https://arxiv.org/abs/2602.09268) | 7486 |
| 2026-02-12 | [FireRed-Image-Edit](../papers/2026-02_FireRed-Image-Edit/解读.md) | [2602.13344](https://arxiv.org/abs/2602.13344) | 7109 |
| 2026-02-22 | [ChordEdit](../papers/2026-02_ChordEdit/解读.md) | [2602.19083](https://arxiv.org/abs/2602.19083) | 7579 |
| 2026-03-09 | [care-edit](../papers/2026-03_care-edit/解读.md) | [2603.08589](https://arxiv.org/abs/2603.08589) | 6830 |
| 2026-03-09 | [coco-code-cot](../papers/2026-03_coco-code-cot/解读.md) | [2603.08652](https://arxiv.org/abs/2603.08652) | 6950 |
| 2026-03-10 | [internvl-u](../papers/2026-03_internvl-u/解读.md) | [2603.09877](https://arxiv.org/abs/2603.09877) | 6642 |
| 2026-03-17 | [ug-fight-dpo](../papers/2026-03_ug-fight-dpo/解读.md) | [2603.17044](https://arxiv.org/abs/2603.17044) | 6969 |
| 2026-03-31 | [editing-manifold](../papers/2026-03_editing-manifold/解读.md) | [2603.29736](https://arxiv.org/abs/2603.29736) | 7110 |
| 2026-04-03 | [banana100](../papers/2026-04_banana100/解读.md) | [2604.03400](https://arxiv.org/abs/2604.03400) | 8186 |
| 2026-04-26 | [edit-where-you-mean](../papers/2026-04_edit-where-you-mean/解读.md) | [2604.23763](https://arxiv.org/abs/2604.23763) | 6989 |
| 2026-04-27 | [beyond-accuracy](../papers/2026-04_beyond-accuracy/解读.md) | [2604.25072](https://arxiv.org/abs/2604.25072) | 7280 |
| 2026-04-27 | [meta-cot](../papers/2026-04_meta-cot/解读.md) | [2604.24625](https://arxiv.org/abs/2604.24625) | 6900 |
| 2026-04-27 | [tuna-2](../papers/2026-04_tuna-2/解读.md) | [2604.24763](https://arxiv.org/abs/2604.24763) | 6618 |
| 2026-04-29 | [spatialfusion](../papers/2026-04_spatialfusion/解读.md) | [2604.26341](https://arxiv.org/abs/2604.26341) | 6812 |
| 2026-05-04 | [directedit](../papers/2026-05_directedit/解读.md) | [2605.02417](https://arxiv.org/abs/2605.02417) | 7200 |
| 2026-05-11 | [Qwen-Image-2.0](../papers/2026-05_Qwen-Image-2.0/解读.md) | [2605.10730](https://arxiv.org/abs/2605.10730) | 8086 |
| 2026-05-11 | [masked-gen-transformer](../papers/2026-05_masked-gen-transformer/解读.md) | [2605.10859](https://arxiv.org/abs/2605.10859) | 6797 |
| 2026-05-12 | [sensenova-u1](../papers/2026-05_sensenova-u1/解读.md) | [2605.12500](https://arxiv.org/abs/2605.12500) | 6907 |
| 2026-05-13 | [edit-compass](../papers/2026-05_edit-compass/解读.md) | [2605.13062](https://arxiv.org/abs/2605.13062) | 6567 |
| 2026-05-20 | [decompose-subject](../papers/2026-05_decompose-subject/解读.md) | [2605.20807](https://arxiv.org/abs/2605.20807) | 7064 |
| 2026-06-02 | [bootstrap-generator](../papers/2026-06_bootstrap-generator/解读.md) | [2606.03911](https://arxiv.org/abs/2606.03911) | 7686 |
| 2026-06-09 | [arm-unified](../papers/2026-06_arm-unified/解读.md) | [2606.11188](https://arxiv.org/abs/2606.11188) | 7433 |
| 2026-06-11 | [hydra-x](../papers/2026-06_hydra-x/解读.md) | [2606.13289](https://arxiv.org/abs/2606.13289) | 6583 |
| 2026-06-14 | [mind-the-gap](../papers/2026-06_mind-the-gap/解读.md) | [2606.15982](https://arxiv.org/abs/2606.15982) | 6741 |
| 2026-06-17 | [moebius-inpainting](../papers/2026-06_moebius-inpainting/解读.md) | [2606.19195](https://arxiv.org/abs/2606.19195) | 6843 |
| 2026-06-25 | [lighting-edit-bench](../papers/2026-06_lighting-edit-bench/解读.md) | [2606.26738](https://arxiv.org/abs/2606.26738) | 6897 |
| 2026-06-25 | [qwen-image-rl](../papers/2026-06_qwen-image-rl/解读.md) | [2606.27608](https://arxiv.org/abs/2606.27608) | 8108 |
| 2026-07-06 | [cfg-inversion-fail](../papers/2026-07_cfg-inversion-fail/解读.md) | [2607.04731](https://arxiv.org/abs/2607.04731) | 6682 |
| 2026-07-08 | [implicit-preservation](../papers/2026-07_implicit-preservation/解读.md) | [2607.07051](https://arxiv.org/abs/2607.07051) | 6823 |
| 2026-07-13 | [read-it-back](../papers/2026-07_read-it-back/解读.md) | [2607.11886](https://arxiv.org/abs/2607.11886) | 6611 |
| 2026-07-28 | [IIE-Survey](../papers/2026-07_IIE-Survey/解读.md) | [2607.25642](https://arxiv.org/abs/2607.25642) | 8309 |
| 2026-08-24 | [rl-no-edit-rewards](../papers/2026-08_rl-no-edit-rewards/解读.md) | [2608.22780](https://arxiv.org/abs/2608.22780) | 7117 |

## 4. 第二批：26 项决策型笔记（2026-08-29 补）

这批是围绕 Lark《Image Edit领域论文调研》做核验时补进来的，写法和上面 160 篇不同：
不追 6500–8500 字，只要覆盖「一句话结论 / 问题与适用边界 / 方法与数据构造 / 评测指标 /
关键结果与论文锚点 / 局限与未证实主张 / 对身份与局部保持的决策意义 / venue 与引用来源」即可。
以 benchmark 和评测指标为主，另有 4 项没有独立论文、只做官方资料核验。

逐项的 venue、首发时间、引用量和一手来源在 [`review/`](review/) 四份 manifest 里，
入口是 [LARK清单_核验索引.md](LARK清单_核验索引.md)。

| 时间 | 简称 | 论文 / 条目 | 来源 | venue | 中文字数 |
| --- | --- | --- | --- | --- | ---: |
| 2023-04-13 | [Rich-Text](../papers/2023-04_Rich-Text/解读.md) | Expressive Text-to-Image Generation with Rich Text | [2304.06720](https://arxiv.org/abs/2304.06720) | — | 6817 |
| 2023-05-29 | [InstructEdit](../papers/2023-05_InstructEdit/解读.md) | InstructEdit: Improving Automatic Masks for Diffusion-based Image Editing With User Instructions | [2305.18047](https://arxiv.org/abs/2305.18047) | — | 6897 |
| 2024-08-01 | [FLUX.1](../papers/2024-08_FLUX.1/解读.md) | FLUX.1 Model Family | [官方来源](https://bfl.ai/blog/24-08-01-bfl) | Black Forest Labs official launch blog/model card | 634 |
| 2024-08-26 | [I2EBench](../papers/2024-08_I2EBench/解读.md) | I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing | [2408.14180](https://arxiv.org/abs/2408.14180) | NeurIPS 2024 Main Conference | 2518 |
| 2024-11-27 | [FlowChef](../papers/2024-12_FlowChef/解读.md) | FlowChef: Steering of Rectified Flow Models for Controlled Generations | [2412.00100](https://arxiv.org/abs/2412.00100) | ICCV 2025 | 4314 |
| 2024-12 | [Grok-Aurora](../papers/2024-12_Grok-Aurora/解读.md) | Grok (Aurora) | [官方来源](https://docs.x.ai/docs/models) | — | 330 |
| 2025-05-01 | [HATIE](../papers/2025-05_HATIE/解读.md) | Towards Scalable Human-aligned Benchmark for Text-guided Image Editing | [2505.00502](https://arxiv.org/abs/2505.00502) | CVPR 2025 Highlight | 6842 |
| 2025-05-16 | [GIE-Bench](../papers/2025-05_GIE-Bench/解读.md) | GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing | [2505.11493](https://arxiv.org/abs/2505.11493) | arXiv; submitted to ICLR 2026 | 2670 |
| 2025-05-22 | [Everyday-Image-Editing](../papers/2025-05_Everyday-Image-Editing/解读.md) | Understanding Generative AI Capabilities in Everyday Image Editing Tasks | [2505.16181](https://arxiv.org/abs/2505.16181) | WACV 2026 | 2986 |
| 2025-05-26 | [DICE](../papers/2025-05_DICE/解读.md) | What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models | [2505.20405](https://arxiv.org/abs/2505.20405) | ICCV 2025 | 3306 |
| 2025-06-03 | [RefEdit](../papers/2025-06_RefEdit/解读.md) | RefEdit: A Benchmark and Method for Improving Instruction-based Image Editing Model on Referring Expressions | [2506.03448](https://arxiv.org/abs/2506.03448) | ICCV 2025 | 2516 |
| 2025-06-15 | [BPM](../papers/2025-06_BPM/解读.md) | Balancing Preservation and Modification: A Region and Semantic Aware Metric for Instruction-Based Image Editing | [2506.13827](https://arxiv.org/abs/2506.13827) | ICML 2025 | 2528 |
| 2025-06-15 | [ComplexBench-Edit](../papers/2025-06_ComplexBench-Edit/解读.md) | ComplexBench-Edit: Benchmarking Complex Instruction-Driven Image Editing via Compositional Dependencies | [2506.12830](https://arxiv.org/abs/2506.12830) | ACM Multimedia 2025 | 2534 |
| 2025-07-22 | [LMM4Edit](../papers/2025-07_LMM4Edit/解读.md) | LMM4Edit: Benchmarking and Evaluating Multimodal Image Editing with LMMs | [2507.16193](https://arxiv.org/abs/2507.16193) | ACM Multimedia 2025 | 2544 |
| 2025-11-29 | [WiseEdit](../papers/2025-12_WiseEdit/解读.md) | WiseEdit: Benchmarking Cognition- and Creativity-Informed Image Editing | [2512.00387](https://arxiv.org/abs/2512.00387) | arXiv | 2593 |
| 2025-12-04 | [I2I-Bench](../papers/2025-12_I2I-Bench/解读.md) | I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models | [2512.04660](https://arxiv.org/abs/2512.04660) | CVPR 2026 | 7049 |
| 2025-12-17 | [Qwen-Image-Edit-2511](../papers/2025-12_Qwen-Image-Edit-2511/解读.md) | Qwen-Image-Edit-2511 | [官方来源](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | Qwen official model card | 666 |
| 2026-02-02 | [VIBE](../papers/2026-02_VIBE/解读.md) | How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing | [2602.01851](https://arxiv.org/abs/2602.01851) | arXiv 预印本 | 2564 |
| 2026-03-16 | [Omni-IIE-Bench](../papers/2026-03_Omni-IIE-Bench/解读.md) | Omni IIE Bench: Benchmarking the Practical Capabilities of Image Editing Models | [2603.16944](https://arxiv.org/abs/2603.16944) | CVPR 2026 | 3225 |
| 2026-03-20 | [TIEdit-EditProbe](../papers/2026-03_TIEdit-EditProbe/解读.md) | Evaluating Image Editing with LLMs: A Comprehensive Benchmark and Intermediate-Layer Probing Approach | [2603.19775](https://arxiv.org/abs/2603.19775) | Displays, Volume 94 | 2864 |
| 2026-03-30 | [GEditBench-v2](../papers/2026-03_GEditBench-v2/解读.md) | GEditBench v2: A Human-Aligned Benchmark for General Image Editing | [2603.28547](https://arxiv.org/abs/2603.28547) | arXiv | 3755 |
| 2026-04-21 | [GPT-Image-2](../papers/2026-04_GPT-Image-2/解读.md) | GPT Image 2 | [官方来源](https://developers.openai.com/api/docs/models/gpt-image-2) | OpenAI official model documentation | 732 |
| 2026-04-22 | [GSI-Bench](../papers/2026-04_GSI-Bench/解读.md) | Exploring Spatial Intelligence from a Generative Perspective | [2604.20570](https://arxiv.org/abs/2604.20570) | CVPR 2026 | 2510 |
| 2026-05-29 | [PaintBench](../papers/2026-05_PaintBench/解读.md) | PaintBench: Deterministic Evaluation of Precise Visual Editing | [2606.00188](https://arxiv.org/abs/2606.00188) | arXiv 预印本 | 3038 |
| 2026-06-01 | [Inter-Edit](../papers/2026-06_Inter-Edit/解读.md) | Inter-Edit: First Benchmark for Interactive Instruction-Based Image Editing | [官方来源](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Inter-Edit_First_Benchmark_for_Interactive_Instruction-Based_Image_Editing_CVPR_2026_paper.html) | CVPR 2026 | 2661 |
| 2026-08-14 | [CPI-Bench](../papers/2026-08_CPI-Bench/解读.md) | CPI-Bench: A Comprehensive, Practical and Intelligent Benchmark for Real-World Image Editing | [2608.14546](https://arxiv.org/abs/2608.14546) | arXiv 预印本 | 2517 |

⚠️ 最后 4 项（FLUX.1、Grok/Aurora、Qwen-Image-Edit-2511、GPT Image 2）**没有独立论文**，
目录里也没有 `paper.pdf`。它们的笔记只记录官方资料和核验边界，不能用来反推架构、训练数据或身份保持机制。
