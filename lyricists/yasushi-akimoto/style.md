# Yasushi Akimoto — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yasushi Akimoto: idol chorus as a crowd, simple words everyone can sing, youth as a slogan that still feels true`
- ZH: 秋元康风格：偶像合唱即人群，人人会唱的简单词，青春作口号却仍真诚。

## (2) 意象

- 青春意象群：制服、饼干、幸运、夏天，青春写进日常小物；人群意象群：合唱、应援、舞台，歌词为人群而写；河流意象群：川流不息，时间如河。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语音拍填词，韵脚简单、重复性强；Hook 短句先行，副歌易唱易记；换韵少，靠重复推进；口号句即韵脚。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，简单、明快；语气词多；书面语极少；对话感强、合唱感强。 `impression`

## (5) 情感弧线

- 起：一个青春场景进场；转：小物点破心意，情绪翻面；合：副歌收在人人会唱的口号短句上，结尾明亮、不拖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：人人会唱的短句、青春小物、合唱感副歌、明亮收束、口号式标题句。
- 不该写：复杂意象、抽象议论、华丽辞藻、沉郁收束、拗口长句。
- Negative prompt: `No complex imagery, no abstract commentary, no ornate diction, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Yasushi Akimoto, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：秋元康风格：偶像合唱即人群，人人会唱的简单词，青春作口号却仍真诚。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No complex imagery, no abstract commentary, no ornate diction, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
