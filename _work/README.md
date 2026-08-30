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

⚠️ 上面这些脚本依赖当时的本机路径和 DeepSeek API key，**没有做过在别的机器上重跑的验证**。
它们的用途是说明产出流程和校验环节，不是开箱即用的工具。

## 2026-08-30 加的，这几个是能直接跑的

| 脚本 | 干什么 |
| --- | --- |
| `gen_paper_table.py` | 读 `pdf_link_check.json` + 各目录 `meta.json`，生成 README 附二那张 186 行的表 |
| `check_anchors.py` | 复刻 github-slugger 的去标点规则，检查 md 里的站内锚点能不能对上真实标题 |
| `check_table_rows.py` | 全量核对附二每一行：解读路径、简称、标题、链接、⚠️ 标注、字数必须都来自同一个目录 |
| `spotcheck.py` | 从成品 README 随机抽几行，真去打开链接，比对返回的 `citation_title` 和表里写的标题 |
| `pdf_link_check.json` | 不是脚本，是 [`scripts/verify_pdf_links.py`](../scripts/verify_pdf_links.py) 的核验结果快照，附二那张表的依据 |

这三个只用标准库（`gen_paper_table.py` 要能 import `scripts/pdf_sources.py`），在本仓库里跑过。
