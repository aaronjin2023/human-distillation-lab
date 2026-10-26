# Tsai Chin — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandopop vocal in the style of Tsai Chin: deep warm contralto, slow deliberate phrasing, precise Mandarin diction, minimal vibrato, late-night radio intimacy, nostalgia without sentimentality, a song as a whisper to one listener at 2 a.m.`
- ZH: 蔡琴风格：深沉温暖的女中音，缓慢而有意的乐句，精准的国语咬字，极少颤音，深夜电台般的亲密感，怀旧而不伤感，歌如凌晨两点对一位听者的耳语。

## (2) 音色与音域

- 声部：女中音（contralto），常用中低音区。
- 音色：主音色：深沉、温暖、富于穿透力的女中音；辅音色：耳语般的气声；禁音色：撕裂高音、摇滚喊腔、甜腻颤音。音域以中低音区为叙事主场，高音区收敛。

## (3) 唱腔与发声技法

- 深沉女中音：低音区厚实，是声口标记。`verbatim`
- 缓慢乐句：速度极慢，停顿即意义。`impression`
- 极少颤音：直声为主，颤音只在句尾轻现。`impression`
- 国语咬字：字正腔圆，辅音轻、元音饱满。`impression`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：深沉音色本身就是深夜的距离感。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是怀旧的底色。`impression`
- 节奏：缓慢的抒情节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如耳语，换气在句间。`impression`
- 与伴奏的咬合：钢琴与弦乐只铺底，不抢人声。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：深沉抒情、温柔与遗忘的叙事、深夜耳语式慢歌、缓慢乐句的华语流行。
- 不该唱：No tearing high notes、no rock shouting、no sweet pop vibrato、no mumbled diction、no sentimental outburst。
- Negative prompt: `No tearing high notes, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于午夜空房间里听旧收音机的女人的歌）

- Prompt: `Sing in the style of Tsai Chin, a song about a woman listening to an old radio in an empty apartment at midnight. Deep warm contralto, slow deliberate phrasing, precise Mandarin diction, minimal vibrato, late-night radio intimacy, nostalgia without sentimentality.`
- 中文对照：深沉温暖的女中音，缓慢而有意的乐句，精准的国语咬字，极少颤音，深夜电台般的亲密感，怀旧而不伤感，歌如凌晨两点对一位听者的耳语。 唱一首关于午夜空房间里听旧收音机的女人的歌。
- Negative: `No tearing high notes, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
