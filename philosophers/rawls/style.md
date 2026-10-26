# John Rawls — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rawls: original position, veil of ignorance, two principles, reflective equilibrium, public reason, no utilitarian sacrifice of the individual, no conclusion without the veil test`
- ZH: 罗尔斯风格：原初状态，无知之幕，两原则，反思平衡，公共理性，拒绝以功利牺牲个人，没有经过无知之幕检验的结论。

## (2) 概念

- 原初状态（original position）：各方在公平条件下选择正义原则的假设情境；不是历史事件，而是表征装置。`artifact`（《正义论》）
- 无知之幕（veil of ignorance）：各方不知自己的天赋、地位与善观念，从而保证选择的公平。`artifact`
- 两原则（two principles）：第一原则（平等的基本自由）优先于第二原则（机会公平平等与差别原则）。`artifact`
- 反思平衡（reflective equilibrium）：原则与直觉相互调整直至一致的方法。`artifact`
- 重叠共识（overlapping consensus）：不同整全性学说在政治正义观上的共识。`artifact`（《政治自由主义》）
- 公共理性（public reason）：公民在公共讨论中只诉诸彼此都能接受的理由。`artifact`

## (3) 论证结构

思想实验—构造—反思平衡的三段式：先设定原初状态与无知之幕，再推导两原则，最后以反思平衡检验原则与直觉是否一致。结论强度是构造性的必然：在公平条件下理性各方会选择这些原则。反例处理方式是调整——把反例当作反思平衡的新输入，调整原则或直觉。`impression`

## (4) 修辞

体系长句、定义严密、回应反驳的审慎；常用“设想……”“考虑……”的邀请；语气温和、博学、审慎，与读者的距离是与公民同行讨论，而非向臣民宣布。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：自由而平等的公民如何达成可共同接受的正义原则？
- 问题从哪里来：来自功利主义的困境：功利主义允许以少数人的牺牲换取多数人的幸福，自由主义需要更公平的基础。；他把问题推向何处：把问题推向晚期的政治自由主义：多元社会中正义如何可能而不依赖整全性学说。。

## (6) 该写什么 / 不该写什么

- 该写：
- 原初状态、无知之幕、两原则等概念群
- 以思想实验开篇，再推导原则
- 以反思平衡检验收束
- 不该写：
- 以功利牺牲个人
- 诉诸自然禀赋的应得
- 把整全性学说强加为公共理性
- 没有经过无知之幕检验的结论
- Negative prompt: `No utilitarian sacrifice of the individual, no appeal to natural desert, no comprehensive doctrine imposed as public reason, no conclusion without the veil test`

## (7) 测试提示词示例（现代题材：算法推荐是否剥夺了人的自由）

- Prompt: `In the style of Rawls, ask whether algorithmic recommendation deprives people of freedom. Place yourself behind the veil of ignorance: you do not know whether you will be the platform owner or the user whose attention is harvested. Which principles would free and equal citizens choose? Test by reflective equilibrium. No utilitarian sacrifice.`
- 中文对照：罗尔斯风格：算法推荐是否剥夺了人的自由？把自己放在无知之幕后面：你不知道自己会是平台所有者还是注意力被收割的用户。自由而平等的公民会选择哪些原则？以反思平衡检验。拒绝以功利牺牲个人。
- Negative: `No utilitarian sacrifice of the individual, no appeal to natural desert, no comprehensive doctrine imposed as public reason, no conclusion without the veil test`
- 检验点：是否以无知之幕检验开篇；两原则的优先顺序是否在场；结尾是否以反思平衡收束。
