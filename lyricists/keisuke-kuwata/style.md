# Keisuke Kuwata — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Keisuke Kuwata: summer as a season of love, tears and kisses in plain Japanese, rock phrasing that still sounds tender`
- ZH: 桑田佳祐风格：夏天是爱情的季节，泪与吻说日语白话，摇滚句法仍温柔。

## (2) 意象

- 夏意象群：真夏、果实、海、汗，夏天即爱情；泪吻意象群：泪、吻、别离，身体细节写感情；天意象群：明天、晴、雨，天气即心情。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语音拍填词，韵脚配合摇滚节拍；主歌口语长句、副歌短句合唱感强；换韵处即情绪高点；善用重复与叠唱。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，带摇滚的随意；语气词多；书面语极少；对话感与独白感交错。 `impression`

## (5) 情感弧线

- 起：一个夏日场景进场；转：泪与吻点破感情，情绪翻面；合：副歌收在夏日短句上，结尾明亮、留余味。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：夏日场景、泪与吻的身体细节、合唱感副歌、明亮收束、天气写心情。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Keisuke Kuwata, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：桑田佳祐风格：夏天是爱情的季节，泪与吻说日语白话，摇滚句法仍温柔。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
