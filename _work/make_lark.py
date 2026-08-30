#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""INDEX.md -> _work/INDEX_lark.md：本地路径换成 arXiv 链接，换掉开头和第 2 节。"""
import re, json, glob, os, datetime
ROOT = "/Users/yuzhang/ZhangYu/image_edit_paper"
os.chdir(ROOT)
url = {}
for m in glob.glob("20*/meta.json"):
    d = json.load(open(m, encoding="utf-8"))
    url[os.path.dirname(m)] = d["url"]
s = open("INDEX.md", encoding="utf-8").read()

def fix(mo):
    return f"[{mo.group(1)}]({url[mo.group(2)]})"
s = re.sub(r"\[([^\]]+)\]\((20[^)/]+)/解读\.md\)", fix, s)
n = len(url)
dates = sorted(json.load(open(m, encoding="utf-8"))["date"][:7].replace("/", "-") for m in glob.glob("20*/meta.json"))

HEAD = f"""# 图像编辑论文库索引（2022–2026，{n} 篇）

> 读者：要系统补齐 2022–2026 图像编辑技术脉络的人
> 目标：按脉络挑论文；每篇本地都有一份 11 节中文深读，链接指向 arXiv 原文
> 覆盖：{n} 篇，{dates[0]} ～ {dates[-1]}
> 最后核对：{datetime.date.today().isoformat()}

## 0. 先说这个库怎么用

**正文和 PDF 都在本地**，这份 Lark 文档只是目录，方便分享和挑论文。
库在张钰的 Mac 上：`/Users/yuzhang/ZhangYu/image_edit_paper`，
每篇一个文件夹，里面是 `paper.pdf`（arXiv 原文）、`解读.md`（11 节中文深读）、
`meta.json`（arXiv ID、日期、字数）。下面表里的链接指向 arXiv 原文。
跨论文的结论在本地 `总结分析.md`，不在这份文档里。
解读按 `prompt.md` 的规范写：
先定位问题，再画数据流，然后拆公式、训练、推理、实验、选型、工程风险。
**它的定位是替代第一次泛读**，不是替代精读——要抠实现细节仍然得回 PDF。

所有 arXiv ID 都实抓 `arxiv.org/abs` 比对过标题与日期，不是凭记忆写的。

"""
CRED = f"""## 2. 这份库的可信度边界

解读由 DeepSeek v4 Pro 依据 **PDF 抽取的论文正文** 生成，`prompt.md` 原样作为约束：
只以论文为事实来源、区分「论文写明 / 实验支持 / 工程推断」、不确定就写「论文未明确披露」。

**做过的校验**

| 环节 | 怎么验的 | 结果 |
| --- | --- | --- |
| arXiv ID | 逐个实抓 `arxiv.org/abs`，比对 citation_title 与 citation_date | {n}/{n} 标题日期吻合 |
| 结构完整 | 机器检查 H1、11 个二级标题、结尾 `<!-- COMPLETE -->` | {n}/{n} 通过 |
| 篇幅 | 中文字符数 | {n}/{n} 落在 6502~8830（规范要求 6500~8500，4 篇轻微超上限，没有截） |
| PDF | 大小 + pypdf 解析 | {n}/{n} 存在且可解析 |
| 数字溯源 | 解读里每个数字回原文抽取文本比对 | 9214 个数字中 485 个未直接匹配（5.3%） |

**那 5.3% 是什么**：逐篇看未匹配率，只有 2 篇超过 25%，两篇都手工核过，**全部是检查脚本误报**——
pypdf 把表格单元格粘成一串（原文 `6.696.932.17` 实为 6.69 / 6.93 / 2.17），
或把 `110K` 当成一个 token，正则匹配不上。累计手工抽查 8 篇，**没有发现编造的数字**，但没有全量核完。

**⚠️ 2026 那 38 篇是怎么选的，和其他年份不一样**

建库时 `export.arxiv.org` 的 API 在本机不可达（curl 返回 000），只能靠已知论文名逐个抓，
2026 当时只收进 5 篇。2026-08-28 复查发现 API 已恢复，重跑了整年：
15 条检索式取到 1123 篇去重结果 → 关键词预筛 410 篇 → DeepSeek 逐篇对 15 条脉络打分留下 111 篇（≥4 分）
→ 横向比选定 33 篇入库。111 个 ID 全部实抓 `arxiv.org/abs` 核过，111/111 命中。

所以 2026 的选题**是模型判断，不是人工判断**；33 这个数是照 2025 的月均密度（51 篇 / 12 个月）定的配额，
不代表 2026 只有 33 篇值得读。另外 2026 还没有引用量可以参考（最早的一篇才 8 个月）。

**已知局限，读的时候留意**

| 局限 | 说明 |
| --- | --- |
| 只读得到文字 | 图表、示意图、定性对比图的内容没有进入模型，纯图里的信息解读不到 |
| 公式符号会丢 | PDF 抽取常丢下标、希腊字母和矩阵记号，公式细节以 PDF 为准 |
| 枝节描述可能出错 | 已发现一例：Imagic 那篇把 Imagen/SD 说成「ImageNet 预训练模型基础」，不准确。数字溯源查不出这类错 |
| 未做交叉复核 | 每篇只生成一次（偏短的做过扩写），没有第二个模型独立复核结论 |
| 不含论文外信息 | 按规范刻意不写后续工作、引用量、社区评价——要看影响力得另找来源 |

选题参考过引用量和 HuggingFace upvotes，但**这部分判断没有写进任何一篇解读**，只用于决定收哪些论文。

"""
# 换头
i = s.index("## 1. 15 条脉络")
s = HEAD + s[i:]
# 换第 2 节
a = s.index("## 2. 可信度边界"); b = s.index("## 3. 按时间的全量清单")
s = s[:a] + CRED + s[b:]
open("_work/INDEX_lark.md", "w", encoding="utf-8").write(s)
print("INDEX_lark.md 已生成", n, "篇", len(s), "字")
