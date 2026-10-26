# Chico Buarque — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chico Buarque: a samba that carries a coded message, plain Portuguese built brick by brick, a chorus that the crowd finishes for you`
- ZH: 布阿尔克风格：一首桑巴藏着暗语，平实的葡萄牙语一砖一瓦砌起来，副歌由人群替你唱完。

## (2) 意象

- 建造意象（砖、楼、工人）／乐队意象（乐队、街头、游行）／暗语意象（你、明天、窗）；意象密度高；多用并置与暗喻。 `impression`
- 意象密度：意象密度高 `impression`
- 禁意象：华丽辞藻、抽象口号、直白的控诉、与建造无关的抒情。`impression`

## (3) 韵律

- 葡萄牙语韵脚工整，韵脚多为开口音；《Construção》以每句尾词同韵（-ão）砌成，换韵即换一层楼；音节与桑巴节拍对位。 `impression`
- 音节与字数：句式以中短句为主，叙事句与抒情句交替；建造段落长短一致，一砖一瓦。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中短句为主，陈述与暗语交替；口语密度高，巴西口语与书面语并置；多用第二人称暗指与第一人称独白。 `impression`
- 口语密度：口语密度高：巴西口语自然入词；书面语只在建造段落出现；独白体与合唱体交错。 `impression`

## (5) 情感弧线

- 起于一个街头的乐队，中段一砖一瓦砌起工人的命运，副歌收在人群的合唱上，结尾常是暗语的回响；情感克制而深沉。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：建造与乐队意象、一砖一瓦的推进、副歌的人群合唱、暗语的回响。
- 不该写：华丽辞藻、抽象口号、直白的控诉、与建造无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no direct denunciation, no lyricism unrelated to building`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Chico Buarque, lyrics about a small Yorkshire terrier on the subway, building a song brick by brick while the crowd finishes the chorus. Plain Portuguese, coded message. Verse, chorus, bridge. No ornate diction.`
- 中文对照：布阿尔克风格：歌词写一只约克夏犬在地铁上，一砖一瓦砌一首歌，副歌由人群唱完。平实的葡萄牙语，藏着暗语。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no direct denunciation, no lyricism unrelated to building`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
