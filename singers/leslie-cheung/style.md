# Leslie Cheung — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Cantopop vocal in the style of Leslie Cheung: warm romantic tenor, intimate breathy delivery, precise Cantonese diction, gentle vibrato, dance-pop energy with ballad tenderness, romance whispered rather than declared`
- ZH: 张国荣风格：温暖浪漫的男高音，亲密的气声演唱，精准的粤语咬字，轻柔颤音，舞曲能量与抒情柔情并存，浪漫是耳语而非宣告。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：温暖、浪漫、富于亲密感的男高音；辅音色：气声耳语；禁音色：摇滚喊腔、美声式高音、甜腻颤音。音域以中音区为叙事主场，高音区轻收。

## (3) 唱腔与发声技法

- 气声亲密感：近距离麦克风，气息声即亲密感的一部分。`verbatim`
- 轻柔颤音：颤音窄而均匀，句尾轻现。`impression`
- 粤语咬字：辅音轻、元音饱满，重音落在词义上。`impression`
- 舞曲能量：快歌以节奏驱动，人声踩在节拍上。`artifact`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：温暖音色本身就是浪漫的距离感。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是浪漫的底色。`impression`
- 节奏：流行节拍，快歌踩拍、慢歌拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如低语，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：浪漫抒情、风与往事的叙事、舞曲能量的粤语流行、气声耳语的情歌。
- 不该唱：No rock shouting、no operatic high notes、no sentimental outburst、no mumbled diction、no wide vibrato。
- Negative prompt: `No rock shouting, no operatic high notes, no sentimental outburst, no mumbled diction, no wide vibrato`

## (7) 测试提示词示例（现代题材：唱一首关于深夜公交车上折纸鹤的男人的歌）

- Prompt: `Sing in the style of Leslie Cheung, a song about a man folding paper cranes on a night bus home. Warm romantic tenor, intimate breathy delivery, precise Cantonese diction, gentle vibrato, dance-pop energy with ballad tenderness, romance whispered rather than declared.`
- 中文对照：温暖浪漫的男高音，亲密的气声演唱，精准的粤语咬字，轻柔颤音，舞曲能量与抒情柔情并存，浪漫是耳语而非宣告。 唱一首关于深夜公交车上折纸鹤的男人的歌。
- Negative: `No rock shouting, no operatic high notes, no sentimental outburst, no mumbled diction, no wide vibrato`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
