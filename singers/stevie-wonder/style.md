# Stevie Wonder — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul vocal in the style of Stevie Wonder: joyful agile tenor, harmonica-like phrasing, intricate melisma, rhythmic precision, playful scat against tender ballad sincerity, optimism inside funk`
- ZH: 旺德风格：欢快的敏捷男高音，口琴式乐句，复杂的转音，节奏精准，俏皮拟声对照抒情歌的真诚，放克中有乐观。

## (2) 音色与音域

- 音色：明亮温暖的男高音，高音区开放；主音色为欢快的胸声，辅音色为假声与拟声；禁音色为沙哑粗粝与沉重低音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻快，起音干脆，收尾短促或拖长；颤音自然；《Superstition》以放克节奏型乐句为标记，《Isn't She Lovely》以口琴式乐句为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，辅音干脆；重音落在节奏点上；换气短促。`artifact`

## (5) 节奏与即兴

- 节奏：放克与灵魂节拍上精准切分，乐句如口琴般起伏；即兴以拟声与转音为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 放克灵魂歌与欢快流行歌曲（如《Superstition》一类）
- 口琴式乐句与拟声即兴
- 温柔抒情歌的真诚演唱
- 节奏精准的副歌推进
- 不该唱：`No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery, no loose off-beat phrasing`
- Negative prompt: `No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery, no loose off-beat phrasing`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `Sing in the style of Stevie Wonder, a song about riding a shared bicycle through a modern city at night. Joyful agile tenor, harmonica-like phrasing, intricate melisma, rhythmic precision, playful scat against tender ballad sincerity.`
- 中文对照：旺德风格：唱一首关于深夜骑共享单车的歌。欢快的敏捷男高音，口琴式乐句，复杂的转音，节奏精准，俏皮拟声对照抒情歌的真诚。
- Negative: `No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
