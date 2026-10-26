# Elton John — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of Elton John: warm melodic tenor, piano-driven phrasing, effortless falsetto lifts, sincere ballad intimacy, gospel-tinged choruses, melody first and always`
- ZH: 埃尔顿·约翰风格：温暖的旋律男高音，钢琴驱动的乐句，毫不费力的假声上扬，真诚的抒情亲密感，福音色彩的副歌，旋律永远第一。

## (2) 音色与音域

- 音色：温暖明亮的男高音，中高音区圆润；主音色为歌唱性胸声，辅音色为假声点缀；禁音色为沙哑撕裂与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑稳，起音柔和，收尾拖长渐弱；真假声切换平滑；《Your Song》以平稳连音为标记，《Rocket Man》以假声上扬为标记。`artifact`

## (4) 咬字与语言

- 咬字：英式发音清晰，元音饱满；重音落在旋律重音上；换气点藏在钢琴乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：钢琴驱动的节拍，抒情歌用 rubato，摇滚曲目抢拍推进；即兴以钢琴间奏与尾段加花为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 钢琴驱动的抒情歌与旋律优美的流行歌曲（如《Your Song》一类）
- 温柔主歌接开放副歌的旋律弧线
- 假声上扬与福音色彩副歌
- 叙事与告别主题的演唱
- 不该唱：`No raspy shouting, no mumbled diction, no operatic vibrato, no flat monotone delivery, no harsh distortion`
- Negative prompt: `No raspy shouting, no mumbled diction, no operatic vibrato, no flat monotone delivery, no harsh distortion`

## (7) 测试提示词示例（现代题材：深夜外卖骑手）

- Prompt: `Sing in the style of Elton John, a song about a food delivery rider working late at night in a modern city. Warm melodic tenor, piano-driven phrasing, effortless falsetto lifts, sincere ballad intimacy, gospel-tinged choruses.`
- 中文对照：埃尔顿·约翰风格：唱一首关于深夜外卖骑手的歌。温暖的旋律男高音，钢琴驱动的乐句，毫不费力的假声上扬，真诚的抒情亲密感，福音色彩的副歌。
- Negative: `No raspy shouting, no mumbled diction, no operatic vibrato, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
