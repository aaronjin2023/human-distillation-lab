# Luther Vandross — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `R&B vocal in the style of Luther Vandross: velvet tenor, silky legato, precise melisma, warm mid-register, intimate phrasing, gospel-rooted ad-libs, romantic and restrained rather than showy`
- ZH: 卢瑟·范德罗斯风格：丝绒男高音，圆润连音，精准转音，温暖的中音区，亲密的乐句，福音根源的即兴装饰，浪漫而克制，不炫技。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：丝绒般圆润、温暖的男高音，中音区最厚实；辅音色：轻柔的气声与福音式即兴高音；禁音色：沙哑摇滚喊腔、干硬的说唱式咬字。音域以中音区为叙事主场，高音区以假声轻收，不硬顶。

## (3) 唱腔与发声技法

- 丝绒连音：乐句以 legato 贯穿，音与音之间无断点，气息支撑平稳。`verbatim`
- 精准转音：melisma 每个音都落点清晰，转音为装饰而非炫技。`verbatim`
- 福音即兴：尾句的 ad-lib 源自福音传统，自由但不离和声。`impression`
- 换气藏于乐句间：长乐句一气呵成，换气点极隐蔽。`impression`
- 和声伴唱出身的声部感：主唱与和声的咬合极准，层次分明。`artifact`
- 录音室多遍录制：同一乐句多遍备选，选最贴合情感的一遍。`impression`

## (4) 咬字与语言

- 音色即语言：丝绒音色本身就是亲密感，听者先被音色安抚，再听歌词。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是浪漫的底色。`impression`
- 节奏：略拖拍，摇摆感柔和，与伴奏错位极小。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如独白，句尾渐弱收束，不戛然而止。`impression`
- 与伴奏的咬合：人声居中，弦乐与键盘只铺底，不抢主唱。`impression`
- 情感递进：由低语到倾诉再到高潮，层层推进，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：浪漫 R&B 情歌、中音区叙事抒情、福音式尾句即兴、《Dance with My Father》式的怀念叙事。
- 不该唱：No rough rock shouting、no showy high-note belting、no sentimental outburst、no mumbled diction、no harsh gospel scream。
- Negative prompt: `No rough rock shouting, no showy high-note belting, no sentimental outburst, no mumbled diction, no harsh gospel scream`

## (7) 测试提示词示例（现代题材：唱一首关于夜班护士凌晨三点在便利店买咖啡的歌）

- Prompt: `Sing in the style of Luther Vandross, a song about a night-shift nurse buying coffee at a convenience store at 3 a.m. Velvet tenor, silky legato, precise melisma, warm mid-register, intimate phrasing, soft R&B groove, romantic and restrained.`
- 中文对照：丝绒男高音，圆润连音，精准转音，温暖的中音区，亲密的乐句，福音根源的即兴装饰，浪漫而克制，不炫技。 唱一首关于夜班护士凌晨三点在便利店买咖啡的歌。
- Negative: `No rough rock shouting, no showy high-note belting, no sentimental outburst, no mumbled diction, no harsh gospel scream`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
