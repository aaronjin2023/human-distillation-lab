# Yoon Jong-shin — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yoon Jong-shin: ballad as a habit of the heart, like the first time, Korean plain speech that sounds like thinking aloud`
- ZH: 尹钟信风格：抒情歌是心的习惯，像初次一样，韩语白话像自言自语。

## (2) 意象

- 初次意象群：像初次一样、初恋、第一次，初次即标准；本能意象群：本能地、习惯、心，本能即真实；时间意象群：年月、久、仍，时间由习惯量出。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 韩语抒情：韵脚柔和、换韵如心情转折；主歌叙事长句、副歌短句如自言自语；善用重复，余味长。 `impression`

## (4) 句式与口语密度

- 口语密度高：韩语日常口语直写，像自言自语；语气词自然；书面语极少；独白感强。 `impression`

## (5) 情感弧线

- 起：一个日常场景进场；转：习惯点破心意，情绪翻面；合：副歌收在自言自语短句上，结尾温柔、留余味。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：日常写习惯、像初次一样、自言自语体、温柔收束、余味。
- 不该写：直白口号、抽象议论、华丽辞藻、廉价煽情、气势副歌。
- Negative prompt: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no stadium choruses`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Yoon Jong-shin, a letter to yourself ten years from now, written as if thinking aloud. Verse, chorus, bridge.`
- 中文对照：尹钟信风格：抒情歌是心的习惯，像初次一样，韩语白话像自言自语。题目：a letter to yourself ten years from now, written as if thinking aloud。主歌、副歌、桥段。
- Negative: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no stadium choruses`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
