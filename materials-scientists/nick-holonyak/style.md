# Nick Holonyak — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Nick Holonyak: grow the alloy until the bandgap turns direct, make a diffused p-n junction, and let the first visible light out of the crystal decide whether the material works`
- ZH: 何伦亚克方法：把合金长到能带变直接带隙为止，做扩散 p-n 结，让晶体里发出的第一道可见光来判定材料行不行。

## (2) 合成路线偏好

- 闭管气相输运生长 GaAsP 合金单晶；组分连续调变以扫过直接—间接带隙转变点；扩散法做 p-n 结；生长气氛与组分均匀性是关键。

## (3) 表征手段组合

- 先测合金组分与能带（光致发光定带隙），再测结特性与发光；直接—间接转变组分是核心判据：发光效率骤变处即转变点。

## (4) 理论模型与图表风格

- 直接带隙发光模型：用组分—带隙曲线画出直接—间接转变，图表以发光谱 + 效率—组分曲线为主；论证靠“组分扫过转变点，发光随之出现/消失”。

## (5) 性能指标与取舍

- 优先保住可见光发射与发光效率，牺牲红外波段的成熟工艺；保住合金组分可调性，牺牲单组分材料的简单性。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：用组分扫描找到直接—间接带隙转变点；先测发光谱定带隙，再做器件；用扩散 p-n 结做发光器件；以肉眼可见的发光作材料判据；把激光器与 LED 用同一合金体系贯通。
- 不该做：不做无带隙测量的器件试错；不把间接带隙材料的弱发光当作 LED；不跳过组分均匀性检查直接报效率；不以红外结果冒充可见光结果；不脱离发光谱谈合金质量。
- Negative prompt: `no device trial without bandgap measurement, no weak indirect-gap emission presented as an LED, no efficiency claims without checking alloy uniformity, no infrared results presented as visible light, no alloy quality claims without a luminescence spectrum`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性发光材料）

- Prompt: `In the method of Nick Holonyak, design a flexible light-emitting material for a wearable device. Scan alloy composition across the direct-indirect bandgap transition, verify the gap by luminescence, form a p-n junction, and let visible emission decide whether the material works.`
- 中文对照：用何伦亚克的方法，为可穿戴设备设计一种柔性发光材料：扫描合金组分扫过直接—间接带隙转变点，用发光谱定带隙，做 p-n 结，让可见发光来判定材料行不行。
- Negative: `no device trial without bandgap measurement, no weak indirect-gap emission presented as an LED, no efficiency claims without checking alloy uniformity, no infrared results presented as visible light, no alloy quality claims without a luminescence spectrum`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
