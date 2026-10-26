# Johann Wolfgang von Goethe — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Goethe: classical balance with romantic longing, the eternal feminine, nature as symbol, plain German that opens into the infinite`
- ZH: 歌德风格：古典的平衡与浪漫的渴望同体，永恒之女性，自然即象征，朴素德语通向无限。

## (2) 意象

- 主意象：浮士德、梅菲斯特、永恒之女性、自然、月亮、玫瑰；辅意象：山、泉、星、旅途；禁意象：煽情堆砌、口号；密度中等，意象多取自自然与神话，象征层层递进。

## (3) 韵律与句式

- 以自由体与定型诗并行，《浮士德》以自由韵体写成；句式精确、克制，长短交错；善用象征与警句；节奏平稳而深沉，朗读时如沉思。

## (4) 语言密度与词汇

- 词汇朴素而象征：日常德语词承载大义；动词克制；形容词少而重；禁词：煽情形容词、口号。

## (5) 结构习惯

- 长诗与短诗并行：《浮士德》两部，场景成组；短诗成集，以象征分组；开头多直入场景或意象，结尾多以象征或警句收束；视角多为第一人称沉思者与第三人称叙事；推进靠象征递进。

## (6) 该写什么 / 不该写什么

- 该写：浮士德与梅菲斯特、永恒之女性、自然象征；古典平衡与浪漫渴望的并置；朴素德语的象征力量。
- 不该写：风格上的禁区——sentimental excess, no political slogans, no ornate excess, no abstract discourse without a symbol, no cynical ending。
- Negative prompt: `No sentimental excess, no political slogans, no ornate excess, no abstract discourse without a symbol, no cynical ending`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Goethe, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Classical balance with romantic longing, the eternal feminine, nature as symbol, plain words opening into the infinite.`
- 中文对照：歌德风格：一只约克夏犬深夜坐在地铁座位上。古典的平衡与浪漫的渴望，永恒之女性，自然即象征，朴素词语通向无限。
- Negative: `No sentimental excess, no political slogans, no ornate excess, no abstract discourse without a symbol, no cynical ending`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
