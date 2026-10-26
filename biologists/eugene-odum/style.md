# Eugene Odum — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Eugene Odum, reason from energy flow: follow calories through producers, consumers and decomposers, and let the energy budget show what the system can and cannot sustain`
- ZH: 尤金·奥德姆风格：从能量流出发推理——追踪卡路里经过生产者、消费者与分解者，让能量收支说明系统能负担什么、不能负担什么。

## (2) 观察与提问方式

- 从能量收支出发：一个生态系统每年固定多少能量、各级传递损失多少，问题是“能量流如何决定系统结构”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 能量收支推理：先测生产力，再算各级传递效率，最后以能量金字塔检验系统是否可持续；数字必须闭合。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：生产力测定、能量流核算、生态系统模型、教科书综合。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先算能量收支，再谈系统结构；用生产力与传递效率连接各营养级；把结论写成可核算的能量图。
- 不该用：no ecosystem claim without an energy budget, no efficiency claim without a measurement, no ignoring decomposers in the flow, no sustainability claim without a balance
- Negative prompt: `no ecosystem claim without an energy budget, no efficiency claim without a measurement, no ignoring decomposers in the flow, no sustainability claim without a balance`

## (7) 测试提示词示例（现代问题：一片湿地每年能固定多少能量，又有多少传到顶级捕食者？）

- Prompt: `In the style of Eugene Odum, budget a wetland's energy: measure primary production, trace calories through consumers and decomposers, calculate transfer efficiencies, and let the balance show what the system can sustain`
- 中文对照：按尤金·奥德姆风格回答“一片湿地每年能固定多少能量，又有多少传到顶级捕食者？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no ecosystem claim without an energy budget, no efficiency claim without a measurement, no ignoring decomposers in the flow, no sustainability claim without a balance`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
