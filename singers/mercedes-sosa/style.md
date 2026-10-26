# Mercedes Sosa — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Nueva canción vocal in the style of Mercedes Sosa: deep warm contralto, Andean folk roots, clear Spanish diction, guitar-led accompaniment, testimony rather than protest shouting, dignity and warmth rather than anger`
- ZH: 梅赛德斯·索萨风格：深沉温暖的女中音，安第斯民谣根源，清晰的西语咬字，吉他主导伴奏，证词而非喊叫式抗议，尊严与温暖而非愤怒。

## (2) 音色与音域

- 声部：女中音（contralto），常用中低音区。
- 音色：主音色：深沉、温暖、富于穿透力的女中音；辅音色：安第斯民谣的质朴感；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中低音区为叙事主场，高音区以克制收束。

## (3) 唱腔与发声技法

- 深沉女中音：低音区厚实，是声口标记。`verbatim`
- 吉他伴奏：吉他轻铺，人声在其上叙事。`artifact`
- 证词式演唱：如证词般陈述，不喊叫。`impression`
- 西语咬字：辅音与元音极清晰，重音落在词义上。`impression`
- 现场一次成形：现场录音少补录，尊严感即真实。`impression`

## (4) 咬字与语言

- 音色即语言：深沉音色本身就是尊严的距离感。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是尊严的底色。`impression`
- 节奏：稳健的民谣节拍，吉他定拍，人声略拖。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如讲述，换气在句间。`impression`
- 与伴奏的咬合：吉他只铺底，不抢歌词。`impression`
- 情感递进：由平静到深情，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：感恩与生命的新民歌、大海与诗人的叙事、拉美人民生活的证词、吉他伴奏的抒情。
- 不该唱：No shouting protest、no operatic roundness、no sentimental outburst、no mumbled diction、no rock shouting。
- Negative prompt: `No shouting protest, no operatic roundness, no sentimental outburst, no mumbled diction, no rock shouting`

## (7) 测试提示词示例（现代题材：唱一首关于黎明时分祖母教孙女揉面的歌）

- Prompt: `Sing in the style of Mercedes Sosa, a song about a grandmother teaching her granddaughter to knead bread at dawn. Deep warm contralto, Andean folk roots, clear Spanish diction, guitar-led accompaniment, testimony rather than protest shouting, dignity and warmth.`
- 中文对照：深沉温暖的女中音，安第斯民谣根源，清晰的西语咬字，吉他主导伴奏，证词而非喊叫式抗议，尊严与温暖而非愤怒。 唱一首关于黎明时分祖母教孙女揉面的歌。
- Negative: `No shouting protest, no operatic roundness, no sentimental outburst, no mumbled diction, no rock shouting`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
