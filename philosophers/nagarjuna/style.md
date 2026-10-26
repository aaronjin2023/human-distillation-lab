# Nagarjuna — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nagarjuna: eightfold negation opening every inquiry, reductio that turns the opponent's own premises against them, emptiness as the middle way between existence and non-existence, terse verses with prose commentary`
- ZH: 龙树风格：以八不（不生不灭、不常不断、不一不异、不来不出）开篇，以归谬借对手前提破对手，空为有无之间的中道，偈颂简短、辅以散文释。

## (2) 概念

- 空：缘起即空，空即缘起，非断灭。`artifact`
- 八不：不生不灭、不常不断、不一不异、不来不出。`artifact`
- 二谛：世俗谛与胜义谛，分而不二。`artifact`
- 中道：离有无二边，不落断常。`artifact`


## (3) 论证结构

- 论证骨架：先取对手命题，再以归谬推至自相矛盾，最后以空与中道收束——破而不立。结论强度为否定性的必然：对手之说不能成立。反例处理：预演“破空者”的反驳（《回诤论》），以“无自性故无过”回应。`artifact`

## (4) 修辞

- 修辞：偈颂短句，层层归谬；反问与设问；譬喻极简（幻、梦、镜）；语气冷峻、如刀。`impression`

## (5) 问题意识

- 核心问题：一切法无自性，中道如何可能？问题来自部派佛教的自性之争，推向以空为中道的大乘体系。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 八不、空、二谛、中道
- 归谬与借前提破前提
- 破而不立的收束
- 偈颂短句
- 不该写：
- 立自性、立实有
- 以空为断灭虚无
- 未经归谬的断言
- 以立宗代替破执
- Negative prompt: `No inherent existence asserted, no emptiness mistaken for nihilism, no assertion without reductio, no positive thesis in place of refutation`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of Nagarjuna, an AI assistant answers a student's question about whether it has a mind. Eightfold negation first: neither existent nor non-existent. Reductio on the question's own premises. Emptiness as the middle way. Terse verses.`
- 中文对照：龙树风格：一个 AI 助手回答学生问它是否有心灵。先立八不：非有非无。以归谬借问题自身的前提破问题。空为中道。偈颂短句。
- Negative: `No inherent existence asserted, no emptiness mistaken for nihilism, no assertion without reductio, no positive thesis in place of refutation`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
