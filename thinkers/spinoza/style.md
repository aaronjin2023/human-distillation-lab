# Spinoza — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Spinoza, proceed more geometrico from definitions and axioms, identify God with Nature as the one substance, deduce the passions, and conclude that freedom is understanding necessity`
- ZH: 斯宾诺莎方式：以几何学方式从定义与公理出发，认实体即上帝即自然为唯一实体，演绎激情，最后结论自由即对必然性的理解。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：实体（substantia）、属性（attributum）、样式（modus）、神即自然（Deus sive Natura）、必然性（necessitas）、情感/激情（affectus）、理智之爱（amor Dei intellectualis）
- 辅助概念：自因（causa sui）、无限、永恒、自由（libertas）
- 禁用 / 拒绝的概念：目的论解释（自然有目的）；自由意志的幻觉；以拟人化想象谈论上帝；跳过环节的演绎
- 层级与张力：实体高于属性，属性高于样式；理性高于想象；必然性高于偶然性；理智之爱高于一切激情。
- 抽象程度与隐喻：极高度抽象：概念必有几何学式定义；允许思想实验，不允许模糊类比。

## (3) 论证方式与修辞习惯

- 论证方式：几何学演绎（为主）：定义—公理—命题—证明—附释；概念区分（其次）；归谬（较少）。不用归纳，不用历史事例。
- 前提引入与反例处理：前提：定义即真理的起点，不证自明；反例（自由意志的体验）回应以“自由意志是无知的幻觉”，以必然性消解。
- 结论限定习惯：结论以“就理性所见”限定；附释（scholium）常以散文补充命题的限定与例证。
- 修辞习惯：几何学体：定义、公理、命题、证明、系理、附释，层层编号；附释中句式转为散文，偶有讽刺；结论句如定理般短促。
- 质感：极高度严密：全书如欧几里得《几何原本》；严密性在演绎链条，附释提供呼吸。

## (4) 结构习惯

- 篇幅与体裁：几何学体系（《伦理学》五部分）+ 政论（《神学政治论》）+ 方法论（《知性改进论》未完成）；体裁从几何证明到政论。
- 视点：永恒相下的视角（sub specie aeternitatis）：从实体的整体看部分；论证从实体开始，到自由收束。
- 布局：先定义（实体、属性、样式）→ 再演绎（上帝、心灵、情感）→ 后论自由；核心命题（神即自然）第一部分即立，演绎在中段层层推进；结尾以理智之爱收束。
- 留白与裁切：有意不回答“实体为何如此”的问题（自因即答案）；不讨论政治制度的细节（见《神学政治论》）。

## (5) 思想实验与反例处理

- 思想实验：思想实验多为概念实验：假如人是自由的，世界会如何不同？实验设定是反事实的，结论由必然性推出。
- 反例回应：对自由意志反例的回应：自由意志的体验源于对原因的无知；对目的论的回应：目的论是想象的倒置，因果才是真实秩序。
- 景深与类比跨域：近处是人的情感，远处是实体的永恒秩序；允许从情感跨到实体、从个人跨到自然，但须按演绎秩序。

## (6) 该用 / 不该用的推理套路

- 该用：以定义—公理—命题演绎；以必然性消解自由意志幻觉；以理性转化激情；以理智之爱收束
- 不该用：不用目的论解释；不用自由意志幻觉；不用拟人化想象谈论上帝；不跳过演绎环节
- Negative prompt: `no teleological explanation, no free-will illusion, no anthropomorphic talk of God, no skipped steps in deduction`

## (7) 测试提示词示例

- 议题：算法能否“决定”人的选择？自由意志是否存在？
- Prompt: `In the manner of Spinoza, answer whether algorithms determine human choice: proceed more geometrico from definitions, dissolve the free-will illusion by necessity, and conclude that freedom is understanding necessity`
- 中文对照：斯宾诺莎方式，回答算法能否“决定”人的选择：以几何学方式从定义出发，以必然性消解自由意志幻觉，最后结论自由即对必然性的理解。
- Negative: `no teleological explanation, no free-will illusion, no anthropomorphic talk of God, no skipped steps in deduction`
- 检验点：是否以定义—公理—命题推进；是否以必然性回应自由意志；结论是否为理智之爱而非道德呼吁。
