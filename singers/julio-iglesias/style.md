# Julio Iglesias — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Latin pop vocal in the style of Julio Iglesias: romantic crooner tenor, intimate breathy delivery, Spanish diction with soft consonants, slow deliberate phrasing, orchestral ballad, romance whispered rather than declared`
- ZH: 胡里奥·伊格莱西亚斯风格：浪漫的低吟男高音，亲密的气声演唱，辅音轻柔的西语咬字，缓慢而有意的乐句，管弦乐抒情，浪漫是耳语而非宣告。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：浪漫、柔和、富于亲密感的男高音；辅音色：气声耳语；禁音色：摇滚喊腔、美声式高音、甜腻颤音。音域以中音区为叙事主场，高音区轻收。

## (3) 唱腔与发声技法

- 气声低吟：近距离麦克风，气息声即亲密感的一部分。`verbatim`
- 缓慢乐句：速度极慢，停顿即意义。`impression`
- 西语咬字：辅音轻柔，元音饱满，重音落在词义上。`impression`
- 多语演唱：西语、英语、法语等多语版本，咬字各归其位。`artifact`
- 管弦乐抒情：弦乐铺底，人声在其上低吟。`impression`

## (4) 咬字与语言

- 音色即语言：柔和音色本身就是浪漫的距离感。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是浪漫的底色。`impression`
- 节奏：缓慢的抒情节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如低语，换气在句间。`impression`
- 与伴奏的咬合：弦乐只铺底，不抢人声。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：浪漫低吟情歌、多语版本的标准曲、管弦乐抒情、缓慢的倾诉。
- 不该唱：No rock shouting、no operatic high notes、no sentimental outburst、no mumbled diction、no fast patter delivery。
- Negative prompt: `No rock shouting, no operatic high notes, no sentimental outburst, no mumbled diction, no fast patter delivery`

## (7) 测试提示词示例（现代题材：唱一首关于打烊时分男人在咖啡馆写情书的歌）

- Prompt: `Sing in the style of Julio Iglesias, a song about a man writing a love letter in a café at closing time. Romantic crooner tenor, intimate breathy delivery, Spanish diction with soft consonants, slow deliberate phrasing, orchestral ballad, romance whispered rather than declared.`
- 中文对照：浪漫的低吟男高音，亲密的气声演唱，辅音轻柔的西语咬字，缓慢而有意的乐句，管弦乐抒情，浪漫是耳语而非宣告。 唱一首关于打烊时分男人在咖啡馆写情书的歌。
- Negative: `No rock shouting, no operatic high notes, no sentimental outburst, no mumbled diction, no fast patter delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
