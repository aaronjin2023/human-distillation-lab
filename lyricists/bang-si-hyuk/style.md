# Bang Si-hyuk — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bang Si-hyuk: K-pop as temptation and youth, blood sweat and tears in plain Korean, a chorus built for a stadium`
- ZH: 方时赫风格：K-pop 即诱惑与青春，血汗泪说韩语白话，副歌为体育场而写。

## (2) 意象

- 身体意象群：血、汗、泪，身体即代价；青春意象群：少年、恋爱、初恋，青春即冒险；诱惑意象群：坏女孩、甜、毒，诱惑即主题。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 韩语流行：韵脚配合舞曲节拍；Hook 短句先行，副歌易唱易记；换韵少，靠重复与气势推进；英语词作韵脚点。 `impression`

## (4) 句式与口语密度

- 口语密度高：韩语日常口语直写，带少年气；语气词多；书面语极少；合唱感强。 `impression`

## (5) 情感弧线

- 起：一个诱惑场景进场；转：代价点破，情绪翻面；合：副歌收在气势短句上，结尾明亮、有力。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：身体写代价、青春冒险、体育场副歌、气势收束、韩英混写。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bang Si-hyuk, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：方时赫风格：K-pop 即诱惑与青春，血汗泪说韩语白话，副歌为体育场而写。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
