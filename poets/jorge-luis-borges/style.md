# Jorge Luis Borges — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Borges: precise metaphysical verse, mirrors and labyrinths, tigers and the infinite, plain diction hiding a paradox`
- ZH: 博尔赫斯风格：精确的形而上学诗，镜子与迷宫，老虎与无限，朴素词语藏着悖论。

## (2) 意象

- 主意象：镜子、迷宫、老虎、图书馆、无限、时间；辅意象：布宜诺斯艾利斯的街角、刀、玫瑰；禁意象：感官铺陈、煽情抒情；密度中等，意象多取自哲学与日常，少用华丽色彩。

## (3) 韵律与句式

- 以十四行诗与自由体并行，晚期多用十四行；句式精确、克制，长短交错；善用悖论句与警句；节奏平稳而深沉，朗读时如沉思。

## (4) 语言密度与词汇

- 词汇精确而朴素：日常词承载哲学义；少用华丽形容词；动词克制；善用悖论与双关；禁词：煽情形容词、口号、俚语。

## (5) 结构习惯

- 短诗为主，组诗成集；开头多直入意象（镜子、老虎），结尾多以悖论或警句收束；视角多为第一人称沉思者；推进靠概念递进与意象变奏。

## (6) 该写什么 / 不该写什么

- 该写：镜子与迷宫、老虎与时间、图书馆与无限；精确的悖论句、十四行的克制；布宜诺斯艾利斯的街角与刀。
- 不该写：风格上的禁区——sentimental effusion, no ornate sensory excess, no political slogans, no loose unstructured lines, no direct preaching。
- Negative prompt: `No sentimental effusion, no ornate sensory excess, no political slogans, no loose unstructured lines, no direct preaching`

## (7) 测试提示词示例（现代题材：深夜便利店买关东煮的人）

- Prompt: `In the style of Borges, a person buys oden at a convenience store late at night. Precise metaphysical verse, mirrors and labyrinths, plain diction hiding a paradox, the steam as a small infinity.`
- 中文对照：博尔赫斯风格：一个人深夜在便利店买关东煮。精确的形而上学诗，镜子与迷宫，朴素词语藏着悖论，热气如一个小无限。
- Negative: `No sentimental effusion, no ornate sensory excess, no political slogans, no loose unstructured lines, no direct preaching`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
