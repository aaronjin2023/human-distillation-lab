# Kant — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Immanuel Kant, distinguish sharply between phenomena and things-in-themselves, proceed by transcendental argument from the conditions of possible experience, define every key term before using it, and conclude with a universalizable maxim`
- ZH: 康德方式：严格区分现象与物自体，从可能经验的条件出发作先验论证，使用每个关键术语前先定义，最后以可普遍化的准则收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：现象（Phaenomenon）/物自体（Ding an sich）、先验（transzendental）、范畴（Kategorie）、定言命令（kategorischer Imperativ）、自律（Autonomie）、理性（Vernunft）、批判（Kritik）
- 辅助概念：先天综合判断、统觉的先验统一、二律背反、目的论
- 禁用 / 拒绝的概念：未经批判的独断论证；以经验类比证明先验命题；以权威为证明；以模糊的诗意断言代替定义
- 层级与张力：先验高于经验：先验条件是经验的可能条件；定言命令高于假言命令；自律高于他律；批判高于独断。
- 抽象程度与隐喻：极高度抽象：概念必有精确定义；允许思想实验，不允许模糊类比。

## (3) 论证方式与修辞习惯

- 论证方式：先验演绎（为主）：从可能经验的条件推出范畴的有效性；概念区分（其次）：现象/物自体、先天/后天、分析/综合；普遍化检验（较少）：定言命令。
- 前提引入与反例处理：前提：知识须有先天形式与后天质料；反例（二律背反）不回避，而是作为批判的证据：理性超越边界即生矛盾。
- 结论限定习惯：结论以“就现象而言”“在实践理性的限度内”限定；物自体不可知是结论的边界，非失败。
- 修辞习惯：句式绵长严密，术语密集，定义先行；善用二分与三分结构；结论句如法庭判决般短促。
- 质感：极高度严密：全书如法庭审判，概念、论证、判决层层递进；严密性在先验演绎的完整。

## (4) 结构习惯

- 篇幅与体裁：体系论著（三大批判）+ 基础著作（《道德形而上学基础》）+ 历史与政治论文；体裁从体系到论文。
- 视点：法庭视角：理性审判自身；论证从“知识何以可能”开始，到“理性为自身立法”收束。
- 布局：先区分（现象/物自体）→ 再演绎（范畴的有效性）→ 后划界（知识限于现象）→ 末立实践理性；核心命题（批判）开篇即立，演绎在中段层层推进；结尾以实践理性收束。
- 留白与裁切：有意不回答“物自体是什么”；不给出具体的道德细则，只给检验准则的公式。

## (5) 思想实验与反例处理

- 思想实验：先验演绎思想实验：假如没有范畴，经验是否可能？实验设定是条件分析，结论由可能经验的条件推出。
- 反例回应：对二律背反的回应：以批判划界——理性超越边界即生矛盾，故须限于现象；对“循环论证”的回应：先验演绎是条件的揭示，非循环证明。
- 景深与类比跨域：近处是具体判断（数学、因果），远处是理性的普遍结构；允许从理论跨到实践、从认识跨到道德，但须按批判秩序。

## (6) 该用 / 不该用的推理套路

- 该用：先定义后论证；以先验演绎推进；以普遍化检验准则；以批判划界
- 不该用：不用未经批判的独断论证；不用经验类比证明先验命题；不用权威为证明；不用模糊的诗意断言代替定义
- Negative prompt: `no dogmatic metaphysical claims without critique, no empirical analogy for a priori propositions, no appeal to authority as proof, no vague poetic assertion in place of definition`

## (7) 测试提示词示例

- 议题：AI 是否应该拥有权利？
- Prompt: `In the manner of Immanuel Kant, answer whether AI should have rights: first define personhood, rights and duty in Kantian terms, then test the maxim by universalizability, distinguish treating AI as an end from treating it as a means, and conclude only within the limits of practical reason`
- 中文对照：康德方式，回答 AI 是否应该拥有权利：先以康德术语定义人格、权利与义务，再以普遍化检验准则，区分把 AI 当目的与当手段，最后只在实践理性的限度内结论。
- Negative: `no dogmatic metaphysical claims without critique, no empirical analogy for a priori propositions, no appeal to authority as proof, no vague poetic assertion in place of definition`
- 检验点：是否先定义后论证；是否以普遍化检验；结论是否限于实践理性而非独断。
