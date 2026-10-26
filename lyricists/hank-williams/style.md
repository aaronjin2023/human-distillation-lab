# Hank Williams — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hank Williams: plain heartbreak in three verses, a lonesome whistle of a line, the chorus as a wound that will not close`
- ZH: 汉克·威廉姆斯风格：三段主歌写尽平实的心碎，一句孤独的口哨般的词句，副歌是一道合不上的伤口。

## (2) 意象

- 心碎意象（冷心、眼泪、午夜、火车汽笛）／乡村意象（小路、老屋、月亮）／身体意象（心、眼泪、颤抖的手）；意象密度低，每句一个意象；多用明喻，少用典。 `impression`
- 意象密度：意象密度低，每句一个意象 `impression`
- 禁意象：华丽辞藻、抽象口号、廉价的安慰、与心碎无关的风景。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为闭口音与开口音交替；副歌韵脚最痛，换韵即换一段心碎；音节与乡村节拍对位。 `impression`
- 音节与字数：句式整齐，每句字数接近；主歌叙事、副歌抒情，长短句交错少。 `impression`

## (4) 句式与口语密度

- 句式：句式以中短句为主，陈述与自问交替；口语密度极高，像深夜的人说话；多用第一人称倾诉与第二人称指责。 `impression`
- 口语密度：口语密度极高：南方口语、口头语自然入词；书面语极少；独白体为主。 `impression`

## (5) 情感弧线

- 起于一句心碎的陈述，中段沿细节推进、越讲越冷，副歌收在伤口本身上，结尾常是认命而非和解；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：平实的心碎、冷心与午夜意象、副歌的伤口感、口语的准确。
- 不该写：华丽辞藻、抽象口号、廉价的安慰、与心碎无关的风景。
- Negative prompt: `No ornate diction, no abstract slogans, no cheap comfort, no scenery unrelated to heartbreak`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Hank Williams, lyrics about a small Yorkshire terrier on the subway, lonesome in a crowd. Plain heartbreak, chorus as a wound that will not close. Verse, chorus, bridge. No ornate diction.`
- 中文对照：汉克风格：歌词写一只约克夏犬在地铁人群里孤独。平实的心碎，副歌是一道合不上的伤口。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no cheap comfort, no scenery unrelated to heartbreak`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
