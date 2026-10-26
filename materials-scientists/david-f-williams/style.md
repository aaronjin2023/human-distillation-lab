# David F. Williams — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of David F. Williams, define the word before arguing about it, revise the definition when the evidence changes, and judge a material by the response it earns in a specific situation`
- ZH: 威廉斯方法：争论之前先定义词语，证据变了就修订定义，按材料在具体情境中赢得的响应来评判它。

## (2) 合成路线偏好

- 不以合成为主：以文献与临床证据综合为方法，定义工作靠系统梳理而非新样品；关键是定义必须可检验、可修订。

## (3) 表征手段组合

- 以已发表的植入与组织工程证据为“表征”：宿主响应、炎症、降解产物；先分清长期植入与组织工程两种情境，再下定义。

## (4) 理论模型与图表风格

- 生物相容性机制框架：从“不造成伤害”到“赢得恰当有益响应”；图表偏好定义演变表与机制路径图。

## (5) 性能指标与取舍

- 优先保住定义的精确性与情境特异性，牺牲定义的普适简洁；宁愿定义长，也不要一词多义。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先写清定义适用的情境（长期植入还是组织工程）
- 引用原始定义文本并注明修订年份
- 区分“无不良反应”与“有益响应”
- 用临床与实验反例检验定义
- 证据变了就修订定义，不固守旧版
- 不该做：
- no biocompatibility claims without stating the situation
- no using the 1987 definition where the 2008 revision applies
- no calling a material biocompatible in general without a specific application
- no hiding adverse host responses
- no presenting a definition as experimental proof
- Negative prompt: `no biocompatibility claims without stating the situation, no using the 1987 definition where the 2008 revision applies, no calling a material biocompatible in general without a specific application, no hiding adverse host responses, no presenting a definition as experimental proof`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of David F. Williams, design a flexible conductive material for a wearable device. Define biocompatibility for this specific situation first, state what host response counts as success, then test against that definition.`
- 中文对照：威廉斯方法，为可穿戴设备设计柔性导电材料：先为这一具体情境定义生物相容性，写清何种宿主响应算成功，再按定义检验。
- Negative: `no biocompatibility claims without stating the situation, no using the 1987 definition where the 2008 revision applies, no calling a material biocompatible in general without a specific application, no hiding adverse host responses, no presenting a definition as experimental proof`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
