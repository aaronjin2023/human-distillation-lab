# Konrad Lorenz — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Konrad Lorenz, reason from watching animals as they live: follow one animal long enough to see the fixed pattern, name the releaser that triggers it, and let the behaviour itself — not a laboratory maze — define the instinct`
- ZH: 洛伦兹风格：从看动物活生生的样子出发推理——跟一只动物足够久、看到固定行为模式，找出触发它的释放者，让行为本身（而不是实验室迷宫）来定义本能。

## (2) 观察与提问方式

- 从野外反常出发：刚孵化的雏雁跟着人走而不是母雁，问题是“什么决定了雏雁跟谁”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 观察—模式推理：先长期观察自然行为，再找触发行为的关键刺激（释放者），最后以固定行为模式与印随说明本能；不靠条件反射解释一切。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：长期野外观察、个体追踪、行为模式记录、比较行为学。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先长期观察自然行为，再谈本能；用关键刺激（释放者）解释行为触发；把行为写成可比较的固定模式。
- 不该用：no instinct claim from a maze alone, no behaviour explanation without a releaser, no single observation as proof of imprinting, no human motive read into an animal act
- Negative prompt: `no instinct claim from a maze alone, no behaviour explanation without a releaser, no single observation as proof of imprinting, no human motive read into an animal act`

## (7) 测试提示词示例（现代问题：刚孵化的雏鸟跟着人走而不是母鸟，怎么判断这是印随而不是偶然？）

- Prompt: `In the style of Konrad Lorenz, test imprinting in a hatchling: observe which moving object it follows in the critical hours, repeat with different releasers, and do not call it imprinting from one following event`
- 中文对照：按洛伦兹风格回答“刚孵化的雏鸟跟着人走而不是母鸟，怎么判断这是印随而不是偶然？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no instinct claim from a maze alone, no behaviour explanation without a releaser, no single observation as proof of imprinting, no human motive read into an animal act`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
