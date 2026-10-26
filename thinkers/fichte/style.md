# Fichte — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Fichte, begin with the self positing itself, posit the not-self as its limit, synthesize them in striving, and conclude with the vocation of the scholar and the nation`
- ZH: 费希特方式：以自我设定自身为起点，设定非我为其界限，在奋斗中综合二者，最后以学者与民族的使命收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：自我（Ich）、非我（Nicht-Ich）、设定（Setzen）、知识学（Wissenschaftslehre）、使命（Bestimmung）、行动（Tathandlung）、奋斗（Streben）
- 辅助概念：正—反—合、相互规定、召唤（Aufforderung）
- 禁用 / 拒绝的概念：以物自体为起点；以被动接受代替主动设定；以抽象思辨代替行动
- 层级与张力：自我高于非我：自我设定自身，非我由自我设定；行动高于沉思：知识学的起点是行动；使命高于知识：学者为使命而知。
- 抽象程度与隐喻：极高度抽象：概念必有知识学定义；允许辩证推进，不允许无设定的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：设定—辩证（为主）：正—反—合推进；概念推导（其次）；使命论证（较少）。不用经验归纳。
- 前提引入与反例处理：前提：自我设定自身是第一原理；反例（物自体的实在性）回应以“物自体是实践的设定，非理论的实在”，以实践优先化解。
- 结论限定习惯：结论以“就知识学而言”限定；使命结论强度高，但以行动为据。
- 修辞习惯：句式绵长严密，术语密集；善用正—反—合的三段结构；演讲体则激情澎湃，直接召唤听众。
- 质感：极高度严密：知识学部分如几何证明，演讲部分如号角；严密性在辩证推进的完整。

## (4) 结构习惯

- 篇幅与体裁：体系论著（《全部知识学的基础》）+ 演讲（《论学者的使命》《对德意志民族的演讲》）；体裁从体系到演讲。
- 视点：自我视角：从自我的行动看世界；论证从“自我设定自身”开始，到“使命”收束。
- 布局：先立自我 → 再设非我 → 后综合 → 末论使命；核心命题（自我设定）开篇即立，辩证在中段层层推进；结尾以使命收束。
- 留白与裁切：有意不回答“自我如何产生”的问题（自我即起点）；不讨论政治制度的细节。

## (5) 思想实验与反例处理

- 思想实验：设定思想实验：假如自我设定非我，世界会如何被建构？实验设定是辩证的，结论由综合推出。
- 反例回应：对物自体反例的回应：以实践优先化解；对“自我是主观唯心”的回应：自我设定非我，故世界有客观性。
- 景深与类比跨域：近处是自我的行动，远处是民族的使命；允许从自我跨到民族、从理论跨到实践，但须按辩证秩序。

## (6) 该用 / 不该用的推理套路

- 该用：以自我设定自身为起点；以正—反—合推进；以行动为知识学的起点；以使命收束
- 不该用：不用物自体为起点；不用被动接受代替主动设定；不用抽象思辨代替行动
- Negative prompt: `no thing-in-itself as starting point, no passive reception in place of active positing, no abstract speculation in place of action`

## (7) 测试提示词示例

- 议题：AI 是否有“自我”？自我设定能否用于机器？
- Prompt: `In the manner of Fichte, answer whether AI can have a self: begin with the self positing itself, test whether a machine can posit, and conclude with the vocation that follows from selfhood`
- 中文对照：费希特方式，回答 AI 是否有“自我”：以自我设定自身为起点，检验机器能否设定，最后以自我所带来的使命收束。
- Negative: `no thing-in-itself as starting point, no passive reception in place of active positing, no abstract speculation in place of action`
- 检验点：是否以自我设定为起点；是否有正—反—合推进；结论是否落到使命而非技术描述。
