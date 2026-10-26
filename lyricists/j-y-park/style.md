# J.Y. Park — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of J.Y. Park: idol pop as a direct confession, tell me and nobody else, Korean plain speech built for a dance chorus`
- ZH: 朴振英风格：偶像流行即直接告白，告诉我、除了你没别人，韩语白话为舞曲副歌而写。

## (2) 意象

- 告白意象群：Tell Me、Nobody、Only You，告白即全曲；身体意象群：舞、步、眼神，身体即节奏；夜意象群：夜、电话、等待，夜是告白的场。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 韩语流行：韵脚配合舞曲节拍；Hook 短句先行，副歌易唱易跳；换韵少，靠重复推进；英语 Hook 词作韵脚点。 `impression`

## (4) 句式与口语密度

- 口语密度高：韩语日常口语直写，简单、直接；语气词多；书面语极少；对话感与合唱感交错。 `impression`

## (5) 情感弧线

- 起：一个告白场景进场；转：心意点破，情绪翻面；合：副歌收在告白 Hook 短句上，结尾明亮、不拖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：直接告白、舞曲副歌、Hook 短句、明亮收束、韩英混写。
- 不该写：复杂意象、抽象议论、华丽辞藻、沉郁收束、拗口长句。
- Negative prompt: `No complex imagery, no abstract commentary, no ornate diction, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of J.Y. Park, lyrics about a man buying oden at a convenience store late at night, thinking of someone he wants to call. Verse, chorus, bridge.`
- 中文对照：朴振英风格：偶像流行即直接告白，告诉我、除了你没别人，韩语白话为舞曲副歌而写。题目：lyrics about a man buying oden at a convenience store late at night, thinking of someone he wants to call。主歌、副歌、桥段。
- Negative: `No complex imagery, no abstract commentary, no ornate diction, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
