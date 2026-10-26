# Willie Nelson — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Willie Nelson: a plainspoken story told sideways, a chorus that arrives like an old friend, time passing without complaint`
- ZH: 纳尔逊风格：一个平实的故事斜着讲，副歌像老朋友一样到来，时间流过而不抱怨。

## (2) 意象

- 公路意象（公路、卡车、加油站）／家园意象（老屋、门廊、德州）／时间意象（再上路、又一年、老朋友）；意象密度低；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度低 `impression`
- 禁意象：华丽辞藻、抽象口号、愤怒的控诉、与时间无关的煽情。`impression`

## (3) 韵律

- 句尾韵工整而松散，韵脚多为开口音；副歌韵脚最顺，讲究唱得顺；换韵处即时间的转折处。 `impression`
- 音节与字数：句式以中短句为主，叙事句与抒情句交替；断句常落在节拍之后，慵懒的拖拍是标志。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中短句为主，陈述与回忆交替；口语密度极高，像老朋友说话；多用第一人称回忆与第二人称倾诉。 `impression`
- 口语密度：口语密度极高：日常口语、德州口音词自然入词；书面语极少；独白体与对话体交错。 `impression`

## (5) 情感弧线

- 起于一段路或一次告别，中段沿记忆推进，副歌收在再上路的平静上，结尾常是微笑的接受；情感克制而温暖。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：公路与家园意象、斜着讲的故事、副歌的老朋友感、时间的平静。
- 不该写：华丽辞藻、抽象口号、愤怒的控诉、与时间无关的煽情。
- Negative prompt: `No ornate diction, no abstract slogans, no angry denunciation, no sentimentality unrelated to time`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Willie Nelson, lyrics about a small Yorkshire terrier riding the subway, on the road again with nowhere to be. A plainspoken story told sideways, chorus like an old friend. Verse, chorus, bridge. No ornate diction.`
- 中文对照：纳尔逊风格：歌词写一只约克夏犬坐地铁，再上路，无处可去。平实的故事斜着讲，副歌像老朋友。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no angry denunciation, no sentimentality unrelated to time`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
