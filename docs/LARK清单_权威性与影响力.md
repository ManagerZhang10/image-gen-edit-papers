# Lark 论文清单：权威性与影响力

> 核对日期：2026-08-29  
> 范围：Lark Wiki《Image Edit领域论文调研》中的论文、模型与 benchmark。组合条目（如 SeedEdit/Seedream、FLUX、Qwen-Image Edit）按可独立核验的论文或版本拆开，共 55 个载体。  
> 引用量是动态快照。每行必须连同 provider 一起读，不把 Semantic Scholar 与 OpenAlex 数值直接混排得出精确名次。

## 怎么判断“有权威背书”

本次把证据分成三层：

1. **同行评审正式论文**：34 项。优先记录 CVPR、ICCV、NeurIPS、ICLR、ICML、ACM MM、SIGGRAPH、WACV、TMLR 或正式期刊页面。
2. **arXiv / 技术报告 / 在审投稿**：17 项。技术内容可以参考，但不能把“投稿某会”写成“已被某会接收”。
3. **只有官方产品文档或模型卡**：4 项，包括 GPT Image 2、基础 FLUX.1、Qwen-Image-Edit-2511、Grok/Aurora。它们没有对应的独立正式论文，不能用产品说明替代可复核的训练数据、消融和 benchmark 证据。

首次公开时间和正式发表时间分列：前者通常是 arXiv v1，后者是 proceedings/期刊日期。这样不会把“2025 年预印本、2026 年正式发表”混成一个年份。

## 完整逐项表

- [Benchmark 前半组：12 项](review/bench_early_manifest.md)
- [Benchmark 后半组与综述：12 项](review/bench_late_manifest.md)
- [基础模型、数据与控制方法：18 项](review/models_core_manifest.md)
- [其余编辑方法与产品条目：13 项](review/models_methods_manifest.md)

四张表均包含：本地目录、PDF/笔记状态、首次公开、正式 venue/发表时间、引用量、provider、核对日和一手来源入口。没有被引用数据库收录的论文写“未收录/不可得”，而不是伪写成 0。

## 影响力快照：高引用条目

下面只用于快速定位成熟基线。由于 provider 不完全一致，不能把相近数字看成严格排名。

| 条目 | 正式状态 | 引用量快照 | Provider |
| --- | --- | ---: | --- |
| ControlNet | ICCV 2023 | 7602 | Semantic Scholar |
| IP-Adapter | 仅确认 arXiv/官方开源 | 1739 | Semantic Scholar |
| InstructPix2Pix | CVPR 2023 | 1303 | OpenAlex |
| FLUX.1 Kontext | arXiv 技术报告 | 1004 | Semantic Scholar |
| Qwen-Image | arXiv 技术报告/官方开源 | 930 | Semantic Scholar |
| Paint by Example | CVPR 2023 | 664 | Semantic Scholar |
| Null-text Inversion | CVPR 2023 | 657 | OpenAlex |
| Plug-and-Play Diffusion Features | CVPR 2023 | 565 | OpenAlex |
| Drag Your GAN | SIGGRAPH 2023 | 368 | Semantic Scholar |
| Prompt-to-Prompt | 仅确认 arXiv | 367 | OpenAlex |

## 使用这些数字时的边界

- **引用量不是效果分**：老论文天然积累更多引用；2026 新论文为 0 不等于无价值。
- **venue 不是产品可用性**：同行评审能提高事实可信度，但延迟、成本、许可证、身份保持仍要在自有数据上验证。
- **产品说明不是论文结论**：官方模型卡能证明版本和公开能力声明，不能证明未披露的架构、训练数据或因果机制。
- **benchmark 相关性不是逐样本 gate**：即使榜单与 Arena 排名相关，也不能直接把单张图的 VLM 分数当线上放行阈值。
