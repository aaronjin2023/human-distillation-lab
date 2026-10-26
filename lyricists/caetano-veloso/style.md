# Caetano Veloso — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Caetano Veloso: joy walking against the wind, a collage of Brazil old and new, plain Portuguese that turns suddenly strange, a chorus that smiles while it bites`
- ZH: 维罗索风格：快乐顶着风走，巴西新旧并置的拼贴，平实的葡萄牙语忽然变得陌生，副歌笑着咬人。

## (2) 意象

- 巴西意象（风、太阳、海滩、桑巴）／拼贴意象（旧与新、土与洋、街头与电视）／身体意象（走路、跳舞、微笑）；意象密度高；多用并置与暗喻。 `impression`
- 意象密度：意象密度高 `impression`
- 禁意象：华丽辞藻、抽象口号、直白的控诉、与巴西无关的抒情。`impression`

## (3) 韵律

- 葡萄牙语韵脚工整，韵脚多为开口音；拼贴段落换韵频繁，副歌韵脚最亮；音节与桑巴节拍对位。 `impression`
- 音节与字数：句式以中短句为主，叙事句与抒情句交替；拼贴段落长短悬殊。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事与抒情为主，陈述与反讽交替；口语密度高，巴西口语与书面语并置；多用第一人称漫步与第二人称召唤。 `impression`
- 口语密度：口语密度高：巴西口语、街头用语自然入词；书面语只在反讽段落出现；独白体与对话体交错。 `impression`

## (5) 情感弧线

- 起于一句顶风的快乐，中段拼贴新旧巴西、越拼越亮，副歌收在微笑与咬人之间，结尾常是一个开放的漫步；情感轻快而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：巴西拼贴意象、顶风的快乐、副歌的微笑与咬人、开放的漫步。
- 不该写：华丽辞藻、抽象口号、直白的控诉、与巴西无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no direct denunciation, no lyricism unrelated to Brazil`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Caetano Veloso, lyrics about a small Yorkshire terrier on the subway, walking against the wind of the city. Joy as collage, chorus that smiles while it bites. Verse, chorus, bridge. No ornate diction.`
- 中文对照：维罗索风格：歌词写一只约克夏犬在地铁上，顶着城市的风走。快乐是拼贴，副歌笑着咬人。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no direct denunciation, no lyricism unrelated to Brazil`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
