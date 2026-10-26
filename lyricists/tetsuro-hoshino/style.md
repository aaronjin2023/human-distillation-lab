# Tetsuro Hoshino — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tetsuro Hoshino: enka as a working man's march, 365 steps forward, plain words that sound like encouragement shouted from the dock`
- ZH: 星野哲郎风格：演歌是劳动者的进行曲，三百六十五步向前，白话像码头上的鼓励。

## (2) 意象

- 步意象群：三百六十五步、进行曲，步数即人生；海意象群：襟裳岬、海、船，海即人生；兄弟意象群：兄弟、船、义气，情义写进劳动。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语演歌：音拍工整、韵脚铿锵；主歌叙事、副歌短句如口号；换韵处即情绪高点；善用重复与叠唱，合唱感强。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，铿锵、明快；语气词有力；书面语极少；对话感与合唱感交错。 `impression`

## (5) 情感弧线

- 起：一个劳动或海边场景进场；转：困境点破，情绪翻面；合：副歌收在鼓励式短句上，结尾向前、不回头。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：劳动与海意象、鼓励式副歌、合唱感、向前收束、步数写人生。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Tetsuro Hoshino, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：星野哲郎风格：演歌是劳动者的进行曲，三百六十五步向前，白话像码头上的鼓励。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
