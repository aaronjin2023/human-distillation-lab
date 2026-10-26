# Hibari Misora — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Enka vocal in the style of Hibari Misora: warm contralto, enka kobushi ornamentation, precise Japanese diction, slow deliberate phrasing, dramatic vibrato, tears held back rather than shed, a song as a river flowing on`
- ZH: 美空云雀风格：温暖的女中音，演歌小节装饰音，精准的日语咬字，缓慢而有意的乐句，戏剧性颤音，忍住的眼泪而非哭出，歌如川流不息。

## (2) 音色与音域

- 声部：女中音（contralto），常用中低音区。
- 音色：主音色：温暖、富于穿透力的女中音；辅音色：演歌小节的装饰音；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中低音区为叙事主场，高音区以颤音收束。

## (3) 唱腔与发声技法

- 演歌小节：装饰音如小节般起伏，是声口标记。`verbatim`
- 戏剧性颤音：颤音宽而均匀，句尾轻现。`impression`
- 日语咬字：辅音清晰，元音饱满，重音落在词义上。`impression`
- 缓慢乐句：速度极慢，停顿即意义。`impression`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：温暖音色本身就是川流的距离感。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是演歌的底色。`impression`
- 节奏：缓慢的演歌节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如川流，换气在句间。`impression`
- 与伴奏的咬合：弦乐与尺八式音色只铺底，不抢人声。`impression`
- 情感递进：由平静到深情，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：演歌抒情、川流与柔情的叙事、演歌小节装饰、缓慢乐句的慢歌。
- 不该唱：No operatic roundness、no rock shouting、no sweet pop vibrato、no mumbled diction、no sentimental outburst。
- Negative prompt: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于黄昏时分老妇人看河水从家门前流过的歌）

- Prompt: `Sing in the style of Hibari Misora, a song about an old woman watching a river flow past her house at dusk. Warm contralto, enka kobushi ornamentation, precise Japanese diction, slow deliberate phrasing, dramatic vibrato, tears held back rather than shed.`
- 中文对照：温暖的女中音，演歌小节装饰音，精准的日语咬字，缓慢而有意的乐句，戏剧性颤音，忍住的眼泪而非哭出，歌如川流不息。 唱一首关于黄昏时分老妇人看河水从家门前流过的歌。
- Negative: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
