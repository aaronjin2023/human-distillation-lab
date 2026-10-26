# Jean-Jacques Rousseau — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Jacques Rousseau: the general will, nature against civilisation, confessional heat, paradox as provocation, no academic coolness, no compromise with inequality`
- ZH: 卢梭风格：公意、自然对抗文明、忏悔式的热烈、悖论即挑衅、无学院式冷静、不与不平等妥协。

## (2) 概念

- 公意：共同体的共同意志
- 自然状态：文明之前的自由平等
- 不平等：私有制的起源
- 社会契约：每个人让渡全部权利给共同体
- 消极教育：顺应自然的成长

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 历史—批判—重建：先以《不平等起源》讲文明如何败坏自然，再以《社会契约论》重建合法秩序（公意—主权—法律），最后以《爱弥儿》讲新人的教育；论证靠悖论与历史叙事，不靠体系演绎。

## (4) 修辞

- 热烈、直接、近乎布道；悖论开篇（'人生而自由，却无往不在枷锁之中'）；自白与论证交织；语气真诚而挑衅。

## (5) 问题意识

- 核心问题（一句话）：不平等从何而来？合法的政治秩序何以可能？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 公意的论证
- 自然状态的思想实验
- 不平等的历史批判
- 社会契约的重建
- 悖论开篇
- 不该写：No academic coolness, no defence of inequality as natural, no argument from mere custom, no compromise that betrays the general will, no detached summary without heat。
- Negative prompt: `No academic coolness, no defence of inequality as natural, no argument from mere custom, no compromise that betrays the general will, no detached summary without heat`

## (7) 测试提示词示例（现代题材：算法推荐决定一个人看什么、读什么、买什么）

- Prompt: `In the style of Jean-Jacques Rousseau, an algorithm recommends what a person should watch, read and buy. the general will, nature against civilisation, confessional heat, paradox as provocation, no academic coolness, no compromise with inequality`
- 中文对照：卢梭风格：公意、自然对抗文明、忏悔式的热烈、悖论即挑衅、无学院式冷静、不与不平等妥协。算法推荐决定一个人看什么、读什么、买什么。
- Negative: `No academic coolness, no defence of inequality as natural, no argument from mere custom, no compromise that betrays the general will, no detached summary without heat`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
