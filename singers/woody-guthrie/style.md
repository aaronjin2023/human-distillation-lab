# Woody Guthrie — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Folk vocal in the style of Woody Guthrie: plainspoken Dust Bowl voice, conversational delivery, harmonica and guitar, flat unadorned phrasing, plain diction, a song as a newspaper report rather than a performance`
- ZH: 伍迪·格思里风格：朴素的沙尘暴之声，口语化演唱，口琴与吉他，平直无装饰的乐句，咬字质朴，歌如新闻报道而非表演。

## (2) 音色与音域

- 声部：男中音（baritone），常用中低音区。
- 音色：主音色：质朴、平直、略带鼻音的男中音；辅音色：口琴的呼应；禁音色：美声式圆润、摇滚喊腔、甜美颤音。音域窄，中低音区为叙事主场，高音区收敛。

## (3) 唱腔与发声技法

- 口语化演唱：像说话一样唱歌，旋律服从语言重音。`verbatim`
- 吉他与口琴：吉他扫弦定节奏，口琴在间奏呼应。`artifact`
- 平直乐句：少装饰音，旋律线短而直。`impression`
- 咬字质朴：元音扁平，辅音直接，无美化。`impression`
- 现场一次成形：录音少补录，瑕疵即真实。`impression`

## (4) 咬字与语言

- 音色即语言：质朴音色本身就是底层叙事的可信度。`impression`
- 力度：中弱力度为主，几乎不抬高潮，平直是立场。`impression`
- 节奏：稳健的民谣节拍，口琴与吉他定拍，人声略拖。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如口述，句尾自然收束。`impression`
- 与伴奏的咬合：吉他只定节奏，不抢歌词。`impression`
- 情感递进：由平静陈述到愤怒控诉，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：土地与流浪工人的新闻式叙事、口语化民谣、吉他口琴伴奏的抗议歌曲、家园主题的合唱式民谣。
- 不该唱：No operatic roundness、no rock shouting、no sweet vibrato、no ornate melisma、no polished pop phrasing。
- Negative prompt: `No operatic roundness, no rock shouting, no sweet vibrato, no ornate melisma, no polished pop phrasing`

## (7) 测试提示词示例（现代题材：唱一首关于外卖骑手在雨中等单的歌）

- Prompt: `Sing in the style of Woody Guthrie, a song about a delivery rider waiting for an order in the rain. Plainspoken voice, conversational delivery, acoustic guitar and harmonica, flat unadorned phrasing, plain diction, a song as a newspaper report.`
- 中文对照：朴素的沙尘暴之声，口语化演唱，口琴与吉他，平直无装饰的乐句，咬字质朴，歌如新闻报道而非表演。 唱一首关于外卖骑手在雨中等单的歌。
- Negative: `No operatic roundness, no rock shouting, no sweet vibrato, no ornate melisma, no polished pop phrasing`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
