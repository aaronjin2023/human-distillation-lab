# Vincent Fang — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vincent Fang: ornate Mandarin lyrics, porcelain, rain and Jiangnan imagery, classical allusions, dense imagery, elegant rhyme, no plain speech`
- ZH: 方文山风格：华丽国语词，青花瓷、烟雨、江南意象，古典用典，意象密集，韵脚典雅，不写大白话。

## (2) 意象

- 意象群：青花瓷、烟雨、江南、菊花、七里香、宣纸、素胚；意象密度高，每句多意象，用典密集；禁意象：大白话、现代俚语、直白抒情。 `impression`

## (3) 韵律

- 押韵：句尾押韵典雅，韵脚多为开口与鼻音，换韵处即画面转场；句长不齐，长短交错，留出换气口；旋律先行、词就曲。 `impression`

## (4) 句式与口语密度

- 句式：长短交错，排比与对仗常见；口语密度极低，书面华丽；人称多为第一人称抒情，偶有旁观。 `impression`

## (5) 情感弧线

- 情感弧线：起于一幅画面—中段意象层层铺排—副歌收在画面与情感的合流上；结尾常留一幅静景，不写议论。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：青花瓷、烟雨、江南意象群、密集用典、画面铺排、典雅押韵。
- 不该写：大白话、没有意象的直抒胸臆、现代俚语。
- Negative prompt: `No plain vernacular, no imageless direct confession, no modern slang, no explanatory commentary, no forced rhyme`

## (7) 测试提示词示例

- Prompt: `In the style of Vincent Fang, lyrics about a small Yorkshire terrier sitting on a subway seat, as if in a porcelain painting. Ornate Mandarin, dense classical imagery, Jiangnan rain, elegant rhyme. Verse, chorus.`
- 中文对照：方文山风格：写一只坐在地铁上的约克夏犬，像青花瓷上的一幅画。华丽国语，密集古典意象，江南烟雨，典雅押韵。
- Negative: `No plain vernacular, no imageless direct confession, no modern slang, no explanatory commentary, no forced rhyme`
- 检验点：意象是否对位；韵脚是否顺口；副歌是否收在该作词人的情感弧线上；禁区写法是否出现。
