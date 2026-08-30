import json,sys,re
sys.path.insert(0,"_work"); from synth import deepseek
rows=json.load(open("_work/2026/merged.json",encoding="utf-8"))
keep=[r for r in rows if r.get("keep") and r.get("score",0)>=4]
keep.sort(key=lambda r:r["real_date"])
TN={1:"训练-free",2:"反演精度",3:"指令式编辑",4:"条件控制",5:"个性化",6:"局部/对象",
    7:"拖拽点控",8:"统一多模态",9:"生成骨干",10:"推理RL评测",11:"奖励模型与在线RL",
    12:"think-then-edit",13:"编辑数据工程",14:"新一代旗舰",15:"新一代评测"}
lines=[]
for r in keep:
    lines.append(f'{r["id"]} | {r["real_date"]} | T{r["thread"]}:{TN.get(r["thread"],"?")} '
                 f'| 引用{r["cit"]} HF赞{r["up"]} | {r["real_title"]}\n    摘要: {r["summary"][:380]}')
mat="\n\n".join(lines)

SYS="""你在给一个「2022-2026 图像编辑关键论文库」定 2026 年的最终收录名单。

背景：库里 2022-2025 已收 122 篇，其中 2025 全年 51 篇。2026 只统计到 8 月（8 个月），
按同样密度应该收 **32~36 篇**。我给你 111 篇已经初筛过的候选，你要选出最终名单。

选择原则，按优先级：
1. **优先能改变判断的工作**，而不是效果好一点的工作。一篇让人重新理解某条脉络卡在哪里的
   诊断/实证研究，比一篇刷高分的方法论文更该收。
2. **脉络要铺开**。15 条脉络里，2026 明显活跃的（奖励模型与在线RL、think-then-edit、
   统一多模态、新一代评测）可以多收；但不要一条线收 15 篇而另一条线 0 篇。
   反演、条件控制、局部对象、个性化这些老线，2026 有真进展的也要留位置。
3. **同一主题重复的只留最强的一篇**。比如多篇都在做 spatial reward、多篇都在做
   inversion 精度，选贡献最清楚、证据最完整的，其余不收。
4. 引用数和 HF 点赞是弱信号——2026 的论文都还没时间积累。高赞说明社区已经在用，
   可以加分；**零引用零赞不构成排除理由**，摘要里的贡献才是主要依据。
5. 宁可收一篇诊断性 benchmark，也不收第 5 篇同类方法。

输出严格 JSON 数组，不要解释文字不要代码围栏。按日期升序。每个元素：
{"id":"...","short":"英文短名，字母数字连字符，<=22字符，同名要区分开",
 "thread":脉络编号,"why":"一句中文，说清凭什么收它——要具体到它的贡献，不要写「很重要」"}

只输出被选中的 32~36 篇。"""

d=None
for att in range(4):
    r=deepseek(SYS,mat[:300000],max_tokens=30000,temp=0.25 if att==0 else 0.4)
    r=re.sub(r"```(?:json)?","",r).replace("```","").strip()
    mo=re.search(r"\[.*\]",r,re.S)
    try: d=json.loads(mo.group(0) if mo else r); break
    except Exception as e:
        objs=re.findall(r"\{[^{}]*\}",r,re.S); got=[]
        for o in objs:
            try: got.append(json.loads(o))
            except Exception: pass
        if len(got)>=25: d=got; break
        print("[RETRY]",e,"| 原始响应长度",len(r),"| 开头:",repr(r[:300]),flush=True)
byid={r["id"]:r for r in keep}
d=[x for x in d if x.get("id") in byid]
for x in d:
    x["date"]=byid[x["id"]]["real_date"]; x["title"]=byid[x["id"]]["real_title"]
    x["cit"]=byid[x["id"]]["cit"]; x["up"]=byid[x["id"]]["up"]
json.dump(d,open("_work/2026/final.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("选中",len(d))
