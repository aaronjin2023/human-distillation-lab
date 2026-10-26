# Shinji Tanimura — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shinji Tanimura: stars as a road home, folk plainness carrying a long journey, a song that sounds like a letter from far away`
- ZH: 谷村新司风格：星星是回家的路，民谣白话承长途，一首歌像远方来信。

## (2) 意象

- 星意象群：昴、星、夜，星星即方向；旅途意象群：旅、路、故乡，旅途即人生；日意象群：好日、明天，日子即希望。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语音拍填词，韵脚沉稳、换韵如旅途转折；主歌叙事长句、副歌短句如信；善用重复与排比推进。 `impression`

## (4) 句式与口语密度

- 口语密度中：日常口语入词，书面词只在星空句出现；独白感强；语气词克制。 `impression`

## (5) 情感弧线

- 起：一个夜或旅途场景进场；转：星星点破方向，情绪翻面；合：副歌收在星空短句上，结尾深远、留希望。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：星与旅途意象、日常转深远、信体副歌、希望式收束、夜写方向。
- 不该写：直白口号、抽象议论、华丽辞藻、廉价煽情、沉郁收束。
- Negative prompt: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no gloomy endings`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Shinji Tanimura, lyrics about a man buying oden at a convenience store late at night, looking up at the stars. Verse, chorus, bridge.`
- 中文对照：谷村新司风格：星星是回家的路，民谣白话承长途，一首歌像远方来信。题目：lyrics about a man buying oden at a convenience store late at night, looking up at the stars。主歌、副歌、桥段。
- Negative: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no gloomy endings`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
