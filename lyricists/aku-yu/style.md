# Aku Yu — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Aku Yu: enka scenery as emotion, winter sea and sake bar, plain words that hit like a scene from a film`
- ZH: 阿久悠风格：演歌风景即情绪，冬海与酒场，白话如电影画面。

## (2) 意象

- 风景意象群：津轻海峡、冬、雪、海，风景即心境；酒场意象群：北酒场、酒、灯，孤独写进酒场；旅途意象群：列车、北国、故乡，旅途即人生。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语歌谣曲：五七调与口语节奏交错；韵脚松散、靠重复与排比推进；音拍与假名轻重贴合旋律；副歌短句如点题。 `impression`

## (4) 句式与口语密度

- 口语密度中：日常口语入词，书面词只在风景句出现；对话感弱、独白感强；语气词克制。 `impression`

## (5) 情感弧线

- 起：一个风景或酒场场景进场；转：风景里点破孤独或乡愁，情绪翻面；合：副歌收在风景短句上，结尾如电影定格。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：风景写情绪、酒场与旅途意象、日常口语、电影式场景、风景短句收束。
- 不该写：抽象议论、华丽辞藻、直白说教、无风景的抒情、廉价煽情。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no lyricism without a scene, no cheap sentimentality`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Aku Yu, lyrics about a man buying oden at a convenience store late at night, thinking of the winter sea. Verse, chorus, bridge.`
- 中文对照：阿久悠风格：演歌风景即情绪，冬海与酒场，白话如电影画面。题目：lyrics about a man buying oden at a convenience store late at night, thinking of the winter sea。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no lyricism without a scene, no cheap sentimentality`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
