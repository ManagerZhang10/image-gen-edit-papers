import json,re,os,glob,collections,sys
sys.path.insert(0,"_work")
from diagram import D as DIAG

ts=json.load(open("_work/threads.json",encoding="utf-8"))
cross=open("_work/cross.md",encoding="utf-8").read()
def part(tag,nxt):
    mo=re.search(rf"### {tag}\..*?$(.*?)(?=^### {nxt}\.|\Z)" if nxt else rf"### {tag}\..*?$(.*)",
                 cross,re.S|re.M)
    return mo.group(1).strip()
A,B,C,D=[part(t,n) for t,n in [("A","B"),("B","C"),("C","D"),("D",None)]]
B=open("_work/crossB.md",encoding="utf-8").read().strip()

meta={}
for f in glob.glob("20*/meta.json"):
    d=json.load(open(f,encoding="utf-8")); meta[d["short"]]=d
yr=collections.Counter(re.match(r"(\d{4})",str(d["date"])).group(1) for d in meta.values())
ARX={"2022":96,"2023":228,"2024":289,"2025":428,"2026":392}

hy=collections.Counter()
for d in meta.values():
    y,m=re.match(r"(\d{4})[/-](\d{2})",str(d["date"])).groups()
    hy[f"{y}{'H1' if int(m)<=6 else 'H2'}"]+=1
spark="\n".join(f"| {k[:4]} {k[4:]} | {v:2d} | {'█'*v} |" for k,v in sorted(hy.items()))

L=[]
L.append("""# 图像编辑 2022–2026：160 篇读完之后的总结分析

> 读者：已经知道图像编辑大概在做什么，想搞清楚这五年的技术主线怎么走的、现在该押哪条路
> 目标：读完能判断一个新方法值不值得跟、卡点在哪一层、自己的项目该从哪条线取经
> 素材：`/Users/yuzhang/ZhangYu/image_edit_paper` 里 160 篇论文的深读笔记，逐篇的正文见 [INDEX.md](INDEX.md)
> 最后核对：2026-08-28

这篇只讲跨论文的结论。单篇怎么做的看各自的 `解读.md`，这里不重复。
2026 那一年的收录方式和别的年份不同（还没有引用量可参考，是靠模型逐篇判断筛出来的），
**凡是只由 2026 论文支撑的结论，用之前先看第 5 节。**

""")

L.append("## 0. 先破一个误解\n\n"+A+"\n")

L.append("## 1. 五年里真正的转折点\n\n"+B+"\n\n哪些算「转折」是判断题，不是算出来的。这里的标准是「之后大部分工作都改了做法」，而不是「这篇有影响力」——所以表里只有 6 行，第 3 节里更多有名的工作没进来。表末那段自己点出了证据最薄的一条。另外前两列的年份是我按素材里的论文日期改过的：模型原本给的是「早期/中期/后期」，评测那一行原写 2025 H2，但它引的 banana100 是 2026/04，所以改成 2025 H2–2026 H1。\n")
L.append("### 论文密度（库内 160 篇按半年）\n\n| 半年 | 篇数 | |\n| --- | --- | --- |\n"+spark+
 "\n\n⚠️ **这是库内密度，不是领域热度。**2026 前八个月的 38 篇是照着 2025 的月均密度（51 篇 / 12 个月）反推出来的配额，\n不是「2026 就产出了这么多值得读的工作」。2022 那一头偏少则是另一个原因：早期工作被后续综述反复引用，容易识别，\n所以收得准但收得少。怎么筛的、漏了什么，见第 5 节。\n")

L.append("""## 2. 十五条脉络怎么互相咬合

先看结构，再看每条线各自的结论。编号对应第 3 节。

```
"""+DIAG+"""
```

读法：**越靠上的层越晚成熟，也越是现在的主战场**。2022–2023 全部精力在中间那层（怎么改图），
2024 下沉到底下两层（骨干和数据），2025 之后上移到顶上两层（评什么、拿什么当奖励）。

### 反复出现的模式

"""+C+"\n")

L.append("## 3. 十五条脉络各自的结论\n")
for i,t in enumerate(ts):
    ps=t["papers"]; ds=sorted(p["date"] for p in ps)
    reps="、".join(p["short"] for p in ps[:3])+("…" if len(ps)>3 else "")
    syn=open(f"_work/syn_{i}.md",encoding="utf-8").read().strip()
    syn=re.sub(r"^#### ",r"##### ",syn,flags=re.M)
    L.append(f"### {i+1}. {t['name']}\n\n"
             f"`{len(ps)} 篇 · {ds[0]} ~ {ds[-1]} · {reps}`\n\n{syn}\n")

L.append("## 4. 全领域还没解决的\n\n"+D+
 "\n\n这七条里，**空间推理**和**评估错位**是被最多脉络同时点名的两条。"
 "前者决定编辑能不能可靠执行，后者决定你有没有办法知道它可靠——"
 "一个模型在自动指标上变好，可能只是学会了少改一点。\n")

cov="\n".join(f"| {y} | {yr.get(y,0)} | {ARX[y]} | {yr.get(y,0)/ARX[y]:.0%} |" for y in sorted(ARX))
L.append(f"""## 5. 覆盖度自查与可信度边界

### 5.1 收了多少，漏了多少

分母是 arXiv 上 `abs:"image editing" AND cat:cs.CV` 的命中数（2026-08-28 实查，
2026 只统计到 8 月）。分母包含大量边缘论文，所以比例不代表「漏了九成」，只用来做**年份间的横向对比**。

| 年份 | 库里收了 | arXiv 命中 | 收录比例 |
| --- | --- | --- | --- |
{cov}

另有 2021 年 2 篇（SDEdit、Latent-Diffusion），因为后面几乎所有工作都建立在它们上面。

2026 这一年的收录方式和别的年份不一样，得单独说清楚。

建库时 `export.arxiv.org` 的 API 在本机不可达（curl 返回 000），只能靠已知论文名逐个抓，
严重偏向已经出名的工作——2026 当时只收进 5 篇，占比 1%。
2026-08-28 复查发现该 API 已恢复，于是把 2026 整年重跑了一遍：

```
15 条检索式 × 分页 ──► 1123 篇去重      submittedDate 2026-01-01 ~ 2026-09-01
        │  关键词预筛：正列表加权（标题命中权重 3），负列表剔除
        │  （video editing / 3D / 医疗 / 遥感 / 人脸识别 / knowledge editing / 水印 / 攻击 …）
        ▼
      410 篇 ──► DeepSeek 逐篇对着 15 条脉络打 1~5 分 ──► 111 篇拿到 ≥4 分
        │  111 个 arXiv ID 全部实抓 arxiv.org/abs 比对 citation_title + citation_date：111/111 命中
        ▼
      111 篇 ──► 同一模型横向比选（脉络均衡、同题只留最强）──► 33 篇入库
```

命中率从 1% 回到 10%，和其他年份齐平了。但比覆盖率更该注意的是下面这四条：

| 问题 | 说明 |
| --- | --- |
| 2026 没有引用量可以参考 | 最早的一篇也才 8 个月。Semantic Scholar 上 407/410 有记录但数值普遍是个位数，HF upvotes 只有 208/410 有。这两个信号只在**筛选阶段**用过、权重很低，没有写进任何一篇解读（prompt.md 禁止论文外信息） |
| 筛选是模型判断，不是人工判断 | 410→111→33 两道都是 DeepSeek 打的分，我只定标准和脉络配额。会漏掉"摘要写得平淡但实际重要"的工作 |
| 两条脉络 2026 收 0 篇 | 拖拽与点控编辑、以及不带奖励模型的那类 RL 编辑，1123 篇里没有够 4 分的。可能真的沉寂了，也可能是我的检索式没覆盖到——**未验证** |
| 33 这个数是配额定的 | 见第 1 节密度表下面那段。不是"2026 只有 33 篇值得读" |

### 5.2 这份总结是怎么产生的

```
160 篇 PDF ──pypdf 抽文本──► DeepSeek v4 Pro 按 prompt.md 逐篇写解读（160 次调用）
                                          │
              每篇取 §1 定位 + §10 工程判断 + §11 脉络位置
                                          ▼
                        按 15 条脉络分组 ──► 脉络级综述（15 次调用）
                                          ▼
                                  横向归纳（1 次调用）──► 本文第 0/1/2/4 节
```

脉络的划分是我人工定的，不是聚类出来的；分到哪条线带主观判断，有些论文本可以跨线。

### 5.3 已知会出错的地方

| 局限 | 说明 |
| --- | --- |
| 2026 靠模型筛选 | 见 5.1 的四条。2026 的 38 篇里 33 篇是模型从 1123 篇里选的，人工只定了标准 |
| 图表信息全部丢失 | 只有 PDF 抽出的文字进了模型，示意图、定性对比图读不到 |
| 公式细节会失真 | pypdf 常丢下标、希腊字母、矩阵记号，§5 的公式以原 PDF 为准 |
| 枝节描述可能出错 | 已发现一例：Imagic 那篇把 Imagen/SD 说成「ImageNet 预训练模型基础」，不准确 |
| 数字溯源有 5.3% 未命中 | 9214 个数字里 485 个没在原文抽取文本里直接匹配。逐篇看未命中率，只有 2 篇超过 25%（Kontinuous-Kontext 28.2%、Bootstrap-Your-Generator 27.5%），两篇都手工核过，**全部是检查脚本的误报**：pypdf 把表格单元格粘成 `6.696.932.17`（真值 6.69 / 6.93 / 2.17）、把 `110K` 写成一个 token，所以正则匹配不上。累计手工抽查 8 篇，无一例真错。但**没有全量核完** |
| 没有交叉复核 | 每篇只生成一次，本文的归纳也只跑了一遍，没有第二个模型独立验证 |
| 不含论文外信息 | 按 prompt.md 的规定不写引用量、社区评价、后续产品。选题时参考过影响力，但那部分判断没写进任何一篇 |

**可以放心的**：160 个 arXiv ID 全部实抓 `arxiv.org/abs` 比对过 citation_title 和 citation_date，
没有编造的论文。160 篇解读结构完整（11 节齐全）、PDF 全部可解析、篇幅全部 ≥6500 中文字。
prompt.md 要求 6500–8500，有 4 篇轻微超上限（MGIE 8830、FLUX-Kontext 8553、Kontinuous-Kontext 8551、MimicBrush 8536），没有截。

## 参考

- 逐篇解读索引：[INDEX.md](INDEX.md)
- 解读的写作规范：[prompt.md](prompt.md)
- arXiv 检索接口：http://export.arxiv.org/api/query
""")

out="\n".join(L)
open("总结分析.md","w",encoding="utf-8").write(out)
print("字数",len(out.replace(" ","")))
