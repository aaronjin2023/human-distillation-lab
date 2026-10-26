# Joan Baez — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Folk vocal in the style of Joan Baez: clear crystalline soprano, pure vibrato, precise diction, guitar-led accompaniment, narrative restraint, protest song delivered as testimony rather than shouting`
- ZH: 琼·贝兹风格：清澈水晶女高音，纯净颤音，咬字精准，吉他主导伴奏，叙事克制，抗议歌曲如证词般陈述而不喊叫。

## (2) 音色与音域

- 声部：女高音（soprano），常用中高音区。
- 音色：主音色：清澈、明亮、水晶般纯净的女高音；辅音色：低音区的讲述感；禁音色：沙哑摇滚、甜腻流行颤音、歌剧式花腔。音域以中高音区为叙事主场，高音清亮不尖锐。

## (3) 唱腔与发声技法

- 纯净颤音：颤音均匀而窄，音准极稳，是声口标记。`verbatim`
- 吉他自弹自唱：尼龙弦吉他的指弹与人声同步呼吸。`artifact`
- 咬字清晰：每个辅音都交代清楚，歌词可听性极高。`verbatim`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`
- 现场一次成形：民谣现场少补录，瑕疵即真实。`impression`

## (4) 咬字与语言

- 音色即语言：清澈音色本身就是证词的可信度，听者先信声音，再信歌词。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是抗议的底色。`impression`
- 节奏：稳健的民谣节拍，偶有自由延长，拖拍极少。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：叙事乐句如讲述，句尾渐弱收束。`impression`
- 与吉他的咬合：人声与吉他同呼吸，吉他只铺底，不抢歌词。`impression`
- 情感递进：由平静讲述到内心涌动，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：抗议民谣与历史叙事、清澈女高音的个人回忆、吉他自弹自唱的翻唱演绎、现场清唱与观众合唱。
- 不该唱：No shouting protest、no sweet pop crooning、no mumbled diction、no operatic coloratura、no rough rock rasp。
- Negative prompt: `No shouting protest, no sweet pop crooning, no mumbled diction, no operatic coloratura, no rough rock rasp`

## (7) 测试提示词示例（现代题材：唱一首关于清晨菜市场卖菜老妇人的歌）

- Prompt: `Sing in the style of Joan Baez, a song about an old woman selling vegetables at a morning market. Clear crystalline soprano, pure vibrato, precise diction, acoustic guitar, narrative restraint, testimony rather than shouting.`
- 中文对照：清澈水晶女高音，纯净颤音，咬字精准，吉他主导伴奏，叙事克制，抗议歌曲如证词般陈述而不喊叫。 唱一首关于清晨菜市场卖菜老妇人的歌。
- Negative: `No shouting protest, no sweet pop crooning, no mumbled diction, no operatic coloratura, no rough rock rasp`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
