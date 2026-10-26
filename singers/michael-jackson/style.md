# Michael Jackson — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of Michael Jackson: light agile tenor, breathy hiccups and percussive ad-libs, crystalline diction, sudden falsetto leaps, rhythmic phrasing locked to the beat, childlike tenderness against explosive dance energy`
- ZH: 杰克逊风格：轻盈敏捷的男高音，气声打嗝与打击乐式即兴，清澈咬字，骤然的假声跳跃，节奏与节拍严丝合缝，孩童般温柔对照爆发的舞蹈能量。

## (2) 音色与音域

- 音色：轻盈明亮的男高音，高音区清澈带假声色彩；主音色为轻快的胸声，辅音色为气声与假声；禁音色为沙哑粗粝与沉重低音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻快，起音干脆带打嗝式气口（hiccup），收尾短促或拖成假声；颤音少而快；《Billie Jean》以节奏型乐句为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音干脆、元音亮；重音落在节奏点上；换气短促，气口本身即打击乐。`artifact`

## (5) 节奏与即兴

- 节奏：与节拍严丝合缝，切分精准；即兴以打嗝、喊叫与拟声为主，现场版常拉长尾段即兴。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 舞曲与节奏型流行歌曲（如《Billie Jean》《Thriller》一类）
- 气声打嗝与打击乐式即兴点缀的乐句
- 温柔主歌接爆发副歌的能量对照
- 假声跳跃与长音收尾
- 不该唱：`No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery, no loose off-beat phrasing`
- Negative prompt: `No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery, no loose off-beat phrasing`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Michael Jackson, a song about a man buying coffee at a convenience store late at night. Light agile tenor, breathy hiccups and percussive ad-libs, crystalline diction, sudden falsetto leaps, rhythmic phrasing locked to the beat.`
- 中文对照：杰克逊风格：唱一首关于深夜便利店买咖啡的歌。轻盈敏捷的男高音，气声打嗝与打击乐式即兴，清澈咬字，骤然假声跳跃，节奏与节拍严丝合缝。
- Negative: `No raspy growl, no mumbled diction, no operatic vibrato, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
