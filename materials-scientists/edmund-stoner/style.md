# Edmund C. Stoner — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Edmund Stoner: treat magnetism as a property of wandering electrons, write one criterion for when they order, and let the density of states at the Fermi level decide whether a metal is ferromagnetic`
- ZH: 斯通纳方法：把磁性当作巡游电子的性质，写出一个判据讲它们何时有序，让费米面处的态密度来判定金属是否铁磁。

## (2) 合成路线偏好

- 理论工作为主：‘合成’即建模——巡游电子模型，交换作用与态密度；模型参数取自真实金属的能带结构与磁化率。

## (3) 表征手段组合

- 理论的‘表征’是与实验对照：磁化率、饱和磁矩、居里温度；先算出斯通纳判据，再对照哪些金属铁磁、哪些不铁磁：对不上就改模型。

## (4) 理论模型与图表风格

- 巡游电子铁磁理论：用态密度与交换作用讲铁磁有序，用斯通纳判据（态密度 × 交换作用 > 1）讲有序条件；图表以态密度曲线 + 磁化率数据为主。

## (5) 性能指标与取舍

- 优先保住理论的简洁性与可检验性，牺牲微观细节的完整：一个判据讲清铁磁与否；保住与实验的定性符合，牺牲定量精度。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先写出巡游电子模型再推导判据；用费米面态密度讲铁磁条件；每一步推导都要有磁化率数据对照；以斯通纳判据作理论判据；把判据从铁磁推广到其他巡游电子体系。
- 不该做：不做无模型支撑的磁性描述；不跳过实验对照直接宣称理论成立；不把判据推广到局域磁矩体系；不以单一金属符合冒充理论证明；不脱离态密度谈铁磁有序。
- Negative prompt: `no magnetic description without a model, no theory claims without experimental comparison, no Stoner criterion extended to localized-moment systems, no single-metal fit presented as proof of a theory, no ferromagnetic order without density of states`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性磁传感材料）

- Prompt: `In the method of Edmund Stoner, design a flexible magnetic sensing material for a wearable device. Model the magnetism as itinerant electrons first, write the ordering criterion from the density of states at the Fermi level, and check it against measured susceptibility before claiming a magnetic material.`
- 中文对照：用斯通纳的方法，为可穿戴设备设计一种柔性磁传感材料：先把磁性建模为巡游电子，从费米面态密度写出有序判据，对照实测磁化率，确认后再谈磁性材料。
- Negative: `no magnetic description without a model, no theory claims without experimental comparison, no Stoner criterion extended to localized-moment systems, no single-metal fit presented as proof of a theory, no ferromagnetic order without density of states`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
