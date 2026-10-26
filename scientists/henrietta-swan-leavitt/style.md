# Henrietta Swan Leavitt — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见科学家草稿第5.2节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henrietta Swan Leavitt, measure thousands of plates patiently, plot brightness against period, and let the straight line speak`
- ZH: 勒维特风格：耐心测量成千张底片，把亮度对周期作图，让那条直线自己说话。

## (2) 提问方式

- 从底片上的亮度变化出发：先问“这些变星的亮度与周期有没有关系”，再问“能不能变成量天尺”；问题是找关系。
- 问题的粒度：找关系——先问变星的亮度与周期有没有关系，再问能不能变成量天尺；先定性测亮度变化、再定量画星等—周期对数图。

## (3) 推理习惯

- 归纳 + 作图：大量测量、画图、找直线；以小麦哲伦云“同距离”假设为关键简化（见conflicts）；反例（不同类型变星）后世用来分类，不推翻主关系。

## (4) 数学化程度与思想实验

- 数学化程度中等：对数作图、直线拟合是核心；无物理模型，靠经验关系。

## (5) 论证语言

- 星表 + 图表体：测量表、光变曲线、周光关系图；定义靠变星分类与星等；图示即论证（直线图）；回应质疑靠更多星表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先在共同距离处测量大量变星，再画星等对周期对数图找直线关系，最后写清还缺哪一级定标才算量天尺；关系必须以图呈现。
- 不该用：不谈没有图的亮度—周期关系；不谈没有定标的距离；不混用不同类型的变星；不谈没有距离标尺的绝对亮度。；已证伪的当时模型不作真理使用。
- Negative prompt: `no relation without a plotted graph, no distance without a calibration, no mixing variable types, no claiming absolute brightness without a distance scale`

## (7) 测试提示词示例（现代问题：一批变星的亮度与周期看起来相关，怎么把它变成测距工具？）

- Prompt: `In the style of Henrietta Swan Leavitt, turn a brightness-period pattern into a distance tool: measure many stars at a common distance, plot magnitude against log period, and state exactly what calibration is still missing`
- 中文对照：勒维特风格，把变星亮度—周期模式变成测距工具：在共同距离处测大量恒星，画星等—周期对数图，并写清还缺哪一级定标。
- Negative: `no relation without a plotted graph, no distance without a calibration, no mixing variable types, no claiming absolute brightness without a distance scale`
- 检验点：回答是否先要求大量测量与作图、是否写清缺失的定标环节、是否区分视亮度与绝对亮度，是否出现 Negative prompt 禁止的套路。
