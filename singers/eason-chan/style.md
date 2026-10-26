# Eason Chan — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Cantopop vocal in the style of Eason Chan: versatile tenor, conversational delivery, precise Cantonese and Mandarin diction, emotional restraint with sudden release, storytelling phrasing, a song as a monologue overheard rather than a performance`
- ZH: 陈奕迅风格：多变的男高音，口语化演唱，精准的粤国语咬字，克制中突然释放的情感，讲故事的乐句，歌如无意中听到的独白而非表演。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：温暖、多变、富于叙事感的男高音；辅音色：口语化的低语与突然释放的高音；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中音区为叙事主场，高音区以释放攀升。

## (3) 唱腔与发声技法

- 口语化演唱：像说话一样唱歌，旋律服从语言重音。`verbatim`
- 克制与释放：全曲克制，只在关键句突然释放。`impression`
- 粤国双语咬字：粤语与国语切换自然，重音各归其位。`artifact`
- 讲故事乐句：乐句如独白，停顿即意义。`impression`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：温暖音色本身就是独白的可信度。`impression`
- 力度：中弱力度为主，释放处只抬半格，克制是独白的底色。`impression`
- 节奏：稳健的流行节拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如独白，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由克制到释放，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：独白式粤语流行、十年与往事的叙事、小丑自述的戏剧歌曲、克制与释放的抒情。
- 不该唱：No operatic roundness、no rock shouting、no sweet pop vibrato、no mumbled diction、no sentimental outburst。
- Negative prompt: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于凌晨两点在手机里翻到一张旧照片的男人的歌）

- Prompt: `Sing in the style of Eason Chan, a song about a man who finds an old photo in his phone at 2 a.m. Versatile tenor, conversational delivery, precise Cantonese diction, emotional restraint with sudden release, storytelling phrasing, a song as a monologue overheard.`
- 中文对照：多变的男高音，口语化演唱，精准的粤国语咬字，克制中突然释放的情感，讲故事的乐句，歌如无意中听到的独白而非表演。 唱一首关于凌晨两点在手机里翻到一张旧照片的男人的歌。
- Negative: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
