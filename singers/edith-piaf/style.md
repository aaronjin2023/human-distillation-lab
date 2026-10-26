# Édith Piaf — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Chanson vocal in the style of Édith Piaf: small raw voice with huge dramatic force, Parisian accent, vibrato that trembles rather than ornaments, spoken-sung phrasing, accordion and orchestra, love and regret delivered as testimony, climax as cry rather than polish`
- ZH: 艾迪特·皮亚芙风格：小而粗粝却戏剧张力巨大的声音，巴黎腔，颤抖而非装饰的颤音，说唱式乐句，手风琴与管弦乐，爱与悔恨如证词般陈述，高潮是哭喊而非圆润。

## (2) 音色与音域

- 声部：女中音（mezzo-soprano），常用中音区。
- 音色：主音色：粗粝、直接、富于穿透力的女中音；辅音色：颤抖的颤音与气声；禁音色：美声式圆润、甜腻流行颤音、摇滚喊腔。音域以中音区为叙事主场，高音区以哭喊攀升。

## (3) 唱腔与发声技法

- 颤抖的颤音：颤音如颤抖而非装饰，是声口标记。`verbatim`
- 说唱式乐句：半说半唱，旋律服从法语重音。`verbatim`
- 巴黎腔咬字：辅音清晰，元音饱满，重音落在词义上。`impression`
- 戏剧性停顿：停顿即意义，沉默也是语言。`impression`
- 现场一次成形：奥林匹亚现场少补录，哭喊即真实。`artifact`

## (4) 咬字与语言

- 音色即语言：粗粝音色本身就是街头证词的可信度。`impression`
- 力度：由低语到哭喊，幅度大，高潮是哭喊而非圆润。`impression`
- 节奏：自由节奏，钢琴定拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如倾诉，换气在句间。`impression`
- 与伴奏的咬合：手风琴与弦乐铺底，人声居中。`impression`
- 情感递进：由平静到哭喊，层层推进，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：爱与悔恨的香颂、巴黎街头叙事、证词式倾诉、哭喊式高潮。
- 不该唱：No operatic roundness、no sweet pop vibrato、no mumbled diction、no rock shouting、no polished studio gloss。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no polished studio gloss`

## (7) 测试提示词示例（现代题材：唱一首关于午夜地铁站卖花女人的歌）

- Prompt: `Sing in the style of Édith Piaf, a song about a woman selling flowers at a metro station at midnight. Small raw voice with huge dramatic force, Parisian accent, trembling vibrato, spoken-sung phrasing, accordion and orchestra, testimony rather than polish.`
- 中文对照：小而粗粝却戏剧张力巨大的声音，巴黎腔，颤抖而非装饰的颤音，说唱式乐句，手风琴与管弦乐，爱与悔恨如证词般陈述，高潮是哭喊而非圆润。 唱一首关于午夜地铁站卖花女人的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no polished studio gloss`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
