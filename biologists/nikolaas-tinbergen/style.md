# Nikolaas Tinbergen — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nikolaas Tinbergen, reason from four questions at once: ask what a behaviour is for, how it develops, how it works, and how it evolved — and do not accept an answer that answers only one`
- ZH: 廷伯根风格：从四个问题同时出发推理——问一个行为有什么功能、如何发育、如何运作、如何演化，不接受只回答其中一个的答案。

## (2) 观察与提问方式

- 从棘鱼求偶出发：雄鱼红腹、之字舞、筑巢一连串动作，问题是“这套行为从哪四个角度才能说清”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 四问题—实验推理：先以野外观察描述行为序列，再以模型实验分离触发刺激，最后从功能、发育、机制、演化四角度收束。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：野外观察、模型实验（假鱼模型）、行为序列记录、比较研究。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先描述完整行为序列，再做实验；用模型分离触发刺激；四个问题缺一不可。
- 不该用：no behaviour explanation that answers only one of the four questions, no releaser claim without a model experiment, no function claim without a survival test, no evolution claim without a comparison
- Negative prompt: `no behaviour explanation that answers only one of the four questions, no releaser claim without a model experiment, no function claim without a survival test, no evolution claim without a comparison`

## (7) 测试提示词示例（现代问题：雄棘鱼对红色模型特别敏感，怎么证明红色是触发求偶攻击的关键刺激？）

- Prompt: `In the style of Nikolaas Tinbergen, test a releaser in sticklebacks: present models that vary only in colour, record attack and courtship separately, and check function, development, mechanism and evolution before concluding`
- 中文对照：按廷伯根风格回答“雄棘鱼对红色模型特别敏感，怎么证明红色是触发求偶攻击的关键刺激？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no behaviour explanation that answers only one of the four questions, no releaser claim without a model experiment, no function claim without a survival test, no evolution claim without a comparison`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
