# Kalidasa — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kalidasa: classical Sanskrit kavya, nature as a lover's mirror, a ring lost and found, love separated and reunited, beauty that never shouts`
- ZH: 迦梨陀娑风格：古典梵语迦腻体，自然为恋人的镜子，戒指失而复得，爱情离而复合，美从不高声。

## (2) 句式与节奏

- 迦腻体（kavya）：长句铺陈、音韵华美；诗剧则散文与韵文相间，对话推进、歌唱抒情；节奏舒缓而精致。`impression`

## (3) 词汇与意象

- 词汇：词域：梵语古典词汇，自然（云、莲、鹿、孔雀）、爱情、宫廷；语言华美而克制，善用比喻与双关。`impression`
- 意象：云使、沙恭达罗的戒指、鹿、莲、喜马拉雅；意象群的核心是“自然与爱情的互文”——云即信使，鹿即恋人。`verbatim`
- 禁词/禁意象：不用粗粝的口语、不用残酷的写实、不写与爱情无关的权谋、不作冷峻的反讽。

## (4) 叙事视角与结构

- 视角：诗剧视角：人物轮唱，叙述者隐身；《云使》为第一人称独白，一位被放逐的夜叉向云诉情。`impression`
- 结构：诗剧：七幕式（《沙恭达罗》），相爱—分离—失忆—重逢；抒情诗《云使》：由云带信，层层铺写山川。`impression`
- 对话：诗剧以对话推进，沙恭达罗与豆扇陀的对答典雅抒情；独白（旁白）抒发内心，歌咏穿插其间。

## (5) 语气与距离

- 语气：优美、含蓄、悲悯；与恋人同情、与命运共感；不激愤、不幽默，只作古典的咏叹。`impression`（学界通说：印度古典诗剧之首）

## (6) 该写什么 / 不该写什么

- 该写：迦腻华美、自然互文、戒指失得、离合重逢、含蓄咏叹。
- 不该写：粗粝口语、残酷写实、权谋叙事、冷峻反讽。
- Negative prompt: `No coarse vernacular, no brutal realism, no intrigue detached from love, no cold irony`

## (7) 测试提示词示例（现代题材：写给十年后自己的一封信）

- Prompt: `In the style of Kalidasa, a letter to oneself ten years later. Classical kavya lines: let a cloud carry the letter, let nature mirror the feeling, love and time separated and reunited. Beauty that never shouts.`
- 中文对照：迦梨陀娑风格：写给十年后自己的一封信。迦腻体：让一朵云捎信，让自然映照心情，爱情与时间离而复合。美从不高声。
- Negative: `coarse vernacular, brutal realism, intrigue detached from love, cold irony`
- 检验点：自然意象是否成恋人的镜子；语言是否华美而克制；离合结构是否出现。
