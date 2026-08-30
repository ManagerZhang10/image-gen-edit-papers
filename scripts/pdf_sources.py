"""meta.json → PDF 直链。fetch_pdfs.py 和 verify_pdf_links.py 共用这一套规则。

默认规则：有 arXiv ID 就用 arXiv，否则认 CVF Open Access 的 /html/ → /papers/ 变换。
OVERRIDES 里是默认规则会拿错东西的三个例外，每条都注明了为什么。
"""

# 默认规则会取到"能打开但不是本库读的那一份"的条目。
# 每条都用 sha256 对着本地 paper.pdf 验过（2026-08-30）。
OVERRIDES = {
    # arXiv 上 2412.00100 已改题为 "Steering Rectified Flow Models in the
    # Vector Field for Controlled Image Generation" 并大幅改写（13,933,891 字节）。
    # 本库解读依据的是 ICCV 2025 proceedings 版，CVF 这条与本地 sha256 一致。
    "2024-12_FlowChef":
        "https://openaccess.thecvf.com/content/ICCV2025/papers/"
        "Patel_FlowChef_Steering_of_Rectified_Flow_Models_for_"
        "Controlled_Generations_ICCV_2025_paper.pdf",
    # 裸链 https://arxiv.org/pdf/2603.17044 稳定返回 404（复测 2 次），
    # 带版本号的 v1 正常，且与本地 sha256 一致。
    "2026-03_ug-fight-dpo": "https://arxiv.org/pdf/2603.17044v1",
    # arXiv v1 是 15 页 4,016,508 字节的预印本；本库解读依据的本地副本是
    # 10 页 1,739,117 字节，PDF 元数据写着 /Subject: IEEE International
    # Conference on Computer Vision、/Producer: pikepdf——即 ICCV 2025
    # proceedings 版。CVF 这条与本地 sha256 完全一致（2026-08-30 实拉比对）。
    "2025-05_DICE":
        "https://openaccess.thecvf.com/content/ICCV2025/papers/"
        "Baraldi_What_Changed_Detecting_and_Evaluating_Instruction-Guided_"
        "Image_Edits_with_Multimodal_ICCV_2025_paper.pdf",
}

# 链接指向的论文没错（标题、作者、日期、版本数都核过），但渲染版本和本库
# 解读所依据的本地副本不是同一份。给链接，但必须在文档里标出来。
# 2026-08-30 起为空：原先唯一一条 2025-05_DICE 已定位到 ICCV proceedings 版，
# 移入 OVERRIDES。这个机制保留，下次再遇到同类情况直接往这里加。
RENDITION_DIFFERS = {}


def pdf_url(meta, dirname=None):
    """由 meta.json（和目录名）推出 PDF 直链；没有可下载来源时返回 None。"""
    if dirname and dirname in OVERRIDES:
        return OVERRIDES[dirname]
    if meta.get("arxiv_id"):
        return f"https://arxiv.org/pdf/{meta['arxiv_id']}"
    url = meta.get("url") or ""
    if "openaccess.thecvf.com" in url and url.endswith(".html"):
        return url.replace("/html/", "/papers/")[: -len(".html")] + ".pdf"
    return None
