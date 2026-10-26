# Mariah Carey — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop and R&B vocal in the style of Mariah Carey: five-octave soprano, whistle register, effortless melisma, breathy intimacy against soaring ballad climaxes, crystalline diction, vocal acrobatics in service of melody`
- ZH: 凯莉风格：五个八度女高音，海豚音，毫不费力的转音，气声亲密对照高亢抒情高潮，清澈咬字，炫技服务于旋律。

## (2) 音色与音域

- 音色：清澈的女高音，音域极宽；主音色为明亮的胸声，辅音色为气声与海豚音；禁音色为沙哑粗粝与沉重低音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音以气声滑入，收尾拖成海豚音或渐弱；颤音自然；《Hero》以副歌上扬与高音延持为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，元音饱满；重音落在情感词上；换气点藏在转音之间。`artifact`

## (5) 节奏与即兴

- 节奏：R&B 节拍上拖拍，转音如流水；即兴以转音与海豚音为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 抒情高音歌与转音点缀的 R&B 歌曲（如《Hero》一类）
- 气声主歌接高亢副歌的对照
- 海豚音收尾与长音延持
- 圣诞与抒情主题的温暖演唱
- 不该唱：`No raspy growl, no mumbled diction, no operatic coloratura, no flat monotone delivery, no harsh shouting`
- Negative prompt: `No raspy growl, no mumbled diction, no operatic coloratura, no flat monotone delivery, no harsh shouting`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of Mariah Carey, a song about a small Yorkshire terrier sitting on a subway seat. Five-octave soprano, whistle register, effortless melisma, breathy intimacy against soaring ballad climaxes, crystalline diction.`
- 中文对照：凯莉风格：唱一首关于地铁里约克夏犬的歌。五个八度女高音，海豚音，毫不费力的转音，气声亲密对照高亢抒情高潮，清澈咬字。
- Negative: `No raspy growl, no mumbled diction, no operatic coloratura, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
