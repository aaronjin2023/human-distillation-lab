# James Brown — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul and funk vocal in the style of James Brown: explosive raspy baritone, rhythmic grunts and screams, call-and-response with the band, every syllable on the beat, the hardest working voice in show business`
- ZH: 布朗风格：爆发的沙哑男中音，节奏型低吼与尖叫，与乐队呼应，每个音节都落在节拍上，演艺界最拼命的声音。

## (2) 音色与音域

- 音色：沙哑有力的男中音，中音区带颗粒感；主音色为爆发式胸声，辅音色为尖叫式假声；禁音色为圆润美声与温吞抒情。`artifact`

## (3) 唱腔与发声技法

- 发声：气息爆发式，起音硬而直接，收尾短促或拖成尖叫；颤音几乎不用；《I Got You》以号角式副歌与节奏型低吼为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音，辅音极重；重音落在节拍点上；换气短促，气口即节奏。`artifact`

## (5) 节奏与即兴

- 节奏：放克节拍上每个音节都卡点，乐句如打击乐；即兴以低吼、尖叫与呼应为主，现场版常拉长尾段。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 放克舞曲与节奏型灵魂歌曲（如《I Got You》一类）
- 节奏型低吼与尖叫点缀的乐句
- 呼应式副歌与乐队对话
- 缓慢抒情歌的爆发式演唱（如《It's a Man's Man's Man's World》）
- 不该唱：`No smooth crooning, no operatic vibrato, no mumbled diction, no thin head voice, no loose off-beat phrasing`
- Negative prompt: `No smooth crooning, no operatic vibrato, no mumbled diction, no thin head voice, no loose off-beat phrasing`

## (7) 测试提示词示例（现代题材：凌晨的机场）

- Prompt: `Sing in the style of James Brown, a song about waiting at an airport in the early morning. Explosive raspy baritone, rhythmic grunts and screams, call-and-response with the band, every syllable on the beat, relentless energy.`
- 中文对照：布朗风格：唱一首关于凌晨机场等候的歌。爆发的沙哑男中音，节奏型低吼与尖叫，与乐队呼应，每个音节都落在节拍上，永不停歇的能量。
- Negative: `No smooth crooning, no operatic vibrato, no mumbled diction, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
