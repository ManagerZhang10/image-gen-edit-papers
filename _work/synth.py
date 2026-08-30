import json,os,re,sys,urllib.request,time

ENV=os.environ.get("LLM_ENV_FILE",
                   os.path.expanduser("~/ZhangYu/BaseModel/.env"))
cfg={}
for l in open(ENV,encoding="utf-8"):
    l=l.strip()
    if "=" in l and not l.startswith("#"):
        k,v=l.split("=",1); cfg[k.strip()]=v.strip().strip('"').strip("'")
KEY=cfg["DEEPSEEK_API_KEY"]; BASE=cfg["DEEPSEEK_BASE_URL"]; MODEL=cfg["DEEPSEEK_V4_PRO_MODEL"]

def deepseek(sysmsg,usermsg,max_tokens=16000,temp=0.3):
    body=json.dumps({"model":MODEL,"messages":[{"role":"system","content":sysmsg},
        {"role":"user","content":usermsg}],"max_tokens":max_tokens,
        "temperature":temp}).encode()
    req=urllib.request.Request(BASE.rstrip("/")+"/chat/completions",data=body,
        headers={"Content-Type":"application/json","Authorization":"Bearer "+KEY})
    for att in range(4):
        try:
            with urllib.request.urlopen(req,timeout=1800) as r:
                return json.loads(r.read())["choices"][0]["message"]["content"]
        except Exception as e:
            if att==3: raise
            time.sleep(10*(att+1))

def sec(md,n):
    """取第 n 节正文"""
    mo=re.search(rf"^## {n}\. .*?$(.*?)(?=^## \d+\. |\Z)",md,re.S|re.M)
    return mo.group(1).strip() if mo else ""

SYS="""你在为一个 160 篇的图像编辑论文库写「脉络级综述」。素材是每篇论文解读里的三节：
定位（这篇解决什么）、工程判断（可行性/风险/上限）、脉络收束（在研究谱系里的位置）。

硬规则：
- 事实只能来自给你的素材。素材没写的，不要补充、不要脑补论文之外的信息。
- 不写引用量、社区评价、后续产品、开源生态——素材里没有这些。
- 不确定就不写，不要用「据了解」「普遍认为」这类模糊措辞。
- 禁止营销词：碾压、吊打、开山之作、革命性、里程碑、颠覆。
- 中文写作，技术术语保留英文原词（inversion、cross-attention、CFG、LoRA 等）。
- 能用表格表达对照关系就用表格，不要写成大段散文。
- 不要写「总结」「展望」「结语」这类凑数章节。
- 不要复述我的问题，不要写元话语（「本节将……」「接下来我们……」）。

输出格式，严格照抄这四个小标题，不要加别的：

#### 这条线在解决什么
两三句话。说清这条线独有的技术矛盾——别的线不用面对、或者用别的办法绕不过去的那个矛盾。

#### 怎么演进的
一个表格，一行一个阶段（3~5 行，不是一行一篇论文）。列：`阶段 | 代表工作 | 关键动作 | 换来了什么 / 代价是什么`。
「关键动作」写具体技术手段，不要写「提出了新方法」这种废话。
表格下面接两三句话，点出这条线真正的转折点在哪、为什么是那里。

#### 已经稳定下来的做法
3~5 条。写那些被多篇论文反复采用、可以当默认选项的做法。每条一行，`- **做法** —— 一句话说清什么时候用`。

#### 还没解决的
3~5 条。写素材里明确提到的局限、失败模式、未解问题。每条一行，`- **问题** —— 一句话说清它卡在哪`。
只写素材支持的，不要自己发明开放问题。"""

def run(idx):
    ts=json.load(open("_work/threads.json",encoding="utf-8"))
    t=ts[idx]; out=f"_work/syn_{idx}.md"
    if os.path.exists(out) and len(open(out,encoding="utf-8").read())>800:
        print(f"[SKIP] {t['name']}"); return
    parts=[]
    for p in t["papers"]:
        md=open(f"{p['folder']}/解读.md",encoding="utf-8").read()
        parts.append(f"### {p['short']}（{p['date']}）\n"
                     f"【定位】{sec(md,1)}\n\n【工程判断】{sec(md,10)}\n\n【脉络位置】{sec(md,11)}")
    body="\n\n".join(parts)
    u=(f"脉络名：{t['name']}\n本脉络 {len(t['papers'])} 篇，按时间排序如下。\n\n{body}")
    r=deepseek(SYS,u[:200000])
    open(out,"w",encoding="utf-8").write(r.strip())
    print(f"[OK] {t['name']} {len(r)}")

if __name__=="__main__":
    run(int(sys.argv[1]))
