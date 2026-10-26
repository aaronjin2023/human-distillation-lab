# João Gilberto — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Bossa nova vocal in the style of João Gilberto: whispered baritone, almost spoken delivery, guitar batida rhythm, minimal vibrato, Brazilian Portuguese diction, samba rhythm made intimate, silence as part of the melody`
- ZH: 若昂·吉尔贝托风格：耳语般的男中音，近乎说话的演唱，吉他巴蒂达节奏，极少颤音，巴西葡语咬字，桑巴节奏变得私密，沉默也是旋律的一部分。

## (2) 音色与音域

- 声部：男中音（baritone），常用中低音区。
- 音色：主音色：耳语般、轻柔、富于亲密感的男中音；辅音色：吉他巴蒂达的节奏；禁音色：美声式圆润、摇滚喊腔、甜腻颤音、高音炫技。音域窄，中低音区为叙事主场。

## (3) 唱腔与发声技法

- 耳语式演唱：近距离麦克风，气息声即语言的一部分。`verbatim`
- 吉他巴蒂达：自创的吉他节奏型，人声与吉他同呼吸。`artifact`
- 极少颤音：直声为主，颤音几乎不用。`impression`
- 沉默即旋律：停顿与留白是结构的一部分。`impression`
- 葡语咬字：辅音轻柔，元音饱满，重音落在词义上。`impression`

## (4) 咬字与语言

- 音色即语言：耳语音色本身就是私密感的距离。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是本体。`impression`
- 节奏：轻盈的桑巴节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如低语，换气在句间。`impression`
- 与伴奏的咬合：吉他只铺底，不抢人声。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：耳语式波萨诺瓦、吉他巴蒂达伴奏的抒情、乡愁与海滩叙事、沉默与留白的结构。
- 不该唱：No operatic roundness、no rock shouting、no showy high notes、no wide vibrato、no loud climax。
- Negative prompt: `No operatic roundness, no rock shouting, no showy high notes, no wide vibrato, no loud climax`

## (7) 测试提示词示例（现代题材：唱一首关于黎明时分男人在阳台看海的歌）

- Prompt: `Sing in the style of João Gilberto, a song about a man watching the sea from a balcony at dawn. Whispered baritone, almost spoken delivery, guitar batida rhythm, minimal vibrato, Brazilian Portuguese diction, samba rhythm made intimate, silence as part of the melody.`
- 中文对照：耳语般的男中音，近乎说话的演唱，吉他巴蒂达节奏，极少颤音，巴西葡语咬字，桑巴节奏变得私密，沉默也是旋律的一部分。 唱一首关于黎明时分男人在阳台看海的歌。
- Negative: `No operatic roundness, no rock shouting, no showy high notes, no wide vibrato, no loud climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
