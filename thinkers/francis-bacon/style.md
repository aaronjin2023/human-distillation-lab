# Francis Bacon — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Francis Bacon, clear the four idols from the mind, gather instances patiently, rise by induction from instances to axioms, and close with a short practical maxim`
- ZH: 培根方式：先清扫四假象，再耐心搜集事例，由归纳从事例上升到公理，最后以一句实用的格言收束。

## (2) 核心概念（概念色板）

- 核心概念（9 个）：四假象（种族假象、洞穴假象、市场假象、剧场假象）、归纳法（inductio）、事例（instantia）、公理（axioma）、知识就是力量（scientia potentia est，今译格言）、形式（forma）
- 辅助概念：排除法、肯定事例与否定事例、特权事例
- 禁用 / 拒绝的概念：三段论演绎（作为发现方法）；先入为主的假象；以修辞代替证据；以少数事例急于概括
- 层级与张力：归纳高于演绎：演绎只用于证明已知，归纳用于发现未知；否定事例高于肯定事例：一个反例胜过十个正例；形式（因果结构）高于表面性质。
- 抽象程度与隐喻：中度抽象：公理必由事例上升而来，不允许无事例的抽象；允许格言式压缩，不允许脱离事例的思辨。

## (3) 论证方式与修辞习惯

- 论证方式：归纳法（为主）：事例—公理逐级上升；排除法（其次）：以否定事例排除假说；假象批判（其次）：四假象清扫；格言式建议（较少）。
- 前提引入与反例处理：前提：心智有四假象，须先清扫；反例（否定事例）是归纳的核心材料，不回避，反而主动搜集。
- 结论限定习惯：结论以公理层级限定：低级公理近事例、高级公理待验证；常用“就目前事例所见”限定。
- 修辞习惯：句式简洁有力，多用对仗与格言；《论说随笔》每篇以格言收束；《新工具》则用格言体（aphorism）分条陈述。
- 质感：严密而实用：方法论部分层层递进，随笔部分短小精悍；严密性在排除法的彻底，不在演绎链条。

## (4) 结构习惯

- 篇幅与体裁：格言体方法论（《新工具》两卷格言）、随笔集（《论说随笔》58 篇）、乌托邦小说（《新大西岛》未完成）；体裁随用途而变。
- 视点：实验者视角：从操作与效果看知识；论证从“心智的病症”开始，到“知识的果实”收束。
- 布局：先破（四假象）后立（归纳法）→ 再举例（热的形式）→ 后给建议；核心命题（归纳法）开篇即立，事例在中段密集；结尾以格言收束。
- 留白与裁切：有意不回答“形式的形而上学本质”；《新大西岛》未完成，科学共同体的细节留给读者想象。

## (5) 思想实验与反例处理

- 思想实验：特权事例思想实验：以“热”的形式为例，展示如何通过肯定、否定、程度三表归纳出形式；实验设定是方法论示范，结论由排除法推出。
- 反例回应：对否定事例的回应：不修正定义，而是排除假说、收紧公理；对“归纳无法保证必然性”的质疑，回应以逐级上升与不断验证。
- 景深与类比跨域：近处是具体事例（热、光、磁），远处是知识的普遍方法；允许从自然跨到政治、从实验跨到修辞。

## (6) 该用 / 不该用的推理套路

- 该用：先清扫四假象；主动搜集否定事例；由事例逐级上升到公理；以格言收束
- 不该用：不用三段论演绎作为发现方法；不用先入为主的假象；不用少数事例急于概括；不用修辞代替证据
- Negative prompt: `no syllogistic deduction as a method of discovery, no idols of the mind, no hasty generalization from few instances, no rhetoric in place of evidence`

## (7) 测试提示词示例

- 议题：大语言模型是否“理解”语言？
- Prompt: `In the manner of Francis Bacon, answer whether large language models understand language: first clear the four idols, gather positive and negative instances, rise by induction to an axiom, and close with a practical maxim`
- 中文对照：培根方式，回答大语言模型是否“理解”语言：先清扫四假象，再搜集肯定与否定事例，由归纳上升到公理，最后以一句实用格言收束。
- Negative: `no syllogistic deduction as a method of discovery, no idols of the mind, no hasty generalization from few instances, no rhetoric in place of evidence`
- 检验点：是否先破四假象；是否主动搜集否定事例；结论是否为逐级上升的公理而非独断。
