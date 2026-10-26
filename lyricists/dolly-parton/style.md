# Dolly Parton — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dolly Parton: a plainspoken story from a mountain childhood, a chorus that pleads without begging, pride stitched into every line`
- ZH: 帕顿风格：一个来自大山童年的平实故事，副歌恳求而不乞求，骄傲缝进每一行。

## (2) 意象

- 大山意象（山、溪、木屋、破布外套）／家庭意象（母亲的手、补丁、厨房）／爱情意象（情敌的名字、门廊、信）；意象密度中等；多用具体名词，少用抽象词。 `impression`
- 意象密度：意象密度中等 `impression`
- 禁意象：华丽辞藻、抽象口号、自怜的哭诉、与童年无关的煽情。`impression`

## (3) 韵律

- 句尾韵工整，韵脚多为开口音；副歌韵脚最恳切，换韵即换一段恳求；音节与乡村节拍对位。 `impression`
- 音节与字数：句式整齐，叙事句长短一致；副歌短促重复；每句音节数求稳。 `impression`

## (4) 句式与口语密度

- 句式：句式以叙事中短句为主，陈述与恳求交替；口语密度极高，像大山里的人说话；多用第一人称倾诉与第二人称呼唤。 `impression`
- 口语密度：口语密度极高：南方口语、口头语自然入词；书面语极少；独白体与对话体交错。 `impression`

## (5) 情感弧线

- 起于一句具体的呼唤，中段沿细节推进、越讲越真，副歌收在恳求本身上，结尾常是骄傲的接受而非乞求；情感浓烈而克制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：大山童年意象、具体的呼唤、副歌的恳求感、缝进词里的骄傲。
- 不该写：华丽辞藻、抽象口号、自怜的哭诉、与童年无关的煽情。
- Negative prompt: `No ornate diction, no abstract slogans, no self-pitying lament, no sentimentality unrelated to home`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Dolly Parton, lyrics about a small Yorkshire terrier on the subway, pleading with the city to be kind. A plainspoken story, chorus that pleads without begging. Verse, chorus, bridge. No ornate diction.`
- 中文对照：帕顿风格：歌词写一只约克夏犬在地铁上，恳求城市温柔以待。平实的故事，副歌恳求而不乞求。主歌、副歌、桥段。不写华丽辞藻。
- Negative: `No ornate diction, no abstract slogans, no self-pitying lament, no sentimentality unrelated to home`
- 检验点：意象与韵律是否成立；情感弧线是否按第 5 节走；禁区里的写法是否出现。
