# 基础模型/方法组处理清单

核对日期：2026-08-29。范围严格限定为 GPT Image 2、FlowChef、FLUX、ICEdit、MGIE、Step1X、HQ-Edit、Paint by Example、SeedEdit/Seedream、IP-Adapter、Drag Your GAN、Qwen-Image Edit、Null-text Inversion、ControlNet。

引用量为核对当日实时返回值，不进入技术结论。除 Null-text Inversion 外，论文引用量统一来自 [Semantic Scholar Graph API](https://api.semanticscholar.org/api-docs/graph) 的同一次 batch 查询；Null-text 因 Semantic Scholar 对 arXiv ID 返回空记录、按 DOI 亦不可用，单独使用 [OpenAlex Works API](https://docs.openalex.org/api-entities/works)。两种 provider 的数值不相加，也不做严格横向排名。

| 条目/落盘目录 | 载体与权威性 | 首次公开 | 正式发表 | 实时引用量 | 引用数据源 | PDF/笔记状态 | 一手核验入口 |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| GPT Image 2 — `2026-04_GPT-Image-2` | 官方产品文档；无正式论文 | 2026-04-21 | — | — | — | 无 PDF（正确）；新建官方资料笔记/meta | [OpenAI Docs](https://developers.openai.com/api/docs/models/gpt-image-2) |
| FlowChef — `2024-12_FlowChef` | ICCV 2025 同行评审正式论文 | 2024-11-27 | 2025-10，ICCV 2025 | 40 | Semantic Scholar API | 已下载 CVF 正式 `paper.pdf`；新建深读/meta | [CVF](https://openaccess.thecvf.com/content/ICCV2025/html/Patel_FlowChef_Steering_of_Rectified_Flow_Models_for_Controlled_Generations_ICCV_2025_paper.html) |
| FLUX.1 基础模型 — `2024-08_FLUX.1` | 官方发布博客/模型卡；无正式论文 | 2024-08-01 | — | — | — | 无 PDF（正确）；新建官方资料笔记/meta | [BFL](https://bfl.ai/blog/24-08-01-bfl) |
| FLUX.1 Kontext — `2025-06_FLUX-Kontext` | arXiv 技术报告；另有 BFL 官方产品发布 | 2025-06-17 | 仅 arXiv | 1004 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2506.15742) |
| ICEdit — `2025-04_ICEdit` | NeurIPS 2025 同行评审正式论文 | 2025-04-29 | 2025-12，NeurIPS 2025 | 201 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [项目页](https://river-zhang.github.io/ICEdit-gh-pages/) |
| MGIE — `2023-09_MGIE` | ICLR 2024 同行评审正式论文 | 2023-09-29 | 2024-05，ICLR 2024 | 201 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [OpenReview](https://openreview.net/forum?id=S1RKWSyZ2Y) |
| Step1X-Edit — `2025-04_Step1X-Edit` | arXiv 论文/官方开源模型；未查到正式 venue | 2025-04-24 | 仅 arXiv | 408 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2504.17761) |
| HQ-Edit — `2024-04_HQ-Edit` | ICLR 2025 同行评审正式论文 | 2024-04-15 | 2025-04，ICLR 2025 | 209 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [OpenReview](https://openreview.net/forum?id=mZptYYttFj) |
| Paint by Example — `2022-11_Paint-by-Example` | CVPR 2023 同行评审正式论文 | 2022-11-23 | 2023-06，CVPR 2023 | 664 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Yang_Paint_by_Example_Exemplar-Based_Image_Editing_With_Diffusion_Models_CVPR_2023_paper.html) |
| SeedEdit — `2024-11_SeedEdit` | arXiv 论文；未查到正式 venue | 2024-11-11 | 仅 arXiv | 64 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2411.06686) |
| SeedEdit 3.0 — `2025-06_SeedEdit3` | arXiv 技术报告 | 2025-06-05 | 仅 arXiv | 52 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2506.05083) |
| Seedream 4.0 — `2025-09_Seedream4` | arXiv 技术报告/产品系统报告 | 2025-09-24 | 仅 arXiv | 234 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2509.20427) |
| IP-Adapter — `2023-08_IP-Adapter` | arXiv 论文/官方开源实现；未查到正式 venue | 2023-08-13 | 仅 arXiv | 1739 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2308.06721) |
| Drag Your GAN — `2023-05_DragGAN` | ACM SIGGRAPH 2023 同行评审正式论文 | 2023-05-18 | 2023-08，SIGGRAPH 2023 | 368 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [ACM DOI](https://doi.org/10.1145/3588432.3591500) |
| Qwen-Image 报告/编辑基础 — `2025-08_Qwen-Image` | arXiv 技术报告/官方开源模型 | 2025-08-04 | 仅 arXiv | 930 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [arXiv](https://arxiv.org/abs/2508.02324) |
| Qwen-Image-Edit-2511 — `2025-12_Qwen-Image-Edit-2511` | 官方 checkpoint/model card；无独立论文 | 2025-12-17 | — | —（关联报告 930） | 关联数来自 Semantic Scholar API | 无 PDF（正确）；新建版本核验笔记/meta | [官方模型卡](https://huggingface.co/Qwen/Qwen-Image-Edit-2511) |
| Null-text Inversion — `2022-11_Null-text-Inversion` | CVPR 2023 同行评审正式论文 | 2022-11-17 | 2023-06，CVPR 2023 | 657 | OpenAlex（S2 无记录） | 既有 PDF/meta/深读复核；补来源与决策说明 | [CVF](https://openaccess.thecvf.com/content/CVPR2023/html/Mokady_NULL-Text_Inversion_for_Editing_Real_Images_Using_Guided_Diffusion_Models_CVPR_2023_paper.html) |
| ControlNet — `2023-02_ControlNet` | ICCV 2023 同行评审正式论文 | 2023-02-10 | 2023-10，ICCV 2023 | 7602 | Semantic Scholar API | 既有 PDF/meta/深读复核；补来源与决策说明 | [CVF](https://openaccess.thecvf.com/content/ICCV2023/html/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.html) |

## 验收说明

- 本组所有有正式论文/技术报告的条目均已有 `paper.pdf`；本轮唯一缺失的 FlowChef 已从 CVF 正式 proceedings 下载并校验为 11 页 PDF，SHA-256 已写入 meta。
- GPT Image 2、基础 FLUX.1、Qwen-Image-Edit-2511 没有各自独立正式论文，按要求只有官方资料笔记与 `meta.json`，没有伪造 `paper.pdf`。
- 基础 FLUX.1 与 FLUX.1 Kontext、Qwen-Image 技术报告与 2511 checkpoint 均分开记录，避免把后续编辑能力倒灌到早期基础模型。
- 未修改根 `INDEX.md`。
