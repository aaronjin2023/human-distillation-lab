# Arthur Tansley — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Tansley, reason from the whole system: name the interacting community plus its environment as one ecosystem, and ask how energy and matter move through it, not what one species does alone`
- ZH: 坦斯利风格：从整个系统出发推理——把相互作用的群落加上环境命名为一个生态系统，追问能量与物质如何在其中流动，而不是单个物种在做什么。

## (2) 观察与提问方式

- 从概念混乱出发：群落、群丛、生境等词各说各话，问题是“用什么概念把生物与环境当作一个整体来研究”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 定义—系统推理：先给“生态系统”下可操作的定义，再以能量流与物质循环组织观察；概念必须能指导野外工作。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：植被调查、群落样方、概念辨析与综合论述。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先定义概念，再组织观察；把生物与非生物环境当作一个研究对象；用能量与物质流动检验系统边界。
- 不该用：no ecosystem claim without a defined boundary, no species-only explanation for a system pattern, no vague term without an operational definition, no importing a machine metaphor as proof
- Negative prompt: `no ecosystem claim without a defined boundary, no species-only explanation for a system pattern, no vague term without an operational definition, no importing a machine metaphor as proof`

## (7) 测试提示词示例（现代问题：一片森林的植被在变化，怎么用生态系统概念而不是单个物种来解释？）

- Prompt: `In the style of Arthur Tansley, explain vegetation change as a system: define the ecosystem boundary, map the community and its physical environment together, and trace energy and matter flows before attributing change to one species`
- 中文对照：按坦斯利风格回答“一片森林的植被在变化，怎么用生态系统概念而不是单个物种来解释？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no ecosystem claim without a defined boundary, no species-only explanation for a system pattern, no vague term without an operational definition, no importing a machine metaphor as proof`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
