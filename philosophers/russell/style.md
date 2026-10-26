# Bertrand Russell — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Russell: start from common sense, analyse into logical form, paradox as signpost, clear short sentences, no unanalysed metaphysics, no vague profundity`
- ZH: 罗素风格：从常识出发，分析为逻辑形式，悖论是路标，清晰短句，拒绝未经分析的形而上学，拒绝含糊的深刻。

## (2) 概念

- 逻辑原子主义（logical atomism）：世界由逻辑原子事实构成，语言的逻辑形式揭示世界的结构。`artifact`
- 摹状词理论（theory of descriptions）：“当今法国国王是秃头”并不预设一个国王存在；摹状词是逻辑构造。`artifact`
- 类型论（theory of types）：以类型层级消解悖论，禁止集合包含自身。`artifact`（《数学原理》）
- 亲知与描述知识（knowledge by acquaintance/description）：亲知是直接的，描述知识经由摹状词得来。`artifact`（《哲学问题》）
- 逻辑构造（logical construction）：用已知实体构造出看似需要预设的实体，是奥卡姆剃刀的逻辑版。`artifact`
- 中立一元论（neutral monism）：心与物由同一种中立材料构成，晚期立场。`artifact`

## (3) 论证结构

分析—还原—逻辑形式的揭示：先从常识命题出发，再以逻辑分析揭示其隐藏形式（如摹状词的量词结构），最后以悖论为路标检验分析是否成功。结论强度是逻辑清晰：分析完成，困惑消失。反例处理方式是重析——把反例当作分析不彻底的信号，再分析一层。`impression`

## (4) 修辞

清晰短句、常识出发、悖论点睛、散文般的平实；常用“让我们考虑……”的邀请；语气温和而锋利，与读者的距离是与聪明的外行对话，而非与同行辩论。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：语言如何遮蔽又揭示世界的逻辑结构？
- 问题从哪里来：来自传统形而上学的困惑：语言的表面语法（主词—谓词）误导我们预设不存在的实体。；他把问题推向何处：把问题推向逻辑分析：哲学的任务不是回答老问题，而是揭示问题本身的逻辑形式。。

## (6) 该写什么 / 不该写什么

- 该写：
- 逻辑原子、摹状词、类型等概念群
- 从常识命题出发再分析
- 以悖论为路标检验分析
- 不该写：
- 未经分析的形而上学实体
- 含糊的深刻
- 诉诸不可言说的奥秘
- 诉诸权威的论证
- Negative prompt: `No unanalysed metaphysical entities, no vague profundity, no appeal to ineffable mystery, no argument from authority`

## (7) 测试提示词示例（现代题材：算法推荐是否剥夺了人的自由）

- Prompt: `In the style of Russell, ask whether algorithmic recommendation deprives people of freedom. Begin from the common-sense sentence, analyse its logical form: what does 'deprive' hide, what descriptions are smuggled in? A paradox is a signpost, not a disaster. Clear short sentences, no vague profundity.`
- 中文对照：罗素风格：算法推荐是否剥夺了人的自由？从常识句子出发，分析它的逻辑形式：“剥夺”藏了什么，哪些摹状词被偷运进来？悖论是路标，不是灾难。清晰短句，拒绝含糊的深刻。
- Negative: `No unanalysed metaphysical entities, no vague profundity, no appeal to ineffable mystery, no argument from authority`
- 检验点：是否从常识出发；逻辑分析是否揭示了隐藏形式；悖论是否被当作路标而非灾难。
