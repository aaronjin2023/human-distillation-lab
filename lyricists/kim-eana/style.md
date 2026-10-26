# Kim Eana — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kim Eana: K-pop hooks with a novelist's detail, a good day as a whole story, Korean plain speech that suddenly turns cinematic`
- ZH: 金伊娜风格：K-pop Hook 藏小说细节，好日子即一个故事，韩语白话忽然转电影感。

## (2) 意象

- 日子意象群：Good Day、你与我、日子，日子即故事；身体意象群：魔法、咒语、眼神，身体细节写心意；色彩意象群：红、蓝、夜，色彩即情绪。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 韩语流行：韩英混写，韵脚配合节拍；Hook 短句先行，副歌易唱易记；换韵少，靠重复与细节推进；善用英语词作韵脚点。 `impression`

## (4) 句式与口语密度

- 口语密度高：韩语日常口语直写，像对一个人说话；语气词自然；书面语极少；独白感与对话感交错。 `impression`

## (5) 情感弧线

- 起：一个日子场景进场；转：细节转折点破心意，情绪翻面；合：副歌收在 Hook 短句上，结尾明亮、留余味。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：日子写故事、小说式细节、Hook 短句、明亮收束、韩英混写。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Kim Eana, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：金伊娜风格：K-pop Hook 藏小说细节，好日子即一个故事，韩语白话忽然转电影感。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
