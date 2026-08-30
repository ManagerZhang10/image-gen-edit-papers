# Lark《Image Edit领域论文调研》核验索引

> 来源：[Lark Wiki](https://romangic.sg.larksuite.com/wiki/Ab9QwdNuTiv41FkWyB7lLic9gHh)，读取 revision 1687  
> 核对日期：2026-08-29  
> 仓库：<https://github.com/romangic/image_edit_paper>

## 交付结果

| 分组 | 条目 | 有论文 PDF | 无独立论文的产品说明 | 逐项清单 |
| --- | ---: | ---: | ---: | --- |
| Benchmark 前半 | 12 | 12 | 0 | [manifest](_review/bench_early_manifest.md) |
| Benchmark 后半与综述 | 12 | 12 | 0 | [manifest](_review/bench_late_manifest.md) |
| 基础模型、数据与控制方法 | 18 | 15 | 3 | [manifest](_review/models_core_manifest.md) |
| 其余编辑方法与产品 | 13 | 12 | 1 | [manifest](_review/models_methods_manifest.md) |
| **合计** | **55** | **51** | **4** | — |

Lark 中的组合条目被拆成可独立核验的版本，例如基础 FLUX.1 与 FLUX.1 Kontext、Qwen-Image 报告与 Qwen-Image-Edit-2511、SeedEdit/SeedEdit3/Seedream4，因此本地载体数多于原始标题数。

硬验收结果：55/55 有 `解读.md` 和有效 `meta.json`；51/51 正式论文或技术报告有 `%PDF` 文件；4 个没有独立论文的产品条目刻意不创建 `paper.pdf`。51 篇研究笔记的中文正文最短 2510 字，最长 8943 字；新生成的决策型笔记以 2500–4500 字为主，已有质量合格的长稿保留。

## 先看哪几个文件

1. `_review/` 下四份 `*_errors.md`：会影响技术或权威性判断的问题，逐条给了 Lark 里该改成什么、为什么影响决策。
   （汇总版 `严重事实错误_待Review_临时.md` 是内部 review 件，只留在维护者本地，没有进仓库。）
2. [LARK清单_权威性与影响力.md](LARK清单_权威性与影响力.md)：venue、首发/正式发表时间、引用量口径与完整逐项表入口。
3. 四份分组 manifest：定位每个本地目录、PDF、笔记和一手来源。
4. 每篇目录内的 `解读.md`：论文内容、实验边界与对简单人像编辑/身份保持/局部保持的决策意义。

## 本轮新增或补齐的代表条目

- [FlowChef](2024-12_FlowChef/解读.md)：补正式 ICCV PDF 与方法深读。
- [InstructEdit](2023-05_InstructEdit/解读.md)：补自动 mask 生成/编辑流水线深读。
- [Rich Text](2023-04_Rich-Text/解读.md)：补富文本区域控制深读，并纠正真实图仍需 grounded segmentation。
- [GPT Image 2](2026-04_GPT-Image-2/解读.md)、[FLUX.1](2024-08_FLUX.1/解读.md)、[Qwen-Image-Edit-2511](2025-12_Qwen-Image-Edit-2511/解读.md)、[Grok/Aurora](2024-12_Grok-Aurora/解读.md)：明确标注“没有独立正式论文”，只保留官方资料/核验边界。

## 笔记验收口径

不再机械追求 6500–8500 字。新笔记只要完整覆盖以下决策信息即可：一句话结论、问题与适用边界、方法/数据构造、评测指标、关键结果与论文锚点、局限/未证实主张、对人像身份和局部保持的意义、venue/日期/引用来源。复杂论文或原有长稿可以更长，但不会为了字数填充细枝末节。

## 没有修改的内容

根目录已有的 [INDEX.md](INDEX.md) 覆盖整座 160+ 篇论文库，本轮没有机械重排它，以免干扰现有技术脉络。当前 Lark 清单的准确入口以本文件和四份 manifest 为准。
