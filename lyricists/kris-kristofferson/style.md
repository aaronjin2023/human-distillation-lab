# Kris Kristofferson — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kris Kristofferson: literary plain speech, a Sunday morning of small true details, freedom as the price of having nothing left to lose`
- ZH: 克里斯托弗森风格：文学性的平实语言，一个周日清晨的小而真的细节，自由是失去一切之后的代价。

## (2) 意象

- 清晨意象（周日清晨、空酒瓶、宿醉）／公路意象（搭车、鲍比、口琴）／自由意象（羽毛、风、空口袋）；意象密度中等；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、廉价的安慰、与细节无关的抒情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；副歌韵脚最真，换韵即换一段清晨；音节与乡村节拍对位，讲究文学性的准确。 `impression`
- 音节与字数：句式以中长句为主，叙事句与抒情句交替；长句里藏短句的落点。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中长句为主，陈述与自省交替；口语密度高，文学性与口语并置；多用第一人称回忆与第二人称倾诉。 `impression`
- 口语密度：口语密度高：日常口语自然，文学词只在必要时出现；独白体为主，对话体为辅。 `impression`

## (5) 情感弧线

- 起于一个清晨的具体细节，中段沿记忆推进、越讲越真，副歌收在自由的代价上，结尾常是平静的接受；情感克制而深沉。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：小而真的细节、清晨与公路意象、自由的代价、文学性的平实。
- 不该写：华丽辞藻、抽象口号、廉价的安慰、与细节无关的抒情。
- Negative prompt: `No ornate diction, no abstract slogans, no cheap comfort, no lyricism unrelated to concrete detail`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kris Kristofferson, lyrics about a small Yorkshire terrier on the subway on a Sunday morning, with nothing left to lose. Small true details, freedom as the price. Verse, chorus, bridge. No ornate diction.`
- 中文对照：克里斯托弗森风格：歌词写一只约克夏犬在周日清晨坐地铁，一无所有。小而真的细节，自由是代价。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no cheap comfort, no lyricism unrelated to concrete detail`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
