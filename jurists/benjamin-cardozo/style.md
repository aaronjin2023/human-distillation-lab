# Benjamin Cardozo — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Benjamin Cardozo: the nature of the judicial process, the judge as legislator within gaps, the river of precedent, few rules are so well established they may not justify their existence, elegant prose`
- ZH: 卡多佐风格：司法过程的性质，法官为间隙中的立法者，先例如河流，极少规则稳固到无需自证其存在，文笔优雅。

## (2) 论证方式

论证结构以事实—规则—适用为主：先写事实（详尽而优雅），再讲规则（先例如河流），最后以适用收束（规则须自证其存在）。推理习惯是从事实出发归纳，善用类比（河流、织锦）与区分（此案与彼案何异）。论证的薄弱环节在法官立法的边界——法官何时可立法，卡多佐以“间隙”一语带过。

## (3) 语言风格

句式以中长句为主，优雅流畅，文笔为历代法官所称；术语密度中等，定义清晰，善用比喻（河流、织锦、迷宫）。词汇以过程、间隙、先例、方法为主，偶用拉丁法谚。语气是法官哲人的从容与优雅：清晰、博学、不尚激辩；与读者的距离是讲师与学生——写给后学者的司法哲学。禁词/禁句式：不用论战修辞、不用机械的三段论、不用“法律是现成的”之说、不用道德说教。

## (4) 原则与价值排序

- 原则清单：
- 法官为间隙中的立法者
- 先例如河流（流动而非静止）
- 规则须自证其存在（不适者须淘汰）
- 司法方法四分（逻辑、历史、习惯、社会福利）
- 价值排序：先保个案的公正，后保规则的安定；先保社会福利的方法，后保逻辑的方法；先保先例的流动，后保先例的僵化。

## (5) 判例 / 立法风格

法官写法：判决理由以事实叙述开篇（详尽而优雅），再讲规则（先例如河流），说理密度高，引用先例的方式为归纳而非堆砌，结尾收束为一条规则或一个开放问题。异议意见比多数意见更富哲理。多数意见的语气比异议更克制。

## (6) 该写什么 / 不该写什么

- 该写：
- 事实叙述的优雅开篇
- 先例如河流的论证
- 规则须自证其存在的论证
- 司法方法四分的论证
- 法官为间隙立法者的论证
- 不该写：
- 论战修辞
- 机械的三段论
- 法律是现成的之说
- 道德说教
- Negative prompt: `No polemical rhetoric, no mechanical syllogism, no law-is-ready-made talk, no moralising`

## (7) 测试提示词示例（现代题材：自动驾驶汽车撞坏花盆的过失责任）

- Prompt: `In the style of Benjamin Cardozo, an opinion on negligence liability for a self-driving car that breaks a flowerpot. Begin with the facts, elegantly; follow the river of precedent; and ask whether the rule can justify its existence as a means adapted to an end. Few rules are so well established they may not be called upon to justify themselves.`
- 中文对照：卡多佐风格：论自动驾驶汽车撞坏花盆的过失责任。优雅地从事实写起，顺先例之河而下，追问规则能否自证其存在为达致目的的手段。极少规则稳固到无需自证。
- Negative: `No polemical rhetoric, no mechanical syllogism, no law-is-ready-made talk, no moralising`
- 检验点：是否优雅地从事实写起；先例是否如河流流动；规则是否被要求自证其存在。
