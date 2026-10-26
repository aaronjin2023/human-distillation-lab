# Kim Dong-ryul — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Dong-ryul: ballad as a departure, like first love, Korean plain speech that sounds like a letter you never sent`
- ZH: 金东律风格：抒情歌是出发，像初恋一样，韩语白话像没寄出的信。

## (2) 意象

- 初恋意象群：像初恋一样、初恋、第一次，初恋即标准；出发意象群：出发、路、远方，出发即人生；孩子意象群：孩子、纯真、长大，孩子即初心。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 韩语抒情：韵脚柔和、换韵如人生转折；主歌叙事长句、副歌短句如信；善用重复，余味长。 `impression`

## (4) 句式与口语密度

- 口语密度高：韩语日常口语直写，像写信；语气词自然；书面语极少；独白感强。 `impression`

## (5) 情感弧线

- 起：一个出发或初恋场景进场；转：初心点破，情绪翻面；合：副歌收在信体短句上，结尾温柔、向前。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：出发与初恋意象、信体、温柔收束、余味、初心。
- 不该写：直白口号、抽象议论、华丽辞藻、廉价煽情、气势副歌。
- Negative prompt: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no stadium choruses`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kim Dong-ryul, lyrics about a man buying oden at a convenience store late at night, thinking of a departure. Verse, chorus, bridge.`
- 中文对照：金东律风格：抒情歌是出发，像初恋一样，韩语白话像没寄出的信。题目：lyrics about a man buying oden at a convenience store late at night, thinking of a departure。主歌、副歌、桥段。
- Negative: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no stadium choruses`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
