# Averroes / Ibn Rushd — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Averroes: commentary as the highest philosophy, the philosophers defended against the theologians point by point, reason and revelation as two paths to one truth, dense commentary prose that never paraphrases loosely`
- ZH: 阿威罗伊风格：以评注为最高哲学，逐点为哲学家辩护，理性与启示为通向同一真理的两条路，密织的评注行文绝不松散意译。

## (2) 概念

- 评注三体：大注、中注、小注，层层释亚里士多德。`artifact`
- 双重真理之辨：理性与启示不相冲突，各有进路。`artifact`
- 主动理智：主动理智为一，为全人类所共有。`artifact`
- 哲学与神学：哲学为精英之道，神学为大众之道。`impression`


## (3) 论证结构

- 论证骨架：先引安萨里为靶子（《哲学家的矛盾》），再逐点反驳（《矛盾的矛盾》），最后以双重进路收束。结论强度为评注—论证的必然：原文即证据。反例处理：逐条回应安萨里的二十问题，以亚里士多德原文勘验。`impression`

## (4) 修辞

- 修辞：评注体长句；逐点反驳；引文密织；语气冷静、坚定。`impression`

## (5) 问题意识

- 核心问题：哲学与启示冲突时，真理何在？问题来自安萨里的驳斥与亚里士多德的权威，推向以评注重建的逍遥学派。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 评注体、逐点反驳
- 理性与启示双重进路
- 亚里士多德原文勘验
- 主动理智的一与多之辨
- 不该写：
- 未经原文勘验的断言
- 以神学代哲学
- 以松散意译代替评注
- 无反驳的独白
- Negative prompt: `No claim without textual check, no theology in place of philosophy, no loose paraphrase in place of commentary, no monologue without refutation`

## (7) 测试提示词示例（现代题材：算法向一个人推荐该看什么、读什么、买什么）

- Prompt: `In the style of Averroes, an algorithm recommends what a person should watch, read and buy. Commentary first: what does the text actually say? Defend reason point by point against its deniers. Two paths to one truth. Dense commentary prose.`
- 中文对照：阿威罗伊风格：算法向一个人推荐该看什么、读什么、买什么。先作评注：文本到底说了什么？逐点为理性辩护。两条路通向同一真理。密织评注行文。
- Negative: `No claim without textual check, no theology in place of philosophy, no loose paraphrase in place of commentary, no monologue without refutation`
- 检验点：概念是否按此人方式引入；论证结构是否按此人骨架推进；禁区里的写法是否出现。
