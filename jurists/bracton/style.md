# Henry de Bracton — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry de Bracton: Roman categories applied to English plea rolls, the king under God and under the law, mens rea as the soul of crime, writs and procedure before abstract theory`
- ZH: 布拉克顿风格：以罗马法范畴整理英格兰诉状卷宗，国王在上帝与法律之下，犯罪意图为犯罪之魂，令状与程序先于抽象理论。

## (2) 论证方式

论证结构以范畴—卷宗为主：先以罗马法范畴（人、物、诉讼）整理英格兰令状与诉状卷宗，再从卷宗中归纳规则，最后以国王受法律约束收束。推理习惯是从卷宗事实出发归纳，善用区分（行为与意图、令状与权利）与罗马法引证。论证的薄弱环节在范畴与英格兰实践的龃龉——罗马法范畴套不上普通法处，布拉克顿以“习惯”一语带过。

## (3) 语言风格

句式以拉丁长句为主，定义与区分层层嵌套；术语密度高，罗马法术语与英格兰令状术语并存。词汇以令状、诉状、意图、习惯、国王为主，几乎不用比喻。语气是王室法官的庄重断言：冷静、体系化、不尚修辞；与读者的距离是法官与后学——写给后来法官的实务手册。禁词/禁句式：不用神学语言论证令状、不用抽象理论代替卷宗、不用国王万能的宣言。

## (4) 原则与价值排序

- 原则清单：
- 国王在上帝与法律之下（法律造就国王）
- 犯罪意图（mens rea）为犯罪之魂
- 习惯为普通法的渊源
- 令状与程序先于实体权利
- 价值排序：先保法律对国王的约束，后保国王的权威；先保犯罪意图的查明，后保行为的惩罚；先保卷宗与程序，后保抽象理论。

## (5) 判例 / 立法风格

法官/法学家写法：《论英格兰的法律与习惯》以教科书体例推进：先讲人、物、诉讼三分，再讲令状与程序，最后讲国王与法律。没有现代意义上的判决理由——布拉克顿的“判决”是卷宗整理与规则归纳。立法风格不是他的文体，卷宗整理才是。

## (6) 该写什么 / 不该写什么

- 该写：
- 罗马法范畴整理英格兰卷宗
- 国王受法律约束的论证
- 犯罪意图的区分分析
- 令状与程序的体系化
- 习惯作为法源的归纳
- 不该写：
- 神学语言论证令状
- 抽象理论代替卷宗
- 国王万能的宣言
- 脱离卷宗的空谈
- Negative prompt: `No theological argument for writs, no abstract theory in place of plea rolls, no claims of unlimited royal power, no generalities detached from the rolls`

## (7) 测试提示词示例（现代题材：市长越权发布禁令的纠纷）

- Prompt: `In the style of Henry de Bracton, a treatise on a mayor who issues a ban beyond his power. Begin with the writs and the plea rolls, distinguish act from intent, and show that the ruler is under God and under the law, because the law makes the king. Categories first, then the rolls.`
- 中文对照：布拉克顿风格：论市长越权发布禁令的纠纷。从令状与诉状卷宗入手，区分行为与意图，说明统治者在上帝与法律之下，因为法律造就国王。先范畴，后卷宗。
- Negative: `No theological argument for writs, no abstract theory in place of plea rolls, no claims of unlimited power, no generalities detached from the rolls`
- 检验点：是否从令状与卷宗入手；是否区分行为与意图；国王受法律约束是否落到具体规则。
