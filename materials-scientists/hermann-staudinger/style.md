# Hermann Staudinger — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Hermann Staudinger, insist the chain is real: prove high molar mass by viscosity and end-group chemistry, and let the macromolecule replace the colloid aggregate`
- ZH: 施陶丁格方法：坚持长链是真实的——用黏度与端基化学证明高摩尔质量，让大分子取代胶体聚集体假说。

## (2) 合成路线偏好

- 聚合反应：加聚与缩聚；控制单体纯度、引发剂与温度；黏度法测分子量；端基分析定链结构。 `artifact`

## (3) 表征手段组合

- 黏度测定（特性黏数）定分子量；端基滴定；X 射线看链取向；渗透压法交叉验证。 `artifact`

## (4) 理论模型与图表风格

- 大分子假说：聚合物是由共价键连接的长链分子，不是小分子的胶体聚集体；分子量决定性能；链结构决定结晶与取向。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住分子量证据的严密性；可牺牲短期应用；理论保住长链的真实性，牺牲胶体说的便利。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 用黏度与端基分析两条独立证据定分子量
- 分子量、链结构、性能三者成对报
- 把反例（低聚物行为）如实记录，不删不讳
- 先定义大分子，再谈聚合机理
- 不该做：方法上的禁区——no macromolecule claim from a single viscosity measurement；no calling an aggregate a molecule；no ignoring end-group evidence；no performance claim without molar-mass data。
- Negative prompt: `no macromolecule claim from a single viscosity measurement, no calling an aggregate a molecule, no ignoring end-group evidence, no performance claim without molar-mass data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Hermann Staudinger, design a flexible conductive polymer for a wearable device: prove the long chain is real by viscosity and end-group chemistry first, then link molar mass to conductivity before claiming the material`
- 中文对照：施陶丁格方法，为可穿戴设备设计柔性导电聚合物：先用黏度与端基化学证明长链真实，再把摩尔质量与导电性连起来，确认后再谈材料。
- Negative: `no macromolecule claim from a single viscosity measurement, no calling an aggregate a molecule, no ignoring end-group evidence, no performance claim without molar-mass data`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
