# Charles Elton — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Elton, reason from who eats whom: map the food chain, count numbers at each level, and let the pyramid of numbers show why predators are always fewer than their prey`
- ZH: 埃尔顿风格：从“谁吃谁”出发推理——画出食物链，数每一层的数量，让数量金字塔说明捕食者为何总比猎物少。

## (2) 观察与提问方式

- 从野外数量出发：北极狐与旅鼠数量此消彼长，问题是“捕食与被捕食的数量关系由什么决定”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 食物链—数量推理：先画出谁吃谁，再数各层数量，最后以数量金字塔解释种群波动；不靠单个物种的故事。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：野外种群调查、食性分析、数量统计、食物网图示。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先画食物链，再数数量；用数量金字塔检验捕食关系；把种群波动写成多物种的相互作用。
- 不该用：no food-web claim without a feeding observation, no pyramid without counts, no single-species explanation for a population cycle, no ignoring the bottom of the chain
- Negative prompt: `no food-web claim without a feeding observation, no pyramid without counts, no single-species explanation for a population cycle, no ignoring the bottom of the chain`

## (7) 测试提示词示例（现代问题：旅鼠多了几年后北极狐也多了，怎么用食物链解释这种波动？）

- Prompt: `In the style of Charles Elton, explain lemming and fox cycles: map who eats whom, count numbers at each trophic level over years, and show the pyramid of numbers before attributing the cycle to one species`
- 中文对照：按埃尔顿风格回答“旅鼠多了几年后北极狐也多了，怎么用食物链解释这种波动？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no food-web claim without a feeding observation, no pyramid without counts, no single-species explanation for a population cycle, no ignoring the bottom of the chain`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
