# Barbra Streisand — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Broadway and pop vocal in the style of Barbra Streisand: theatrical soprano, actor's diction, conversational verses building into soaring ballad climaxes, precise phrasing, every lyric delivered as if it were a scene`
- ZH: 史翠珊风格：戏剧化女高音，演员式咬字，口语化主歌 渐强至高亢抒情高潮，乐句精准，每句歌词都如一场戏。

## (2) 音色与音域

- 音色：戏剧化的女高音，中高音区圆润开放；主音色为抒情胸声，辅音色为口语化气声；禁音色为沙哑撕裂与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音如台词般直接，收尾拖长渐弱；颤音自然；《The Way We Were》以回忆式乐句与高音推进为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音重、元音饱满；重音落在词义上，如演台词；换气点藏在句意停顿处。`artifact`

## (5) 节奏与即兴

- 节奏：百老汇式自由节奏（rubato），乐句随词义伸缩；即兴少，以乐句处理制造变化。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 百老汇抒情歌与电影主题曲（如《The Way We Were》一类）
- 演员式口语主歌接高亢副歌的对照
- 回忆与告别主题的叙事演唱
- 精准乐句与长音推进
- 不该唱：`No raspy growl, no mumbled diction, no detached cool delivery, no operatic coloratura, no flat monotone delivery`
- Negative prompt: `No raspy growl, no mumbled diction, no detached cool delivery, no operatic coloratura, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：雨夜的出租车）

- Prompt: `Sing in the style of Barbra Streisand, a song about a taxi ride through a rainy modern city at night. Theatrical soprano, actor's diction, conversational verses building into soaring ballad climaxes, precise phrasing, every lyric delivered as if it were a scene.`
- 中文对照：史翠珊风格：唱一首关于雨夜出租车的歌。戏剧化女高音，演员式咬字，口语化主歌 渐强至高亢抒情高潮，乐句精准，每句歌词都如一场戏。
- Negative: `No raspy growl, no mumbled diction, no detached cool delivery, no operatic coloratura`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
