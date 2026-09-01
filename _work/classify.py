#!/usr/bin/env python3
"""给 187 篇打 task / type / line → _work/class_cache.json。

依据是每篇 解读.md 的第 1 节「30 秒定位」+ 标题——都是本库依据 PDF 产出的文字，
不是模型对这篇论文的记忆。line 只允许从 INDEX.md 已有的 15 条脉络里选，
不新造分类；160 篇已有脉络的直接沿用，只有 27 篇需要判定。
"""
import json, os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = f"{ROOT}/_work/class_cache.json"
LINES = json.load(open(f"{ROOT}/_work/line_map.json", encoding="utf-8"))
LINE_SET = sorted(set(LINES.values()))

for envp in ("/Users/yuzhang/ZhangYu/.env",
             "/Users/yuzhang/ZhangYu/self_learning/BaseModel/.env"):
    if os.path.exists(envp):
        cfg = {k.strip(): v.strip() for k, v in
               (l.split("=", 1) for l in open(envp) if "=" in l and not l.startswith("#"))}
        break
KEY, BASE = cfg["DEEPSEEK_API_KEY"], cfg["DEEPSEEK_BASE_URL"]
MODEL = cfg.get("DEEPSEEK_MODEL") or cfg["DEEPSEEK_V4_PRO_MODEL"]

SYS = """你给一篇图像领域的论文打三个标签。只依据给定的标题和笔记摘录，不使用背景知识。

输出严格 JSON，无 markdown 代码块，无解释：
{"task": ["编辑"], "type": "方法", "line": "...", "reason": "不超过 25 字"}

task —— 这篇论文的产出任务，可多选，至少一项：
  "生成" = 从文本/噪声造出新图（含生成骨干、一步生成、自回归生成、评测生成质量）
  "编辑" = 输入已有图像并改动它（含指令编辑、反演、局部修补、拖拽、参考图注入）
  统一模型同时做两件事的，给 ["生成","编辑"]。判断依据是论文自己声明的任务，
  不要因为方法建立在生成骨干上就自动加"生成"。

type —— 主要贡献类型，单选，按以下优先级取第一个命中的：
  "综述" = 综述、系统性分析或诊断性研究，不提新方法
  "基准" = 主要贡献是 benchmark、评测协议或评价指标
  "数据集" = 主要贡献是训练数据集或数据构造管线
  "奖励与 RL" = 主要贡献是奖励模型、偏好对齐或强化学习后训练
  "模型" = 发布一个模型/系统或厂商技术报告
  "方法" = 提出一个算法或技术

line —— 技术脉络，必须从下面这个固定清单里原样挑一条，不要改写、不要新造：
%s""" % "\n".join(f"  - {l}" for l in LINE_SET)


def call(prompt, tries=4):
    body = json.dumps({"model": MODEL, "max_tokens": 700, "temperature": 0,
                       "messages": [{"role": "system", "content": SYS},
                                    {"role": "user", "content": prompt}]}).encode()
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
            time.sleep(8 * (i + 1))


def sec1(d):
    p = f"{ROOT}/papers/{d}/解读.md"
    if not os.path.exists(p):
        return ""
    body = open(p, encoding="utf-8").read()
    m = re.search(r"^## 1\..*?(?=^## 2\.)", body, re.S | re.M)
    return (m.group(0) if m else body)[:1400]


def main():
    ps = json.load(open(f"{ROOT}/scripts/papers.json", encoding="utf-8"))
    cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
    todo = [p for p in ps if p["dir"] not in cache or "error" in (cache.get(p["dir"]) or {})]
    print(f"待分类 {len(todo)} / {len(ps)}")

    def work(p):
        known = LINES.get(p["dir"])
        hint = (f"\n\n【本库已把这篇归入脉络】{known}\n（line 请沿用这一条，除非摘录明显矛盾）"
                if known else "\n\n【本库尚未给这篇归脉络】请从清单里挑最贴的一条。")
        prompt = (f"标题：{p['title']}\n简称：{p['short']}\n首次公开：{p.get('date')}"
                  f"{hint}\n\n【笔记第 1 节摘录】\n{sec1(p['dir']) or '（这篇没有解读正文，只有官方资料记录）'}")
        return p["dir"], call(prompt)

    done = 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for d, res in ex.map(work, todo):
            cache[d] = res; done += 1
            if done % 20 == 0 or done == len(todo):
                json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                print(f"  {done}/{len(todo)}", flush=True)
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    bad = [k for k, v in cache.items() if "error" in v or v.get("line") not in LINE_SET]
    print(f"完成 {len(cache)}；异常 {len(bad)}: {bad[:8]}")


if __name__ == "__main__":
    main()
