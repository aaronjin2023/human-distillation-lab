# Sam Cooke — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul vocal in the style of Sam Cooke: smooth silken tenor, gospel phrasing, effortless melisma, conversational warmth, dignity inside tenderness, every line perfectly placed`
- ZH: 库克风格：圆滑丝绸般的男高音，福音乐句，毫不费力的转音，口语化温暖，温柔中有尊严，每句都恰到好处。

## (2) 音色与音域

- 音色：圆滑温暖的男高音，中音区最有亲密感；主音色为丝绸般胸声，辅音色为假声点缀；禁音色为沙哑嘶吼与强力呐喊。`artifact`

## (3) 唱腔与发声技法

- 发声：气息平稳，起音柔和滑入，收尾拖长渐弱；颤音自然；《A Change Is Gonna Come》以管弦乐铺底上的克制叙事与高潮推进为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音轻、元音圆；重音落在词义上；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂节拍上略拖后，乐句如波浪起伏；即兴以转音与加花为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 福音灵魂抒情歌（如《A Change Is Gonna Come》一类）
- 圆滑温柔的流行灵魂歌曲（如《You Send Me》）
- 口语化叙事与转音点缀
- 尊严与希望主题的演唱
- 不该唱：`No raspy shouting, no operatic vibrato, no mumbled diction, no harsh distortion, no flat monotone delivery`
- Negative prompt: `No raspy shouting, no operatic vibrato, no mumbled diction, no harsh distortion, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Sam Cooke, a song about a man buying coffee at a convenience store late at night. Smooth silken tenor, gospel phrasing, effortless melisma, conversational warmth, dignity inside tenderness, every line perfectly placed.`
- 中文对照：库克风格：唱一首关于深夜便利店买咖啡的歌。圆滑丝绸般的男高音，福音乐句，毫不费力的转音，口语化温暖，温柔中有尊严，每句都恰到好处。
- Negative: `No raspy shouting, no operatic vibrato, no mumbled diction, no harsh distortion`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
