import sys,glob,json
sys.path.insert(0,"_work"); from synth import deepseek
ts=json.load(open("_work/threads.json",encoding="utf-8"))
mat="\n\n".join(f"## {t['name']}\n\n"+open(f"_work/syn_{i}.md",encoding="utf-8").read()
                for i,t in enumerate(ts))
cur=open("_work/cross.md",encoding="utf-8").read().split("### B.")[1].split("### C.")[0]
SYS="""你在复核一张「五年真正的转折点」表。规则同前：事实只能来自素材，禁营销词，中文，表格。

现有的表有两个问题，都要修：
1. 「时间」列写的是「早期/中期/后期」，太虚。改成具体年份或半年（如 `2022 H2`、`2024–2025`），
   依据是「触发它的工作」在素材里标注的时间。
2. 表里可能漏了 2022 到 2023 年初的转折。对着素材判断那段时间有没有同等分量的转折——
   即「之后大部分工作都改了做法」的那种，而不是单纯有影响力的论文。有就补进去。

判定「转折」的标准，逐条对照，不满足就不要往表里写：
- 之后大部分工作换了做法，而不是只多了一个可选方案；
- 素材里能看到多篇后续工作沿用它的做法。

输出完整替换版：一个表格（列：`时间 | 转折 | 触发它的工作 | 之前怎么做 → 之后怎么做`，按时间升序，
4~6 行），表格下接一段话说清这些转折之间的因果关系，并点明哪一条的证据最薄。
不要写别的，不要解释你改了什么。"""
r=deepseek(SYS,f"【现有的表】\n{cur}\n\n【全部素材】\n{mat[:380000]}",max_tokens=24000,temp=0.3)
open("_work/crossB.md","w",encoding="utf-8").write(r.strip()); print("OK",len(r))
