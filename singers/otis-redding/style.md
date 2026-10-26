# Otis Redding — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul vocal in the style of Otis Redding: Raw pleading baritone, gospel grit, conversational verses building into desperate choruses, every line sung as if it were the last chance, warmth inside urgency`
- ZH: 雷丁风格： 粗粝恳求的男中音，福音的粗粝感，口语化主歌 渐强至绝望的副歌，每句都如最后一次机会，急切中有温暖。

## (2) 音色与音域

- 音色： 粗粝沙哑的男中音，中低音区最有恳求感；主音色为恳求式胸声，辅音色为气声；禁音色为圆润美声与冷漠平铺。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音直接，收尾拖长或戛然而止；颤音自然；《Dock of the Bay》以口哨收尾与缓慢叙事为标记，《Try a Little Tenderness》以层层推进为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式南方口音，辅音重；重音落在恳求词上；换气点短促。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂节拍上拖拍，乐句如波浪起伏；即兴以尾段加花与呼喊为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 灵魂抒情歌与恳求式副歌（如《Try a Little Tenderness》一类）
- 缓慢叙事歌（如《Dock of the Bay》）
- 口语化主歌接绝望副歌的对照
- 福音粗粝感的演唱
- 不该唱：`No operatic vibrato, no sweet crooning, no mumbled diction, no thin head voice, no detached cool delivery`
- Negative prompt: `No operatic vibrato, no sweet crooning, no mumbled diction, no thin head voice, no detached cool delivery`

## (7) 测试提示词示例（现代题材：阳台上的绿植）

- Prompt: `Sing in the style of Otis Redding, a song about plants growing on a balcony in a modern city. Raw pleading baritone, gospel grit, conversational verses building into desperate choruses, every line sung as if it were the last chance, warmth inside urgency.`
- 中文对照：雷丁风格：唱一首关于阳台绿植的歌。粗粝恳求的男中音，福音的粗粝感，口语化主歌 渐强至绝望的副歌，每句都如最后一次机会，急切中有温暖。
- Negative: `No operatic vibrato, no sweet crooning, no mumbled diction, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
