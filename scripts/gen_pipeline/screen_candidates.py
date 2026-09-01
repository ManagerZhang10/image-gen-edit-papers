#!/usr/bin/env python3
"""从 HF 候选池筛出图像生成相关条目，合并必查种子清单，产出 _work/cand.json。"""
import json, os, re

W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)
pool = json.load(open(f"{W}/hf_pool.json", encoding="utf-8"))

INC = ["text-to-image", "text to image", "image generation", "image synthesis", "t2i",
       "image generative", "visual generation", "visual autoregressive", "image tokenizer",
       "visual tokenizer", "tokenizer", "rectified flow", "flow matching", "diffusion transformer",
       "unified multimodal", "multimodal understanding and generation", "autoregressive image",
       "image model", "image foundation", "diffusion model", "diffusion models", "generative model",
       "photorealistic", "aesthetic", "geneval", "image editing", "native multimodal",
       "text rendering", "typography", "image gen", "imagen", "one-step", "few-step", "distillation"]
EXC_HARD = ["video", "3d ", " 3d", "mesh", "audio", "speech", "music", "point cloud", "motion",
            "avatar", "4d", "robot", "driving", "medical", "protein", "molecul", "world model",
            "scene generation", "depth", "segmentation", "detection", "super-resolution", "restoration"]
IMG_STRONG = ["text-to-image", "image generation", "image synthesis", "t2i ", "visual autoregressive",
              "image generative", "unified multimodal", "image model", "image tokenizer"]

def hit(text, words):
    return [w for w in words if w in text]

cand, dropped = [], 0
for r in pool:
    if r["published"] < "2023-01-01":
        continue
    t = r["title"].lower()
    kw = " ".join(r.get("kw") or []).lower()
    blob = t + " || " + kw
    if not hit(blob, INC):
        dropped += 1; continue
    if hit(t, EXC_HARD) and not hit(t, IMG_STRONG):
        dropped += 1; continue
    cand.append({"id": r["id"], "title": r["title"], "published": r["published"],
                 "upvotes": r["upvotes"], "stars": r.get("stars"), "kw": r.get("kw") or []})

seen = {c["id"] for c in cand}
json.dump(cand, open(f"{W}/cand.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("pool", len(pool), "-> cand", len(cand), "dropped", dropped)
by_year = {}
for c in cand: by_year[c["published"][:4]] = by_year.get(c["published"][:4], 0) + 1
print(sorted(by_year.items()))
