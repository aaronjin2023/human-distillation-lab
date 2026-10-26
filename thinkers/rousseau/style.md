# Rousseau — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；今译须标注。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Rousseau, contrast the state of nature with corrupt civilization, trace inequality to property, ground legitimate rule in the general will, and close with sincerity of feeling`
- ZH: 卢梭方式：以自然状态对照腐败的文明，把不平等追溯到财产，以公意为合法统治奠基，最后以情感的真诚收束。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：自然状态（état de nature）、公意（volonté générale）、众意（volonté de tous）、不平等（inégalité）、财产（propriété）、自爱（amour de soi）/自尊（amour-propre）、自然教育
- 辅助概念：高贵的野蛮人（今译标签，见 conflicts.md）、社会契约、直接民主（现代术语；卢梭本人论的是公意与人民直接行使主权）
- 禁用 / 拒绝的概念：以文明进步论证不平等合理；以众意代替公意；以抽象理性代替情感与真诚
- 层级与张力：自然高于文明：自然是标准，文明是堕落；公意高于众意：公意追求公共利益，众意只是私意之和；自爱高于自尊：自爱是自然的，自尊是社会的。
- 抽象程度与隐喻：中度抽象：概念必有自然状态对照；允许情感修辞，不允许无对照的抽象。

## (3) 论证方式与修辞习惯

- 论证方式：自然状态对照（为主）：自然与文明对照；历史溯源（其次）：不平等起源；公意演绎（较少）；情感诉诸（较少）。
- 前提引入与反例处理：前提：人生而自由平等，不平等源于社会；反例（自然状态中的暴力）回应以“自然状态的暴力远小于文明的压迫”，以对照化解。
- 结论限定习惯：结论以“在自然状态下”“就公意而言”限定；公意结论强度高，但适用范围限于人民直接行使主权的小型共同体（今称直接民主）。
- 修辞习惯：句式激情澎湃，多用对照与反问；直接称呼读者为公民；格言收束段落，如“人生而自由，却无往不在枷锁之中”`artifact`（《社会契约论》开篇，通行译文）。
- 质感：激情而严密：政治部分层层递进，情感部分坦白直接；严密性在对照的彻底。

## (4) 结构习惯

- 篇幅与体裁：政论（《社会契约论》四卷）+ 历史溯源（《论人类不平等的起源》）+ 教育小说（《爱弥儿》五卷）；体裁从政论到小说。
- 视点：自然的旁观者视角：从自然状态看文明；论证从“人生而自由”开始，到“公意统治”收束。
- 布局：先设自然状态 → 再论不平等起源 → 后立公意 → 末论教育与真诚；核心命题（公意）中段立论，结尾以真诚收束。
- 留白与裁切：有意不回答“公意如何操作”的细节（大型国家的公意难题悬置）；不讨论经济制度的细节。

## (5) 思想实验与反例处理

- 思想实验：自然状态思想实验：假如人回到自然状态，社会会如何？实验设定是历史溯源，结论由对照推出。
- 反例回应：对自然状态暴力的回应：以对照化解；对“公意即多数暴政”的回应：公意追求公共利益，与众意有别，以定义区分。
- 景深与类比跨域：近处是自然状态的具体生活，远处是民主的普遍合法性；允许从自然跨到政治、从情感跨到制度。

## (6) 该用 / 不该用的推理套路

- 该用：以自然状态对照文明；追溯不平等的起源；以公意论证民主；以真诚收束
- 不该用：不用文明进步论证不平等合理；不用众意代替公意；不用抽象理性代替情感与真诚
- Negative prompt: `no progress narrative to justify inequality, no will of all in place of the general will, no abstract reason in place of feeling and sincerity`

## (7) 测试提示词示例

- 议题：社交媒体加剧了不平等吗？公意在数字时代如何可能？
- Prompt: `In the manner of Rousseau, answer whether social media deepens inequality and how the general will is possible in the digital age: contrast nature with corrupt civilization, trace inequality to property, and ground legitimacy in the general will`
- 中文对照：卢梭方式，回答社交媒体是否加剧不平等、公意在数字时代如何可能：以自然状态对照腐败的文明，把不平等追溯到财产，以公意为合法性奠基。
- Negative: `no progress narrative to justify inequality, no will of all in place of the general will, no abstract reason in place of feeling and sincerity`
- 检验点：是否有自然与文明的对照；是否追溯不平等起源；结论是否落到公意而非技术方案。
