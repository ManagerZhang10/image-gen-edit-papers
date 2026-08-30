import urllib.request,urllib.parse,re,time,json,os,sys,html

RANGE="submittedDate:[202601010000 TO 202609010000]"
QUERIES=[
 f'abs:"image editing" AND {RANGE}',
 f'ti:"image editing" AND {RANGE}',
 f'abs:"image edit" AND {RANGE}',
 f'abs:"instruction-based editing" AND {RANGE}',
 f'abs:"instruction-guided" AND cat:cs.CV AND {RANGE}',
 f'abs:"unified multimodal" AND cat:cs.CV AND {RANGE}',
 f'abs:"visual editing" AND {RANGE}',
 f'abs:"image inpainting" AND {RANGE}',
 f'abs:"subject-driven generation" AND {RANGE}',
 f'abs:"identity preservation" AND cat:cs.CV AND {RANGE}',
 f'abs:"reward model" AND abs:"image generation" AND {RANGE}',
 f'abs:"diffusion" AND abs:"inversion" AND cat:cs.CV AND {RANGE}',
 f'abs:"editing benchmark" AND {RANGE}',
 f'abs:"autoregressive image generation" AND {RANGE}',
 f'abs:"image customization" AND {RANGE}',
]
def page(sq,start,n=100):
    u="http://export.arxiv.org/api/query?"+urllib.parse.urlencode(
      {"search_query":sq,"start":start,"max_results":n,
       "sortBy":"submittedDate","sortOrder":"descending"})
    for att in range(5):
        try:
            return urllib.request.urlopen(u,timeout=90).read().decode()
        except Exception as e:
            if att==4: raise
            time.sleep(6*(att+1))

ENT=re.compile(r"<entry>(.*?)</entry>",re.S)
def parse(x):
    out=[]
    for e in ENT.findall(x):
        def g(t):
            mo=re.search(rf"<{t}>(.*?)</{t}>",e,re.S)
            return html.unescape(re.sub(r"\s+"," ",mo.group(1)).strip()) if mo else ""
        aid=re.search(r"arxiv.org/abs/([\d.]+)v(\d+)",e)
        if not aid: continue
        cats=re.findall(r'term="([^"]+)"',e)
        out.append({"id":aid.group(1),"title":g("title"),"date":g("published")[:10],
                    "summary":g("summary"),"cats":cats,
                    "authors":re.findall(r"<name>(.*?)</name>",e)[:6],
                    "comment":g("arxiv:comment")})
    return out

all_={}
for qi,q in enumerate(QUERIES):
    start=0; got=0
    while True:
        x=page(q,start)
        tot=int(re.search(r"totalResults>(\d+)<",x).group(1))
        es=parse(x)
        if not es: break
        for e in es: all_.setdefault(e["id"],e)
        got+=len(es); start+=len(es)
        if start>=min(tot,600): break
        time.sleep(3)
    print(f"[{qi+1}/{len(QUERIES)}] tot={tot:4d} 取={got:4d} 累计唯一={len(all_)}  {q[:55]}",flush=True)

json.dump(list(all_.values()),open("_work/2026/raw.json","w",encoding="utf-8"),ensure_ascii=False)
print("唯一论文",len(all_))
