# Benchmark 前半组交付清单

核对日期：2026-08-29。技术内容以论文原文、官方 proceedings、作者项目页和官方仓库为准。引用量原计划统一查询 Semantic Scholar，但其 API 返回 HTTP 429，因此本组统一回退到 OpenAlex，不混用 provider；数字是核对时快照，不代表永久值。

| 条目 | 目录 | PDF/笔记状态 | 正式 venue | 首次公开 | 正式发表 | 实时引用量 | 引用数据源 |
| --- | --- | --- | --- | --- | --- | ---: | --- |
| CPI-Bench | 2026-08_CPI-Bench | 已保存 | arXiv 预印本 | 2026-08-14 | — | 0 | OpenAlex W7203615284 |
| I2EBench | 2024-08_I2EBench | 已保存 | NeurIPS 2024 Main | 2024-08-26 | 2024-12 | 1 | OpenAlex W7103752508 |
| HATIE | 2025-05_HATIE | 已保存 | CVPR 2025 Highlight | 2025-05-01 | 2025-06 | 0 | OpenAlex W4413144382 |
| I2I-Bench | 2025-12_I2I-Bench | 已保存 | CVPR 2026 | 2025-12-04 | 2026-06 | 0 | OpenAlex W4417086874 |
| Complex-Edit | 2025-04_Complex-Edit | 已保存（arXiv v1；正式页已核验） | TMLR | 2025-04-17 | 2026-03 | 0 | OpenAlex W4416538115 |
| ComplexBench-Edit | 2025-06_ComplexBench-Edit | 已保存 | ACM Multimedia 2025 | 2025-06-15 | 2025-10-27 | 2 | OpenAlex W4415541163 |
| RefEdit | 2025-06_RefEdit | 已保存 | ICCV 2025 | 2025-06-03 | 2025-10 | 0 | OpenAlex W4416072503 |
| Inter-Edit | 2026-06_Inter-Edit | 已保存（CVF 正式 PDF） | CVPR 2026 | 2026-06（未发现更早预印本） | 2026-06 | 未收录/不可得 | OpenAlex 无精确记录 |
| VIBE | 2026-02_VIBE | 已保存 | arXiv 预印本 | 2026-02-02 | — | 0 | OpenAlex W7127284895 |
| PaintBench | 2026-05_PaintBench | 已保存 | arXiv 预印本 | 2026-05-29 | — | 0 | OpenAlex W7163156560 |
| GSI-Bench | 2026-04_GSI-Bench | 已保存 | CVPR 2026 | 2026-04-22 | 2026-06 | 0 | OpenAlex W7155353408 |
| KRIS-Bench | 2025-05_KRIS-Bench | 已保存 | NeurIPS 2025 Datasets & Benchmarks | 2025-05-22 | 2025-12 | 0 | OpenAlex W4416452763 |

## 状态说明

- 12/12 条均有 paper.pdf、解读.md、meta.json。
- Complex-Edit 本地 PDF 为 arXiv v1；TMLR 2026-03 正式发表状态已通过 OpenReview 官方论文页核验，并在笔记/meta 中注明。未用受限下载覆盖现有可验证 PDF。
- Inter-Edit 未找到更早 arXiv 预印本，本地保存的是 CVPR 2026 Open Access 正式 PDF；OpenAlex 在核对日未返回精确标题记录，所以引用量记为“未收录/不可得”，而不是 0。
- 解读.md 的技术结论不使用引用量作为证据；引用量只用于权威性/影响力元数据。

