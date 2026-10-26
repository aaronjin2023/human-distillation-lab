# Bono — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Alternative rock vocal in the style of Bono: soaring Irish tenor, falsetto leaps, earnest anthemic delivery, whispered intimacy building into stadium-sized choruses, spiritual urgency in every line`
- ZH: Bono 风格：高扬的爱尔兰男高音，假声跳跃，真诚的颂歌式演唱，耳语亲密 渐强至体育场级副歌，每句都有灵性的急切。

## (2) 音色与音域

- 音色：明亮高扬的男高音，高音区带假声色彩；主音色为颂歌式胸声，辅音色为耳语气声；禁音色为冷漠平铺与沙哑嘶吼。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音滑入或直接，收尾拖长渐弱；真假声切换频繁，《With or Without You》以假声收尾为标记；颤音自然。`artifact`

## (4) 咬字与语言

- 咬字：爱尔兰口音底色的英式发音，元音开、辅音清晰；重音落在信念词上；换气点长，气口即祈祷感。`artifact`

## (5) 节奏与即兴

- 节奏：另类摇滚节拍上拖拍，副歌常以长音推进；即兴以现场拉长尾句与即兴呼喊为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 颂歌式副歌与信念、爱、救赎主题的歌曲（如《One》《Beautiful Day》一类）
- 耳语主歌接高扬副歌的 渐强 推进
- 假声收尾与长音延持
- 体育场式的召唤与合唱
- 不该唱：`No detached irony, no mumbled delivery, no raspy shouting, no operatic vibrato, no flat monotone delivery`
- Negative prompt: `No detached irony, no mumbled delivery, no raspy shouting, no operatic vibrato, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：凌晨的机场）

- Prompt: `Sing in the style of Bono, a song about waiting at an airport in the early morning. Soaring Irish tenor, falsetto leaps, earnest anthemic delivery, whispered intimacy building into stadium-sized choruses, spiritual urgency.`
- 中文对照：Bono 风格：唱一首关于凌晨机场等候的歌。高扬的爱尔兰男高音，假声跳跃，真诚的颂歌式演唱，耳语亲密 渐强至体育场级副歌，灵性的急切。
- Negative: `No detached irony, no mumbled delivery, no raspy shouting, no operatic vibrato`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
