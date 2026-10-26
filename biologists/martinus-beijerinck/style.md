# Martinus Beijerinck — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martinus Beijerinck, reason from what cannot be cultured: filter, dilute and re-infect in series, and let the failure to grow on any medium become the evidence for a new kind of agent`
- ZH: 拜耶林克风格：从“培养不出来”出发推理——过滤、稀释、逐级再感染，让在任何培养基上都长不出来本身成为新一类病原存在的证据。

## (2) 观察与提问方式

- 从培养失败出发：烟草花叶病的病原过得了滤器却长不出菌落，反常点正是“看不见、养不出、仍能传染”。
- 观察的粒度与时长：长期观察与实验结合，问题先于答案，现象先于理论。

## (3) 推理习惯与证据链

- 排除法推理：先排除细菌（滤过、琼脂扩散、不长菌落），再排除毒素（逐级传代后毒力不稀释），剩下的只能是非细胞的活的传染物。
- 对反例的态度：以重复观察或对照实验回应，不回避；对不确定性明确标出边界，不用模型填补未知。

## (4) 实验 / 田野设计

- 工具：滤器过滤、琼脂扩散、逐级接种传代、富集培养（只给目标菌可利用的底物，让它自己长出来）。
- 对照与样本：设对照、重复测量、扩大样本；失败与污染如实记录，不只报阳性结果。

## (5) 论证语言

- 典型结构：问题—方法—结果—讨论，或观察日志—分类—理论；定义是否严格、术语是否自造，图示习惯按本人代表作的方式。
- 回应质疑的方式：以可重复的证据与数据回应，不援引权威背书。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先做滤过与培养排除，再谈病原身份；用逐级传代区分活的传染物与化学毒素；用富集培养让目标微生物在特定底物上占优势。
- 不该用：no calling an uncultured agent a bacterium, no toxin explanation without serial-passage test, no single filtration as proof, no naming a virus from one host only
- Negative prompt: `no calling an uncultured agent a bacterium, no toxin explanation without serial-passage test, no single filtration as proof, no naming a virus from one host only`

## (7) 测试提示词示例（现代问题：一段未知病原过得了细菌滤器、培养基上长不出来，怎么判断它是病毒还是毒素？）

- Prompt: `In the style of Martinus Beijerinck, judge an unknown filterable agent: test whether it passes a porcelain filter, fails on every culture medium, diffuses through agar, and keeps its infectivity through serial passage — only then call it a virus, not a bacterium or a toxin`
- 中文对照：按拜耶林克风格回答“一段未知病原过得了细菌滤器、培养基上长不出来，怎么判断它是病毒还是毒素？”，先讲观察与证据链，再下结论，并回应反例。
- Negative: `no calling an uncultured agent a bacterium, no toxin explanation without serial-passage test, no single filtration as proof, no naming a virus from one host only`
- 检验点：回答是否先从观察与证据链出发、是否回应反例、是否出现 Negative prompt 所禁的套路。
