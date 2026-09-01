#!/usr/bin/env python3
"""org 抽取的第二轮：只处理第一轮失败或抽不到机构的 17 项。

第一轮暴露两个问题：①模型偶发返回非 JSON（10 篇）；②厂商技术报告只写团队名
（"Qwen Team" + qwen.ai）而不写法人机构，模型按「只要作者所属单位」的字面
规则弃权（7 篇）。这一轮放宽到「团队名 + 可从品牌/域名确定的公司」也算，
并加大文本窗口到 7000 字、放宽 JSON 解析。
"""
import json, os, re, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = f"{ROOT}/_work/org_cache.json"
for envp in ("/Users/yuzhang/ZhangYu/.env",
             "/Users/yuzhang/ZhangYu/self_learning/BaseModel/.env"):
    if os.path.exists(envp):
        cfg = {k.strip(): v.strip() for k, v in
               (l.split("=", 1) for l in open(envp) if "=" in l and not l.startswith("#"))}
        break
KEY, BASE = cfg["DEEPSEEK_API_KEY"], cfg["DEEPSEEK_BASE_URL"]
MODEL = cfg.get("DEEPSEEK_MODEL") or cfg["DEEPSEEK_V4_PRO_MODEL"]

SYS = """你从论文首页的机器抽取文本里提取机构与发表信息。只依据给定文本，不使用背景知识。

只输出一个 JSON 对象，不要 markdown 代码块，不要任何解释文字：
{"orgs_en": ["..."], "orgs_cn": ["..."], "venue_hint": "...", "confidence": "high"}

- orgs_en / orgs_cn：作者所属机构，去重，按首次出现顺序，最多 5 个，两个数组一一对应。
- 厂商技术报告常常只写团队名而不写法人机构。这种情况也要给出机构：
  团队名 + 文本里的官网域名或模型仓库路径已经足以确定公司时，就写出来。
  例：文本只有 "Qwen Team" 与 qwen.ai / QwenLM → orgs_en ["Qwen Team, Alibaba Group"]，
  orgs_cn ["阿里巴巴通义千问团队"]。同理 Seed Team + ByteDance → 字节跳动 Seed。
  确实无法确定公司的，就只写团队名本身。
- orgs_cn 用中文常用名：大学写中文校名，公司实验室写中文惯用名，
  没有公认中文名的保留英文原名。
- venue_hint：文本开头写明的发表信息原样摘出（"CVPR 2024"、"Preprint. Under review."、
  期刊名与卷号等）；没有就写 null。
- confidence：作者块清晰可辨写 "high"；靠域名/品牌推断出公司写 "medium"；
  文本残缺、机构靠猜写 "low"。
- 抽不出来给空数组或 null。禁止编造。"""


def call(text, tries=5):
    body = json.dumps({"model": MODEL, "max_tokens": 2000, "temperature": 0,
                       "messages": [{"role": "system", "content": SYS},
                                    {"role": "user", "content": text}]}).encode()
    req = urllib.request.Request(f"{BASE}/chat/completions", data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {KEY}"})
    last = None
    for i in range(tries):
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=300).read())
            c = (r["choices"][0]["message"].get("content") or "").strip()
            c = re.sub(r"^```(?:json)?|```$", "", c, flags=re.M).strip()
            try:
                return json.loads(c)
            except json.JSONDecodeError:
                m = re.search(r"\{.*\}", c, re.S)     # 正文里夹了解释时兜一下
                if m:
                    return json.loads(m.group(0))
                last = f"非 JSON 返回: {c[:120]!r}"
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        time.sleep(8 * (i + 1))
    return {"error": str(last)}


def txt_for(p):
    for k in (p.get("arxiv_id"), p["dir"]):
        if k and os.path.exists(f"{ROOT}/_work/txt_{k}.txt"):
            return f"{ROOT}/_work/txt_{k}.txt"
    return None


ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
cache = json.load(open(CACHE, encoding="utf-8"))
todo = [p for p in ps if p["dir"] in cache
        and ("error" in cache[p["dir"]] or not cache[p["dir"]].get("orgs_cn"))]
print(f"第二轮待处理 {len(todo)} 项")

def work(p):
    t = txt_for(p)
    return p["dir"], call(open(t, encoding="utf-8", errors="replace").read(7000)) if t else {"error": "无文本"}

with ThreadPoolExecutor(max_workers=4) as ex:
    for d, res in ex.map(work, todo):
        cache[d] = res
        print(f"  {d:34s} -> {res.get('orgs_cn')} [{res.get('confidence')}] {res.get('error','')[:50]}")
json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
ok = sum(1 for v in cache.values() if v.get("orgs_cn"))
print(f"\n累计有机构 {ok}/{len(cache)}；仍失败 {[k for k,v in cache.items() if 'error' in v]}")
