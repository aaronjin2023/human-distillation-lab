# Ray Charles — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul vocal in the style of Ray Charles: gospel-fired baritone, raspy warmth, call-and-response phrasing, piano-driven swing, secular and sacred in one voice, heartbreak with a smile`
- ZH: 查尔斯风格：福音点燃的男中音，沙哑的温暖，呼应式乐句，钢琴驱动的摇摆，世俗与神圣集于一身，心碎中带笑。

## (2) 音色与音域

- 音色：沙哑温暖的男中音，中低音区最有福音感；主音色为沙哑胸声，辅音色为呼喊式假声；禁音色为圆润美声与冷漠平铺。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音直接，收尾拖长或戛然而止；颤音自然而宽；《Georgia on My Mind》以缓慢抒情与沙哑音色为标记，《Hit the Road Jack》以呼应式乐句为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式南方口音，元音开、辅音重；重音落在情感词上；换气点短促。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂与摇摆节拍上拖拍，呼应式乐句与乐队对话；即兴以呼喊与变奏为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 福音灵魂歌与呼应式乐句（如《Hit the Road Jack》一类）
- 缓慢抒情歌的沙哑叙事（如《Georgia on My Mind》）
- 钢琴驱动的摇摆演唱
- 世俗与神圣并存的演唱
- 不该唱：`No operatic vibrato, no sweet crooning, no mumbled diction, no thin head voice, no detached cool delivery`
- Negative prompt: `No operatic vibrato, no sweet crooning, no mumbled diction, no thin head voice, no detached cool delivery`

## (7) 测试提示词示例（现代题材：深夜外卖骑手）

- Prompt: `Sing in the style of Ray Charles, a song about a food delivery rider working late at night in a modern city. Gospel-fired baritone, raspy warmth, call-and-response phrasing, piano-driven swing, secular and sacred in one voice, heartbreak with a smile.`
- 中文对照：查尔斯风格：唱一首关于深夜外卖骑手的歌。福音点燃的男中音，沙哑的温暖，呼应式乐句，钢琴驱动的摇摆，世俗与神圣集于一身，心碎中带笑。
- Negative: `No operatic vibrato, no sweet crooning, no mumbled diction, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
