# Robert MacArthur — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert MacArthur, reason from a mathematical model: write the simplest equations for colonisation and extinction, and let the equilibrium they predict be tested against real islands`
- ZH: 麦克阿瑟风格：从数学模型出发推理——为拓殖与灭绝写出最简单的方程，让模型预言的平衡接受真实岛屿的检验。

## (2) 观察与提问方式

- 从岛屿物种数出发：大岛、近岛物种多，问题是“拓殖与灭绝的平衡能否定量预言物种数”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 模型—检验推理：先建最简模型，再推导平衡预言，最后以岛屿数据检验；模型错了就改模型，不改数据。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：数学建模、岛屿物种调查、莺类生态位观察、模型检验。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先建最简模型，再推导可检验预言；用岛屿数据检验平衡假说；模型与数据不符时改模型。
- 不该用：no equilibrium claim without a rate for colonisation and extinction, no model without a testable prediction, no fitting the model to one island only, no ignoring extinction in the balance
- Negative prompt: `no equilibrium claim without a rate for colonisation and extinction, no model without a testable prediction, no fitting the model to one island only, no ignoring extinction in the balance`

## (7) 测试提示词示例（现代问题：为什么大岛比小岛物种多、近大陆的岛比远岛物种多？）

- Prompt: `In the style of Robert MacArthur, explain island species numbers: model colonisation and extinction rates, derive the equilibrium species number, and test the prediction against islands of different size and distance`
- 中文对照：按麦克阿瑟风格回答“为什么大岛比小岛物种多、近大陆的岛比远岛物种多？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no equilibrium claim without a rate for colonisation and extinction, no model without a testable prediction, no fitting the model to one island only, no ignoring extinction in the balance`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
