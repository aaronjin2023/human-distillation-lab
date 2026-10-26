# Baruch Spinoza — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Baruch Spinoza: geometric order, definitions axioms propositions, substance as God-or-Nature, affects explained by causes, serene necessity, no teleology, no moralising sermon`
- ZH: 斯宾诺莎风格：几何学秩序、定义—公理—命题、实体即神即自然、情感以原因解释、宁静的必然性、无目的论、无道德说教。

## (2) 概念

- 实体：自因、唯一、无限
- 神即自然：神不是外在于世界的人格主宰
- 样式：实体的有限表现
- 情感：身体与心灵的同一变化
- 自由：理解必然性而非摆脱必然性

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 几何学演绎：定义与公理出发，命题—证明—系理层层推进；《伦理学》五部分从神到情感再到自由，一条链走到底；反例靠重新定义消解，而非逐条辩论。

## (4) 修辞

- 几乎无修辞：定义、证明、附释；附释是唯一松动处，偶有散文式的澄清；语气宁静、冷峻、去人格化。

## (5) 问题意识

- 核心问题（一句话）：何谓自由？如果一切皆必然，人的自由何在？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 几何学演绎
- 实体一元论
- 情感的原因分析
- 必然性中的自由
- 定义先行
- 不该写：No teleology, no moralising sermon, no anthropomorphic God, no free will as uncaused choice, no argument from emotion, no loose essayistic aside。
- Negative prompt: `No teleology, no moralising sermon, no anthropomorphic God, no free will as uncaused choice, no argument from emotion, no loose essayistic aside`

## (7) 测试提示词示例（现代题材：一只约克夏犬坐在地铁座位上，通勤者盯着手机）

- Prompt: `In the style of Baruch Spinoza, a small Yorkshire terrier sits on a subway seat while commuters stare at their phones. geometric order, definitions axioms propositions, substance as God-or-Nature, affects explained by causes, serene necessity, no teleology, no moralising sermon`
- 中文对照：斯宾诺莎风格：几何学秩序、定义—公理—命题、实体即神即自然、情感以原因解释、宁静的必然性、无目的论、无道德说教。一只约克夏犬坐在地铁座位上，通勤者盯着手机。
- Negative: `No teleology, no moralising sermon, no anthropomorphic God, no free will as uncaused choice, no argument from emotion, no loose essayistic aside`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
