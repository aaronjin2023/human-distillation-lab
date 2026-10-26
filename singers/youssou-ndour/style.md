# Youssou N'Dour — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mbalax vocal in the style of Youssou N'Dour: soaring Senegalese tenor, griot declamation, sabar drum polyrhythm, Wolof diction, ecstatic melisma, call-and-response with chorus, celebration and praise rather than lament`
- ZH: 尤素·恩杜尔风格：翱翔的塞内加尔男高音，格里奥式 declamation，萨巴尔鼓复节奏，沃洛夫语咬字，狂喜的转音，与合唱队呼应，欢庆与赞颂而非哀诉。

## (2) 音色与音域

- 声部：男高音（tenor），音域宽。
- 音色：主音色：明亮、穿透、富于弹性的塞内加尔男高音；辅音色：格里奥式的 declamation 与狂喜转音；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域宽，高音翱翔、低音叙事。

## (3) 唱腔与发声技法

- 格里奥式 declamation：如史诗讲述般的演唱，节奏自由。`impression`
- 狂喜转音：melisma 如即兴攀升，落点清晰。`verbatim`
- 萨巴尔鼓复节奏：人声踩在复节奏上，身体感强。`artifact`
- 沃洛夫语咬字：辅音颗粒清晰，重音落在词义上。`impression`
- 呼应合唱：主唱与合唱队一呼一应。`verbatim`

## (4) 咬字与语言

- 音色即语言：明亮高音本身就是赞颂的幅度。`impression`
- 力度：中强力度为主，高潮处抬高，不煽情。`impression`
- 节奏：复节奏，人声与萨巴尔鼓咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如史诗，换气在句间。`impression`
- 与伴奏的咬合：鼓与合唱队构成呼应，人声居中。`impression`
- 情感递进：由讲述到狂喜，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：姆巴拉克斯赞颂歌曲、格里奥史诗讲述、跨文化二重唱、主唱与合唱队的呼应。
- 不该唱：No operatic roundness、no rock shouting、no sentimental outburst、no mumbled diction、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no rock shouting, no sentimental outburst, no mumbled diction, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于黎明时分渔民在海边补网的歌）

- Prompt: `Sing in the style of Youssou N'Dour, a song about fishermen mending nets at dawn by the sea. Soaring Senegalese tenor, griot declamation, sabar drum polyrhythm, Wolof diction, ecstatic melisma, call-and-response with chorus, celebration and praise.`
- 中文对照：翱翔的塞内加尔男高音，格里奥式 declamation，萨巴尔鼓复节奏，沃洛夫语咬字，狂喜的转音，与合唱队呼应，欢庆与赞颂而非哀诉。 唱一首关于黎明时分渔民在海边补网的歌。
- Negative: `No operatic roundness, no rock shouting, no sentimental outburst, no mumbled diction, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
