# Cui Jian — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Chinese rock vocal in the style of Cui Jian: raw hoarse tenor, shouted declamation, suona and electric guitar, northwestern folk inflection, Beijing accent, a song as a shout from the street rather than a melody`
- ZH: 崔健风格：粗粝沙哑的男高音，喊叫式 declamation，唢呐与电吉他，西北民歌腔调，北京口音，歌如街头的喊叫而非旋律。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：粗粝、沙哑、富于穿透力的男高音；辅音色：唢呐的呼应；禁音色：美声式圆润、甜腻颤音、气声耳语。音域以中音区为叙事主场，高音区以喊叫攀升。

## (3) 唱腔与发声技法

- 喊叫式 declamation：半喊半唱，旋律服从语言重音。`verbatim`
- 唢呐呼应：唢呐与人声一呼一应，是声口标记。`artifact`
- 西北民歌腔调：旋律带西北民歌的滑音与拖腔。`impression`
- 北京口音咬字：辅音硬朗，重音落在词义上。`impression`
- 电吉他：吉他定节奏，人声在其上喊叫。`impression`

## (4) 咬字与语言

- 音色即语言：粗粝音色本身就是街头喊叫的可信度。`impression`
- 力度：中强力度为主，高潮处抬高，不煽情。`impression`
- 节奏：摇滚节拍，人声与吉他咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如喊叫，换气在句间。`impression`
- 与伴奏的咬合：唢呐与吉他构成呼应，人声居中。`impression`
- 情感递进：由讲述到喊叫，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：华语摇滚、喊叫式 declamation、唢呐呼应的摇滚、西北民歌腔调的叙事。
- 不该唱：No operatic roundness、no sweet pop vibrato、no breathy whisper、no mumbled diction、no polished studio gloss。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no breathy whisper, no mumbled diction, no polished studio gloss`

## (7) 测试提示词示例（现代题材：唱一首关于黎明时分建筑工人在脚手架上唱歌的歌）

- Prompt: `Sing in the style of Cui Jian, a song about a construction worker singing on scaffolding at dawn. Raw hoarse tenor, shouted declamation, suona and electric guitar, northwestern folk inflection, Beijing accent, a song as a shout from the street.`
- 中文对照：粗粝沙哑的男高音，喊叫式 declamation，唢呐与电吉他，西北民歌腔调，北京口音，歌如街头的喊叫而非旋律。 唱一首关于黎明时分建筑工人在脚手架上唱歌的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no breathy whisper, no mumbled diction, no polished studio gloss`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
