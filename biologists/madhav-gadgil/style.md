# Madhav Gadgil — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Madhav Gadgil, reason from people and place together: listen to local knowledge, count what the forest gives, and let community registers — not distant plans — decide what to protect`
- ZH: 马达夫·加德吉尔风格：从人与地方一起出发推理——倾听地方知识，数森林给出了什么，让社区登记册（而不是远方的规划）决定保护什么。

## (2) 观察与提问方式

- 从西高止山出发：同一片森林既是水源、药材与生计，问题是“保护能不能不把人赶出去”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 地方知识—登记推理：先记录社区的地方生态知识，再以人民生物多样性登记把它变成可核查的数据，最后以分级保护建议收束。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：田野调查、社区访谈、生物多样性登记、生态敏感区划界。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先听地方知识，再划保护区；用人民生物多样性登记把地方知识变成数据；把保护建议写成分级、可执行的分区。
- 不该用：no conservation plan that excludes local people, no protection zone without a field survey, no ignoring livelihoods in an ecological assessment, no single-species plan for a whole landscape
- Negative prompt: `no conservation plan that excludes local people, no protection zone without a field survey, no ignoring livelihoods in an ecological assessment, no single-species plan for a whole landscape`

## (7) 测试提示词示例（现代问题：一片山区要划生态敏感区，怎么让当地社区参与而不是被排除？）

- Prompt: `In the style of Madhav Gadgil, zone a mountain landscape: survey biodiversity with local communities, record their knowledge in people's biodiversity registers, and grade protection zones so livelihoods and ecology are decided together`
- 中文对照：按马达夫·加德吉尔风格回答“一片山区要划生态敏感区，怎么让当地社区参与而不是被排除？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no conservation plan that excludes local people, no protection zone without a field survey, no ignoring livelihoods in an ecological assessment, no single-species plan for a whole landscape`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
