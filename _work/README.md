# 生产管线

这批解读是怎么跑出来的。只保留 `.py`——日志、PDF 抽取文本、候选清单、被拒草稿这些
中间产物没有进仓库，读者不会重复遇到它们。

| 脚本 | 干什么 |
| --- | --- |
| `pipeline.py` | 主编排：下载 PDF → pypdf 抽正文 → 调 DeepSeek v4 Pro → 机器校验 → 落盘，失败回传原因重生成最多 4 次 |
| `synth.py` | 单篇生成，`prompt.md` 原样作为 system prompt |
| `expand_more.py` / `repair.py` | 篇幅不达标时的扩写，以及结构缺项的修补 |
| `factcheck.py` | 数字溯源：把解读里每个数字回 PDF 抽取文本比对 |
| `cross.py` / `recheckB.py` | 跨论文归纳（`总结分析.md`）与复核 |
| `make_index.py` | 由各目录的 `meta.json` 生成 `INDEX.md` |
| `make_lark.py` | 生成 Lark 版索引 |
| `assemble.py` / `diagram.py` / `fixbox.py` | `主线.html` 的数据组装与排版 |
| `fetch2026.py` | 2026 那轮：15 条检索式抓 `export.arxiv.org`，去重得 1123 篇 |
| `2026/judge.py` | 2026 那轮：DeepSeek 逐篇对 15 条脉络打分 |
| `2026/pick.py` / `2026/signal.py` | 按分数和月均密度配额横向比选，最终留下 33 篇 |

⚠️ 这些脚本依赖当时的本机路径和 DeepSeek API key，**没有做过在别的机器上重跑的验证**。
它们的用途是说明产出流程和校验环节，不是开箱即用的工具。
