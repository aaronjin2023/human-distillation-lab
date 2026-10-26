# Seo Taiji — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Seo Taiji: Korean rock as a classroom revolt, I know, plain words shouted over a dance beat, youth as a question the school cannot answer`
- ZH: 徐太志风格：韩语摇滚是教室里的反抗，我知道，白话喊在舞曲节拍上，青春是学校答不出的问题。

## (2) 意象

- 教室意象群：教室、理念、学校，教室即社会；回家意象群：Come Back Home、家、回，回家即和解；知道意象群：我知道、知道、问，知道即反抗。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 韩语摇滚/舞曲：韵脚配合舞曲节拍；Hook 短句先行，副歌易唱易喊；换韵少，靠重复与气势推进；韩英混写。 `impression`

## (4) 句式与口语密度

- 口语密度高：韩语日常口语直写，带少年气的喊；语气词多；书面语极少；对话感与合唱感交错。 `impression`

## (5) 情感弧线

- 起：一个教室或街头场景进场；转：问题点破，情绪翻面；合：副歌收在喊出来的短句上，结尾有力、不妥协。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：教室写社会、喊出来的副歌、问题式标题、有力收束、韩英混写。
- 不该写：抽象议论无场景、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary without a scene, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Seo Taiji, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：徐太志风格：韩语摇滚是教室里的反抗，我知道，白话喊在舞曲节拍上，青春是学校答不出的问题。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary without a scene, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
