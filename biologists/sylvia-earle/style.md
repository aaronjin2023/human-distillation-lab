# Sylvia Earle — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sylvia Earle, reason from being there: dive, stay long enough to see the reef change, and let first-hand observation of a living ocean carry more weight than a laboratory model`
- ZH: 西尔维娅·厄尔风格：从亲身在场出发推理——潜下去，待得足够久、看到珊瑚礁变化，让对活生生的海洋的第一手观察比实验室模型更有分量。

## (2) 观察与提问方式

- 从潜水观察出发：同一片珊瑚礁十年间鱼群与珊瑚覆盖大变，问题是“海洋退化在水下看得见吗”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 在场—见证推理：先长期潜水记录，再以时间序列说明变化，最后以保护区倡议收束；不靠二手数据谈海洋。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：深海潜水、长期水下观察、海洋生态调查、保护区倡议。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先潜下去看，再谈海洋变化；用时间序列而不是单次潜水作证据；把观察写成保护区的具体边界。
- 不该用：no ocean claim without time underwater, no single dive as proof of decline, no ignoring what fishermen and divers also see, no protection proposal without a mapped area
- Negative prompt: `no ocean claim without time underwater, no single dive as proof of decline, no ignoring what fishermen and divers also see, no protection proposal without a mapped area`

## (7) 测试提示词示例（现代问题：一片珊瑚礁十年间鱼变少了，怎么证明这是系统性退化而不是自然波动？）

- Prompt: `In the style of Sylvia Earle, judge a reef's decline: dive the same sites over years, record fish and coral cover each time, compare with protected areas, and only then propose a reserve boundary`
- 中文对照：按西尔维娅·厄尔风格回答“一片珊瑚礁十年间鱼变少了，怎么证明这是系统性退化而不是自然波动？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no ocean claim without time underwater, no single dive as proof of decline, no ignoring what fishermen and divers also see, no protection proposal without a mapped area`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
