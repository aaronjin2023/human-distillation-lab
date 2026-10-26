# Jacques Brel — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Chanson vocal in the style of Jacques Brel: theatrical baritone, spoken-sung declamation, Flemish-French accent, crescendo that builds from whisper to shout, precise diction, piano and orchestra, a song as a one-act play rather than a melody`
- ZH: 雅克·布雷尔风格：戏剧男中音，说唱式 declamation，弗拉芒法语口音，从耳语到喊叫的渐强，咬字精准，钢琴与管弦乐，歌如独幕剧而非旋律。

## (2) 音色与音域

- 声部：男中音（baritone），常用中音区。
- 音色：主音色：戏剧化、富于变化的男中音；辅音色：耳语与喊叫的两极；禁音色：美声式圆润、甜腻颤音、摇滚喊腔。音域以中音区为叙事主场，高音区以喊叫攀升。

## (3) 唱腔与发声技法

- 戏剧渐强：从耳语到喊叫的渐强（布雷尔式渐强）是声口标记。`verbatim`
- 说唱式 declamation：半说半唱，旋律服从法语重音。`verbatim`
- 弗拉芒口音：法语带弗拉芒腔，辅音硬朗。`impression`
- 戏剧性停顿：停顿即意义，沉默也是语言。`impression`
- 现场一次成形：奥林匹亚现场少补录，汗水与喊叫即真实。`artifact`

## (4) 咬字与语言

- 音色即语言：戏剧音色本身就是独幕剧的舞台。`impression`
- 力度：由耳语到喊叫，幅度为香颂之最。`impression`
- 节奏：自由节奏，钢琴定拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如独白，换气在句间。`impression`
- 与伴奏的咬合：钢琴轻铺，管弦乐只在高潮点进入。`impression`
- 情感递进：由低语到喊叫，层层推进，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：告别与死亡的独幕剧、水手与港口的叙事、戏剧渐强的香颂、说唱式 declamation。
- 不该唱：No operatic roundness、no sweet pop vibrato、no mumbled diction、no rock shouting、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于打烊时分独自在港口酒吧喝酒的老水手的歌）

- Prompt: `Sing in the style of Jacques Brel, a song about an old sailor drinking alone at a harbour bar at closing time. Theatrical baritone, spoken-sung declamation, Flemish-French accent, crescendo from whisper to shout, precise diction, piano and orchestra, a song as a one-act play.`
- 中文对照：戏剧男中音，说唱式 declamation，弗拉芒法语口音，从耳语到喊叫的渐强，咬字精准，钢琴与管弦乐，歌如独幕剧而非旋律。 唱一首关于打烊时分独自在港口酒吧喝酒的老水手的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
