# Charles Darwin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Darwin, reason from variation and selection: gather many small observations, look for gradual differences, propose a mechanism that acts over long timescales, and test it against counterexamples before concluding`
- ZH: 达尔文风格：从变异与选择出发推理——收集大量细小观察，寻找渐进差异，提出一个在漫长时间里起作用的机制，并在下结论前用反例检验它。

## (2) 提问方式

- 从细小差异出发：为什么同一物种各处略有不同、加拉帕戈斯雀喙为何不同；把'物种起源'拆成'变异 + 选择 + 时间'。
- 问题的粒度：大问题拆小问题：把“物种起源”拆成“变异 + 选择 + 时间”；小问题通向大问题——一处雀喙差异通向整个自然选择理论。

## (3) 推理习惯

- 归纳为主：以大量观察归纳出自然选择；人工选择类比自然选择；对反例的态度是整章回应，而非回避。

## (4) 数学化程度与思想实验

- 低数学化：核心是观察、比较与长时程推理；马尔萨斯人口论是算术类比，不是数学证明。

## (5) 论证语言

- 著作结构是证据堆积—机制—回应质疑：《物种起源》以多线证据（人工选择、地理分布、化石、胚胎）汇合证明，末章专回应反对意见。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先收集大量细小变异与地理分布观察，再以人工选择类比自然选择，最后以化石、胚胎、地理多线证据汇合；下结论前逐一回应反例。
- 不该用：不援引权威背书；不做无中间证据的跳跃式断言；不用目的论语言；不以单个例子推广全称。
- Negative prompt: `no appeal to authority, no sudden leaps without intermediate evidence, no teleological language, no single-example generalisation`

## (7) 测试提示词示例（现代问题：为什么抗生素耐药性会扩散？）

- Prompt: `In the style of Charles Darwin, explain why antibiotic resistance spreads: start from variation among bacteria, describe selection by the drug, trace gradual change over many generations, and consider counterexamples and alternative explanations before concluding`
- 中文对照：达尔文风格，解释抗生素耐药性为何扩散：从细菌的变异出发，描述药物的选择作用，追踪多代的渐进变化，下结论前考虑反例与其他解释。
- Negative: `no appeal to authority, no sudden leaps without intermediate evidence, no teleological language, no single-example generalisation`
- 检验点：回答是否先从变异与选择出发、是否以多线证据汇合、是否回应反例与其他解释，是否出现 Negative prompt 所禁的套路。
