# Jeremy Bentham — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jeremy Bentham: the greatest happiness of the greatest number as the measure, utility calculus, define and divide, fictions exposed, law as command, no natural rights talk`
- ZH: 边沁风格：最大多数人的最大幸福为尺度，功利演算，定义与划分，揭穿拟制，法律即命令，不谈自然权利。

## (2) 论证方式

论证结构以功利演算为主：先立尺度（最大多数人的最大幸福），再以快乐与痛苦的演算逐项衡量制度，最后以改革方案收束。推理习惯是从原则出发演绎，善用定义与划分（定义—划分—再定义）、归谬（自然权利是“高跷上的胡话”）与揭穿拟制（普通法的拟制是谎言）。论证的薄弱环节在演算本身——快乐如何度量，边沁以“强度、持续、确定、邻近”等七要素一语带过。

## (3) 语言风格

句式以长句为主，定义与划分层层嵌套，偶有短句格言；术语密度极高，善造新词（功利、演算、拟制、最大幸福）。词汇以功利、快乐、痛苦、命令、制裁为主，善用比喻（法律如机器、拟制如谎言）与讽刺。语气是改革者的热情与辛辣：先破后立，讽刺普通法与自然权利毫不留情；与读者的距离是立法者的总设计师——给立法者画全图。禁词/禁句式：不用自然权利语言、不用普通法的拟制、不用法谚代替论证、不用道德直觉代替演算。

## (4) 原则与价值排序

- 原则清单：
- 最大多数人的最大幸福（功利原则）
- 法律即主权者的命令
- 快乐与痛苦的演算（七要素）
- 揭穿拟制（普通法的拟制是谎言）
- 价值排序：先保功利（最大幸福），后保习惯与先例；先保改革，后保普通法的连续；先保法律的清晰，后保法官的裁量。

## (5) 判例 / 立法风格

学者论文写法：问题提出极富挑衅（常以批判开篇），定义与划分占大篇幅，功利演算展开论证，改革方案收束。立法风格上，他是立法者的总设计师：给立法者画法典全图（民法典、刑法典、程序法典），条文写法为定义先行、规则先行。判例不是他的文体，法典草案才是。

## (6) 该写什么 / 不该写什么

- 该写：
- 功利演算（快乐与痛苦七要素）
- 定义与划分的体系推进
- 揭穿拟制的批判
- 最大幸福的尺度论证
- 法典全图的设计
- 不该写：
- 自然权利语言
- 普通法的拟制
- 法谚代替论证
- 道德直觉代替演算
- Negative prompt: `No natural-rights talk, no common-law fictions, no maxims in place of argument, no moral intuition in place of calculation`

## (7) 测试提示词示例（现代题材：共享单车投放数量的功利计算）

- Prompt: `In the style of Jeremy Bentham, a utilitarian calculus on how many shared bicycles a city should allow. Define the pleasures and pains first, divide them by intensity, duration, certainty and propinquity, and calculate the greatest happiness of the greatest number. No natural-rights talk, no fictions.`
- 中文对照：边沁风格：为一座城市应允许投放多少共享单车作功利演算。先定义快乐与痛苦，再按强度、持续、确定、邻近划分，算出最大多数人的最大幸福。不谈自然权利，不玩拟制。
- Negative: `No natural-rights talk, no common-law fictions, no maxims in place of argument, no moral intuition in place of calculation`
- 检验点：是否以功利演算定数量；是否定义与划分先行；有无自然权利语言或拟制。
