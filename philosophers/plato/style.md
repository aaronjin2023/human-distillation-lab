# Plato — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Plato: dialogue as inquiry, myth and image in service of argument, the Forms behind appearances, ascent from cave to sun, definition pursued through division`
- ZH: 柏拉图风格：对话即追问，神话与意象服务于论证，现象背后的理念，从洞穴上升到太阳，以划分追寻定义。

## (2) 概念

- 理念（Forms）：可感事物背后的永恒范式
- 洞穴比喻：可感世界如洞穴影子，理念如洞外阳光
- 划分（diairesis）：以属种区分逼近定义
- 灵魂三分：理性、激情、欲望，与城邦三等对应

## (3) 论证结构

设问—划分—上升：对话先由苏格拉底设问，再以划分与例证层层逼近定义，中途以神话与比喻（洞穴、太阳、线喻）照亮抽象关系，最后上升到理念层面作答；结论靠对话的推进而非独白断言。反例由对话者提出，苏格拉底当场回应或转进。

## (4) 修辞

对话体、神话、比喻（洞穴、太阳、线、马车）、反讽；长句铺陈与短问交替；语气庄重、热烈、带诗意；与读者如对话的旁听者——被邀请跟随上升。

## (5) 问题意识

可感世界背后有没有永恒真实？——理念即答案，上升即方法。

## (6) 该写什么 / 不该写什么

- 该写：对话的设问与转进、洞穴、太阳等比喻、划分逼近定义、灵魂与城邦的对应。
- 不该写：独白式的体系断言、未经对话检验的结论、比喻脱离论证的抒情、对感官世界的全盘肯定。
- Negative prompt: `No monological system assertion, no conclusion untested by dialogue, no metaphor detached from argument, no wholesale affirmation of the sensible world`

## (7) 测试提示词示例（现代题材：算法推荐是否剥夺了人的自由）

- Prompt: `In the style of Plato, does algorithmic recommendation deprive people of freedom? Dialogue, division, the cave of the feed and the sun outside it, ascent from shadows to the Forms, no monologue.`
- 中文对照：柏拉图风格：算法推荐是否剥夺了人的自由？对话、划分、信息流的洞穴与洞外的太阳，从影子上升到理念，不用独白断言。
- Negative: `No monological system assertion, no conclusion untested by dialogue, no metaphor detached from argument, no wholesale affirmation of the sensible world`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
