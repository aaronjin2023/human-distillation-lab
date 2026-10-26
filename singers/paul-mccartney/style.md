# Paul McCartney — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock and pop vocal in the style of Paul McCartney: warm melodic tenor, effortless legato, bright open tone, graceful melisma, tender ballad intimacy rising to joyful rock shouting, impeccable diction`
- ZH: 麦卡特尼风格：温暖的旋律男高音，毫不费力的连音，明亮开放的音色，优雅的转音，抒情歌的亲密感可升至欢快的摇滚喊唱，咬字无可挑剔。

## (2) 音色与音域

- 音色：明亮温暖的男高音，中高音区圆润开放；主音色为歌唱性强的连音乐句，辅音色为轻柔的气声与假声点缀；禁音色为沙哑撕裂与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑稳，起音柔和滑入，收尾渐弱或拖长；颤音自然而窄；真假声切换平滑，《Hey Jude》尾段以喊唱推进而不破音。`artifact`

## (4) 咬字与语言

- 咬字：标准英式发音，元音饱满、辅音轻；歌词与旋律咬合如歌唱，换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：节拍稳而带摇摆感，抒情歌用自由节奏（rubato），摇滚曲目抢拍推进；即兴以尾段重复与加花为主，现场常拉长《Hey Jude》的“na-na-na”段落。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 旋律优美的抒情歌与民谣式叙事（如《Yesterday》《Let It Be》一类）
- 欢快摇滚与副歌大合唱式的尾段推进（如《Hey Jude》）
- 温柔主歌接开放副歌的旋律弧线
- 钢琴或吉他伴奏下的亲密独唱
- 不该唱：`No raspy shouting, no mumbled diction, no harsh distortion, no flat monotone delivery, no operatic vibrato`
- Negative prompt: `No raspy shouting, no mumbled diction, no harsh distortion, no flat monotone delivery, no operatic vibrato`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of Paul McCartney, a song about a small Yorkshire terrier sitting on a subway seat. Warm melodic tenor, effortless legato, bright open tone, tender ballad intimacy, joyful lift in the chorus, impeccable diction.`
- 中文对照：麦卡特尼风格：唱一首关于地铁里约克夏犬的歌。温暖的旋律男高音，毫不费力的连音，明亮开放的音色，抒情的亲密感，副歌欢快上扬，咬字清晰。
- Negative: `No raspy shouting, no mumbled diction, no harsh distortion, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
