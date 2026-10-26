# Lo Ta-yu — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandarin folk vocal in the style of Lo Ta-yu: plainspoken baritone, conversational delivery, precise Mandarin diction, social commentary as storytelling, guitar and piano, nostalgia without sentimentality, a song as a newspaper editorial sung plain`
- ZH: 罗大佑风格：质朴的男中音，口语化演唱，精准的国语咬字，社会评论如讲故事，吉他与钢琴，怀旧而不伤感，歌如唱出来的社论。

## (2) 音色与音域

- 声部：男中音（baritone），常用中低音区。
- 音色：主音色：质朴、平直、富于叙事感的男中音；辅音色：口语化的低语；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中低音区为叙事主场，高音区收敛。

## (3) 唱腔与发声技法

- 口语化演唱：像说话一样唱歌，旋律服从语言重音。`verbatim`
- 社会评论式叙事：歌词如社论，演唱如讲述。`impression`
- 国语咬字：字正腔圆，辅音清晰。`impression`
- 吉他与钢琴：伴奏轻铺，人声在其上叙事。`artifact`
- 换气藏于句间：长乐句气息平稳，换气点在叙事停顿处。`impression`

## (4) 咬字与语言

- 音色即语言：质朴音色本身就是社论的可信度。`impression`
- 力度：中弱力度为主，几乎不抬高潮，平直是立场。`impression`
- 节奏：稳健的民谣节拍，人声略拖。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如口述，句尾自然收束。`impression`
- 与伴奏的咬合：吉他与钢琴只铺底，不抢歌词。`impression`
- 情感递进：由平静陈述到愤怒控诉，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：童年与故乡的叙事、社会评论式民谣、恋曲与时代、口语化演唱。
- 不该唱：No operatic roundness、no rock shouting、no sweet pop vibrato、no mumbled diction、no sentimental outburst。
- Negative prompt: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于在地铁口卖了三十年报纸、看着城市变迁的老人的歌）

- Prompt: `Sing in the style of Lo Ta-yu, a song about an old man selling newspapers at a subway exit who has watched the city change for thirty years. Plainspoken baritone, conversational delivery, precise Mandarin diction, social commentary as storytelling, guitar and piano, nostalgia without sentimentality.`
- 中文对照：质朴的男中音，口语化演唱，精准的国语咬字，社会评论如讲故事，吉他与钢琴，怀旧而不伤感，歌如唱出来的社论。 唱一首关于在地铁口卖了三十年报纸、看着城市变迁的老人的歌。
- Negative: `No operatic roundness, no rock shouting, no sweet pop vibrato, no mumbled diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
