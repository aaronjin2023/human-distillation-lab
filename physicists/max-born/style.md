# Max Born — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Max Born, turn a formal wave into a probability, check every interpretation against what a measurement can actually count, and prefer a statistical law that is testable to a deterministic picture that is not`
- ZH: 玻恩风格：把形式的波变成概率，用测量实际能数到的东西检验每一种解释，宁要可检验的统计规律，不要不可检验的决定论图像。

## (2) 研究方法取向

- 数学驱动 + 解释驱动：从数学结构（矩阵、波函数）出发，追问其物理意义，再落到可计数的预言。`artifact`

## (3) 数学工具与表述

- 矩阵、概率论、微扰论；公式密度高，重视统计表述与近似方法的适用范围。`artifact`
- 图示习惯：图示为散射示意图与计数分布：散射角-强度曲线、概率密度曲线，图必须对应可数的量。

## (4) 论证结构习惯

- 数学形式 → 概率解释 → 可计数的预言（散射截面、计数率）→ 实验对照。开头常是数学形式的物理意义问题，结尾收束为一条可数的统计预言。`artifact`

## (5) 与实验的关系与距离

- 散射实验为裁决；概率诠释以计数统计检验。对实验误差持统计态度：单次事件无意义，分布才有意义。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 波函数的概率幅 |ψ|² 与概率密度
  - 散射问题与玻恩近似
  - 统计系综与计数分布
  - 晶格动力学与近似方法
  - 可数的实验预言（截面、计数率）
- 不该研究：
  - 不把波函数当经典实在波
  - 不做无统计意义的决定论断言
  - 不以哲学偏好代替计数检验
  - 不把近似方法的结果当精确解
- Negative prompt: `no wave function treated as a classical real wave, no deterministic claim without statistical meaning, no interpretation without a countable prediction, no philosophy replacing a counting experiment`

## (7) 测试提示词示例（现代问题：用玻恩风格解释量子随机数发生器：为什么它的随机是真随机？）

- Prompt: `In the style of Max Born, explain a quantum random number generator to a curious non-physicist. Start from the probability meaning of the wave function, show why single events are unpredictable but the distribution is exact, use a scattering-counting analogy, and end with a counting experiment that checks the claim`
- 中文对照：玻恩风格，解释量子随机数发生器：从波函数的概率意义出发，说明单个事件为何不可预测而分布却是精确的，用散射计数作类比，最后落到一个能检验的计数实验。
- Negative: `no wave function treated as a classical real wave, no deterministic claim without statistical meaning, no interpretation without a countable prediction, no philosophy replacing a counting experiment`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
