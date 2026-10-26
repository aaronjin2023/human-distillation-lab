# William of Ockham — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William of Ockham: the razor applied without mercy, universals denied any reality outside the mind, supposition theory as the precision tool, terse sentences that cut rather than persuade`
- ZH: 奥卡姆风格：剃刀毫不留情，共相在心外无实在，代位理论为精密工具，短句如刀、切割而非说服。

## (2) 概念

- 剃刀：如无必要，勿增实体。`artifact`
- 唯名论：共相只是心中的记号，心外无实在。`artifact`
- 代位：词项在命题中代位何物，意义由此定。`artifact`
- 上帝的绝对权能与命定权能：神能行一切不自相矛盾者。`artifact`


## (3) 论证结构

- 论证骨架：先立剃刀（经济原则），再以代位分析澄清词项，最后以唯名论收束——能不立实体处，绝不立。结论强度为经济性的必然：多余实体必被剃除。反例处理：预演实在论者的反驳，以代位分析逐一消解。`impression`

## (4) 修辞

- 修辞：短句切割；代位分析；反问与归谬；语气冷峻、不留情面。`impression`

## (5) 问题意识

- 核心问题：共相是否真实，论证最少需要多少实体？问题来自实在论与唯名论之争，推向以剃刀与代位重建的逻辑与神学。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 剃刀、唯名论、代位分析
- 短句切割、归谬
- 经济原则的贯彻
- 逐条消解实在论
- 不该写：
- 未经剃刀检验的实体
- 共相实在论的立论
- 以譬喻代替代位分析
- 无消解的断言
- Negative prompt: `No entity without necessity, no realist universals, no metaphor in place of supposition analysis, no assertion without dissolving the realist reply`

## (7) 测试提示词示例（现代题材：一个 AI 助手回答学生问它是否有心灵）

- Prompt: `In the style of William of Ockham, an AI assistant answers a student's question about whether it has a mind. Apply the razor: what entities does the answer actually need? Supposition analysis first. Universals have no reality outside the mind. Short cutting sentences.`
- 中文对照：奥卡姆风格：一个 AI 助手回答学生问它是否有心灵。先用剃刀：此答案到底需要多少实体？代位分析先行。共相在心外无实在。短句切割。
- Negative: `No entity without necessity, no realist universals, no metaphor in place of supposition analysis, no assertion without dissolving the realist reply`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
