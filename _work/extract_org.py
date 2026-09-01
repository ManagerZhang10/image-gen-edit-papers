#!/usr/bin/env python3
"""从 PDF 首页作者块抽机构 + venue 线索 → _work/org_cache.json。

事实来源是 _work/txt_<id>.txt 的开头（论文首页），不是模型记忆。
OpenAlex 对 arXiv 预印本几乎没有机构字段（182 篇里只有 1 篇），且已知会误配，
所以机构只认 PDF 首页。抽不出来就写 null，由 README 标「未核」。
只用标准库。
"""
import json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = f"{ROOT}/_work/org_cache.json"

for envp in ("/Users/yuzhang/ZhangYu/.env",
             "/Users/yuzhang/ZhangYu/self_learning/BaseModel/.env"):
    if os.path.exists(envp):
        cfg = dict(l.split("=", 1) for l in open(envp) if "=" in l and not l.startswith("#"))
        cfg = {k.strip(): v.strip() for k, v in cfg.items()}
        break
else:
    sys.exit("找不到 .env")

KEY, BASE = cfg["DEEPSEEK_API_KEY"], cfg["DEEPSEEK_BASE_URL"]
MODEL = cfg.get("DEEPSEEK_MODEL") or cfg["DEEPSEEK_V4_PRO_MODEL"]

SYS = """你从论文首页的机器抽取文本里提取元数据。只依据给定文本，不使用任何背景知识。

输出严格的 JSON，不要 markdown 代码块，不要解释：
{"orgs_en": ["..."], "orgs_cn": ["..."], "venue_hint": "...", "confidence": "high"}

规则：
- orgs_en：作者块里出现的机构英文原名，去重，按首次出现顺序，最多 5 个。
  只要作者所属单位，不要邮箱域名、不要基金资助方、不要论文里引用的其他机构。
- orgs_cn：与 orgs_en 一一对应的中文常用名。大学用中文校名（Stanford University→斯坦福大学）；
  公司实验室用中文惯用名（Alibaba Group→阿里巴巴、Tencent AI Lab→腾讯 AI Lab、
  Microsoft Research Asia→微软亚洲研究院、ByteDance Seed→字节跳动 Seed）。
  没有公认中文名的保留英文原名。
- venue_hint：文本开头若写明发表信息（如 "CVPR 2024"、"Preprint. Under review."、
  "Accepted to NeurIPS 2025"、期刊名与卷号），原样摘出来；没有就写 null。
- confidence：作者块清晰可辨写 "high"；抽取文本残缺、机构靠猜写 "low"。
- 任何一项抽不出来就给空数组或 null。禁止编造。"""


def call(text, tries=4):
    body = json.dumps({"model": MODEL, "max_tokens": 1200, "temperature": 0,
                       "messages": [{"role": "system", "content": SYS},
                                    {"role": "user", "content": text}]}).encode()
    req = urllib.request.Request(f"{BASE}/chat/completions", data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    for i in range(tries):
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=300).read())
            c = (r["choices"][0]["message"].get("content") or "").strip()
            c = re.sub(r"^```(?:json)?|```$", "", c, flags=re.M).strip()
            return json.loads(c)
        except Exception as e:
            if i == tries - 1:
                return {"error": f"{type(e).__name__}: {e}"}
            time.sleep(10 * (i + 1))


def txt_for(p):
    for k in (p.get("arxiv_id"), p["dir"]):
        if k and os.path.exists(f"{ROOT}/_work/txt_{k}.txt"):
            return f"{ROOT}/_work/txt_{k}.txt"
    return None


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    todo = [p for p in ps if p["dir"] not in cache or "error" in (cache.get(p["dir"]) or {})]
    todo = [(p, txt_for(p)) for p in todo]
    skip = [p["dir"] for p, t in todo if not t]
    todo = [(p, t) for p, t in todo if t]
    print(f"待抽 {len(todo)} 篇；无抽取文本、跳过 {len(skip)} 项: {skip}")

    def work(item):
        p, t = item
        head = open(t, encoding="utf-8", errors="replace").read(4500)
        return p["dir"], call(head)

    done = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for d, res in ex.map(work, todo):
            cache[d] = res
            done += 1
            if done % 20 == 0 or done == len(todo):
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                print(f"  {done}/{len(todo)}")
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    ok = sum(1 for v in cache.values() if v.get("orgs_cn"))
    low = sum(1 for v in cache.values() if v.get("confidence") == "low")
    err = [k for k, v in cache.items() if "error" in v]
    print(f"完成：{ok} 篇抽到机构，{low} 篇标 low，{len(err)} 篇失败 {err[:6]}")


if __name__ == "__main__":
    main()
