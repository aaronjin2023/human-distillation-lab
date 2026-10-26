# Mildred Dresselhaus — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Mildred Dresselhaus: calculate the band structure first, let the calculation predict what the nanotube must do, and check the prediction with Raman spectroscopy before claiming an electronic property`
- ZH: 德雷斯尔豪斯方法：先算能带结构，让计算预言纳米管必须有什么性质，再用拉曼光谱检验预言，确认后再谈电学性质。

## (2) 合成路线偏好

- 理论与实验结合：‘合成’即模型与样品——石墨、石墨插层化合物、碳纳米管；能带计算先行，样品制备对照计算预言。

## (3) 表征手段组合

- 拉曼光谱是核心表征：先算能带，再测拉曼谱对照；拉曼峰位与强度是判据：计算预言的峰对不上，就改模型。

## (4) 理论模型与图表风格

- 碳材料能带理论：用能带结构讲纳米管金属性与半导体性之分，用拉曼光谱讲声子与电子耦合；图表以能带图 + 拉曼谱为主。

## (5) 性能指标与取舍

- 优先保住理论与光谱的定量符合，牺牲模型的简便性：能带计算复杂但预言可靠；保住拉曼判据的可靠性，牺牲对应用前景的夸大。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先算能带结构再做样品；用拉曼光谱检验能带预言；先分金属性与半导体性再测器件；以拉曼峰作结构与性质判据；把碳材料理论从石墨推广到纳米管与石墨烯。
- 不该做：不做无能带计算支撑的输运解释；不跳过拉曼验证直接报电学性质；不把混合样品的平均性质当作单管性质；不以单根纳米管结果冒充统计结论；不脱离手性谈纳米管电子结构。
- Negative prompt: `no transport explanation without band-structure calculation, no electronic properties without Raman verification, no averaged mixed-sample properties presented as single-tube properties, no single-tube result presented as a statistical conclusion, no nanotube electronics without chirality`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性碳纳米导电材料）

- Prompt: `In the method of Mildred Dresselhaus, design a flexible carbon nanomaterial conductor for a wearable device. Calculate the band structure first, let the calculation predict metallic versus semiconducting behavior, verify with Raman spectroscopy, and check the prediction before claiming conductivity.`
- 中文对照：用德雷斯尔豪斯的方法，为可穿戴设备设计一种柔性碳纳米导电材料：先算能带结构，让计算预言金属性与半导体性之分，用拉曼光谱检验预言，确认后再谈导电性。
- Negative: `no transport explanation without band-structure calculation, no electronic properties without Raman verification, no averaged mixed-sample properties presented as single-tube properties, no single-tube result presented as a statistical conclusion, no nanotube electronics without chirality`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
