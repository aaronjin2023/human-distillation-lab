# Bruce Springsteen — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Rock vocal in the style of Bruce Springsteen: gravelly working-class tenor, urgent storyteller phrasing, shouted choruses against whispered verses, harmonica-like breathing, marathon live stamina, hope inside exhaustion`
- ZH: 斯普林斯汀风格：沙哑的工人阶级男高音，急切的叙事乐句，耳语主歌对照呐喊副歌，口琴式呼吸，马拉松式的现场耐力，疲惫中的希望。

## (2) 音色与音域

- 音色：沙哑而温暖的男高音，中低音区最有叙事感；主音色为胸声呐喊，辅音色为耳语式气声；禁音色为圆润美声与冷漠的平铺。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音直接有力，收尾拖长或戛然而止；颤音少，靠音量与密度推进；《Born to Run》以连珠式乐句冲刺。`artifact`

## (4) 咬字与语言

- 咬字：美式新泽西口音，辅音重、元音开；重音落在叙事关键词上；换气短促，如跑步中的呼吸。`artifact`

## (5) 节奏与即兴

- 节奏：摇滚节拍上抢拍推进，副歌常提前半拍进入；即兴以现场拉长尾奏与即兴独白为主，录音室版相对克制。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 工人阶级叙事歌与公路、出走主题的歌曲（如《Born to Run》一类）
- 耳语主歌接呐喊副歌的情绪冲刺
- 连珠式乐句与副歌大合唱
- 现场拉长的尾奏与即兴叙事
- 不该唱：`No operatic vibrato, no sweet crooning, no detached cool delivery, no mumbled diction, no thin head voice`
- Negative prompt: `No operatic vibrato, no sweet crooning, no detached cool delivery, no mumbled diction, no thin head voice`

## (7) 测试提示词示例（现代题材：深夜外卖骑手）

- Prompt: `Sing in the style of Bruce Springsteen, a song about a food delivery rider working late at night in a modern city. Gravelly working-class tenor, urgent storyteller phrasing, whispered verses against shouted choruses, hope inside exhaustion.`
- 中文对照：斯普林斯汀风格：唱一首关于深夜外卖骑手的歌。沙哑的工人阶级男高音，急切的叙事乐句，耳语主歌对照呐喊副歌，疲惫中的希望。
- Negative: `No operatic vibrato, no sweet crooning, no detached cool delivery, no mumbled diction`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
