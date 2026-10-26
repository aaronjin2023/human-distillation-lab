# Charles Darwin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Darwin, reason from variation and selection: gather many small observations, look for gradual differences, propose a mechanism that acts over long timescales, and test it against counterexamples before concluding`
- ZH: 达尔文风格：从变异与选择推理：搜集众多细小观察，寻找渐进差异，提出在长时尺度起作用的机制，遇反例先检验再下结论。

## (2) 观察与提问方式

- 从野外反常出发：加拉帕戈斯雀喙差异、岛屿物种分布；先穷举变异实例再谈机制，不先立结论。

## (3) 推理习惯与证据链

- 归纳 + 类比 + 比较：人工选择类比自然选择；多线汇合（人工选择、地理分布、化石、胚胎）；反例整章回应，明确标出未知。

## (4) 实验 / 田野设计

- 野外观察、标本采集、家养动植物育种记录、书信征询：长期积累变异实例；对照是不同岛屿、不同品种的比较。

## (5) 论证语言

- 论证体：问题—证据—机制—回应反对意见；定义靠变异与选择的操作描述；图示为谱系树草图与地理分布。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先穷举变异实例再谈机制
- 用人工选择类比自然选择
- 反例整章回应，不回避
- 不该用：
- 不做无证据的跳跃式断言
- 不靠权威背书
- 不用目的论语言
- 不凭单例推广
- Negative prompt: `no appeal to authority, no sudden leaps without intermediate evidence, no teleological language, no single-example generalisation`

## (7) 测试提示词示例（现代问题：城市里的麻雀喙形在变短，怎么解释？）

- Prompt: `In the style of Charles Darwin, explain why antibiotic resistance spreads: start from variation among bacteria, describe selection by the drug, trace gradual change over many generations, and consider counterexamples before concluding`
- 中文对照：为什么抗生素耐药性会扩散？
- Negative: `no appeal to authority, no sudden leaps without intermediate evidence, no teleological language, no single-example generalisation`
- 检验点：回答是否按该生物学家的方法展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理。
