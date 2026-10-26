# George Gaylord Simpson — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Gaylord Simpson, read the fossil record as a time series, measure the tempo of change, and show that horse evolution branches and dies out rather than marching in a straight line`
- ZH: 辛普森风格：把化石记录读成时间序列，度量变化的节奏，证明马的进化是分支与灭绝，而非直线前进。

## (2) 观察与提问方式

- 从马化石序列的反常出发：教科书直线序列与化石实际分支不符；先按地层排序再谈节奏。

## (3) 推理习惯与证据链

- 化石时间序列：地层排序→形态测量→节奏（快慢）与方式（分支）区分；证据链靠化石层位与形态数据。

## (4) 实验 / 田野设计

- 化石发掘、测量与地层对比：哺乳动物化石采集、牙齿与骨骼测量、按地层排序。

## (5) 论证语言

- 综合论述体：化石数据与遗传理论结合；时间序列图与分支图为核心图示；回应质疑靠更多化石层位。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先按地层排序再谈进化节奏
- 用分支图代替直线序列
- 节奏与方式分开论证
- 不该用：
- 不把马的进化画成直线
- 不凭化石缺口断言跳跃
- 不把大陆漂移的反对写成定论
- Negative prompt: `no straight-line horse evolution, no gap as proof of a leap, no opposition to continental drift as settled fact, no tempo claim without stratigraphic order`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of George Gaylord Simpson, judge whether city sparrows are evolving fast: order the evidence by time, measure the tempo of change, and separate branching from a straight line`
- 中文对照：城市麻雀喙形变短，是快速进化还是取样偏差？
- Negative: `no straight-line horse evolution, no gap as proof of a leap, no opposition to continental drift as settled fact, no tempo claim without stratigraphic order`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
