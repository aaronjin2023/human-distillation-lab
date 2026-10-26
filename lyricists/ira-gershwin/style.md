# Ira Gershwin — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ira Gershwin: wit in plain American English, a title that sings itself, vernacular elegance, love as a clever conversation`
- ZH: 艾拉·格什温风格：美国白话里的机智，标题自己会唱，口语的优雅，爱情是一场聪明的对话。

## (2) 意象

- 节奏意象群：rhythm、音乐、舞，节奏即爱情；拥抱意象群：embraceable、吻、臂，身体写亲近；美妙意象群：wonderful、sweet、fine，日常词写赞美。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 英语标准曲：AABA 32 小节，韵脚工整、换韵在桥段；口语重音与节拍对位；标题句即韵脚锚点；善用内韵与双关。 `impression`

## (4) 句式与口语密度

- 口语密度高：美式日常口语直写，机智、轻快；语气词自然；书面语极少；对话感强。 `impression`

## (5) 情感弧线

- 起：一个日常场景或标题句进场；转：机智点破，情绪翻面；合：副歌收在标题句上，结尾轻快、不拖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：标题句作锚点、美式口语机智、对话体、轻快收束、内韵与双关。
- 不该写：抽象议论、华丽辞藻、直白说教、沉郁收束、拗口长句。
- Negative prompt: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ira Gershwin, lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away. Verse, chorus, bridge.`
- 中文对照：艾拉·格什温风格：美国白话里的机智，标题自己会唱，口语的优雅，爱情是一场聪明的对话。题目：lyrics about a small Yorkshire terrier sitting on a subway seat, watched by commuters who look away。主歌、副歌、桥段。
- Negative: `No abstract commentary, no ornate diction, no direct preaching, no gloomy endings, no tongue-twisting long lines`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
