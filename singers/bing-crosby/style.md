# Bing Crosby — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Popular standard vocal in the style of Bing Crosby: warm intimate baritone, crooning close to the microphone, effortless swing phrasing, conversational diction, relaxed ease in every line`
- ZH: 克罗斯比风格：温暖亲密的男中音，贴近话筒的 crooning，毫不费力的摇摆乐句，口语化咬字，每句都轻松自如。

## (2) 音色与音域

- 音色：温暖的男中音，中低音区圆润；主音色为贴近话筒的 crooning，辅音色为轻快的摇摆胸声；禁音色为强力呐喊与歌剧式颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息平稳，起音柔和滑入，收尾拖长渐弱；颤音自然而窄；《White Christmas》以贴近话筒的亲密感为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，辅音轻、元音圆；重音落在词义上；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 节奏：摇摆节拍上略拖后，乐句如说话般自然；即兴以轻微的变奏与拟声为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 流行标准曲与圣诞、抒情主题的歌曲（如《White Christmas》一类）
- 贴近话筒的 crooning 式亲密演唱
- 摇摆乐句与口语化叙事
- 轻松自如的副歌推进
- 不该唱：`No powerful belting, no operatic vibrato, no raspy shouting, no mumbled diction, no harsh distortion`
- Negative prompt: `No powerful belting, no operatic vibrato, no raspy shouting, no mumbled diction, no harsh distortion`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Bing Crosby, a song about a man buying coffee at a convenience store late at night. Warm intimate baritone, crooning close to the microphone, effortless swing phrasing, conversational diction, relaxed ease in every line.`
- 中文对照：克罗斯比风格：唱一首关于深夜便利店买咖啡的歌。温暖亲密的男中音，贴近话筒的 crooning，毫不费力的摇摆乐句，口语化咬字，每句都轻松自如。
- Negative: `No powerful belting, no operatic vibrato, no raspy shouting, no mumbled diction`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
