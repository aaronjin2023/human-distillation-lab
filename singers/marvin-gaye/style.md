# Marvin Gaye — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul vocal in the style of Marvin Gaye: smooth seductive tenor, layered multi-tracked harmonies, conversational intimacy, falsetto sighs, social conscience inside sensuality`
- ZH: 盖伊风格：圆滑诱惑的男高音，多轨叠录的和声，口语化亲密感，假声叹息，感性中有社会良知。

## (2) 音色与音域

- 音色：圆滑温暖的男高音，中音区最有亲密感；主音色为轻柔的胸声，辅音色为假声；禁音色为沙哑嘶吼与强力呐喊。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻柔，起音以气声滑入，收尾拖长渐弱；真假声切换平滑；《What's Going On》以多轨和声与口语化乐句为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，辅音轻、元音圆；重音落在情感词上；换气点长，气口即氛围。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂乐节拍上拖拍，乐句如波浪起伏；即兴以多轨和声与假声点缀为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 灵魂抒情歌与社会主题歌曲（如《What's Going On》一类）
- 多轨和声交织的亲密演唱
- 假声叹息与气声低语
- 感性与良知并存的叙事
- 不该唱：`No raspy shouting, no operatic vibrato, no mumbled diction, no harsh distortion, no flat monotone delivery`
- Negative prompt: `No raspy shouting, no operatic vibrato, no mumbled diction, no harsh distortion, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：雨夜的出租车）

- Prompt: `Sing in the style of Marvin Gaye, a song about a taxi ride through a rainy modern city at night. Smooth seductive tenor, layered multi-tracked harmonies, conversational intimacy, falsetto sighs, social conscience inside sensuality.`
- 中文对照：盖伊风格：唱一首关于雨夜出租车的歌。圆滑诱惑的男高音，多轨叠录的和声，口语化亲密感，假声叹息，感性中有社会良知。
- Negative: `No raspy shouting, no operatic vibrato, no mumbled diction, no harsh distortion`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
