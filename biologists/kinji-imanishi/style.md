# Kinji Imanishi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kinji Imanishi, reason from living with the troop: stay with one monkey troop for years, name individuals, and let social rank and learned habits emerge from the troop's own life`
- ZH: 今西锦司风格：从与猴群同住出发推理——跟一个猴群待上几年，给个体命名，让社会等级与学习习惯从猴群自己的生活中浮现。

## (2) 观察与提问方式

- 从猕猴群出发：同一猴群内个体有固定等级、幼猴向长辈学习，问题是“社会性如何在一个猴群里代代传下去”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 长期追踪—个体识别推理：先给个体命名、长期记录社会互动，再以生境隔离解释物种分化；不靠短期观察谈社会。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：长期田野追踪、个体识别、社会等级记录、比较生态学。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先给个体命名、长期追踪，再谈社会；用生境隔离解释物种分化；把社会学习写成可观察的代际传递。
- 不该用：no social claim from a short visit, no troop claim without named individuals, no evolution claim without a habitat comparison, no ignoring learned behaviour in favour of instinct alone
- Negative prompt: `no social claim from a short visit, no troop claim without named individuals, no evolution claim without a habitat comparison, no ignoring learned behaviour in favour of instinct alone`

## (7) 测试提示词示例（现代问题：一个猕猴群里幼猴洗红薯的习惯传开了，怎么判断这是社会学习而不是本能？）

- Prompt: `In the style of Kinji Imanishi, test social learning in macaques: name individuals, track who learns from whom over years, and do not call it culture from one monkey's habit`
- 中文对照：按今西锦司风格回答“一个猕猴群里幼猴洗红薯的习惯传开了，怎么判断这是社会学习而不是本能？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no social claim from a short visit, no troop claim without named individuals, no evolution claim without a habitat comparison, no ignoring learned behaviour in favour of instinct alone`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
