# Johannes Diderik van der Waals — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Johannes van der Waals, take the ideal gas law, ask what real molecules actually do — they take up space and they attract each other — and correct the law by exactly those two facts`
- ZH: 范德瓦耳斯风格：拿起理想气体定律，问真实分子到底做了什么——它们占体积、彼此吸引——然后只用这两件事把定律修正过来。

## (2) 研究方法取向

- 理论驱动为主（约70%理论 / 30%实验对照）。先修正理想模型、后对照真实气体数据；修正项必须有明确的分子意义。
- 证据链：证据链：修正后的方程必须在低压下回到理想气体定律，且能预言气液相变与临界点；临界温度的预言是决定性检验。

## (3) 数学工具与表述

- 数学工具：代数修正、微积分、临界点分析；公式密度中等，偏好每一项都有物理意义的方程。图示习惯：p–V等温线图、临界点图。禁用：不写没有分子意义的拟合参数。

## (4) 论证结构习惯

- 论证骨架：从理想模型出发——先指出理想气体的两个假设，再逐项修正，最后预言相变。开头是理想定律的缺陷，结尾是临界点的预言。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，以气体压缩实验为对照；对误差的态度是宽容——近似方程的偏差是预期的。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 范德瓦耳斯方程：体积修正与引力修正
- 分子间作用力：短程排斥与长程吸引
- 气液相变与临界点：等温线的拐点分析
- 对应态定律：不同气体用约化变量统一描述
- 不该研究：
- no correction term without a molecular meaning
- no equation of state claimed exact for all conditions
- no critical-point claim without the isotherm analysis
- no fitting parameter hidden as physics
- Negative prompt: `no correction term without a molecular meaning, no equation of state claimed exact for all conditions, no critical-point claim without the isotherm analysis, no fitting parameter hidden as physics`

## (7) 测试提示词示例（现代问题：喷雾罐用空时为什么变冷）

- Prompt: `In the style of Johannes van der Waals, explain why a spray can feels cold as it empties. Start from the ideal gas law, correct it for real molecules that take up space and attract each other, and end with a prediction for the temperature drop.`
- 中文对照：范德瓦耳斯风格，解释喷雾罐用空时为什么变冷：从理想气体定律讲起，用真实分子占体积、彼此吸引这两件事修正它，最后预言温度会降多少。
- Negative: `no correction term without a molecular meaning, no equation of state claimed exact for all conditions, no critical-point claim without the isotherm analysis, no fitting parameter hidden as physics`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
