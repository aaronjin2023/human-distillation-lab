# Janis Joplin — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Blues-rock vocal in the style of Janis Joplin: raw raspy contralto, full-throated cry, gospel fire, cracked vulnerability, total emotional commitment`
- ZH: 乔普林风格：原始沙哑的女低音，全力的哭喊，福音的火焰，破裂的脆弱，毫无保留的情感投入。

## (2) 音色与音域

- 女低音原始沙哑，音色带破裂感；主音色为原始沙哑的女低音，辅音色为福音式的高潮，禁音色为甜美的圆润与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声为主，起音果断，收尾或渐弱或喊叫；唱腔：哭腔与喊腔，装饰音克制，颤音粗粝。`artifact`

## (4) 咬字与语言

- 美式英语咬字带南方与蓝调口音，口语化；换气点随乐句呼吸。`artifact`

## (5) 节奏与即兴

- 乐句随情绪起伏，慢板更沉，快板更烈；与乐队咬合紧密。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：布鲁斯摇滚（《Piece of My Heart》《Cry Baby》）、民谣叙事（《Me and Bobby McGee》）、福音式高潮与哭腔段落、现场即兴延展的嘶喊、毫无保留的情感投入段落。
- 不该唱：`No smooth croon, no operatic vibrato, no sweet rounded tone, no breathy whisper, no restrained delivery`
- Negative prompt: `No smooth croon, no operatic vibrato, no sweet rounded tone, no breathy whisper, no restrained delivery`

## (7) 测试提示词示例（现代题材：雨夜外卖员）

- Prompt: `Sing in the style of Janis Joplin, a song about a delivery rider crossing a rainy city at night. Raw raspy contralto, full-throated cry, gospel fire, cracked vulnerability, total emotional commitment, rock band.`
- 中文对照：乔普林风格：唱一首关于深夜雨中外卖员穿过城市的歌。原始沙哑的女低音，全力的哭喊，福音的火焰，破裂的脆弱，毫无保留的情感投入，摇滚乐队伴奏。
- Negative: `No smooth croon, no operatic vibrato, no sweet rounded tone, no breathy whisper, no restrained delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
