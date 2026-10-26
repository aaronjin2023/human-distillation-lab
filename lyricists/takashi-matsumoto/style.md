# Takashi Matsumoto — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Takashi Matsumoto: seasons as love's calendar, small objects carrying big feeling, gentle Japanese diction, a song that smells of rain`
- ZH: 松本隆风格：季节是爱情的日历，小物承大情，温柔日语，一首歌有雨的气味。

## (2) 意象

- 季节意象群：赤色甜豌豆、木棉、雨、雪，季节即感情刻度；小物意象群：手帕、信、伞、站台，日常小物承大情；色彩意象群：赤、青、白，色彩即情绪。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语音拍填词，韵脚柔和、换韵如季节更替；主歌长句铺场景、副歌短句收束；善用季语与色彩词入韵。 `impression`

## (4) 句式与口语密度

- 口语密度中：日常口语温柔入词，书面词只在风景句出现；对话感与独白感交错；语气词温和。 `impression`

## (5) 情感弧线

- 起：一个季节场景进场；转：小物点破感情，情绪翻面；合：副歌收在季节短句上，结尾温柔、留余味。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：季节写感情、小物承大情、色彩写情绪、温柔收束、季语入韵。
- 不该写：直白口号、抽象议论、华丽辞藻、廉价煽情、无季节的抒情。
- Negative prompt: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no lyricism without a season`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Takashi Matsumoto, a letter to yourself ten years from now, written in the style of a seasonal letter. Verse, chorus, bridge.`
- 中文对照：松本隆风格：季节是爱情的日历，小物承大情，温柔日语，一首歌有雨的气味。题目：a letter to yourself ten years from now, written in the style of a seasonal letter。主歌、副歌、桥段。
- Negative: `No plain slogans, no abstract commentary, no ornate diction, no cheap sentimentality, no lyricism without a season`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
