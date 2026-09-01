#!/usr/bin/env python3
"""厂商落地信号：HF Hub 近 30 天下载量 + likes，附 GitHub star。只用标准库。

两种用法：
  python3 scripts/hub_signals.py                # 按 REPOS 逐个查（papers.json 里引用的那些）
  python3 scripts/hub_signals.py --rank         # 按 pipeline_tag 排行，看业界实际在下载什么
"""
import json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, "_work"); os.makedirs(W, exist_ok=True)
# OpenAlex / Semantic Scholar 的 polite pool 要一个联系邮箱。
# 本仓库是公开的，不把邮箱写死在代码里——从环境变量读，没设就不带 mailto
# （不带也能用，只是走匿名池、限流更严）。
#     export PAPER_CONTACT_MAIL=you@example.com
MAIL = os.environ.get("PAPER_CONTACT_MAIL", "")
UA = {"User-Agent": "img-gen-papers/1.0" + (f" (mailto:{MAIL})" if MAIL else "")}

# papers.json 里厂商组用到的 repo，加几个对照
REPOS = [
    "stabilityai/stable-diffusion-xl-base-1.0", "stabilityai/stable-diffusion-3.5-large",
    "Kwai-Kolors/Kolors", "Kwai-Kolors/Kolors-diffusers",
    "black-forest-labs/FLUX.1-dev", "black-forest-labs/FLUX.1-Kontext-dev", "black-forest-labs/FLUX.2-dev",
    "ByteDance-Seed/BAGEL-7B-MoT", "Qwen/Qwen-Image", "lightx2v/Qwen-Image-Lightning",
    "tencent/HunyuanImage-3.0", "tencent/HunyuanImage-3.0-Instruct",
    "Tongyi-MAI/Z-Image", "Tongyi-MAI/Z-Image-Turbo",
    "sensenova/SenseNova-U1.5-8B-MoT", "stepfun-ai/NextStep-1-Large",
    "deepseek-ai/Janus-Pro-7B", "THUDM/CogView4-6B", "meituan-longcat/LongCat-Image",
    "baidu/ERNIE-Image", "krea/Krea-2-Turbo", "ideogram-ai/ideogram-4-fp8",
]
GITHUB = ["Kwai-Kolors/Kolors"]
TAGS = ["text-to-image", "image-to-image", "any-to-any"]


def get(u, t=60):
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read())


def model(repo):
    d = get("https://huggingface.co/api/models/" + repo)
    return {"repo": repo, "downloads_30d": d.get("downloads"), "likes": d.get("likes"),
            "created": (d.get("createdAt") or "")[:10], "pipeline": d.get("pipeline_tag")}


def rank(tag, sort, limit=25):
    return get(f"https://huggingface.co/api/models?pipeline_tag={tag}&sort={sort}&direction=-1&limit={limit}")


def main():
    out = {"checked_at": time.strftime("%Y-%m-%d"), "models": [], "github": [], "rank": {}}
    if "--rank" in sys.argv:
        for tag in TAGS:
            for s in ("downloads", "likes", "trendingScore"):
                try:
                    out["rank"][f"{tag}/{s}"] = [
                        {"repo": r["id"], "downloads_30d": r.get("downloads"), "likes": r.get("likes"),
                         "created": (r.get("createdAt") or "")[:10]} for r in rank(tag, s)]
                    print(f"[rank] {tag}/{s} ok", flush=True)
                except Exception as e:
                    print(f"[rank] {tag}/{s} ERR {type(e).__name__}", flush=True)
                time.sleep(0.5)
    else:
        for r in REPOS:
            try:
                m = model(r); out["models"].append(m)
                print(f"  dl30d={m['downloads_30d']:>9} likes={m['likes']:>6} {m['created']} {r}", flush=True)
            except Exception as e:
                out["models"].append({"repo": r, "error": type(e).__name__})
                print(f"  {'-':>9} {'-':>6} {'':10} {r}  [{type(e).__name__}] 可能是闭源或未发布权重", flush=True)
            time.sleep(0.4)
        for g in GITHUB:
            try:
                d = get("https://api.github.com/repos/" + g)
                out["github"].append({"repo": g, "stars": d.get("stargazers_count"),
                                      "created": (d.get("created_at") or "")[:10]})
                print(f"  github {d.get('stargazers_count')} star  {g}", flush=True)
            except Exception as e:
                print(f"  github ERR {type(e).__name__} {g}", flush=True)
            time.sleep(0.5)
    json.dump(out, open(f"{W}/hub_signals.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("写到 _work/hub_signals.json")


if __name__ == "__main__":
    main()
