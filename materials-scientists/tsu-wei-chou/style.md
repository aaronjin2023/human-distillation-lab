# Tsu-Wei Chou — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Tsu-Wei Chou, weave the reinforcement before you mould the composite, design the preform to meet the load, and let the microstructure carry the performance`
- ZH: 周次伟方法：先织好增强体再成型复合材料，按载荷设计预成型体，让微结构去承载性能。

## (2) 合成路线偏好

- 纺织预成型体：编织、针织、缝合三维增强体，树脂传递模塑成型；关键是预成型体结构先定，成型只填充不改结构。

## (3) 表征手段组合

- 预成型体结构观察、力学测试（拉伸、压缩、层间剪切）、损伤容限测试；先预成型体结构后力学，顺序不可颠倒。

## (4) 理论模型与图表风格

- 纺织复合材料微结构力学模型；图表偏好预成型体结构图与力学性能—结构参数曲线。

## (5) 性能指标与取舍

- 优先保住预成型体的结构完整性与损伤容限，牺牲成型速度；宁愿成型慢，也不要预成型体变形。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先设计预成型体结构再选成型工艺
- 编织、针织、缝合按载荷路径选用
- 力学测试按方向分别报告
- 损伤容限测试设传统层合板对照
- 把预成型体、成型与性能写成一条链
- 不该做：
- no performance claims without preform-structure data
- no moulding steps that distort the preform
- no direction-averaged claims for anisotropic textiles
- no damage-tolerance claims without impact testing
- no presenting a 2D laminate as a 3D textile composite
- Negative prompt: `no performance claims without preform-structure data, no moulding steps that distort the preform, no direction-averaged claims for anisotropic textiles, no damage-tolerance claims without impact testing, no presenting a 2D laminate as a 3D textile composite`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Tsu-Wei Chou, design a flexible conductive material for a wearable device. Weave the reinforcement first, design the preform to meet the load, mould without distorting it, then test direction by direction.`
- 中文对照：周次伟方法，为可穿戴设备设计柔性导电材料：先织好增强体，按载荷设计预成型体，成型时不扭曲它，再逐方向测试。
- Negative: `no performance claims without preform-structure data, no moulding steps that distort the preform, no direction-averaged claims for anisotropic textiles, no damage-tolerance claims without impact testing, no presenting a 2D laminate as a 3D textile composite`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
