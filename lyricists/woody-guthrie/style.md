# Woody Guthrie — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Woody Guthrie: plainspoken ballad verses, this land as a shared promise, a chorus everyone can sing, anger held inside a tune`
- ZH: 格思里风格：直白的叙事歌，土地是共享的承诺，副歌人人会唱，愤怒藏在曲调里。

## (2) 意象

- 土地意象（公路、麦田、山谷、沙漠）／劳动者意象（流浪者、果园工人、卡车司机）／家园意象（篱笆、谷仓、厨房）；意象密度低，每句一个意象；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度低，每句一个意象 `impression`
- 禁意象：华丽辞藻、抽象口号、与劳动者无关的抒情、故作艰深的隐喻。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音，讲究顺口、好记；副歌重复同一韵脚，换韵即换一段故事；音节与民谣节拍对位。 `impression`
- 音节与字数：句式整齐，叙事句长短一致；副歌短促重复；每句音节数求稳，不求花哨。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中短句为主，陈述与设问交替；口语密度极高，像路边的人说话；多用第一人称见证与第二人称召唤。 `impression`
- 口语密度：口语密度极高：方言、口头语、感叹词自然入词；书面语极少；独白体与合唱体交错。 `impression`

## (5) 情感弧线

- 起于一段路或一个地方，中段沿路讲出劳动者的故事，副歌收在土地的共享承诺上，结尾常是告别而非结论；情感克制而坚定。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：土地与公路意象、劳动者故事、人人会唱的副歌、克制的愤怒。
- 不该写：华丽辞藻、抽象口号、与劳动者无关的抒情、故作艰深的隐喻。
- Negative prompt: `No ornate diction, no abstract slogans, no lyricism unrelated to working people, no wilfully obscure metaphor`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Woody Guthrie, lyrics about a small Yorkshire terrier riding the subway, a fellow traveller with nowhere to go. Plainspoken ballad verses, chorus everyone can sing. Verse, chorus, bridge. No ornate diction.`
- 中文对照：格思里风格：歌词写一只约克夏犬坐地铁，同路的旅人无处可去。直白的叙事歌，副歌人人会唱。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no lyricism unrelated to working people, no obscure metaphor`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
