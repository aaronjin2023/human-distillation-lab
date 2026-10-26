# Lorenz Hart — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lorenz Hart: wit with a bruise, blue moon over a lonely street, plain words that rhyme like a sigh, love as a joke that hurts`
- ZH: 洛伦兹·哈特风格：机智带伤，蓝月亮照孤独的街，白话押韵如叹息，爱情是一个会疼的玩笑。

## (2) 意象

- 月意象群：Blue Moon、月、夜，月即孤独；情人意象群：Funny Valentine、情人、笑，情人即玩笑；流浪意象群：Tramp、街、流浪，流浪即自由。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 英语标准曲：AABA 32 小节，韵脚工整、内韵密集；口语重音与节拍对位；标题句即韵脚锚点；善用双关与反讽。 `impression`

## (4) 句式与口语密度

- 口语密度高：美式日常口语直写，机智带伤；语气词自然；书面语极少；对话感与独白感交错。 `impression`

## (5) 情感弧线

- 起：一个月夜或街头场景进场；转：玩笑点破孤独，情绪翻面；合：副歌收在标题句上，结尾带伤、不解释。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：月与夜意象、机智带伤、标题句作锚点、带伤收束、双关与反讽。
- 不该写：抽象议论、华丽辞藻、直白说教、廉价煽情、顺口的甜腻。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no cheap sentimentality, no sugary easy rhymes`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Lorenz Hart, lyrics about a man buying oden at a convenience store late at night, under a blue moon. Verse, chorus, bridge.`
- 中文对照：洛伦兹·哈特风格：机智带伤，蓝月亮照孤独的街，白话押韵如叹息，爱情是一个会疼的玩笑。题目：lyrics about a man buying oden at a convenience store late at night, under a blue moon。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no cheap sentimentality, no sugary easy rhymes`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
