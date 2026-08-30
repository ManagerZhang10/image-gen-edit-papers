import unicodedata
def w(t): return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in t)
W=58                      # 盒子内宽（不含两侧竖线）
def top(l=0,mid=None):    # ┌───┐
    return "┌"+"─"*W+"┐"
def bot(marks=()):        # └──┬──┘  marks 是 ┬ 的内偏移
    s=list("─"*W)
    for m in marks: s[m]="┬"
    return "└"+"".join(s)+"┘"
def topT(marks=()):
    s=list("─"*W)
    for m in marks: s[m]="▼"
    return "┌"+"".join(s)+"┐"
def row(t):
    return "│"+t+" "*(W-w(t))+"│"
def box(w2,t):            # 小盒子
    return "│"+t+" "*(w2-w(t))+"│"

IND=" "*8
L=[]
def a(s): L.append(IND+s)
a(top());                a(row(" (15) 新一代评测        (11) 奖励模型"))
a(row(" EditBench -> KRIS-Bench -> PICABench"))
a(row(" EditScore / EditReward"))
a(bot((28,)))
L.append(IND+" "*29+"│  定义「怎样算编辑对」，并变成可优化的分数")
L.append(IND+" "*29+"▼")
a(top());                a(row(" (10) 推理与 RL          (12) 先想后做"))
a(row(" Flow-GRPO -> Edit-R1 -> ThinkRL-Edit"))
a(bot((28,)))
L.append(IND+" "*29+"│  训练信号")
a(topT((28,)))
a(row(" 编辑方法本体（2022-2024 的主战场）"))
a(row("  (1) 训练-free    (2) 反演精度    (4) 条件控制"))
a(row("  (5) 个性化       (6) 局部/对象   (7) 拖拽点控"))
a(row("  (3) 指令式编辑 -> (8) 统一多模态 -> (14) 2025H2-"))
a(bot((9,42)))
L.append(IND+" "*10+"│ 要成对训练数据"+" "*18+"│ 跑在骨干上")
L.append(IND+" "*10+"▼"+" "*32+"▼")
W2,W3=24,26
L.append(IND+"┌"+"─"*W2+"┐"+" "*6+"┌"+"─"*W3+"┐")
L.append(IND+box(W2," (13) 编辑数据工程")+" "*6+box(W3," (9) 生成骨干"))
L.append(IND+box(W2," IP2P->UltraEdit->")+" "*6+box(W3," LDM->PixArt->SD3/RF"))
L.append(IND+box(W2,"   NoHumansRequired")+" "*6+box(W3,"   ->FLUX/Qwen-Image"))
L.append(IND+"└"+"─"*W2+"┘"+" "*6+"└"+"─"*W3+"┘")
L.append(IND+" "*10+"▲ (11) 的失败样本回流成偏好负例      换骨干 = 全线重标定")
D="\n".join(L)
if __name__=="__main__":
    for l in D.split("\n"): print(f"{w(l):3d}|{l}")
