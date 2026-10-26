# Axl Rose — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Hard rock vocal in the style of Axl Rose: extreme-range tenor, snake-like high screams against low raspy growls, sudden register leaps, urgent diction, theatrical menace and tenderness in one voice`
- ZH: 罗斯风格：极限音域男高音，蛇形高音嘶喊对照低沉沙哑吼声，音区骤然跳跃，咬字急切，威胁与温柔集于一身。

## (2) 音色与音域

- 音色：音域极宽的男高音，高音尖锐明亮、低音沙哑粗粝；主音色为高音嘶喊，辅音色为低声絮语；禁音色为圆润美声与温吞的抒情。`artifact`

## (3) 唱腔与发声技法

- 发声：真假声骤然切换，高音以头声嘶喊、低音以胸声吼叫；起音硬而直接，收尾常拖长嘶喊；《Sweet Child o' Mine》以高音长句为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音，辅音重、元音尖；重音落在攻击性词上；换气短促，气口即爆发点。`artifact`

## (5) 节奏与即兴

- 节奏：硬摇滚节拍上抢拍推进，副歌常提前进入；即兴以高音延持与尾段嘶喊为主，现场版常拉长高音。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 硬摇滚高音嘶喊与低吼对照的歌曲（如《Welcome to the Jungle》一类）
- 抒情主歌接爆发副歌的音区跳跃（如《November Rain》）
- 长句高音延持与尾段嘶喊
- 街头叙事与威胁感的演唱
- 不该唱：`No smooth crooning, no operatic vibrato, no mumbled delivery, no thin head voice, no restrained whisper throughout`
- Negative prompt: `No smooth crooning, no operatic vibrato, no mumbled delivery, no thin head voice, no restrained whisper throughout`

## (7) 测试提示词示例（现代题材：雨夜的出租车）

- Prompt: `Sing in the style of Axl Rose, a song about a taxi ride through a rainy modern city at night. Extreme-range tenor, high screams against low raspy growls, sudden register leaps, urgent diction, menace and tenderness in one voice.`
- 中文对照：罗斯风格：唱一首关于雨夜出租车的歌。极限音域男高音，高音嘶喊对照低沉吼声，音区骤然跳跃，咬字急切，威胁与温柔集于一身。
- Negative: `No smooth crooning, no operatic vibrato, no mumbled delivery, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
