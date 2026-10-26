# Bob Dylan — 作词风格规格 style.md（给文本 / 音乐模型）

> 只描述歌词，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bob Dylan: long free-verse narrative lines, road and train imagery, questions without answers, biblical and folk allusion, chorus that repeats with a twist`
- ZH: 鲍勃·迪伦风格：自由体叙事长句，公路与火车的意象，没有答案的设问，圣经与民谣的用典，副歌重复而每次转义。

## (2) 意象

- 意象群：(1)公路与火车——路、火车、流浪者，行走即命运；(2)审判与先知——审判日、洪水、圣经意象，日常与末世并置；(3)女人与面孔——蓝眼睛、金发、面具，人物即谜面。意象密度高，每句多个意象，明喻与暗喻交错，用典密集（圣经、民谣、蓝调）。禁意象：直白的情歌套路、廉价的流行隐喻。

## (3) 韵律

- 押韵：自由体长句，韵脚松散，靠重复与排比推进；常以尾韵的突然收紧制造冲击；换韵不规则，韵脚跟着叙事走。音节与字数：每句字数长而不齐，长短句大幅交错，留出换气口靠的是呼吸不是格律；重音即口语重音，唱起来像说话又像布道。

## (4) 句式与口语密度

- 句式：长句为主，排比、倒装、设问密集；设问常无答案（How many roads must a man walk down?）。口语密度中等：民谣口语与圣经书面语交错，语气词少；独白体与叙事体并存，对话体少。

## (5) 情感弧线

- 情感弧线：起——一个场景或一句设问进场；转——叙事不断偏离，意象层层叠加；合——副歌重复而转义，收在未解的追问上。情感强度浓烈而疏离，与听众保持先知的距离；结尾常开放或戛然而止，不给答案。

## (6) 该写什么 / 不该写什么

- 该写：公路、火车、审判日意象、自由体叙事长句、没有答案的设问、圣经与民谣用典、副歌重复而转义。
- 不该写：短促的流行副歌、直白的情歌套路、廉价的流行隐喻、解释性的议论。
- Negative prompt: `No short pop chorus, no cliché love-song formula, no cheap pop metaphors, no explanatory moralising, no forced rhyme`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Bob Dylan, lyrics about a man buying oden at a convenience store late at night. Long free-verse lines, road and train imagery, questions without answers, chorus that repeats with a twist. No short pop hook.`
- 中文对照：鲍勃·迪伦风格：自由体叙事长句，公路与火车的意象，没有答案的设问，圣经与民谣的用典，副歌重复而每次转义。以“一个人在深夜便利店买关东煮”为题写歌词，见英文提示词。
- Negative: `No short pop chorus, no cliché love-song formula, no cheap pop metaphors, no explanatory moralising, no forced rhyme`
- 检验点：意象与韵律是否成立；句式与口语密度是否对；情感弧线是否按第 (5) 节走；禁区里的写法是否出现。
