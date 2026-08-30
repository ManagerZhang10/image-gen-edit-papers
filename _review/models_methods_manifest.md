# 模型与方法组清单、发表信息与影响力

> 引用量来源：OpenAlex `cited_by_count`，核对日期 2026-08-29。不同索引库会有差异，数字只可在同一来源内横向比较。  
> “首次公开”采用 arXiv v1 日期；“正式发表”只在能确认正式 proceedings/venue 时填写。

| Lark 条目 | 本地目录/状态 | 首次公开 | 正式发表 | OpenAlex 引用量 | 技术核验 |
| --- | --- | --- | --- | ---: | --- |
| OminiControl | `2024-11_OminiControl`，PDF+深读齐全 | 2024-11-22 | ICCV 2025 | 2 | 关键主张一致；0.1% 是不计额外 encoder 的主配置 |
| CARE-Edit | `2026-03_care-edit`，PDF+深读齐全 | 2026-03-09 | 截至核对日仅确认 arXiv | 0 | 四专家与动态路由描述一致 |
| ACE++ | `2025-01_ACEpp`，PDF+深读齐全 | 2025-01-05 | ICCV Workshops 2025 | 7 | 已有完整深读 |
| Grok (Aurora) | `2024-12_Grok-Aurora`，**无正式论文**；不伪造 `paper.pdf` | 产品时期标签；无论文日期 | 无论文 venue | — | 已建“无论文”核验说明；应按产品能力评估，不能当论文证据 |
| OmniGen2 | `2025-06_OmniGen2`，PDF+深读齐全 | 2025-06-23 | 截至核对日仅确认 arXiv | 0 | 已有完整深读 |
| Emu-Edit | `2023-11_Emu-Edit`，PDF+深读齐全 | 2023-11-16 | CVPR 2024 | 72 | 已有完整深读 |
| AnyEdit | `2024-11_AnyEdit`，PDF+深读齐全 | 2024-11-24 | CVPR 2025 | 12 | 已有完整深读 |
| MagicBrush | `2023-06_MagicBrush`，PDF+深读齐全 | 2023-06-16 | NeurIPS 2023 Datasets and Benchmarks | 32 | 已有完整深读 |
| InstructEdit | `2023-05_InstructEdit`，新补 PDF+深读 | 2023-05-29 | 截至核对日仅确认 arXiv | 9 | Lark 原条目为空，已补齐 |
| InstructPix2Pix | `2022-11_InstructPix2Pix`，PDF+深读齐全 | 2022-11-17 | CVPR 2023 | 1303 | 数据“全合成”表述需纠正 |
| Prompt-to-Prompt | `2022-08_Prompt-to-Prompt`，PDF+深读齐全 | 2022-08-02 | 截至核对日仅确认 arXiv | 367 | 核心机制一致 |
| Plug-and-Play Diffusion Features | `2022-11_Plug-and-Play`，PDF+深读齐全 | 2022-11-22 | CVPR 2023 | 565 | “完全保持”是过度表述 |
| Expressive Image Generation and Editing with Rich Text | `2023-04_Rich-Text`，新补 PDF+深读 | 2023-04-13 | ICCV 2023；正式题名为 *Expressive Text-to-Image Generation with Rich Text* | 63 | 真实图路径仍需 inversion+grounded segmentation |

## 来源入口

- 论文原文与首次公开时间：各目录 `meta.json` 中的 arXiv URL。
- 正式发表：CVF/IEEE proceedings、NeurIPS proceedings；条目只在已确认时填写。
- 引用量：对应 OpenAlex work 的 `cited_by_count`；Semantic Scholar API 本轮触发 429，因此没有把两家的数字混用。
