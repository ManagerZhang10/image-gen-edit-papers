import json,urllib.request,time,sys
pre=json.load(open("_work/2026/pre.json",encoding="utf-8"))
ids=[p["id"] for p in pre]

# --- Semantic Scholar batch ---
ss={}
for i in range(0,len(ids),100):
    ch=ids[i:i+100]
    body=json.dumps({"ids":[f"ARXIV:{x}" for x in ch]}).encode()
    u="https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,influentialCitationCount,title"
    for att in range(6):
        try:
            r=urllib.request.Request(u,data=body,headers={"Content-Type":"application/json"})
            d=json.loads(urllib.request.urlopen(r,timeout=90).read())
            for aid,rec in zip(ch,d):
                if rec: ss[aid]={"cit":rec.get("citationCount",0),"inf":rec.get("influentialCitationCount",0)}
            print(f"SS {i+len(ch)}/{len(ids)} ok={len(ss)}",flush=True); break
        except Exception as e:
            if att==5: print("SS fail",i,e,flush=True)
            else: time.sleep(12*(att+1))
    time.sleep(4)
json.dump(ss,open("_work/2026/ss.json","w",encoding="utf-8"))

# --- HF papers ---
hf={}
for n,aid in enumerate(ids):
    try:
        d=json.loads(urllib.request.urlopen(
            f"https://huggingface.co/api/papers/{aid}",timeout=25).read())
        hf[aid]={"up":d.get("upvotes",0),"nrepo":len(d.get("models",[]) or [])}
    except Exception: pass
    if n%50==0: print(f"HF {n}/{len(ids)} 命中={len(hf)}",flush=True)
    time.sleep(0.35)
json.dump(hf,open("_work/2026/hf.json","w",encoding="utf-8"))
print("SS",len(ss),"HF",len(hf))
