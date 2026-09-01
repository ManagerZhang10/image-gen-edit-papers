#!/usr/bin/env python3
"""HF Papers 双通道候选池：关键词检索 + 逐月 daily papers。只用标准库。"""
import json, os, time, urllib.request, urllib.parse

# OpenAlex / Semantic Scholar 的 polite pool 要一个联系邮箱。
# 本仓库是公开的，不把邮箱写死在代码里——从环境变量读，没设就不带 mailto
# （不带也能用，只是走匿名池、限流更严）。
#     export PAPER_CONTACT_MAIL=you@example.com
MAIL = os.environ.get("PAPER_CONTACT_MAIL", "")
UA = {"User-Agent": "img-gen-papers/1.0" + (f" (mailto:{MAIL})" if MAIL else "")}
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)

QUERIES = [
 "text-to-image generation", "diffusion transformer image synthesis", "rectified flow text-to-image",
 "autoregressive image generation", "visual tokenizer image generation", "masked image generation",
 "unified multimodal understanding and generation", "image generation reinforcement learning",
 "diffusion distillation few-step image", "image generation benchmark evaluation",
 "scaling text-to-image diffusion", "photorealistic image synthesis foundation model",
 "image generation technical report", "flow matching image generation",
 "text rendering image generation", "image generation reward model human preference",
 "continuous tokenizer latent diffusion", "image generation world knowledge reasoning",
 "high resolution image generation efficient", "image generation data curation training recipe",
 "discrete diffusion image generation", "representation alignment diffusion training",
 "guidance sampling diffusion image quality", "compositional text-to-image",
 "open-source image generation model weights", "native multimodal image generation LLM",
]

def get(u, t=90):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()

pool = {}
def add(p, src):
    pid = p.get("id")
    if not pid: return
    r = pool.setdefault(pid, {"id": pid, "title": " ".join(p["title"].split()),
        "published": p.get("publishedAt", "")[:10], "upvotes": p.get("upvotes", 0),
        "stars": p.get("githubStars"), "kw": p.get("ai_keywords") or [], "src": []})
    if src not in r["src"]: r["src"].append(src)
    r["upvotes"] = max(r["upvotes"] or 0, p.get("upvotes") or 0)

for q in QUERIES:
    try:
        d = json.loads(get("https://huggingface.co/api/papers/search?q=" + urllib.parse.quote(q)))
        for it in d: add(it["paper"], "q:" + q[:18])
        print(f"[q] {q[:40]:40s} {len(d):4d}  pool={len(pool)}")
    except Exception as e:
        print(f"[q FAIL] {q}: {e}")
    time.sleep(1)

months = [f"{y}-{m:02d}" for y in (2025, 2026) for m in range(1, 13)]
months = [m for m in months if m <= "2026-08"]
for mo in months:
    for day in ("05", "12", "19", "26"):
        try:
            d = json.loads(get(f"https://huggingface.co/api/daily_papers?date={mo}-{day}&limit=100"))
            for it in d: add(it["paper"], "daily:" + mo)
        except Exception as e:
            print(f"[d FAIL] {mo}-{day}: {e}")
        time.sleep(0.6)
    print(f"[daily] {mo} pool={len(pool)}")

json.dump(sorted(pool.values(), key=lambda r: r["published"]),
          open(f"{W}/hf_pool.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("TOTAL", len(pool))
