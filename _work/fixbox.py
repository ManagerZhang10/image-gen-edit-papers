import re,unicodedata,sys
def w(t): return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in t)
def fix(blk,target=None):
    ls=blk.split("\n")
    ends=[l for l in ls if l.rstrip() and l.rstrip()[-1] in "│┐┘┤"]
    if target is None: target=max(w(l.rstrip()) for l in ends) if ends else 0
    out=[]
    for l in ls:
        r=l.rstrip()
        if r and r[-1] in "│┐┘┤":
            d=target-w(r)
            mo=re.search(r"( +)([│┐┘┤])$",r)
            if d>0: r=r[:mo.start(1)]+mo.group(1)+" "*d+mo.group(2) if mo else r+" "*d
            elif d<0 and mo and len(mo.group(1))>=-d: r=r[:mo.end(1)+d]+mo.group(2)
        out.append(r)
    return "\n".join(out)
if __name__=="__main__":
    p="总结分析.md"; s=open(p,encoding="utf-8").read()
    blks=re.findall(r"```\n(.*?)```",s,re.S)
    s=s.replace(blks[0],fix(blks[0].rstrip("\n"))+"\n")
    open(p,"w",encoding="utf-8").write(s)
    for l in fix(blks[0].rstrip("\n")).split("\n"): print(f"{w(l):3d} |{l}")
