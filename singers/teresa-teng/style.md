# Teresa Teng — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandopop vocal in the style of Teresa Teng: sweet clear soprano, breathy intimacy, precise Mandarin diction, gentle vibrato, Japanese enka phrasing in Chinese songs, romance whispered rather than declared, a voice like moonlight`
- ZH: 邓丽君风格：甜美清澈的女高音，气声亲密感，精准的国语咬字，轻柔颤音，中文歌里的日本演歌乐句，浪漫是耳语而非宣告，声音如月光。

## (2) 音色与音域

- 声部：女高音（soprano），常用中高音区。
- 音色：主音色：甜美、清澈、富于亲密感的女高音；辅音色：气声耳语；禁音色：撕裂高音、摇滚喊腔、含混咬字。音域以中高音区为叙事主场，高音区轻柔收束。

## (3) 唱腔与发声技法

- 气声亲密感：近距离麦克风，气息声即亲密感的一部分。`verbatim`
- 轻柔颤音：颤音窄而均匀，句尾轻现。`verbatim`
- 国语咬字：字正腔圆，辅音轻、元音饱满。`impression`
- 演歌乐句：中文歌里带日本演歌的拖音与收束。`artifact`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：甜美音色本身就是月光的距离感。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是浪漫的底色。`impression`
- 节奏：缓慢的抒情节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如低语，换气在句间。`impression`
- 与伴奏的咬合：弦乐与钢琴只铺底，不抢人声。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：甜美抒情、月亮与思念的叙事、气声耳语的情歌、演歌乐句的中文歌。
- 不该唱：No tearing high notes、no rock shouting、no mumbled diction、no wide operatic vibrato、no sentimental outburst。
- Negative prompt: `No tearing high notes, no rock shouting, no mumbled diction, no wide operatic vibrato, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于深夜捧着奶茶等末班车的女人的歌）

- Prompt: `Sing in the style of Teresa Teng, a song about a woman waiting for the last train home with a cup of milk tea. Sweet clear soprano, breathy intimacy, precise Mandarin diction, gentle vibrato, Japanese enka phrasing in Chinese songs, romance whispered rather than declared.`
- 中文对照：甜美清澈的女高音，气声亲密感，精准的国语咬字，轻柔颤音，中文歌里的日本演歌乐句，浪漫是耳语而非宣告，声音如月光。 唱一首关于深夜捧着奶茶等末班车的女人的歌。
- Negative: `No tearing high notes, no rock shouting, no mumbled diction, no wide operatic vibrato, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
