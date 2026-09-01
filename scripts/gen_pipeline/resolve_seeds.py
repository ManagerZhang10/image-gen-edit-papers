#!/usr/bin/env python3
"""必查种子清单：先在 HF 池里按标题找 ID，找不到的走 arXiv API 标题检索（节流 3 秒）。"""
import json, os, re, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_work")
os.makedirs(W, exist_ok=True)
# OpenAlex / Semantic Scholar 的 polite pool 要一个联系邮箱。
# 本仓库是公开的，不把邮箱写死在代码里——从环境变量读，没设就不带 mailto
# （不带也能用，只是走匿名池、限流更严）。
#     export PAPER_CONTACT_MAIL=you@example.com
MAIL = os.environ.get("PAPER_CONTACT_MAIL", "")
UA = {"User-Agent": "img-gen-papers/1.0" + (f" (mailto:{MAIL})" if MAIL else "")}
NS = {"a": "http://www.w3.org/2005/Atom"}

SEEDS = [
 "Muse: Text-To-Image Generation via Masked Generative Transformers",
 "Consistency Models",
 "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis",
 "Human Preference Score v2: A Solid Benchmark for Evaluating Human Preferences of Text-to-Image Synthesis",
 "T2I-CompBench: A Comprehensive Benchmark for Open-world Compositional Text-to-image Generation",
 "PixArt-alpha: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis",
 "Emu: Enhancing Image Generation Models Using Photogenic Needles in a Haystack",
 "Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference",
 "GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment",
 "Adversarial Diffusion Distillation",
 "One-step Diffusion with Distribution Matching Distillation",
 "Exploring Flow and Diffusion-based Generative Models with Scalable Interpolant Transformers",
 "ELLA: Equip Diffusion Models with LLM for Enhanced Semantic Alignment",
 "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis",
 "Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction",
 "Hunyuan-DiT: A Powerful Multi-Resolution Diffusion Transformer with Fine-Grained Chinese Understanding",
 "Chameleon: Mixed-Modal Early-Fusion Foundation Models",
 "Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation",
 "Autoregressive Image Generation without Vector Quantization",
 "Improved Distribution Matching Distillation for Fast Image Synthesis",
 "Imagen 3",
 "Show-o: One Single Transformer to Unify Multimodal Understanding and Generation",
 "Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model",
 "Emu3: Next-Token Prediction is All You Need",
 "OmniGen: Unified Image Generation",
 "Representation Alignment for Generation: Training Diffusion Transformers Is Easier Than You Think",
 "SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformers",
 "Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation",
 "Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis",
 "Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling",
 "Fluid: Scaling Autoregressive Text-to-image Generative Models with Continuous Tokens",
 "Lumina-Image 2.0: A Unified and Efficient Image Generative Framework",
 "WISE: A World Knowledge-Informed Semantic Evaluation for Text-to-Image Generation",
 "Flow-GRPO: Training Flow Matching Models via Online RL",
 "T2I-R1: Reinforcing Image Generation with Collaborative Semantic-level and Token-level CoT",
 "Emerging Properties in Unified Multimodal Pretraining",
 "Seedream 3.0 Technical Report",
 "HiDream-I1: A High-Efficient Image Generative Foundation Model with Sparse Diffusion Transformer",
 "Qwen-Image Technical Report",
 "HunyuanImage 3.0 Technical Report",
 "Seedream 4.0: Toward Next-generation Multimodal Image Generation",
 "NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale",
 "Emu3.5: Native Multimodal Models are World Learners",
 "FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space",
 "Playground v2.5: Three Insights towards Enhancing Aesthetic Quality in Text-to-Image Generation",
 "Diffusion Transformers with Representation Autoencoders",
 "Inference-time scaling for diffusion models beyond scaling denoising steps",
 "SANA 1.5: Efficient Scaling of Training-Time and Inference-Time Compute in Linear Diffusion Transformer",
 "Transfer between Modalities with MetaQueries",
 "BLIP3-o: A Family of Fully Open Unified Multimodal Models",
 "OmniGen2: Exploration to Advanced Multimodal Generation",
 "Show-o2: Improved Native Unified Multimodal Models",
 "Scalable Diffusion Models with Transformers",
 "Simpler Diffusion: 1.5 FID on ImageNet512 with pixel-space diffusion",
 "Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis",
 "Lumina-Next: Making Lumina-T2X Stronger and Faster with Next-DiT",
 "Star: Scale-wise Text-to-image generation via Auto-Regressive representations",
 "Randomized Autoregressive Visual Generation",
 "Deeply Supervised Flow-Based Generative Models",
 "Diffusion Beats Autoregressive in Data-Constrained Settings",
 "Mean Flows for One-step Generative Modeling",
 "Highly Compressed Tokenizer Can Generate Without Training",
]

def norm(s): return re.sub(r"[^a-z0-9]+", "", (s or "").lower())

pool = json.load(open(f"{W}/hf_pool.json", encoding="utf-8"))
byname = {}
for r in pool:
    byname[norm(r["title"])] = r

def arxiv_title(q):
    u = ("http://export.arxiv.org/api/query?search_query=ti:%22" +
         urllib.parse.quote(re.sub(r"[:\-]", " ", q)) + "%22&max_results=5")
    x = ET.fromstring(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read())
    out = []
    for e in x.findall("a:entry", NS):
        out.append({"id": e.find("a:id", NS).text.rsplit("/", 1)[-1].split("v")[0],
                    "title": " ".join(e.find("a:title", NS).text.split()),
                    "published": e.find("a:published", NS).text[:10]})
    return out

res = []
for s in SEEDS:
    n = norm(s)
    hitp = byname.get(n)
    if not hitp:
        for k, v in byname.items():
            if k.startswith(n[:45]) or n.startswith(k[:45]):
                hitp = v; break
    if hitp:
        res.append({"seed": s, "id": hitp["id"], "title": hitp["title"],
                    "published": hitp["published"], "upvotes": hitp["upvotes"],
                    "kw": hitp.get("kw") or [], "src": "hf"})
        print(f"[hf ] {hitp['id']}  {s[:60]}", flush=True)
        continue
    try:
        cands = arxiv_title(s)
    except Exception as e:
        print(f"[ERR] {s[:60]}: {e}", flush=True); res.append({"seed": s, "id": None}); time.sleep(3); continue
    pick = None
    for c in cands:
        if norm(c["title"]) == n or norm(c["title"]).startswith(n[:40]) or n.startswith(norm(c["title"])[:40]):
            pick = c; break
    if pick:
        res.append({"seed": s, "id": pick["id"], "title": pick["title"],
                    "published": pick["published"], "upvotes": 0, "kw": [], "src": "arxiv"})
        print(f"[ax ] {pick['id']}  {s[:60]}", flush=True)
    else:
        res.append({"seed": s, "id": None, "cands": cands[:3]})
        print(f"[MISS] {s[:60]}  ({len(cands)} 个不匹配)", flush=True)
    time.sleep(3)

json.dump(res, open(f"{W}/seeds_resolved.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("resolved", sum(1 for r in res if r.get("id")), "/", len(res))
