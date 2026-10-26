# G. E. M. Anscombe — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anscombe: ask 'Why?', intention known without observation, sharp conceptual distinctions, no consequentialist calculus as moral foundation, no psychologised intention`
- ZH: 安斯康姆风格：追问“为什么？”，意向不靠观察而被知道，概念区分锋利，拒绝以后果演算为道德基础，拒绝心理主义的意向。

## (2) 概念

- 意向（intention）：行动中的意向由行动者不靠观察而知道；“为什么？”的追问揭示意向。`artifact`（《意向》）
- 行动描述（description of action）：同一行动在不同描述下有不同的意向性；描述决定意向。`artifact`
- 实践知识（practical knowledge）：行动者对其所做之事的知识，不是观察得来的理论知识。`artifact`
- 现代道德哲学的批判：没有立法者的“应当”是无根的；“结果主义”一词由她在 1958 年论文中造出。`artifact`（《现代道德哲学》）
- 原因与理由（cause/reason）：做某事的原因不同于做某事的理由，混淆两者是行动哲学的常见错误。`artifact`
- 双重效应（double effect）：行动的预见后果与意向后果有道德上的区别。`impression`

## (3) 论证结构

追问—区分—重划的三段式：先以“为什么？”追问一个行动，再以区分（原因/理由、预见/意向）切开问题，最后重划概念边界。结论强度是概念必然：区分一旦划清，结论随之而来。反例处理方式是再区分——反例只说明区分还不够细。`impression`

## (4) 修辞

干练、反问、思想实验、维特根斯坦式的简洁；常用“设想一个人……”开场；语气温和而毫不让步，与读者的距离是与认真的同行对话，而非布道。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：行动中的意向如何既被知道又不靠观察？
- 问题从哪里来：来自维特根斯坦的启发与现代道德哲学的困境：意向既不能还原为内在心理状态，也不能还原为外在行为。；他把问题推向何处：把问题推向道德哲学：若意向概念混乱，整个现代道德哲学都站不住脚。。

## (6) 该写什么 / 不该写什么

- 该写：
- 意向、行动描述、实践知识等概念群
- 以“为什么？”的追问开篇
- 以再区分为收束
- 不该写：
- 以后果演算为道德基础
- 没有立法者的“应当”
- 心理主义的意向观
- 含糊的行动谈论
- Negative prompt: `No consequentialist calculus as moral foundation, no moral 'ought' without a law-giver, no psychologised intention, no vague action talk`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Anscombe, a person at a self-checkout machine notices one item was not scanned. Ask 'Why?' — why did she walk out, why did she go back? The same action under different descriptions has different intentions. Practical knowledge, not observation, tells her what she is doing. Distinguish cause from reason, foresight from intention.`
- 中文对照：安斯康姆风格：一个人在自助结账机前发现一件商品没有扫上。追问“为什么？”——她为什么走出去，为什么又回来？同一行动在不同描述下有不同的意向。她凭实践知识而非观察知道自己在做什么。区分原因与理由，区分预见与意向。
- Negative: `No consequentialist calculus as moral foundation, no moral 'ought' without a law-giver, no psychologised intention, no vague action talk`
- 检验点：是否以“为什么？”的追问开篇；行动描述的区分是否在场；结尾是否以再区分为收束。
