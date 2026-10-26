# Yiu-Wing Mai — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Yiu-Wing Mai, follow the crack, find what bridges it, and measure toughness by the energy the bridging consumes`
- ZH: 麦耀华方法：跟着裂纹走，找到桥联它的东西，再用桥联消耗的能量来量度韧性。

## (2) 合成路线偏好

- 不以合成为主：以断裂试验与模型为方法，试样制备（缺口、预制裂纹）是关键；关键是裂纹路径可观察，桥联机制可分离。

## (3) 表征手段组合

- 断裂韧性测试、裂纹扩展观察、纤维拔出/压入试验；先看裂纹走多远、谁在桥联，再算能量。

## (4) 理论模型与图表风格

- 裂纹桥联模型与准脆性断裂力学；图表偏好阻力曲线（R 曲线）与桥联应力分布图。

## (5) 性能指标与取舍

- 优先保住韧性的机理清晰度，牺牲单一韧性数值的简洁；宁愿报告整条 R 曲线，也不要一个孤立的 K 值。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先观察裂纹路径与桥联机制再算韧性
- 报告整条阻力曲线，不只报一个韧性值
- 纤维拔出试验分离界面贡献
- 准脆性材料用能量法，不硬套线弹性
- 把裂纹、桥联与能量写成一条链
- 不该做：
- no toughness claims without crack-path observation
- no single-K claims where an R-curve applies
- no attributing toughness to an unobserved mechanism
- no linear-elastic analysis where quasi-brittle behaviour dominates
- no hiding scatter in fracture data
- Negative prompt: `no toughness claims without crack-path observation, no single-K claims where an R-curve applies, no attributing toughness to an unobserved mechanism, no linear-elastic analysis where quasi-brittle behaviour dominates, no hiding scatter in fracture data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Yiu-Wing Mai, design a flexible conductive material for a wearable device. Follow the crack, find what bridges it, report the full R-curve, and measure toughness by bridging energy.`
- 中文对照：麦耀华方法，为可穿戴设备设计柔性导电材料：跟着裂纹走，找到桥联它的东西，报告整条阻力曲线，用桥联能量量度韧性。
- Negative: `no toughness claims without crack-path observation, no single-K claims where an R-curve applies, no attributing toughness to an unobserved mechanism, no linear-elastic analysis where quasi-brittle behaviour dominates, no hiding scatter in fracture data`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
