# Zhores Alferov — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Zhores Alferov: engineer the band structure layer by layer, confine carriers and photons in a double heterostructure, and prove the device in a working laser or solar cell before claiming a new material`
- ZH: 阿尔费罗夫方法：逐层设计能带结构，把载流子与光子 约束 在双异质结构里，先在能工作的激光器或太阳能电池上证明，再谈新材料。

## (2) 合成路线偏好

- 液相外延与气相外延生长 III-V 族异质结构（GaAs/AlGaAs）；逐层控制组分与掺杂，界面陡峭、缺陷低；生长温度与组分渐变是关键参数窗口。

## (3) 表征手段组合

- 先测能带结构与异质结界面（电学 I-V、C-V），再测光致发光与激光阈值；结构表征服务于器件：界面质量不合格不进入器件测试。

## (4) 理论模型与图表风格

- 能带工程与双异质结构模型：用能带图画出载流子与光子的 约束，图表以能带示意图 + 阈值电流-温度曲线为主；论证结构是“理论预言—外延生长—器件验证”三段。

## (5) 性能指标与取舍

- 优先保住激光阈值低与室温连续工作，牺牲结构简单性：多层异质结构工艺复杂但换来载流子 约束；保住光电转换效率，牺牲单材料体系的通用性。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：逐层设计能带，先画异质结能带图再生长；用双异质结构同时 约束 载流子与光子；外延生长后先测界面质量与发光，再做器件；以室温连续工作的激光器或太阳能电池作最终判据；把异质结构从激光器推广到太阳能电池与光电探测器。
- 不该做：不做无能带设计的单层材料试错；不跳过界面表征直接报器件性能；不把低温脉冲激射当作室温连续工作；不以单一材料替代异质结构的功能分工；不脱离器件验证谈材料优越性。
- Negative prompt: `no single-layer trial without band design, no device claims without interface characterization, no pulsed low-temperature lasing presented as room-temperature continuous operation, no replacing heterostructure function with one bulk material, no material superiority claims without a working device`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性发光材料）

- Prompt: `In the method of Zhores Alferov, design a flexible light-emitting material for a wearable device. Start from the band diagram, use a double-heterostructure-like stack to confine carriers and photons, grow it layer by layer, verify the interface by luminescence, and prove room-temperature continuous emission before claiming a display material.`
- 中文对照：用阿尔费罗夫的方法，为可穿戴设备设计一种柔性发光材料：先画能带图，用类双异质结构叠层同时 约束 载流子与光子，逐层生长，用发光验证界面，先证明室温连续发光再谈显示应用。
- Negative: `no single-layer trial without band design, no device claims without interface characterization, no pulsed low-temperature lasing presented as room-temperature continuous operation, no replacing heterostructure function with one bulk material, no material superiority claims without a working device`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
