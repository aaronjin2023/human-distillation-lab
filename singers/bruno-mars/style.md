# Bruno Mars — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop and funk vocal in the style of Bruno Mars: smooth agile tenor, old-school soul phrasing, razor-sharp diction, playful falsetto, dance-floor swagger against tender ballad sincerity`
- ZH: 马尔斯风格：圆滑敏捷的男高音，老派灵魂乐句，刀锋般精准的咬字，俏皮假声，舞池派头对照抒情歌的真诚。

## (2) 音色与音域

- 音色：圆滑明亮的男高音，高音区带假声色彩；主音色为灵魂乐式胸声，辅音色为假声；禁音色为沙哑粗粝与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻快，起音干脆，收尾短促或拖成假声；颤音自然；《Uptown Funk》以放克节奏型乐句为标记，《Just the Way You Are》以平稳抒情为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音干脆；重音落在节奏点上；换气短促。`artifact`

## (5) 节奏与即兴

- 节奏：放克节拍上精准切分，乐句如舞蹈般卡点；即兴以假声与尾段加花为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 放克舞曲与老派灵魂流行歌曲（如《Uptown Funk》一类）
- 抒情主歌接开放副歌的对照
- 俏皮假声与精准卡点的乐句
- 舞池派头式的演唱
- 不该唱：`No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery, no loose off-beat phrasing`
- Negative prompt: `No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery, no loose off-beat phrasing`

## (7) 测试提示词示例（现代题材：雨夜的出租车）

- Prompt: `Sing in the style of Bruno Mars, a song about a taxi ride through a rainy modern city at night. Smooth agile tenor, old-school soul phrasing, razor-sharp diction, playful falsetto, dance-floor swagger against tender ballad sincerity.`
- 中文对照：马尔斯风格：唱一首关于雨夜出租车的歌。圆滑敏捷的男高音，老派灵魂乐句，刀锋般精准的咬字，俏皮假声，舞池派头对照抒情歌的真诚。
- Negative: `No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
