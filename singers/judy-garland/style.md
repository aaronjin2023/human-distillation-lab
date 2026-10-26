# Judy Garland — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Broadway and pop vocal in the style of Judy Garland: warm vulnerable contralto, actor's diction, conversational verses building into soaring emotional climaxes, every lyric delivered as if it were a scene, hope inside heartbreak`
- ZH: 加兰风格：温暖脆弱的女低音，演员式咬字，口语化主歌 渐强至高亢情感高潮，每句歌词都如一场戏，心碎中有希望。

## (2) 音色与音域

- 音色：温暖的女低音，中低音区最有叙事感；主音色为抒情胸声，辅音色为口语化气声；禁音色为甜美圆润与歌剧式花腔。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音如台词般直接，收尾拖长渐弱；颤音自然而宽；《Over the Rainbow》以梦想式乐句与高音推进为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音重；重音落在词义上，如演台词；换气点藏在句意停顿处。`artifact`

## (5) 节奏与即兴

- 节奏：百老汇式自由节奏（rubato），乐句随词义伸缩；即兴少，以乐句处理制造变化，现场版常拉长尾句。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 百老汇抒情歌与电影歌曲（如《Over the Rainbow》一类）
- 演员式口语主歌接高亢副歌的对照
- 梦想与希望主题的叙事演唱
- 现场拉长的尾句与情感高潮
- 不该唱：`No operatic coloratura, no sweet rounded pop tone, no mumbled diction, no detached cool delivery, no flat monotone delivery`
- Negative prompt: `No operatic coloratura, no sweet rounded pop tone, no mumbled diction, no detached cool delivery, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：凌晨的机场）

- Prompt: `Sing in the style of Judy Garland, a song about waiting at an airport in the early morning. Warm vulnerable contralto, actor's diction, conversational verses building into soaring emotional climaxes, every lyric delivered as if it were a scene, hope inside heartbreak.`
- 中文对照：加兰风格：唱一首关于凌晨机场等候的歌。温暖脆弱的女低音，演员式咬字，口语化主歌 渐强至高亢情感高潮，每句歌词都如一场戏，心碎中有希望。
- Negative: `No operatic coloratura, no sweet rounded pop tone, no mumbled diction, no detached cool delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
