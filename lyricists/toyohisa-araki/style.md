# Toyohisa Araki — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Toyohisa Araki: four seasons as four loves, plain Japanese that anyone can sing, a song that smells of the station platform`
- ZH: 荒木与久风格：四季是四场恋爱，人人会唱的日语白话，一首歌有站台的气味。

## (2) 意象

- 四季意象群：春夏秋冬、花、雪，四季即感情；恋歌意象群：恋、缀、别离，恋爱写成缀锦；海意象群：日本海、悲伤、海岸，海即离别。 `impression`
- 意象密度：每句意象数中等，意象以暗喻与场景为主、明喻为辅；用典克制，不靠典故撑场面。`impression`
- 禁意象：他几乎不用的意象见第 (6) 节“不该写”清单。

## (3) 韵律

- 日语歌谣曲：音拍工整、韵脚简单；主歌四季铺陈、副歌短句收束；换韵如季节更替；善用重复，合唱感强。 `impression`

## (4) 句式与口语密度

- 口语密度高：日常口语直写，简单、明快；语气词温和；书面语极少。 `impression`

## (5) 情感弧线

- 起：一个季节场景进场；转：季节点破恋情，情绪翻面；合：副歌收在季节短句上，结尾温柔、易唱。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：四季写恋爱、人人会唱的短句、站台与海意象、温柔收束、季节换韵。
- 不该写：复杂意象、抽象议论、华丽辞藻、拗口长句、沉郁收束。
- Negative prompt: `No complex imagery, no abstract commentary, no ornate diction, no tongue-twisting long lines, no gloomy endings`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Toyohisa Araki, a letter to yourself ten years from now, written as four seasons. Verse, chorus, bridge.`
- 中文对照：荒木与久风格：四季是四场恋爱，人人会唱的日语白话，一首歌有站台的气味。题目：a letter to yourself ten years from now, written as four seasons。主歌、副歌、桥段。
- Negative: `No complex imagery, no abstract commentary, no ornate diction, no tongue-twisting long lines, no gloomy endings`
- 检验点：意象是否按第 (2) 节走；韵律是否按第 (3) 节走；副歌收束是否按第 (5) 节的弧线走；禁区写法是否出现。
