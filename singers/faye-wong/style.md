# Faye Wong — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandopop vocal in the style of Faye Wong: cool ethereal soprano, airy breathy delivery, precise Mandarin and Cantonese diction, minimal vibrato, dreamlike phrasing, detachment rather than declaration, a voice like mist`
- ZH: 王菲风格：清冷空灵的女高音，气声演唱，精准的国粤语咬字，极少颤音，梦幻般的乐句，疏离而非宣告，声音如雾。

## (2) 音色与音域

- 声部：女高音（soprano），常用中高音区。
- 音色：主音色：清冷、空灵、富于穿透力的女高音；辅音色：气声耳语；禁音色：撕裂高音、摇滚喊腔、甜腻颤音。音域以中高音区为叙事主场，高音区轻柔收束。

## (3) 唱腔与发声技法

- 气声空灵：近距离麦克风，气息声即空灵感的一部分。`verbatim`
- 极少颤音：直声为主，颤音只在句尾轻现。`impression`
- 国粤双语咬字：国语与粤语切换自然，重音各归其位。`artifact`
- 梦幻乐句：乐句如梦境，停顿即意义。`impression`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：清冷音色本身就是疏离的距离感。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是空灵的底色。`impression`
- 节奏：缓慢的抒情节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如梦境，换气在句间。`impression`
- 与伴奏的咬合：钢琴与弦乐只铺底，不抢人声。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：清冷空灵的抒情、红豆与相思的叙事、国粤双语情歌、梦幻乐句的慢歌。
- 不该唱：No tearing high notes、no rock shouting、no sweet pop vibrato、no mumbled diction、no sentimental outburst。
- Negative prompt: `No tearing high notes, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于午夜在阳台看雪的女人的歌）

- Prompt: `Sing in the style of Faye Wong, a song about a woman watching snow fall on a balcony at midnight. Cool ethereal soprano, airy breathy delivery, precise Mandarin diction, minimal vibrato, dreamlike phrasing, detachment rather than declaration, a voice like mist.`
- 中文对照：清冷空灵的女高音，气声演唱，精准的国粤语咬字，极少颤音，梦幻般的乐句，疏离而非宣告，声音如雾。 唱一首关于午夜在阳台看雪的女人的歌。
- Negative: `No tearing high notes, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
