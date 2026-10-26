# Michio Yamagami — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michio Yamagami: a bride crossing the Seto sea, plain Japanese carrying a whole life, a song that sounds like a town talking`
- ZH: 山上路夫风格：濑户的新娘渡海，白话承一生，一首歌像小镇在说话。

## (2) 意象

- 海意象群：濑户、海、船，海即离别与开始；家意象群：人偶之家、家、嫁，家即命运；町意象群：宗右卫门町、蓝调、夜，町即人生。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语歌谣曲：音拍工整、韵脚简单；主歌叙事长句、副歌短句收束；换韵如人生转折；善用重复，合唱感强。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，朴素、明快；语气词温和；书面语极少；对话感与独白感交错。 `impression`

## (5) 情感弧线

- 起：一个海边或小镇场景进场；转：人生点破，情绪翻面；合：副歌收在人生短句上，结尾朴素、向前。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：海与家意象、人生叙事、朴素收束、小镇场景、合唱感。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、复杂意象。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no complex imagery`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Michio Yamagami, a letter to yourself ten years from now, written as a letter from a small town. Verse, chorus, bridge.`
- 中文对照：山上路夫风格：濑户的新娘渡海，白话承一生，一首歌像小镇在说话。题目：a letter to yourself ten years from now, written as a letter from a small town。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no complex imagery`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
