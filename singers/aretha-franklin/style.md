# Aretha Franklin — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul vocal in the style of Aretha Franklin: gospel-fired mezzo-soprano, commanding belt, intricate melisma, piano-driven phrasing, righteous authority in every line, tenderness inside power`
- ZH: 富兰克林风格：福音点燃的女中音，命令式强音，复杂的转音，钢琴驱动的乐句，每句都有正义的权威，力量中有温柔。

## (2) 音色与音域

- 音色：强力温暖的女中音，中低音区最有福音感；主音色为命令式胸声，辅音色为气声与假声；禁音色为甜美圆润与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑极深，起音直接有力，收尾拖长或戛然而止；颤音自然而宽；《Respect》以拼字式副歌与强音推进为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音极清晰，辅音重；重音落在宣言词上；换气点短促有力。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂乐节拍上拖拍与抢拍并用，副歌常以切分推进；即兴以转音与加花为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 福音灵魂歌与宣言式副歌（如《Respect》一类）
- 命令式强音与温柔气声的对照
- 钢琴驱动的叙事与副歌推进
- 转音与加花的即兴点缀
- 不该唱：`No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice, no detached cool delivery`
- Negative prompt: `No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice, no detached cool delivery`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Aretha Franklin, a song about a woman buying coffee at a convenience store late at night. Gospel-fired mezzo-soprano, commanding belt, intricate melisma, piano-driven phrasing, righteous authority in every line, tenderness inside power.`
- 中文对照：富兰克林风格：唱一首关于深夜便利店买咖啡的女人的歌。福音点燃的女中音，命令式强音，复杂的转音，钢琴驱动的乐句，每句都有正义的权威，力量中有温柔。
- Negative: `No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
