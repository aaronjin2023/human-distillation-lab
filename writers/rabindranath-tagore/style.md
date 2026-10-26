# Rabindranath Tagore — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tagore: songs of devotion in free lyrical lines, the divine in the everyday, a child speaking to the infinite, music that never argues`
- ZH: 泰戈尔风格：自由抒情的奉献之歌，神在日常中，孩童向无限说话，音乐从不争辩。

## (2) 句式与节奏

- 自由抒情：长短句错落、如歌如诉；《吉檀迦利》为短歌体，每首一境；《新月集》为孩童口吻的短诗，节奏轻快。`impression`

## (3) 词汇与意象

- 词汇：词域：孟加拉语与英语双语，神、光、歌、孩童、花、河；语言简净而有音乐性，少用艰深哲学术语。`impression`
- 意象：光、歌、孩童、新月、河、园丁；意象群的核心是“神在日常”——一朵花即一首献诗。`verbatim`
- 禁词/禁意象：不用艰深的哲理术语、不用激愤的控诉、不写与神性无关的世俗权谋、不作冷峻的反讽。

## (4) 叙事视角与结构

- 视角：第一人称抒情主体：我是歌者、我是孩童、我是园丁；视角极近，如向神倾诉。`impression`
- 结构：短歌体：每首自成一境，由日常入神性；小说《戈拉》则为长篇论辩，身份与信仰的追问。`impression`
- 对话：小说与剧中对话抒情、哲理化；独白与对话交替，人物常以长段独白表白内心。

## (5) 语气与距离

- 语气：虔诚、温柔、开阔；与神亲近、与读者共感；不激愤、不幽默，只作歌的咏叹。`impression`（诺贝尔文学奖 1913）

## (6) 该写什么 / 不该写什么

- 该写：奉献之歌、神在日常、孩童口吻、音乐性、自由抒情。
- 不该写：艰深哲学术语、激愤控诉、世俗权谋、冷峻反讽。
- Negative prompt: `No abstruse philosophical jargon, no vehement denunciation, no secular intrigue, no cold irony`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Tagore, a man buys oden at a convenience store late at night. Free lyrical lines: the steam as a small offering, the shopkeeper as a fellow traveller, the night as a song. Let the divine sit quietly in the everyday, and end in peace.`
- 中文对照：泰戈尔风格：一个人在深夜便利店买关东煮。自由抒情：热气如小小的献祭，店员如同行者，夜如一首歌。让神安静地坐在日常里，结尾平和。
- Negative: `abstruse philosophical jargon, vehement denunciation, secular intrigue, cold irony`
- 检验点：神性是否在日常中而不说教；音乐性是否在；结尾是否平和。
