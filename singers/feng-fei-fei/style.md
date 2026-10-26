# Feng Fei-fei — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandopop vocal in the style of Feng Fei-fei: warm clear soprano, bright and generous delivery, precise Mandarin diction, gentle vibrato, stage warmth, a song as a greeting to the whole audience rather than a confession`
- ZH: 凤飞飞风格：温暖清澈的女高音，明亮大方的演唱，精准的国语咬字，轻柔颤音，舞台的温暖，歌如向全场观众的问候而非独白。

## (2) 音色与音域

- 声部：女高音（soprano），常用中高音区。
- 音色：主音色：温暖、清澈、富于舞台感的女高音；辅音色：轻柔颤音；禁音色：撕裂高音、摇滚喊腔、含混咬字。音域以中高音区为叙事主场，高音区明亮收束。

## (3) 唱腔与发声技法

- 明亮演唱：音色明亮大方，是声口标记。`verbatim`
- 轻柔颤音：颤音窄而均匀，句尾轻现。`impression`
- 国语咬字：字正腔圆，辅音轻、元音饱满。`impression`
- 舞台感：现场演唱带亲和力，声音即问候。`artifact`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：温暖音色本身就是问候的亲和力。`impression`
- 力度：中强力度为主，高潮处抬高，不煽情。`impression`
- 节奏：稳健的流行节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如问候，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由问候到深情，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：温暖抒情、掌声与追梦的叙事、舞台问候式演唱、明亮的华语流行。
- 不该唱：No tearing high notes、no rock shouting、no mumbled diction、no wide operatic vibrato、no sentimental outburst。
- Negative prompt: `No tearing high notes, no rock shouting, no mumbled diction, no wide operatic vibrato, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于夜市里为街头艺人鼓掌的女人的歌）

- Prompt: `Sing in the style of Feng Fei-fei, a song about a woman applauding a street performer at a night market. Warm clear soprano, bright and generous delivery, precise Mandarin diction, gentle vibrato, stage warmth, a song as a greeting to the whole audience.`
- 中文对照：温暖清澈的女高音，明亮大方的演唱，精准的国语咬字，轻柔颤音，舞台的温暖，歌如向全场观众的问候而非独白。 唱一首关于夜市里为街头艺人鼓掌的女人的歌。
- Negative: `No tearing high notes, no rock shouting, no mumbled diction, no wide operatic vibrato, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
