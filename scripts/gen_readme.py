#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 scripts/papers.json + 实际落盘的解读渲染 README.md。README 不手写。

列顺序遵守 ../CLAUDE.md 第二节：# / 时间 / 简称 / 论文标题 / 发表 / 机构 / 原文
七列必须有、相对顺序固定；任务与解读字数作为附加列插在机构之后、原文之前。
解读字数当场从 解读.md 数（U+4E00–U+9FFF），不读 meta.json。
"""
import json, os, re
from collections import Counter, OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECKED = "2026-09-01"
CJK = lambda t: sum(1 for ch in t if "一" <= ch <= "鿿")


def venue_cell(p):
    """venue_note 只有一种取值「年份未核」——Semantic Scholar 那一档只核到会议名。
    不在 venue 字符串里拼一个假年份，也不让读者误以为年份核过了。"""
    v = p["venue"]
    return f"{v}（{p['venue_note']}）" if p.get("venue_note") else v


def org_cell(p):
    o = p.get("org") or []
    if not o:
        return "**未核**"
    s = " / ".join(o[:2])
    if len(o) > 2:
        s += f" 等 {len(o)} 家"
    if p.get("org_source") and "low" in p["org_source"]:
        s += "（低置信）"
    return s


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    ps.sort(key=lambda p: (p["date"] or "9999/99/99", p["short"]))

    rows, total, have = [], 0, 0
    for i, p in enumerate(ps, 1):
        note = f"{ROOT}/papers/{p['dir']}/解读.md"
        if os.path.exists(note):
            n = CJK(open(note, encoding="utf-8").read())
            total += n; have += 1
            name, chars = f"[{p['short']}](papers/{p['dir']}/解读.md)", f"{n:,}"
        else:
            name, chars = p["short"], "—"
        src = f"[PDF]({p['pdf']})" if p.get("pdf") else f"[官方来源]({p['url']})"
        rows.append(f"| {i} | {(p['date'] or '—').replace('/','-')} | {name} | {p['title']} | "
                    f"{venue_cell(p)} | {org_cell(p)} | {'+'.join(p['task'] or [])} | {src} | {chars} |")

    tasks = Counter(t for p in ps for t in (p["task"] or []))
    both = [p["short"] for p in ps if set(p["task"] or []) == {"生成", "编辑"}]
    types = Counter(p["type"] for p in ps)
    lines = OrderedDict()
    for p in ps:
        lines.setdefault(p["line"], []).append(p["short"])
    line_rows = [f"| {k} | {len(v)} |" for k, v in sorted(lines.items(), key=lambda kv: -len(kv[1]))]

    verified = sum(1 for p in ps if p.get("link_status") == "OK")
    no_paper = [p["short"] for p in ps if not p.get("pdf")]
    org_unknown = [p["short"] for p in ps if not p.get("org")]
    # 三种写作规范。分桶依据是 papers.json 的 spec 字段（由本库自己的批次记录定），
    # 不是数二级标题——11 节那批里有 12 节和 19 节的变体。说明是人写的，不由数据生成。
    SPEC_LABEL = {"v1-11节": "11 节深读（6,502–8,943 字）",
                  "短版": "决策型短笔记（8～9 节）",
                  "v2": "v2 / 8 节 / 3,000–5,000 字"}
    SPEC_DESC = {
        "v1-11节":
            "最初那批的规范。结构上 158 篇是标准 11 节，Complex-Edit 与 KRIS-Bench 在 11 节之后"
            "又接了 benchmark 那套格式的 6 个无编号小节，再补决策意义与一手来源两节",
        "短版":
            "2026-08-29 那轮核验补进来的，以 benchmark 和评测指标为主；"
            "其中 4 项没有独立论文，只记录官方资料与核验边界",
        "v2":
            "2026-09 起的新增篇目，含本次并入的 8 篇生成侧论文。"
            "8 节齐全、3,000–5,000 汉字、证据表至少 4 行，由脚本硬校验，不达标自动重生成",
    }
    ORDER_SPEC = ["v1-11节", "短版", "v2"]
    specs = Counter(p["spec"] for p in ps)

    head = f"""# 图像生成与编辑论文库 2021–2026

[![papers](https://img.shields.io/badge/papers-{len(ps)}-2b7489)](#全量清单)
[![notes](https://img.shields.io/badge/notes-{total/1e6:.2f}M_CJK_chars-4c9a2a)](#全量清单)
[![coverage](https://img.shields.io/badge/coverage-2021.08_--_2026.08-e07b39)](#全量清单)
[![links](https://img.shields.io/badge/source_links-{verified}%2F{len(ps)}_byte--verified-1f883d)](docs/可信度与产出.md#2-原文直链是怎么核的)
[![license](https://img.shields.io/badge/license-CC_BY_4.0-777777)](LICENSE)

**{len(ps)} 篇图像生成与编辑论文，每篇一份中文深读笔记，外加一条核验过的原文直链。**
时间跨度 2021-08 → 2026-08，笔记合计 {total:,} 个汉字。

*{len(ps)} image generation & editing papers, each with an in-depth Chinese reading note and a verified link to the original source. Aug 2021 – Aug 2026.*

> **维护者** [@ManagerYu10](https://github.com/ManagerYu10) · **授权** [CC BY 4.0](LICENSE)（署名即可转载、改写、商用） · **最后核对** {CHECKED}
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
| 编辑 | {tasks['编辑']} |
| 生成 | {tasks['生成']} |
| 两者都是（统一模型） | {len(both)} |

视频侧在另一个库：[video-gen-edit-papers](https://github.com/ManagerYu10/video-gen-edit-papers)。

按贡献类型分：{'、'.join(f'{k} {v}' for k, v in types.most_common())}。

## 怎么用

直接拉到本页最后的[全量清单](#全量清单)，{len(ps)} 行按时间排，浏览器里 `Ctrl/Cmd + F` 搜简称或标题。每行两列可以点：

| 这一列 | 点开是什么 |
| --- | --- |
| **简称** | 这篇的 `解读.md`，中文深读笔记，就在本仓库里 |
| **原文** | 论文本身。{verified} 行标 `PDF` 的过了字节级核验，{len(no_paper)} 行标 `官方来源` 的确实没有独立论文 |

按技术脉络分组的视图在 [docs/INDEX.md](docs/INDEX.md)，跨论文的结论在 [docs/总结分析.md](docs/总结分析.md)。

**解读的定位是替代第一次完整泛读**，不替代精读——要抠实现细节仍然得回 PDF。三种规范并存，
是分批产出留下的，旧的不回炉重写：

| 规范 | 篇数 | 说明 |
| --- | ---: | --- |
{chr(10).join(f'| {SPEC_LABEL[k]} | {specs[k]} | {SPEC_DESC[k]} |' for k in ORDER_SPEC if specs.get(k))}

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
{chr(10).join(line_rows)}

逐篇归入哪条、每条怎么串起来，见 [docs/INDEX.md](docs/INDEX.md)。

## 全量清单

{len(ps)} 行按时间排。**解读字数**是当场从 `解读.md` 数的（U+4E00–U+9FFF），不读 `meta.json`。

| # | 时间 | 简称（→ 解读） | 论文标题 | 发表 | 机构 | 任务 | 原文 | 解读字数 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
"""
    tail = f"""

## 仓库长什么样

```
image-gen-edit-papers/
├── README.md                       ← 本文件。收什么 + 怎么用 + {len(ps)} 项全量清单
├── LICENSE                         ← CC BY 4.0
├── papers/                         ← {len(ps)} 个论文目录，名字就是 YYYY-MM_简称
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
| 机构标 **未核** 的 {len(org_unknown)} 篇 | {'、'.join(org_unknown) or '无'}。这几篇 PDF 首页的抽取文本里确实没有作者机构，不编 |
| 机构一列的来源 | 只认 PDF 首页作者块（模型抽取，人抽查）。**没用 OpenAlex 补**——它对 arXiv 预印本几乎没有机构字段，且已知会误配 |
| 发表信息 | 优先用 `docs/review/` 四份人工核验 manifest；其次 arXiv `journal_ref`；再次 arXiv `comment` 里明确写「已接收」的。**只认接收，不认投稿**——写「submitted to」的一律记作预印本。逐条来源记在 `papers.json` 的 `venue_source` |
| 引用量 | 快照，非实时。provider 混用（人工核验轮用 Semantic Scholar，补齐用 OpenAlex），**不同 provider 的数字不做严格横向排名**。逐条记在 `cites_source` |
| 没有独立论文的 {len(no_paper)} 项 | {'、'.join(no_paper) or '无'}。笔记只记录官方资料和核验边界，不能用来反推架构、训练数据或身份保持机制 |
| 2026 年那批的选文 | 38 篇里有 33 篇是模型从 1,123 篇候选里筛出来的，**人工只定了标准**。详见 [总结分析.md §5](docs/总结分析.md) |
| 跨论文结论的覆盖范围 | [总结分析.md](docs/总结分析.md) 写的是最初 160 篇 / 15 条脉络。2026-09 并入的生成侧论文和新增的 2 条脉络还没进那份分析 |
| 解读正文 | 机器生成，未逐句人工复核。数字与结论以原文为准 |
"""
    open(f"{ROOT}/README.md", "w", encoding="utf-8").write(head + "\n".join(rows) + tail)
    print(f"README 已渲染：{len(ps)} 项，{have} 篇有解读，合计 {total:,} 字，"
          f"{len(lines)} 条脉络\n  任务 {dict(tasks)}  两者都是 {len(both)} 篇"
          f"\n  直链已核 {verified}/{len(ps)}；机构未核 {len(org_unknown)}；无独立论文 {len(no_paper)}")


if __name__ == "__main__":
    main()
