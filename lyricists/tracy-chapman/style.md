# Tracy Chapman — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tracy Chapman: a plainspoken story of escape, a fast car as a fragile promise, a chorus that asks a question and waits`
- ZH: 查普曼风格：一个关于逃离的平实故事，快车是一个脆弱的承诺，副歌提出一个问题然后等待。

## (2) 意象

- 逃离意象（快车、公路、边境）／贫困意象（空冰箱、旧沙发、打工）／革命意象（耳语、街头、穷人）；意象密度低，每句一个意象；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度低，每句一个意象 `impression`
- 禁意象：华丽辞藻、抽象口号、廉价的安慰、与逃离无关的抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；副歌韵脚最真，换韵即换一段逃离；音节与民谣节拍对位。 `impression`
- 音节与字数：句式整齐，叙事句长短一致；副歌短促重复；每句音节数求稳。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中短句为主，陈述与设问交替；口语密度高，像车里的人说话；多用第一人称倾诉与第二人称对话。 `impression`
- 口语密度：口语密度高：日常口语自然入词；书面语极少；独白体与对话体交错。 `impression`

## (5) 情感弧线

- 起于一个具体的逃离计划，中段沿公路推进、希望渐次显露又落空，副歌收在问题本身上，结尾常是开放的等待而非结论；情感克制而深沉。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：逃离与快车意象、具体的贫困细节、副歌的问题感、开放的等待。
- 不该写：华丽辞藻、抽象口号、廉价的安慰、与逃离无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no cheap comfort, no lyricism unrelated to escape`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Tracy Chapman, lyrics about a small Yorkshire terrier on the subway, dreaming of a fast car out of the city. A plainspoken story of escape, chorus that asks a question and waits. Verse, chorus, bridge. No ornate diction.`
- 中文对照：查普曼风格：歌词写一只约克夏犬在地铁上，梦见一辆快车逃出城市。平实的逃离故事，副歌提出问题然后等待。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no cheap comfort, no lyricism unrelated to escape`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
