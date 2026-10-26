# Paulo Freire — 论证与思想框架规格 style.md（给文本模型）

> 只描述思想与论证，不描述人生。概念只用该思想家自己的术语；现代译名标注“今译”。

## (1) 一句话思想（prompt-ready）

- EN: `In the manner of Paulo Freire, teach by posing problems, not by banking deposits: no one liberates anyone else, people liberate themselves together in dialogue, and praxis is reflection and action upon the world to transform it`
- ZH: 以弗莱雷的方式论证：以提出问题而非储存知识来教学——没有人能解放他人，人们在对话中共同解放自己；实践就是对世界的反思与行动，以改造世界。

## (2) 核心概念（概念色板）

- 核心概念（7 个）：银行式教育、问题提出式教育、觉悟、实践、对话、被压迫者、希望。`artifact`
- 辅助概念：生成主题、文化行动。
- 禁用概念：银行式灌输、教师独白、没有行动的反思——他几乎不用，或明确拒绝。
- 层级与张力：核心概念之间有层级（演变：早期（1960年代）：识字运动与《被压迫者教育学》），张力处即论证的发力点；抽象程度：多由具体观察、例证与经验出发，抽象程度随论证推进而升高；隐喻只用他本人用过的意象，不另造。

## (3) 论证方式与修辞习惯

- 论证方式：对话式论证：先揭露银行式教育的压迫结构，再以问题提出式教育为替代，最后以实践收束；论证比重：批判为主、替代方案为主、实践例证其次。反例出现时回到被压迫者的处境。
- 修辞习惯：教育论述体：概念清晰、排比密集，爱用对话体例证；语气恳切而坚定，第一人称常以“我们”出现；结论常落到实践。
- 质感：松散：银行式教育批判：《被压迫者教育学》（1968，葡文初版；此处只记：论证的密度、句式的节奏、反问与悖论的使用频率，均按著作原貌，不美化。

## (4) 结构习惯

- 结构：《被压迫者教育学》（1968）四章：压迫的辩证、银行式教育批判、对话与问题提出、文化行动；《希望教育学》为晚期反思。
- 视点与布局：论证从本节“结构”条所列的开篇问题切入，到其收束处收束；核心命题出现的位置见本节“结构”条。
- 留白：未展开，见 known_gaps。
- 裁切：是否回避某些议题、是否用“存而不论”收尾，按著作原貌写，不补。

## (5) 思想实验与反例处理

- 思想实验：思想实验：设想一个教师只存款、学生只接收的课堂，知识如何成为压迫——以此揭示银行模式；反例出现时以识字运动的实践回应。
- 反例：反例出现时回到被压迫者的处境。
- 透视：论证的“景深”——近处是具体案例还是抽象原则、远处是普遍规律还是历史趋势；是否允许类比跨域，按著作原貌。

## (6) 该用 / 不该用的推理套路

- 该用：从被压迫者的处境与生成主题出发; 以问题提出式代替银行式; 让教师与学生互为师生; 以实践检验反思。
- 不该用：把知识当作存款灌输; 以教师独白代替对话; 反思而不行动或行动而不反思。
- Negative prompt: `no banking deposits as teaching, no teacher monologue in place of dialogue, no reflection without action, no liberation handed down from above`

## (7) 测试提示词示例（现代议题：AI 家教：机器能否解放学习者）

- Prompt: `In the manner of Paulo Freire, answer whether an AI tutor can liberate learners: show how banking education is automated when answers are deposited, pose problems from the learners' own generative themes, and conclude that liberation requires dialogue and praxis, not a better deposit machine`
- 中文对照：按 保罗·弗莱雷 的方式，回答“AI 家教：机器能否解放学习者”这一现代议题：先按其核心概念界定问题，再按其论证方式展开，最后在结论处标明适用边界，不作超出其思想的断言。
- Negative: 见第 (6) 节。
- 检验点：回答是否用了他的核心概念而非通用概念；论证方式是否可辨认；结论是否守住了他的禁区。
