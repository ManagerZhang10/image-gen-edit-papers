# 图像编辑论文库 2021–2026

[![papers](https://img.shields.io/badge/papers-187-2b7489)](#全量清单)
[![notes](https://img.shields.io/badge/notes-1.23M_CJK_chars-4c9a2a)](#全量清单)
[![coverage](https://img.shields.io/badge/coverage-2021.08_--_2026.08-e07b39)](#全量清单)
[![links](https://img.shields.io/badge/source_links-183%2F187_byte--verified-1f883d)](docs/可信度与产出.md#2-原文直链是怎么核的)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**187 篇图像编辑论文，每篇一份中文深读笔记，外加一条核验过的原文直链。**
时间跨度 2021-08 → 2026-08，笔记合计 1,234,956 个汉字。

*187 image-editing papers, each with an in-depth Chinese reading note and a byte-verified link to the original PDF. Aug 2021 – Aug 2026.*

> **维护者** [@ManagerYu10](https://github.com/ManagerYu10) · **授权** [CC BY 4.0](LICENSE)（署名即可转载、改写、商用） · **最后核对** 2026-09-01
>
> ⚠️ **笔记正文由 DeepSeek v4 Pro 依据 PDF 抽取的文字生成**，人定标准、做机器校验、逐条抽查。
> 图里的信息模型读不到，公式符号会在 PDF 抽取时丢失。哪些能直接当依据、哪些必须回原文，
> 见 [可信度与产出.md](docs/可信度与产出.md)。

---

## 怎么用

直接拉到本页最后的[全量清单](#全量清单)，187 行按时间排，浏览器里 `Ctrl/Cmd + F` 搜简称或标题。每行两列可以点：

| 时间 | 简称（→ 解读） | 论文标题 | 原文 | 解读字数 |
| --- | --- | --- | --- | ---: |
| 2022-10-17 | [Imagic](papers/2022-10_Imagic/解读.md) | Imagic: Text-Based Real Image Editing with Diffusion Models | [PDF](https://arxiv.org/pdf/2210.09276) | 7136 |

| 这一列 | 点开是什么 |
| --- | --- |
| **简称** | 这篇的 `解读.md`，中文深读笔记，就在本仓库里 |
| **原文** | 论文本身。183 行标 `PDF`，直链与写笔记时用的那份本地 PDF 逐字节比对一致；4 行标 `官方来源`，那 4 项确实没有独立论文 |

**解读的定位是替代第一次完整泛读**，不替代精读——要抠实现细节仍然得回 PDF。
其中 160 篇是固定 11 节：30 秒定位 → 为什么这篇会出现 → 最小概念 → 数据流 → 核心公式 → 训练 → 推理 → 实验与消融 → 与前作怎么选 → 工程判断 → 收束（规范见 [prompt.md](docs/prompt.md)）。
另外 26 项是决策型短笔记，8～9 节；其中 4 项没有独立论文，只写官方资料和核验边界。
2026-09 起新增的篇目改用 8 节 / 3000～5000 字的 v2 规范（同样见 [prompt.md](docs/prompt.md)），目前 1 篇（FireEdit）；旧的 11 节规范不回炉重写。

**要原文 PDF**：不在仓库里，183 份合计 3.3 GB。单篇点表里的链接就行，批量拉到本地：

```bash
python3 scripts/fetch_pdfs.py                    # 补齐所有缺的，约 10 分钟
python3 scripts/fetch_pdfs.py --list             # 只列缺什么，不下载
python3 scripts/fetch_pdfs.py 2024-11_OmniEdit   # 只下一篇
```

只用标准库，按 arXiv 要求节流到每 3 秒一份，断了重跑只补没下成的。下载到的 `paper.pdf` 被 `.gitignore` 挡住。

**还有三份文档**：[INDEX.md](docs/INDEX.md) 把 186 项按 15 条技术脉络分组（未含 2026-09 新增的 FireEdit）；[总结分析.md](docs/总结分析.md) 只写跨论文的结论；[可信度与产出.md](docs/可信度与产出.md) 写做过哪些校验、哪些地方已知会出错。

---

## 仓库长什么样

```
image_edit_paper/
├── README.md                       ← 本文件。怎么用 + 187 项全量清单
├── LICENSE                         ← CC BY 4.0
│
├── papers/                         ← 187 个论文目录，名字就是 YYYY-MM_简称，按时间自然排序
│   ├── 2021-08_SDEdit/
│   │   ├── 解读.md                  ← 中文笔记（唯一正文）
│   │   ├── meta.json                ← arXiv ID、日期、标题、字数、venue、引用量
│   │   └── paper.pdf                ← 不在仓库里，跑 scripts/fetch_pdfs.py 下载
│   ├── ...
│   └── 2026-08_CPI-Bench/
│
├── docs/
│   ├── INDEX.md                     ← 总索引：15 条脉络 + 按时间全量清单
│   ├── 总结分析.md                   ← 跨论文结论：转折点、脉络咬合、未解问题
│   ├── 可信度与产出.md                ← 做过哪些校验、哪些地方已知会出错、笔记怎么生成的
│   ├── prompt.md                     ← 深读的写作规范（原样作为 system prompt）；现为 v2：8 节 / 3000～5000 字
│   ├── LARK论文短版解读_PROMPT.md      ← 短版解读的写作规范
│   ├── PLAN.md                       ← 建库规划与五个阶段
│   ├── LARK清单_核验索引.md            ← 2026-08-29 那轮核验的总入口
│   ├── LARK清单_权威性与影响力.md       ← venue / 首发时间 / 引用量的口径与高引条目
│   └── review/                       ← 核验产出：4 份逐项 manifest + 4 份错误报告 + 数字溯源与 PDF 直链两份记录
│
├── scripts/
│   ├── pdf_sources.py               ← 直链推导规则 + 4 条例外（默认规则会取错的）
│   ├── fetch_pdfs.py                ← 按 meta.json 把 arXiv / CVF 原文拉回本地
│   └── verify_pdf_links.py          ← 核验清单里那 183 条直链，逐条比对远端与本地字节数
│
└── _work/                          ← 生产管线脚本（只留 .py 和 pdf_link_check.json，日志和中间产物没进仓库）
```

---

## 全量清单

186 项按时间排。**简称**点开是中文解读，**原文**点开是论文本身——182 条标 `PDF` 的都过了四项核验（HTTP 206、`Content-Type: application/pdf`、前 4 字节是 `%PDF`、**远端总字节数与本地 `paper.pdf` 完全一致**），4 项标 `官方来源` 的确实没有独立论文。口径见 [可信度与产出.md §2](docs/可信度与产出.md#2-原文直链是怎么核的)。

**解读字数**是当场从 `解读.md` 数的（U+4E00–U+9FFF），不读 `meta.json`。要复算表格 `python3 _work/gen_paper_table.py`，要复核链接 `python3 scripts/verify_pdf_links.py`。

| 时间 | 简称（→ 解读） | 论文标题 | 原文 | 解读字数 |
| --- | --- | --- | --- | ---: |
| 2021-08-02 | [SDEdit](papers/2021-08_SDEdit/解读.md) | SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations | [PDF](https://arxiv.org/pdf/2108.01073) | 7249 |
| 2021-12-20 | [Latent-Diffusion](papers/2021-12_Latent-Diffusion/解读.md) | High-Resolution Image Synthesis with Latent Diffusion Models | [PDF](https://arxiv.org/pdf/2112.10752) | 7160 |
| 2022-06-06 | [Blended-Latent-Diffusion](papers/2022-06_Blended-Latent-Diffusion/解读.md) | Blended Latent Diffusion | [PDF](https://arxiv.org/pdf/2206.02779) | 6702 |
| 2022-07-26 | [Classifier-Free-Guidance](papers/2022-07_Classifier-Free-Guidance/解读.md) | Classifier-Free Diffusion Guidance | [PDF](https://arxiv.org/pdf/2207.12598) | 6581 |
| 2022-08-25 | [DreamBooth](papers/2022-08_DreamBooth/解读.md) | DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation | [PDF](https://arxiv.org/pdf/2208.12242) | 6553 |
| 2022-08-02 | [Prompt-to-Prompt](papers/2022-08_Prompt-to-Prompt/解读.md) | Prompt-to-Prompt Image Editing with Cross Attention Control | [PDF](https://arxiv.org/pdf/2208.01626) | 7138 |
| 2022-08-02 | [Textual-Inversion](papers/2022-08_Textual-Inversion/解读.md) | An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion | [PDF](https://arxiv.org/pdf/2208.01618) | 6900 |
| 2022-10-20 | [DiffEdit](papers/2022-10_DiffEdit/解读.md) | DiffEdit: Diffusion-based semantic image editing with mask guidance | [PDF](https://arxiv.org/pdf/2210.11427) | 7215 |
| 2022-10-17 | [Imagic](papers/2022-10_Imagic/解读.md) | Imagic: Text-Based Real Image Editing with Diffusion Models | [PDF](https://arxiv.org/pdf/2210.09276) | 7136 |
| 2022-11-22 | [EDICT](papers/2022-11_EDICT/解读.md) | EDICT: Exact Diffusion Inversion via Coupled Transformations | [PDF](https://arxiv.org/pdf/2211.12446) | 6614 |
| 2022-11-17 | [InstructPix2Pix](papers/2022-11_InstructPix2Pix/解读.md) | InstructPix2Pix: Learning to Follow Image Editing Instructions | [PDF](https://arxiv.org/pdf/2211.09800) | 7603 |
| 2022-11-17 | [Null-text-Inversion](papers/2022-11_Null-text-Inversion/解读.md) | Null-text Inversion for Editing Real Images using Guided Diffusion Models | [PDF](https://arxiv.org/pdf/2211.09794) | 7202 |
| 2022-11-23 | [Paint-by-Example](papers/2022-11_Paint-by-Example/解读.md) | Paint by Example: Exemplar-based Image Editing with Diffusion Models | [PDF](https://arxiv.org/pdf/2211.13227) | 7577 |
| 2022-11-22 | [Plug-and-Play](papers/2022-11_Plug-and-Play/解读.md) | Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation | [PDF](https://arxiv.org/pdf/2211.12572) | 7284 |
| 2022-12-08 | [Custom-Diffusion](papers/2022-12_Custom-Diffusion/解读.md) | Multi-Concept Customization of Text-to-Image Diffusion | [PDF](https://arxiv.org/pdf/2212.04488) | 7128 |
| 2022-12-13 | [Imagen-Editor-EditBench](papers/2022-12_Imagen-Editor-EditBench/解读.md) | Imagen Editor and EditBench: Advancing and Evaluating Text-Guided Image Inpainting | [PDF](https://arxiv.org/pdf/2212.06909) | 8394 |
| 2023-02-10 | [ControlNet](papers/2023-02_ControlNet/解读.md) | Adding Conditional Control to Text-to-Image Diffusion Models | [PDF](https://arxiv.org/pdf/2302.05543) | 7943 |
| 2023-02-16 | [T2I-Adapter](papers/2023-02_T2I-Adapter/解读.md) | T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models | [PDF](https://arxiv.org/pdf/2302.08453) | 7127 |
| 2023-02-06 | [pix2pix-zero](papers/2023-02_pix2pix-zero/解读.md) | Zero-shot Image-to-Image Translation | [PDF](https://arxiv.org/pdf/2302.03027) | 6692 |
| 2023-03-16 | [HIVE](papers/2023-03_HIVE/解读.md) | HIVE: Harnessing Human Feedback for Instructional Visual Editing | [PDF](https://arxiv.org/pdf/2303.09618) | 7788 |
| 2023-04-13 | [Inpaint-Anything](papers/2023-04_Inpaint-Anything/解读.md) | Inpaint Anything: Segment Anything Meets Image Inpainting | [PDF](https://arxiv.org/pdf/2304.06790) | 8149 |
| 2023-04-17 | [MasaCtrl](papers/2023-04_MasaCtrl/解读.md) | MasaCtrl: Tuning-Free Mutual Self-Attention Control for Consistent Image Synthesis and Editing | [PDF](https://arxiv.org/pdf/2304.08465) | 6562 |
| 2023-04-13 | [Rich-Text](papers/2023-04_Rich-Text/解读.md) | Expressive Text-to-Image Generation with Rich Text | [PDF](https://arxiv.org/pdf/2304.06720) | 6817 |
| 2023-04-05 | [SAM](papers/2023-04_SAM/解读.md) | Segment Anything | [PDF](https://arxiv.org/pdf/2304.02643) | 6768 |
| 2023-05-18 | [DragGAN](papers/2023-05_DragGAN/解读.md) | Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold | [PDF](https://arxiv.org/pdf/2305.10973) | 7007 |
| 2023-05-29 | [InstructEdit](papers/2023-05_InstructEdit/解读.md) | InstructEdit: Improving Automatic Masks for Diffusion-based Image Editing With User Instructions | [PDF](https://arxiv.org/pdf/2305.18047) | 6897 |
| 2023-06-26 | [DragDiffusion](papers/2023-06_DragDiffusion/解读.md) | DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing | [PDF](https://arxiv.org/pdf/2306.14435) | 7065 |
| 2023-06-16 | [MagicBrush](papers/2023-06_MagicBrush/解读.md) | MagicBrush: A Manually Annotated Dataset for Instruction-Guided Image Editing | [PDF](https://arxiv.org/pdf/2306.10012) | 7080 |
| 2023-06-01 | [Self-Guidance](papers/2023-06_Self-Guidance/解读.md) | Diffusion Self-Guidance for Controllable Image Generation | [PDF](https://arxiv.org/pdf/2306.00986) | 7259 |
| 2023-07-18 | [AnyDoor](papers/2023-07_AnyDoor/解读.md) | AnyDoor: Zero-shot Object-level Image Customization | [PDF](https://arxiv.org/pdf/2307.09481) | 7129 |
| 2023-07-05 | [DragonDiffusion](papers/2023-07_DragonDiffusion/解读.md) | DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models | [PDF](https://arxiv.org/pdf/2307.02421) | 7518 |
| 2023-08-13 | [IP-Adapter](papers/2023-08_IP-Adapter/解读.md) | IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models | [PDF](https://arxiv.org/pdf/2308.06721) | 7379 |
| 2023-09-07 | [InstructDiffusion](papers/2023-09_InstructDiffusion/解读.md) | InstructDiffusion: A Generalist Modeling Interface for Vision Tasks | [PDF](https://arxiv.org/pdf/2309.03895) | 6804 |
| 2023-09-29 | [MGIE](papers/2023-09_MGIE/解读.md) | Guiding Instruction-based Image Editing via Multimodal Large Language Models | [PDF](https://arxiv.org/pdf/2309.17102) | 8943 |
| 2023-09-30 | [PixArt-alpha](papers/2023-09_PixArt-alpha/解读.md) | PixArt-$alpha$: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis | [PDF](https://arxiv.org/pdf/2310.00426) | 6861 |
| 2023-11-20 | [Concept-Sliders](papers/2023-11_Concept-Sliders/解读.md) | Concept Sliders: LoRA Adaptors for Precise Control in Diffusion Models | [PDF](https://arxiv.org/pdf/2311.12092) | 7827 |
| 2023-11-06 | [Cross-Image-Attention](papers/2023-11_Cross-Image-Attention/解读.md) | Cross-Image Attention for Zero-Shot Appearance Transfer | [PDF](https://arxiv.org/pdf/2311.03335) | 7423 |
| 2023-11-16 | [Emu-Edit](papers/2023-11_Emu-Edit/解读.md) | Emu Edit: Precise Image Editing via Recognition and Generation Tasks | [PDF](https://arxiv.org/pdf/2311.10089) | 6854 |
| 2023-11-28 | [LEDITSpp](papers/2023-11_LEDITSpp/解读.md) | LEDITS++: Limitless Image Editing using Text-to-Image Models | [PDF](https://arxiv.org/pdf/2311.16711) | 6869 |
| 2023-12-20 | [Emu2](papers/2023-12_Emu2/解读.md) | Generative Multimodal Models are In-Context Learners | [PDF](https://arxiv.org/pdf/2312.13286) | 6701 |
| 2023-12-07 | [InfEdit](papers/2023-12_InfEdit/解读.md) | Inversion-Free Image Editing with Natural Language | [PDF](https://arxiv.org/pdf/2312.04965) | 6814 |
| 2023-12-07 | [PhotoMaker](papers/2023-12_PhotoMaker/解读.md) | PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding | [PDF](https://arxiv.org/pdf/2312.04461) | 7001 |
| 2023-12-06 | [PowerPaint](papers/2023-12_PowerPaint/解读.md) | A Task is Worth One Word: Learning with Task Prompts for High-Quality Versatile Image Inpainting | [PDF](https://arxiv.org/pdf/2312.03594) | 7204 |
| 2023-12-11 | [SmartEdit](papers/2023-12_SmartEdit/解读.md) | SmartEdit: Exploring Complex Instruction-based Image Editing with Multimodal Large Language Models | [PDF](https://arxiv.org/pdf/2312.06739) | 6742 |
| 2023-12-04 | [StyleAligned](papers/2023-12_StyleAligned/解读.md) | Style Aligned Image Generation via Shared Attention | [PDF](https://arxiv.org/pdf/2312.02133) | 7216 |
| 2024-01-15 | [InstantID](papers/2024-01_InstantID/解读.md) | InstantID: Zero-shot Identity-Preserving Generation in Seconds | [PDF](https://arxiv.org/pdf/2401.07519) | 6825 |
| 2024-01-03 | [Instruct-Imagen](papers/2024-01_Instruct-Imagen/解读.md) | Instruct-Imagen: Image Generation with Multi-modal Instruction | [PDF](https://arxiv.org/pdf/2401.01952) | 7210 |
| 2024-02-04 | [DiffEditor](papers/2024-02_DiffEditor/解读.md) | DiffEditor: Boosting Accuracy and Flexibility on Diffusion-based Image Editing | [PDF](https://arxiv.org/pdf/2402.02583) | 7254 |
| 2024-03-11 | [BrushNet](papers/2024-03_BrushNet/解读.md) | BrushNet: A Plug-and-Play Image Inpainting Model with Decomposed Dual-Branch Diffusion | [PDF](https://arxiv.org/pdf/2403.06976) | 6745 |
| 2024-03-21 | [ReNoise](papers/2024-03_ReNoise/解读.md) | ReNoise: Real Image Inversion Through Iterative Noising | [PDF](https://arxiv.org/pdf/2403.14602) | 6706 |
| 2024-03-05 | [SD3-RectifiedFlow](papers/2024-03_SD3-RectifiedFlow/解读.md) | Scaling Rectified Flow Transformers for High-Resolution Image Synthesis | [PDF](https://arxiv.org/pdf/2403.03206) | 6564 |
| 2024-04-15 | [HQ-Edit](papers/2024-04_HQ-Edit/解读.md) | HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing | [PDF](https://arxiv.org/pdf/2404.09990) | 7232 |
| 2024-04-22 | [SEED-X](papers/2024-04_SEED-X/解读.md) | SEED-X: Multimodal Models with Unified Multi-granularity Comprehension and Generation | [PDF](https://arxiv.org/pdf/2404.14396) | 6648 |
| 2024-04-03 | [VAR](papers/2024-04_VAR/解读.md) | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | [PDF](https://arxiv.org/pdf/2404.02905) | 8136 |
| 2024-05-16 | [Chameleon](papers/2024-05_Chameleon/解读.md) | Chameleon: Mixed-Modal Early-Fusion Foundation Models | [PDF](https://arxiv.org/pdf/2405.09818) | 8109 |
| 2024-05-07 | [SEED-Data-Edit](papers/2024-05_SEED-Data-Edit/解读.md) | SEED-Data-Edit Technical Report: A Hybrid Dataset for Instructional Image Editing | [PDF](https://arxiv.org/pdf/2405.04007) | 6626 |
| 2024-06-11 | [MimicBrush](papers/2024-06_MimicBrush/解读.md) | Zero-shot Image Editing with Reference Imitation | [PDF](https://arxiv.org/pdf/2406.07547) | 8536 |
| 2024-07-07 | [UltraEdit](papers/2024-07_UltraEdit/解读.md) | UltraEdit: Instruction-based Fine-Grained Image Editing at Scale | [PDF](https://arxiv.org/pdf/2407.05282) | 7074 |
| 2024-08-01 | [FLUX.1](papers/2024-08_FLUX.1/解读.md) | FLUX.1 Model Family | [官方来源](https://bfl.ai/blog/24-08-01-bfl) | 634 |
| 2024-08-26 | [I2EBench](papers/2024-08_I2EBench/解读.md) | I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing | [PDF](https://arxiv.org/pdf/2408.14180) | 2518 |
| 2024-08-22 | [Show-o](papers/2024-08_Show-o/解读.md) | Show-o: One Single Transformer to Unify Multimodal Understanding and Generation | [PDF](https://arxiv.org/pdf/2408.12528) | 7514 |
| 2024-08-20 | [Transfusion](papers/2024-08_Transfusion/解读.md) | Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model | [PDF](https://arxiv.org/pdf/2408.11039) | 7019 |
| 2024-08-01 | [TurboEdit](papers/2024-08_TurboEdit/解读.md) | TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models | [PDF](https://arxiv.org/pdf/2408.00735) | 6973 |
| 2024-09-27 | [Emu3](papers/2024-09_Emu3/解读.md) | Emu3: Next-Token Prediction is All You Need | [PDF](https://arxiv.org/pdf/2409.18869) | 7382 |
| 2024-09-17 | [OmniGen](papers/2024-09_OmniGen/解读.md) | OmniGen: Unified Image Generation | [PDF](https://arxiv.org/pdf/2409.11340) | 8139 |
| 2024-10-31 | [In-Context-LoRA](papers/2024-10_In-Context-LoRA/解读.md) | In-Context LoRA for Diffusion Transformers | [PDF](https://arxiv.org/pdf/2410.23775) | 6951 |
| 2024-10-14 | [RF-Inversion](papers/2024-10_RF-Inversion/解读.md) | Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations | [PDF](https://arxiv.org/pdf/2410.10792) | 7312 |
| 2024-11-11 | [Add-it](papers/2024-11_Add-it/解读.md) | Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models | [PDF](https://arxiv.org/pdf/2411.07232) | 7033 |
| 2024-11-24 | [AnyEdit](papers/2024-11_AnyEdit/解读.md) | AnyEdit: Mastering Unified High-Quality Image Editing for Any Idea | [PDF](https://arxiv.org/pdf/2411.15738) | 7500 |
| 2024-11-14 | [MagicQuill](papers/2024-11_MagicQuill/解读.md) | MagicQuill: An Intelligent Interactive Image Editing System | [PDF](https://arxiv.org/pdf/2411.09703) | 7389 |
| 2024-11-22 | [OminiControl](papers/2024-11_OminiControl/解读.md) | OminiControl: Minimal and Universal Control for Diffusion Transformer | [PDF](https://arxiv.org/pdf/2411.15098) | 6543 |
| 2024-11-11 | [OmniEdit](papers/2024-11_OmniEdit/解读.md) | OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision | [PDF](https://arxiv.org/pdf/2411.07199) | 7402 |
| 2024-11-07 | [RF-Solver-Edit](papers/2024-11_RF-Solver-Edit/解读.md) | Taming Rectified Flow for Inversion and Editing | [PDF](https://arxiv.org/pdf/2411.04746) | 7204 |
| 2024-11-11 | [SeedEdit](papers/2024-11_SeedEdit/解读.md) | SeedEdit: Align Image Re-Generation to Image Editing | [PDF](https://arxiv.org/pdf/2411.06686) | 7623 |
| 2024-11-27 | [FlowChef](papers/2024-12_FlowChef/解读.md) | FlowChef: Steering of Rectified Flow Models for Controlled Generations | [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Patel_FlowChef_Steering_of_Rectified_Flow_Models_for_Controlled_Generations_ICCV_2025_paper.pdf) | 4314 |
| 2024-12 | [Grok-Aurora](papers/2024-12_Grok-Aurora/解读.md) | Grok (Aurora) | [官方来源](https://docs.x.ai/developers/models) | 330 |
| 2024-12-10 | [UniReal](papers/2024-12_UniReal/解读.md) | UniReal: Universal Image Generation and Editing via Learning Real-world Dynamics | [PDF](https://arxiv.org/pdf/2412.07774) | 6953 |
| 2025-01-05 | [ACEpp](papers/2025-01_ACEpp/解读.md) | ACE++: Instruction-Based Image Creation and Editing via Context-Aware Content Filling | [PDF](https://arxiv.org/pdf/2501.02487) | 7487 |
| 2025-01-29 | [Janus-Pro](papers/2025-01_Janus-Pro/解读.md) | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | [PDF](https://arxiv.org/pdf/2501.17811) | 8116 |
| 2025-03-10 | [EasyControl](papers/2025-03_EasyControl/解读.md) | EasyControl: Adding Efficient and Flexible Control for Diffusion Transformer | [PDF](https://arxiv.org/pdf/2503.07027) | 7188 |
| 2025-03-25 | [FireEdit](papers/2025-03_FireEdit/解读.md) | FireEdit: Fine-grained Instruction-based Image Editing via Region-aware Vision Language Model | [PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_FireEdit_Fine-grained_Instruction-based_Image_Editing_via_Region-aware_Vision_Language_Model_CVPR_2025_paper.pdf) | 3066 |
| 2025-03-13 | [GoT](papers/2025-03_GoT/解读.md) | GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing | [PDF](https://arxiv.org/pdf/2503.10639) | 7356 |
| 2025-04-17 | [Complex-Edit](papers/2025-04_Complex-Edit/解读.md) | $texttt{Complex-Edit}$: CoT-Like Instruction Generation for Complexity-Controllable Image Editing Benchmark | [PDF](https://arxiv.org/pdf/2504.13143) | 8329 |
| 2025-04-23 | [DreamO](papers/2025-04_DreamO/解读.md) | DreamO: A Unified Framework for Image Customization | [PDF](https://arxiv.org/pdf/2504.16915) | 7727 |
| 2025-04-29 | [ICEdit](papers/2025-04_ICEdit/解读.md) | In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer | [PDF](https://arxiv.org/pdf/2504.20690) | 6865 |
| 2025-04-21 | [Insert-Anything](papers/2025-04_Insert-Anything/解读.md) | Insert Anything: Image Insertion via In-Context Editing in DiT | [PDF](https://arxiv.org/pdf/2504.15009) | 6580 |
| 2025-04-08 | [MetaQuery](papers/2025-04_MetaQuery/解读.md) | Transfer between Modalities with MetaQueries | [PDF](https://arxiv.org/pdf/2504.06256) | 7502 |
| 2025-04-03 | [RISEBench](papers/2025-04_RISEBench/解读.md) | Envisioning Beyond the Pixels: Benchmarking Reasoning-Informed Visual Editing | [PDF](https://arxiv.org/pdf/2504.02826) | 7917 |
| 2025-04-24 | [Step1X-Edit](papers/2025-04_Step1X-Edit/解读.md) | Step1X-Edit: A Practical Framework for General Image Editing | [PDF](https://arxiv.org/pdf/2504.17761) | 7396 |
| 2025-04-02 | [UNO](papers/2025-04_UNO/解读.md) | Less-to-More Generalization: Unlocking More Controllability by In-Context Generation | [PDF](https://arxiv.org/pdf/2504.02160) | 7202 |
| 2025-05-20 | [BAGEL](papers/2025-05_BAGEL/解读.md) | Emerging Properties in Unified Multimodal Pretraining | [PDF](https://arxiv.org/pdf/2505.14683) | 7170 |
| 2025-05-14 | [BLIP3-o](papers/2025-05_BLIP3-o/解读.md) | BLIP3-o: A Family of Fully Open Unified Multimodal Models-Architecture, Training and Dataset | [PDF](https://arxiv.org/pdf/2505.09568) | 6887 |
| 2025-05-26 | [DICE](papers/2025-05_DICE/解读.md) | What Changed? Detecting and Evaluating Instruction-Guided Image Edits with Multimodal Large Language Models | [PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Baraldi_What_Changed_Detecting_and_Evaluating_Instruction-Guided_Image_Edits_with_Multimodal_ICCV_2025_paper.pdf) | 3306 |
| 2025-05-12 | [DanceGRPO](papers/2025-05_DanceGRPO/解读.md) | DanceGRPO: Unleashing GRPO on Visual Generation | [PDF](https://arxiv.org/pdf/2505.07818) | 7294 |
| 2025-05-22 | [Everyday-Image-Editing](papers/2025-05_Everyday-Image-Editing/解读.md) | Understanding Generative AI Capabilities in Everyday Image Editing Tasks | [PDF](https://arxiv.org/pdf/2505.16181) | 2986 |
| 2025-05-08 | [Flow-GRPO](papers/2025-05_Flow-GRPO/解读.md) | Flow-GRPO: Training Flow Matching Models via Online RL | [PDF](https://arxiv.org/pdf/2505.05470) | 6502 |
| 2025-05-16 | [GIE-Bench](papers/2025-05_GIE-Bench/解读.md) | GIE-Bench: Towards Grounded Evaluation for Text-Guided Image Editing | [PDF](https://arxiv.org/pdf/2505.11493) | 2670 |
| 2025-05-01 | [HATIE](papers/2025-05_HATIE/解读.md) | Towards Scalable Human-aligned Benchmark for Text-guided Image Editing | [PDF](https://arxiv.org/pdf/2505.00502) | 6842 |
| 2025-05-28 | [HiDream-I1](papers/2025-05_HiDream-I1/解读.md) | HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer | [PDF](https://arxiv.org/pdf/2505.22705) | 7337 |
| 2025-05-26 | [ImgEdit](papers/2025-05_ImgEdit/解读.md) | ImgEdit: A Unified Image Editing Dataset and Benchmark | [PDF](https://arxiv.org/pdf/2505.20275) | 7451 |
| 2025-05-22 | [KRIS-Bench](papers/2025-05_KRIS-Bench/解读.md) | KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models | [PDF](https://arxiv.org/pdf/2505.16707) | 7494 |
| 2025-05-01 | [T2I-R1](papers/2025-05_T2I-R1/解读.md) | T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT | [PDF](https://arxiv.org/pdf/2505.00703) | 6876 |
| 2025-06-15 | [BPM](papers/2025-06_BPM/解读.md) | Balancing Preservation and Modification: A Region and Semantic Aware Metric for Instruction-Based Image Editing | [PDF](https://arxiv.org/pdf/2506.13827) | 2528 |
| 2025-06-15 | [ComplexBench-Edit](papers/2025-06_ComplexBench-Edit/解读.md) | ComplexBench-Edit: Benchmarking Complex Instruction-Driven Image Editing via Compositional Dependencies | [PDF](https://arxiv.org/pdf/2506.12830) | 2534 |
| 2025-06-17 | [FLUX-Kontext](papers/2025-06_FLUX-Kontext/解读.md) | FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space | [PDF](https://arxiv.org/pdf/2506.15742) | 8679 |
| 2025-06-23 | [OmniGen2](papers/2025-06_OmniGen2/解读.md) | OmniGen2: Towards Instruction-Aligned Multimodal Generation | [PDF](https://arxiv.org/pdf/2506.18871) | 6695 |
| 2025-06-29 | [Ovis-U1](papers/2025-06_Ovis-U1/解读.md) | Ovis-U1 Technical Report | [PDF](https://arxiv.org/pdf/2506.23044) | 6716 |
| 2025-06-03 | [RefEdit](papers/2025-06_RefEdit/解读.md) | RefEdit: A Benchmark and Method for Improving Instruction-based Image Editing Model on Referring Expressions | [PDF](https://arxiv.org/pdf/2506.03448) | 2516 |
| 2025-06-05 | [SeedEdit3](papers/2025-06_SeedEdit3/解读.md) | SeedEdit 3.0: Fast and High-Quality Generative Image Editing | [PDF](https://arxiv.org/pdf/2506.05083) | 7643 |
| 2025-06-18 | [Show-o2](papers/2025-06_Show-o2/解读.md) | Show-o2: Improved Native Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2506.15564) | 6918 |
| 2025-06-03 | [UniWorld-V1](papers/2025-06_UniWorld-V1/解读.md) | UniWorld-V1: High-Resolution Semantic Encoders for Unified Visual Understanding and Generation | [PDF](https://arxiv.org/pdf/2506.03147) | 6657 |
| 2025-07-28 | [GPT-Image-Edit-1.5M](papers/2025-07_GPT-Image-Edit-1.5M/解读.md) | GPT-IMAGE-EDIT-1.5M: A Million-Scale, GPT-Generated Image Dataset | [PDF](https://arxiv.org/pdf/2507.21033) | 6615 |
| 2025-07-22 | [LMM4Edit](papers/2025-07_LMM4Edit/解读.md) | LMM4Edit: Benchmarking and Evaluating Multimodal Image Editing with LMMs | [PDF](https://arxiv.org/pdf/2507.16193) | 2544 |
| 2025-07-18 | [NoHumansRequired](papers/2025-07_NoHumansRequired/解读.md) | NoHumansRequired: Autonomous High-Quality Image Editing Triplet Mining | [PDF](https://arxiv.org/pdf/2507.14119) | 6730 |
| 2025-08-04 | [Qwen-Image](papers/2025-08_Qwen-Image/解读.md) | Qwen-Image Technical Report | [PDF](https://arxiv.org/pdf/2508.02324) | 7310 |
| 2025-08-21 | [VAREdit](papers/2025-08_VAREdit/解读.md) | Visual Autoregressive Modeling for Instruction-Guided Image Editing | [PDF](https://arxiv.org/pdf/2508.15772) | 7076 |
| 2025-08-11 | [X2Edit](papers/2025-08_X2Edit/解读.md) | X2Edit: Revisiting Arbitrary-Instruction Image Editing through Self-Constructed Data and Task-Aware Representation Learning | [PDF](https://arxiv.org/pdf/2508.07607) | 6789 |
| 2025-09-16 | [EdiVal-Agent](papers/2025-09_EdiVal-Agent/解读.md) | EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing | [PDF](https://arxiv.org/pdf/2509.13399) | 6599 |
| 2025-09-30 | [EditReward](papers/2025-09_EditReward/解读.md) | EditReward: A Human-Aligned Reward Model for Instruction-Guided Image Editing | [PDF](https://arxiv.org/pdf/2509.26346) | 7572 |
| 2025-09-28 | [EditScore](papers/2025-09_EditScore/解读.md) | EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling | [PDF](https://arxiv.org/pdf/2509.23909) | 6719 |
| 2025-09-24 | [EditVerse](papers/2025-09_EditVerse/解读.md) | EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning | [PDF](https://arxiv.org/pdf/2509.20360) | 7231 |
| 2025-09-28 | [HunyuanImage3](papers/2025-09_HunyuanImage3/解读.md) | HunyuanImage 3.0 Technical Report | [PDF](https://arxiv.org/pdf/2509.23951) | 6546 |
| 2025-09-29 | [OpenGPT-4o-Image](papers/2025-09_OpenGPT-4o-Image/解读.md) | OpenGPT-4o-Image: A Comprehensive Dataset for Advanced Image Generation and Editing | [PDF](https://arxiv.org/pdf/2509.24900) | 7651 |
| 2025-09-24 | [Seedream4](papers/2025-09_Seedream4/解读.md) | Seedream 4.0: Toward Next-generation Multimodal Image Generation | [PDF](https://arxiv.org/pdf/2509.20427) | 6611 |
| 2025-10-05 | [ChronoEdit](papers/2025-10_ChronoEdit/解读.md) | ChronoEdit: Towards Temporal Reasoning for Image Editing and World Simulation | [PDF](https://arxiv.org/pdf/2510.04290) | 6825 |
| 2025-10-08 | [DreamOmni2](papers/2025-10_DreamOmni2/解读.md) | DreamOmni2: Multimodal Instruction-based Editing and Generation | [PDF](https://arxiv.org/pdf/2510.06679) | 6564 |
| 2025-10-19 | [Edit-R1-UniWorld-V2](papers/2025-10_Edit-R1-UniWorld-V2/解读.md) | Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback | [PDF](https://arxiv.org/pdf/2510.16888) | 6542 |
| 2025-10-30 | [Emu3.5](papers/2025-10_Emu3.5/解读.md) | Emu3.5: Native Multimodal Models are World Learners | [PDF](https://arxiv.org/pdf/2510.26583) | 7580 |
| 2025-10-09 | [InstructX](papers/2025-10_InstructX/解读.md) | InstructX: Towards Unified Visual Editing with MLLM Guidance | [PDF](https://arxiv.org/pdf/2510.08485) | 6671 |
| 2025-10-09 | [Kontinuous-Kontext](papers/2025-10_Kontinuous-Kontext/解读.md) | Kontinuous Kontext: Continuous Strength Control for Instruction-based Image Editing | [PDF](https://arxiv.org/pdf/2510.08532) | 8551 |
| 2025-10-07 | [Lumina-DiMOO](papers/2025-10_Lumina-DiMOO/解读.md) | Lumina-DiMOO: An Omni Diffusion Large Language Model for Multi-Modal Generation and Understanding | [PDF](https://arxiv.org/pdf/2510.06308) | 7291 |
| 2025-10-20 | [PICABench](papers/2025-10_PICABench/解读.md) | PICABench: How Far Are We from Physically Realistic Image Editing? | [PDF](https://arxiv.org/pdf/2510.17681) | 7739 |
| 2025-10-22 | [Pico-Banana-400K](papers/2025-10_Pico-Banana-400K/解读.md) | Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing | [PDF](https://arxiv.org/pdf/2510.19808) | 7750 |
| 2025-11-27 | [ReasonEdit](papers/2025-11_ReasonEdit/解读.md) | ReasonEdit: Towards Reasoning-Enhanced Image Editing Models | [PDF](https://arxiv.org/pdf/2511.22625) | 7349 |
| 2025-11-03 | [UniREditBench](papers/2025-11_UniREditBench/解读.md) | UniREditBench: A Unified Reasoning-based Image Editing Benchmark | [PDF](https://arxiv.org/pdf/2511.01295) | 7321 |
| 2025-11-27 | [Z-Image](papers/2025-11_Z-Image/解读.md) | Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer | [PDF](https://arxiv.org/pdf/2511.22699) | 6667 |
| 2025-12-04 | [I2I-Bench](papers/2025-12_I2I-Bench/解读.md) | I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models | [PDF](https://arxiv.org/pdf/2512.04660) | 7049 |
| 2025-12-17 | [Qwen-Image-Edit-2511](papers/2025-12_Qwen-Image-Edit-2511/解读.md) | Qwen-Image-Edit-2511 | [官方来源](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) | 666 |
| 2025-12-17 | [Qwen-Image-Layered](papers/2025-12_Qwen-Image-Layered/解读.md) | Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition | [PDF](https://arxiv.org/pdf/2512.15603) | 7109 |
| 2025-11-29 | [WiseEdit](papers/2025-12_WiseEdit/解读.md) | WiseEdit: Benchmarking Cognition- and Creativity-Informed Image Editing | [PDF](https://arxiv.org/pdf/2512.00387) | 2593 |
| 2026-01-06 | [ThinkRL-Edit](papers/2026-01_ThinkRL-Edit/解读.md) | ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing | [PDF](https://arxiv.org/pdf/2601.03467) | 7196 |
| 2026-01-05 | [nextflow](papers/2026-01_nextflow/解读.md) | NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation | [PDF](https://arxiv.org/pdf/2601.02204) | 7320 |
| 2026-01-06 | [reward-hacking-t2i](papers/2026-01_reward-hacking-t2i/解读.md) | Understanding Reward Hacking in Text-to-Image Reinforcement Learning | [PDF](https://arxiv.org/pdf/2601.03468) | 7524 |
| 2026-02-22 | [ChordEdit](papers/2026-02_ChordEdit/解读.md) | ChordEdit: One-Step Low-Energy Transport for Image Editing | [PDF](https://arxiv.org/pdf/2602.19083) | 7579 |
| 2026-02-12 | [FireRed-Image-Edit](papers/2026-02_FireRed-Image-Edit/解读.md) | FireRed-Image-Edit-1.0 Technical Report | [PDF](https://arxiv.org/pdf/2602.13344) | 7206 |
| 2026-02-02 | [VIBE](papers/2026-02_VIBE/解读.md) | How Well Do Models Follow Visual Instructions? VIBE: A Systematic Benchmark for Visual Instruction-Driven Image Editing | [PDF](https://arxiv.org/pdf/2602.01851) | 2564 |
| 2026-02-09 | [reasoning-to-pixels](papers/2026-02_reasoning-to-pixels/解读.md) | From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2602.08336) | 6985 |
| 2026-02-09 | [rethink-global-text](papers/2026-02_rethink-global-text/解读.md) | Rethinking Global Text Conditioning in Diffusion Transformers | [PDF](https://arxiv.org/pdf/2602.09268) | 7486 |
| 2026-02-07 | [spatialreward-edit](papers/2026-02_spatialreward-edit/解读.md) | SpatialReward: Bridging the Perception Gap in Online RL for Image Editing via Explicit Spatial Reasoning | [PDF](https://arxiv.org/pdf/2602.07458) | 7019 |
| 2026-02-02 | [unireason](papers/2026-02_unireason/解读.md) | UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing | [PDF](https://arxiv.org/pdf/2602.02437) | 7070 |
| 2026-03-30 | [GEditBench-v2](papers/2026-03_GEditBench-v2/解读.md) | GEditBench v2: A Human-Aligned Benchmark for General Image Editing | [PDF](https://arxiv.org/pdf/2603.28547) | 3755 |
| 2026-03-16 | [Omni-IIE-Bench](papers/2026-03_Omni-IIE-Bench/解读.md) | Omni IIE Bench: Benchmarking the Practical Capabilities of Image Editing Models | [PDF](https://arxiv.org/pdf/2603.16944) | 3225 |
| 2026-03-20 | [TIEdit-EditProbe](papers/2026-03_TIEdit-EditProbe/解读.md) | Evaluating Image Editing with LLMs: A Comprehensive Benchmark and Intermediate-Layer Probing Approach | [PDF](https://arxiv.org/pdf/2603.19775) | 2864 |
| 2026-03-09 | [care-edit](papers/2026-03_care-edit/解读.md) | CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing | [PDF](https://arxiv.org/pdf/2603.08589) | 6830 |
| 2026-03-09 | [coco-code-cot](papers/2026-03_coco-code-cot/解读.md) | CoCo: Code as CoT for Text-to-Image Preview and Rare Concept Generation | [PDF](https://arxiv.org/pdf/2603.08652) | 6950 |
| 2026-03-31 | [editing-manifold](papers/2026-03_editing-manifold/解读.md) | Editing on the Generative Manifold: A Theoretical and Empirical Study of General Diffusion-Based Image Editing Trade-offs | [PDF](https://arxiv.org/pdf/2603.29736) | 7110 |
| 2026-03-10 | [internvl-u](papers/2026-03_internvl-u/解读.md) | InternVL-U: Democratizing Unified Multimodal Models for Understanding, Reasoning, Generation and Editing | [PDF](https://arxiv.org/pdf/2603.09877) | 6642 |
| 2026-03-17 | [ug-fight-dpo](papers/2026-03_ug-fight-dpo/解读.md) | Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2603.17044v1) | 6969 |
| 2026-04-21 | [GPT-Image-2](papers/2026-04_GPT-Image-2/解读.md) | GPT Image 2 | [官方来源](https://developers.openai.com/api/docs/models/gpt-image-2) | 732 |
| 2026-04-22 | [GSI-Bench](papers/2026-04_GSI-Bench/解读.md) | Exploring Spatial Intelligence from a Generative Perspective | [PDF](https://arxiv.org/pdf/2604.20570) | 2510 |
| 2026-04-03 | [banana100](papers/2026-04_banana100/解读.md) | Banana100: Breaking NR-IQA Metrics by 100 Iterative Image Replications with Nano Banana Pro | [PDF](https://arxiv.org/pdf/2604.03400) | 8186 |
| 2026-04-27 | [beyond-accuracy](papers/2026-04_beyond-accuracy/解读.md) | Beyond Accuracy: Benchmarking Cross-Task Consistency in Unified Multimodal Models | [PDF](https://arxiv.org/pdf/2604.25072) | 7280 |
| 2026-04-26 | [edit-where-you-mean](papers/2026-04_edit-where-you-mean/解读.md) | Edit Where You Mean: Region-Aware Adapter Injection for Mask-Free Local Image Editing | [PDF](https://arxiv.org/pdf/2604.23763) | 6989 |
| 2026-04-27 | [meta-cot](papers/2026-04_meta-cot/解读.md) | Meta-CoT: Enhancing Granularity and Generalization in Image Editing | [PDF](https://arxiv.org/pdf/2604.24625) | 6900 |
| 2026-04-29 | [spatialfusion](papers/2026-04_spatialfusion/解读.md) | SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness | [PDF](https://arxiv.org/pdf/2604.26341) | 6812 |
| 2026-04-27 | [tuna-2](papers/2026-04_tuna-2/解读.md) | Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation | [PDF](https://arxiv.org/pdf/2604.24763) | 6618 |
| 2026-05-29 | [PaintBench](papers/2026-05_PaintBench/解读.md) | PaintBench: Deterministic Evaluation of Precise Visual Editing | [PDF](https://arxiv.org/pdf/2606.00188) | 3038 |
| 2026-05-11 | [Qwen-Image-2.0](papers/2026-05_Qwen-Image-2.0/解读.md) | Qwen-Image-2.0 Technical Report | [PDF](https://arxiv.org/pdf/2605.10730) | 8086 |
| 2026-05-20 | [decompose-subject](papers/2026-05_decompose-subject/解读.md) | Decomposing Subject-Driven Image Generation via Intermediate Structural Prediction | [PDF](https://arxiv.org/pdf/2605.20807) | 7064 |
| 2026-05-04 | [directedit](papers/2026-05_directedit/解读.md) | DirectEdit: Step-Level Accurate Inversion for Flow-Based Image Editing | [PDF](https://arxiv.org/pdf/2605.02417) | 7200 |
| 2026-05-13 | [edit-compass](papers/2026-05_edit-compass/解读.md) | Edit-Compass &amp; EditReward-Compass: A Unified Benchmark for Image Editing and Reward Modeling | [PDF](https://arxiv.org/pdf/2605.13062) | 6567 |
| 2026-05-11 | [masked-gen-transformer](papers/2026-05_masked-gen-transformer/解读.md) | Masked Generative Transformer Is What You Need for Image Editing | [PDF](https://arxiv.org/pdf/2605.10859) | 6797 |
| 2026-05-12 | [sensenova-u1](papers/2026-05_sensenova-u1/解读.md) | SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture | [PDF](https://arxiv.org/pdf/2605.12500) | 6907 |
| 2026-06-01 | [Inter-Edit](papers/2026-06_Inter-Edit/解读.md) | Inter-Edit: First Benchmark for Interactive Instruction-Based Image Editing | [PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Liu_Inter-Edit_First_Benchmark_for_Interactive_Instruction-Based_Image_Editing_CVPR_2026_paper.pdf) | 2661 |
| 2026-06-09 | [arm-unified](papers/2026-06_arm-unified/解读.md) | ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations | [PDF](https://arxiv.org/pdf/2606.11188) | 7433 |
| 2026-06-02 | [bootstrap-generator](papers/2026-06_bootstrap-generator/解读.md) | Bootstrap Your Generator: Unpaired Visual Editing with Flow Matching | [PDF](https://arxiv.org/pdf/2606.03911) | 7686 |
| 2026-06-11 | [hydra-x](papers/2026-06_hydra-x/解读.md) | HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers | [PDF](https://arxiv.org/pdf/2606.13289) | 6583 |
| 2026-06-25 | [lighting-edit-bench](papers/2026-06_lighting-edit-bench/解读.md) | Do Image Editing Models Understand Lighting? | [PDF](https://arxiv.org/pdf/2606.26738) | 6897 |
| 2026-06-14 | [mind-the-gap](papers/2026-06_mind-the-gap/解读.md) | Mind the Gap: Diagnosing Constraint Discovery Failures in Text-in-Image Editing | [PDF](https://arxiv.org/pdf/2606.15982) | 6741 |
| 2026-06-17 | [moebius-inpainting](papers/2026-06_moebius-inpainting/解读.md) | Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance | [PDF](https://arxiv.org/pdf/2606.19195) | 6843 |
| 2026-06-25 | [qwen-image-rl](papers/2026-06_qwen-image-rl/解读.md) | Qwen-Image-2.0-RL Technical Report | [PDF](https://arxiv.org/pdf/2606.27608) | 8108 |
| 2026-07-28 | [IIE-Survey](papers/2026-07_IIE-Survey/解读.md) | Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications | [PDF](https://arxiv.org/pdf/2607.25642) | 8309 |
| 2026-07-06 | [cfg-inversion-fail](papers/2026-07_cfg-inversion-fail/解读.md) | When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt--Latent Interactions | [PDF](https://arxiv.org/pdf/2607.04731) | 6682 |
| 2026-07-08 | [implicit-preservation](papers/2026-07_implicit-preservation/解读.md) | Making Implicit Preservation Intent Explicit in Conversational Image Editing | [PDF](https://arxiv.org/pdf/2607.07051) | 6823 |
| 2026-07-13 | [read-it-back](papers/2026-07_read-it-back/解读.md) | Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation | [PDF](https://arxiv.org/pdf/2607.11886) | 6611 |
| 2026-08-14 | [CPI-Bench](papers/2026-08_CPI-Bench/解读.md) | CPI-Bench: A Comprehensive, Practical and Intelligent Benchmark for Real-World Image Editing | [PDF](https://arxiv.org/pdf/2608.14546) | 2517 |
| 2026-08-24 | [rl-no-edit-rewards](papers/2026-08_rl-no-edit-rewards/解读.md) | Can We Perform Online RL for Image Editing without Editing Rewards? | [PDF](https://arxiv.org/pdf/2608.22780) | 7117 |
