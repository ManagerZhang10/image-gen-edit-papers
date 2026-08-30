import json,sys,os,re
sys.path.insert(0,"_work"); from synth import deepseek

THREADS="""1 训练-free 扩散编辑（注意力/反演改图，不训练）
2 反演精度（真实图无损映回噪声）
3 指令式编辑（说人话改图 + 训练数据）
4 条件控制（结构/身份/参考图注入，ControlNet 类）
5 个性化与主体保持（DreamBooth 类）
6 局部与对象级（抠图/补全/搬物体/inpainting）
7 拖拽与点控编辑
8 统一多模态（理解与生成同一个模型）
9 生成骨干（LDM/DiT/rectified flow 等底座）
10 推理、强化学习与评测
11 奖励模型与在线 RL
12 会推理再动手 think-then-edit
13 编辑数据工程（三元组怎么造）
14 新一代编辑与统一模型（旗舰系统）
15 新一代评测（物理合理性/多轮/能力轴）"""

SYS=f"""你在替一个「2022-2026 图像编辑关键论文库」筛 2026 年的新论文。库里已有 127 篇，分成 15 条脉络：

{THREADS}

我给你一批 2026 年的 arXiv 论文（标题 + 摘要）。逐篇判断它**是否够得上「关键论文」**。

够得上的标准，满足任意一条即可：
- 提出新机制或新范式，不是在已有方法上调参数、换数据
- 是大规模模型 / 大规模数据集 / benchmark，别人很可能拿来用
- 直接针对上面某条脉络的已知开放问题（空间推理、评估与人类偏好错位、多轮误差累积、
  身份保持、真实图分布外、VAE 细节上限、延迟显存矛盾）给出可检验的进展
- 是有系统性的综述或实证研究，能改变别人对某条线的判断

不够的（一律 keep=false）：
- 纯垂域应用（医学、遥感、电商、艺术修复、人脸识别模板）
- 视频编辑为主、3D/点云为主、纯图像复原/去噪/超分/去摩尔纹
- 安全方向（对抗攻击、水印、伪造检测、隐私保护）
- 在已有 benchmark 上刷点的增量工作
- 摘要看不出具体贡献的

score 打 1~5：5=这条脉络 2026 年绕不过去；4=值得单独读；3=可读可不读；1~2=不必读。
只有 score>=4 才 keep=true。宁缺勿滥，一批 20 篇里通常只有 2~5 篇够得上。

只输出 JSON 数组，不要任何解释文字、不要 markdown 代码围栏。每个元素：
{{"id":"论文id","keep":true/false,"thread":脉络编号或0,"score":1-5,
  "short":"英文短名，用于文件夹名，只含字母数字连字符，不超过 24 字符",
  "why":"一句中文，说清它凭什么进/不进"}}"""

def run(bi):
    pre=json.load(open("_work/2026/pre.json",encoding="utf-8"))
    B=20; ch=pre[bi*B:(bi+1)*B]
    if not ch: return
    out=f"_work/2026/judge_{bi:02d}.json"
    if os.path.exists(out) and os.path.getsize(out)>20: print("[SKIP]",bi); return
    u="\n\n".join(f'id: {p["id"]}\n日期: {p["date"]}\n标题: {p["title"]}\n摘要: {p["summary"][:1400]}'
                  for p in ch)
    d=None
    for att in range(4):
        r=deepseek(SYS,u,max_tokens=12000,temp=0.2 if att==0 else 0.4)
        r=re.sub(r"```(?:json)?","",r).replace("```","").strip()
        mo=re.search(r"\[.*\]",r,re.S)
        try:
            d=json.loads(mo.group(0) if mo else r); break
        except Exception as e:
            # 逐对象抢救
            objs=re.findall(r"\{[^{}]*\}",r,re.S); got=[]
            for o in objs:
                try: got.append(json.loads(o))
                except Exception: pass
            if len(got)>=len(ch)*0.6: d=got; break
            print(f"[RETRY] batch {bi} att{att} {e}",flush=True)
    if d is None: print(f"[FAIL] batch {bi}",flush=True); return
    json.dump(d,open(out,"w",encoding="utf-8"),ensure_ascii=False)
    k=sum(1 for x in d if x.get("keep"))
    print(f"[OK] batch {bi} 判 {len(d)} 篇，留 {k}",flush=True)

if __name__=="__main__": run(int(sys.argv[1]))
