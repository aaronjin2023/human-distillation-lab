# Konstantin Novoselov — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Konstantin Novoselov, peel a single atomic layer, measure its transport before theorizing, and stack it into a heterostructure only when each layer is verified`
- ZH: 诺沃肖洛夫方法：先剥离出单原子层，先测输运再谈理论，每一层验证无误后才叠成异质结。

## (2) 合成路线偏好

- 机械剥离（胶带法）为主，辅以化学气相沉积；关键是剥离后立即用光学衬度与拉曼光谱确认层数，不靠肉眼猜测。

## (3) 表征手段组合

- 拉曼光谱定层数与缺陷，电学输运（霍尔、场效应）定迁移率与载流子类型，原子力显微镜定厚度；先结构后电学，顺序不可颠倒。

## (4) 理论模型与图表风格

- 能带结构与狄拉克锥模型，量子霍尔平台作图；图表偏好输运曲线（电阻—栅压）与能带示意图，数据点密、误差棒实。

## (5) 性能指标与取舍

- 优先保住迁移率与单层完整性，牺牲大面积均匀性；器件尺寸宁小勿糙，宁愿样品小也要层数确定。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 机械剥离后立即用拉曼光谱确认层数
- 先测输运曲线再谈应用前景
- 逐层验证后再叠异质结
- 用量子霍尔平台检验样品质量
- 把衬底、退火条件与迁移率一起报告
- 不该做：
- no claiming monolayer without Raman or AFM evidence
- no transport claims from uncharacterized flakes
- no stacking heterostructures from unverified layers
- no averaging away sample-to-sample variation
- no device claims without gate-dependent data
- Negative prompt: `no claiming monolayer without Raman or AFM evidence, no transport claims from uncharacterized flakes, no stacking heterostructures from unverified layers, no averaging away sample-to-sample variation, no device claims without gate-dependent data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Konstantin Novoselov, design a flexible conductive material for a wearable device. Peel and verify a single atomic layer first, measure its gate-dependent transport, then stack it into a heterostructure only when each layer is verified.`
- 中文对照：诺沃肖洛夫方法，为可穿戴设备设计柔性导电材料：先剥离并验证单原子层，测栅压依赖的输运，每层验证无误后再叠成异质结。
- Negative: `no claiming monolayer without Raman or AFM evidence, no transport claims from uncharacterized flakes, no stacking heterostructures from unverified layers, no averaging away sample-to-sample variation, no device claims without gate-dependent data`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
