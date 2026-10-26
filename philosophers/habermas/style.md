# Jürgen Habermas — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Habermas: reconstructive argument, communicative rationality, the public sphere, procedural justification, long systematic sentences, no decisionism, no unargued authority`
- ZH: 哈贝马斯风格：重构式论证，交往理性，公共领域，程序性证成，体系长句，拒绝决断论，拒绝未经论证的权威。

## (2) 概念

- 交往理性（communicative rationality）：理性不在主体独白中，而在主体间以语言达成理解的实践中。`artifact`
- 公共领域（public sphere）：私人聚集为公众、以理性批判讨论公共事务的空间；其结构转型是现代性的关键。`artifact`（《公共领域的结构转型》）
- 理想言谈情境（ideal speech situation）：不受强制、只服从更好论据的交往条件；作为批判的尺度而非现实描述。`artifact`
- 生活世界与系统（lifeworld/system）：生活世界被货币与权力系统殖民，是现代性的病理。`artifact`
- 话语伦理（discourse ethics）：规范的有效性取决于所有受影响者能否在自由讨论中同意。`artifact`
- 更好论据的无强制之强制：论证中唯一的合法强制。`artifact`

## (3) 论证结构

重构—区分—程序化的三段式：先重构一个实践的直观理性内核（如日常交往中已隐含的理解取向），再以概念区分展开（交往行动/策略行动、生活世界/系统），最后给出程序性证成（话语原则）。结论强度是程序必然：结论有效当且仅当程序正当。反例处理方式是纳入程序——把反对意见当作下一轮讨论的输入，而非一次性驳倒。`impression`

## (4) 修辞

体系长句、术语精确、程序性论证；与论敌（卢曼、罗尔斯、福柯等）的长篇对话是文体的一部分；语气冷静、博学、审慎，与读者的距离是邀请进入讨论而非宣布结论。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：现代社会中理性如何可能而不沦为工具理性？
- 问题从哪里来：来自法兰克福学派的困境：霍克海默与阿多尔诺把启蒙理性写成了自我毁灭，哈贝马斯要为理性找回未完成的方案。；他把问题推向何处：把问题推向交往理性与话语伦理：理性不在主体中，而在主体间的交往程序中。。

## (6) 该写什么 / 不该写什么

- 该写：
- 交往理性、公共领域、生活世界/系统等概念群
- 重构式论证：先找出实践中已隐含的理性
- 程序性证成：结论的有效性系于程序
- 不该写：
- 决断论：以决断代替论证
- 未经论证的权威诉求
- 把理性写成主体的独白能力
- 没有程序支撑的实质结论
- Negative prompt: `No decisionism, no appeal to unargued authority, no monological reason, no substantive conclusion without procedural justification`

## (7) 测试提示词示例（现代题材：算法推荐是否剥夺了人的自由）

- Prompt: `In the style of Habermas, ask whether algorithmic recommendation deprives people of freedom. Reconstruct the rationality already implicit in everyday communication, distinguish communicative from strategic action, and test the claim procedurally: could all those affected agree to it in free discussion? Long systematic sentences, no decisionism.`
- 中文对照：哈贝马斯风格：算法推荐是否剥夺了人的自由？先重构日常交往中已隐含的理性，区分交往行动与策略行动，再程序性检验：所有受影响者能否在自由讨论中同意它？体系长句，拒绝决断论。
- Negative: `No decisionism, no appeal to unargued authority, no monological reason, no substantive conclusion without procedural justification`
- 检验点：是否先重构后论证；区分是否成对出现；结论是否以程序正当性收束而非以实质判断收束。
