#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""下载 arXiv 论文 PDF -> 抽取正文 -> 调 DeepSeek v4 Pro 生成深读笔记 -> 校验 -> 落盘"""
import json, os, re, sys, time, urllib.request, urllib.error

ROOT = "/Users/yuzhang/ZhangYu/image_edit_paper"
WORK = os.path.join(ROOT, "_work")
PROMPT = open(os.path.join(ROOT, "prompt.md"), encoding="utf-8").read()

def load_env(p):
    e = {}
    for ln in open(p, encoding="utf-8"):
        ln = ln.strip()
        if ln and not ln.startswith("#") and "=" in ln:
            k, v = ln.split("=", 1); e[k] = v.strip().strip('"').strip("'")
    return e
ENV = load_env("/Users/yuzhang/ZhangYu/BaseModel/.env")

HEADS = ["## 1. 30 秒定位","## 2. 为什么这篇论文会出现","## 3. 读懂前需要的最小概念",
         "## 4. 方法全景：先看数据流","## 5. 核心公式与直觉","## 6. 训练到底怎么跑",
         "## 7. 推理到底怎么跑","## 8. 实验和消融到底证明了什么","## 9. 与前作怎么选",
         "## 10. 工程判断：可行性、风险与上限","## 11. 放回研究脉络并收束"]

def log(*a): print(*a, flush=True)

def fetch_pdf(aid, dst):
    if os.path.exists(dst) and os.path.getsize(dst) > 50000: return True
    for url in (f"https://arxiv.org/pdf/{aid}", f"https://arxiv.org/pdf/{aid}v1"):
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=180) as r, open(dst, "wb") as f:
                    f.write(r.read())
                if os.path.getsize(dst) > 50000: return True
            except Exception as ex:
                log(f"    pdf try {url} #{attempt}: {ex}"); time.sleep(4 + attempt * 6)
    return False

def extract(pdf, dst):
    if os.path.exists(dst) and os.path.getsize(dst) > 8000:
        return open(dst, encoding="utf-8").read()
    from pypdf import PdfReader
    rd = PdfReader(pdf)
    pages = []
    for p in rd.pages:
        try: pages.append(p.extract_text() or "")
        except Exception: pages.append("")
    t = "\n".join(pages)
    t = re.sub(r"[\ud800-\udfff]", "", t)   # 去掉 PDF 抽取产生的孤立代理项
    t = re.sub(r"[ \t]{3,}", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    if len(t) > 130000:  # 长文先砍参考文献块
        m = list(re.finditer(r"\n\s*(References|REFERENCES|Bibliography)\s*\n", t))
        if m:
            s = m[0].end()
            nxt = re.search(r"\n\s*(A(ppendix)?\.?\s|Appendix|Supplementary|APPENDIX)", t[s:])
            e = s + nxt.start() if nxt else min(len(t), s + 60000)
            t = t[:s] + "\n[参考文献块已省略]\n" + t[e:]
    open(dst, "w", encoding="utf-8").write(t)
    return t

def deepseek(sysmsg, usermsg, max_tokens=32000, temp=0.35):
    body = json.dumps({"model": ENV.get("DEEPSEEK_V4_PRO_MODEL", "deepseek-v4-pro"),
        "messages": [{"role": "system", "content": sysmsg}, {"role": "user", "content": usermsg}],
        "max_tokens": max_tokens, "temperature": temp}).encode()
    req = urllib.request.Request(ENV["DEEPSEEK_BASE_URL"].rstrip("/") + "/chat/completions",
        data=body, headers={"Authorization": "Bearer " + ENV["DEEPSEEK_API_KEY"],
                            "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=1800) as r:
        d = json.loads(r.read())
    return d["choices"][0]["message"]["content"], d.get("usage", {})

def cn_len(s):
    return len(re.findall(r"[一-鿿]", s))

def validate_struct(md):
    errs = []
    if not md.lstrip().startswith("# 大白话深读"): errs.append("缺少 H1 大白话深读")
    for h in HEADS:
        if h not in md: errs.append("缺章节 " + h)
    if "<!-- COMPLETE -->" not in md[-400:]: errs.append("结尾缺 COMPLETE 标记")
    return errs, cn_len(md)

def validate(md):
    errs, n = validate_struct(md)
    if n < 6300: errs.append(f"中文字符过少 {n}，需 6500~8500")
    if n > 12000: errs.append(f"中文字符过多 {n}")
    return errs, n

def run(aid, short, date, title):
    folder = os.path.join(ROOT, f"{date[:7].replace('/','-')}_{short}")
    os.makedirs(folder, exist_ok=True)
    pdf = os.path.join(folder, "paper.pdf")
    txt = os.path.join(WORK, f"txt_{aid}.txt")
    out = os.path.join(folder, "解读.md")
    lock = os.path.join(folder, ".LOCK")
    try:
        fd_l = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY); os.close(fd_l)
    except FileExistsError:
        if time.time() - os.path.getmtime(lock) < 2400:
            log(f"[LOCKED] {short} 另一进程正在处理"); return 0
        os.utime(lock, None)
    prior = None
    if os.path.exists(out):
        cur = open(out, encoding="utf-8").read()
        errs, n = validate(cur)
        if not errs: log(f"[SKIP] {short} 已完成 ({n}字)"); return 0
        serrs, n = validate_struct(cur)
        if not serrs and n >= 4200:
            prior = (n, cur)   # 结构完整只是偏短：走扩写，不整篇重来
    if not fetch_pdf(aid, pdf): log(f"[FAIL] {short} PDF 下载失败"); return 1
    try: body = extract(pdf, txt)
    except Exception as ex: log(f"[FAIL] {short} 抽取失败 {ex}"); return 1
    if len(body) < 6000: log(f"[FAIL] {short} 正文过短 {len(body)}"); return 1
    body = body[:160000]

    user = (f"论文简称：{short}\n论文标题：{title}\narXiv：{aid}（{date}）\n\n"
            f"以下是该论文的完整正文（PDF 抽取，可能含少量排版噪声，公式符号可能有丢失，"
            f"遇到明显抽取损坏的地方按论文语境判断，不要编造）：\n\n<paper>\n{body}\n</paper>\n\n"
            f"请严格按系统提示的规范，输出《{short}》的中文深读笔记。注意：正文中文字符必须落在 6500~8500 之间，不要写得过短；每一节都要写足规范给出的字数，第 8 节的证据表至少 4 行。")
    def save(md, n, note, att):
        open(out, "w", encoding="utf-8").write(md + "\n")
        json.dump({"arxiv_id": aid, "short": short, "date": date, "title": title,
                   "url": f"https://arxiv.org/abs/{aid}", "cn_chars": n,
                   "note": note, "attempts": att},
                  open(os.path.join(folder, "meta.json"), "w"), ensure_ascii=False, indent=2)

    def clean(md):
        md = md.strip()
        if md.startswith("```"):
            md = re.sub(r"^```[a-z]*\n", "", md); md = re.sub(r"\n```$", "", md)
        return md.strip()

    best = prior  # (n, md) 结构完整里最长的；已有短稿直接作为起点
    last = None
    if prior:
        try:
            n0 = prior[0]
            exp_sys = (PROMPT + "\n\n【本轮任务是扩写，不是重写】\n"
                "用户会给你一份已经写好的笔记草稿。请保持它的结构、结论和全部事实不变，"
                "只把内容写得更充分：补充论文中已有但草稿没展开的实现细节、超参数、"
                "消融设置、数据规模、失败模式和证据锚点（§/Table/Figure/Equation）。"
                "不得引入草稿和论文中都没有的新事实。"
                f"扩写后正文中文字符需达到 6500~8500（当前 {n0}）。"
                "输出完整的 11 节 Markdown 全文，结尾单独一行 <!-- COMPLETE -->。")
            md2, _ = deepseek(exp_sys, user + "\n\n以下是需要扩写的草稿：\n\n<draft>\n" + prior[1] + "\n</draft>", temp=0.4)
            md2 = clean(md2)
            e2, n2 = validate(md2); s2, _ = validate_struct(md2)
            if not e2:
                save(md2, n2, f"扩写达标（原稿 {n0} 字）", 1)
                log(f"[OK] {short} {n2}字 (扩写既有稿, 原{n0})"); return 0
            if not s2 and n2 > best[0]: best = (n2, md2)
        except Exception as ex:
            log(f"    [{short}] 既有稿扩写异常: {ex}")
    for att in range(3):
        try:
            sysmsg = PROMPT
            if att > 0 and last:
                sysmsg += ("\n\n【上一次输出未通过校验，问题如下，请修正后重新完整输出】\n"
                           + "\n".join("- " + e for e in last)
                           + "\n必须输出全部 11 个二级标题，正文 6500~8500 中文字符，"
                             "结尾单独一行 <!-- COMPLETE -->。")
            md, usage = deepseek(sysmsg, user, temp=0.35 + 0.1 * att)
        except Exception as ex:
            log(f"    [{short}] API 第{att+1}次异常: {ex}"); time.sleep(15 + 20 * att); continue
        md = clean(md)
        errs, n = validate(md)
        if not errs:
            save(md, n, "一次通过", att + 1)
            log(f"[OK] {short} {n}字 (第{att+1}次)")
            return 0
        serrs, n = validate_struct(md)
        if not serrs:                       # 结构完整，只是偏短 -> 定向扩写，不整篇重写
            if best is None or n > best[0]: best = (n, md)
            if n >= 4200:
                try:
                    exp_sys = (PROMPT + "\n\n【本轮任务是扩写，不是重写】\n"
                        "用户会给你一份已经写好的笔记草稿。请保持它的结构、结论和全部事实不变，"
                        "只把内容写得更充分：补充论文中已有但草稿没展开的实现细节、超参数、"
                        "消融设置、数据规模、失败模式和证据锚点（§/Table/Figure/Equation）。"
                        "不得引入草稿和论文中都没有的新事实。"
                        f"扩写后正文中文字符需达到 6500~8500（当前 {n}）。"
                        "输出完整的 11 节 Markdown 全文，结尾单独一行 <!-- COMPLETE -->。")
                    exp_user = (user + "\n\n以下是需要扩写的草稿：\n\n<draft>\n" + md + "\n</draft>")
                    md2, _ = deepseek(exp_sys, exp_user, temp=0.4)
                    md2 = clean(md2)
                    e2, n2 = validate(md2)
                    s2, _ = validate_struct(md2)
                    if not e2:
                        save(md2, n2, f"扩写达标（初稿 {n} 字）", att + 1)
                        log(f"[OK] {short} {n2}字 (扩写, 初稿{n})")
                        return 0
                    if not s2 and n2 > best[0]: best = (n2, md2)
                except Exception as ex:
                    log(f"    [{short}] 扩写异常: {ex}")
        last = errs
        log(f"    [{short}] 第{att+1}次未过: {errs[:2]}")
    if best and best[0] >= 4500:            # 结构完整但未达字数下限：保留最长稿并标注
        save(best[1], best[0], f"结构完整但字数 {best[0]} 低于 6500，已保留最长稿", 3)
        log(f"[OK-SHORT] {short} {best[0]}字 （未达 6500，已标注）")
        return 0
    log(f"[FAIL] {short} 3 次均未通过：{last}")
    return 1

if __name__ == "__main__":
    line = sys.argv[1]
    aid, short, date, title = line.split("|", 3)
    short = short.strip(); date = date.strip()
    try:
        rc = run(aid.strip(), short, date, title.strip())
    finally:
        lk = os.path.join(ROOT, f"{date[:7].replace('/','-')}_{short}", ".LOCK")
        if os.path.exists(lk):
            try: os.remove(lk)
            except OSError: pass
    sys.exit(rc)
