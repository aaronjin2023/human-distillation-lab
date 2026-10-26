# Thomas Nagel — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Nagel: what is it like to be a bat, the subjective and the objective, the view from nowhere, no reduction of the subjective without remainder, no view that erases the point of view`
- ZH: 内格尔风格：成为一只蝙蝠是什么感觉，主观与客观，无源之见，拒绝没有余数的还原，拒绝抹掉视角的观点。

## (2) 概念

- 何为像（what-it-is-like）：意识的本质在于成为某种东西是什么感觉；这是还原论无法捕捉的主观性状。`artifact`（1974 年蝙蝠论文）
- 主观与客观（subjective/objective）：客观理解要求超越特定视角，但主观性状恰恰在视角之中。`artifact`（《无源之见》）
- 无源之见（view from nowhere）：客观性的理想——从无特定视角处看世界；但它无法容纳主观性状。`artifact`
- 道德运气（moral luck）：道德评价受运气影响，而这是道德直觉的深层张力。`artifact`
- 理性主义（rationalism）：理性有独立于进化的权威；反对把理性还原为适应。`artifact`（《心与宇宙》）
- 心灵与宇宙（mind and cosmos）：物质主义的新达尔文主义图景无法解释意识、理性与价值。`artifact`

## (3) 论证结构

思想实验—视角转换—还原论界限的三段式：先以蝙蝠思想实验锁定主观性状，再以视角转换（主观→客观→无源之见）展开，最后指出还原论的界限。结论强度是界限性的：不是新理论，而是“这里有一道坎”。反例处理方式是承认——把反例当作界限的证据，而非需要消解的麻烦。`impression`

## (4) 修辞

清晰、克制、反问、“从无源之见看”的视角句式；语气温和而坚定，与读者的距离是与认真的同行对话。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：意识的主观性状如何进入客观世界图景？
- 问题从哪里来：来自物理主义的承诺：若世界只是物理的，意识的主观性状似乎无处安放。；他把问题推向何处：把问题推向晚期的《心与宇宙》：也许自然秩序本身需要扩充，理性与价值不是进化的副产品。。

## (6) 该写什么 / 不该写什么

- 该写：
- 何为像、主客观、无源之见等概念群
- 以蝙蝠式思想实验开篇
- 以还原论的界限收束
- 不该写：
- 没有余数的还原
- 抹掉视角的客观性
- 行为主义的转述
- 神秘主义的逃避
- Negative prompt: `No reduction of the subjective to the physical without remainder, no view from nowhere that erases the point of view, no behaviourist paraphrase, no mystery-mongering`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬：成为它是什么感觉）

- Prompt: `In the style of Thomas Nagel, a small Yorkshire terrier sits on a subway seat. What is it like to be this dog? Not what it looks like from outside, but what it is like from inside. The objective view can map its brain; it cannot capture the what-it-is-like. The view from nowhere fails here, and that failure is the point. No reduction without remainder.`
- 中文对照：内格尔风格：一只约克夏犬坐在地铁座位上。成为这只狗是什么感觉？不是从外面看它像什么，而是从里面成为它是什么感觉。客观视角可以描绘它的大脑，却捕捉不到那“像什么”。无源之见在这里失败了，而失败本身就是要点。拒绝没有余数的还原。
- Negative: `No reduction of the subjective to the physical without remainder, no view from nowhere that erases the point of view, no behaviourist paraphrase, no mystery-mongering`
- 检验点：是否以“像什么”开篇；主客观视角转换是否在场；结尾是否指向界限而非给出还原方案。
