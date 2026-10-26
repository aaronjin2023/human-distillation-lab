# Goro Matsui — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Goro Matsui: rock love as a premonition, plain Japanese with a sudden twist, a chorus that sounds like a confession at midnight`
- ZH: 松井五郎风格：摇滚爱情如预感，日语白话忽然转折，副歌像午夜告白。

## (2) 意象

- 预感意象群：恋之预感、夜、电话，预感即爱情的开始；身体意象群：抱紧、今夜、吻，身体细节写感情；再爱意象群：又爱上你、再一次，爱情是重复。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语音拍填词，韵脚配合摇滚节拍；主歌口语长句、副歌短句合唱感强；换韵处即情绪转折处；善用重复。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，带摇滚的直接；语气词自然；书面语极少；对话感强。 `impression`

## (5) 情感弧线

- 起：一个夜场景进场；转：预感点破，情绪翻面；合：副歌收在告白短句上，结尾直接、不拖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：预感意象、午夜告白、身体细节、直接收束、摇滚节拍。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Goro Matsui, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：松井五郎风格：摇滚爱情如预感，日语白话忽然转折，副歌像午夜告白。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
