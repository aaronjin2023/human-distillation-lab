# Nusrat Fateh Ali Khan — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Qawwali vocal in the style of Nusrat Fateh Ali Khan: ecstatic tenor, sargam improvisation, long breath control, harmonium and tabla, devotional repetition, call-and-response with chorus, spiritual ecstasy built slowly rather than climaxed at once`
- ZH: 努斯拉特·法塔赫·阿里·汗风格：狂喜的男高音，萨伽姆即兴，长气息控制，风琴与塔布拉鼓，虔诚的反复，与合唱队呼应，灵性狂喜缓慢累积而不一次爆发。

## (2) 音色与音域

- 声部：男高音（tenor），音域宽。
- 音色：主音色：明亮、穿透、富于弹性的男高音；辅音色：萨伽姆即兴的快速音阶；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域宽，高音狂喜、低音叙事。

## (3) 唱腔与发声技法

- 萨伽姆即兴：以音节唱音阶，即兴攀升，落点清晰。`verbatim`
- 长气息控制：一口气唱长乐句，换气极隐蔽。`verbatim`
- 虔诚反复：同一诗句反复变奏，情感层层累积。`impression`
- 呼应合唱：主唱与合唱队一呼一应。`verbatim`
- 风琴与塔布拉鼓：伴奏定循环，人声在其上即兴。`artifact`

## (4) 咬字与语言

- 音色即语言：明亮高音本身就是灵性狂喜的幅度。`impression`
- 力度：由弱到强缓慢累积，高潮在长时延展后到达。`impression`
- 节奏：塔布拉鼓循环，人声在其上自由延展。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如祈祷，换气在句间。`impression`
- 与伴奏的咬合：风琴铺底，合唱队呼应，人声居中。`impression`
- 情感递进：由低语到狂喜，缓慢累积，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：苏菲卡瓦里赞颂、萨伽姆音节即兴、同一诗句的反复变奏、主唱与合唱队的呼应。
- 不该唱：No operatic roundness、no rock shouting、no one-shot climax、no mumbled diction、no short pop phrasing。
- Negative prompt: `No operatic roundness, no rock shouting, no one-shot climax, no mumbled diction, no short pop phrasing`

## (7) 测试提示词示例（现代题材：唱一首关于深夜火车穿越星空下沙漠的歌）

- Prompt: `Sing in the style of Nusrat Fateh Ali Khan, a song about a night train crossing a desert under the stars. Ecstatic tenor, sargam improvisation, long breath control, harmonium and tabla, devotional repetition, call-and-response with chorus, ecstasy built slowly.`
- 中文对照：狂喜的男高音，萨伽姆即兴，长气息控制，风琴与塔布拉鼓，虔诚的反复，与合唱队呼应，灵性狂喜缓慢累积而不一次爆发。 唱一首关于深夜火车穿越星空下沙漠的歌。
- Negative: `No operatic roundness, no rock shouting, no one-shot climax, no mumbled diction, no short pop phrasing`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
