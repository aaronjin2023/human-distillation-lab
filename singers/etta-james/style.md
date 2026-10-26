# Etta James — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Soul and blues vocal in the style of Etta James: Raw powerful contralto, gospel grit, conversational verses building into desperate choruses, every line sung as if it cost something, tenderness inside fire`
- ZH: 詹姆斯风格： 粗粝强力的女低音，福音的粗粝感，口语化主歌 渐强至绝望的副歌，每句都如付出了代价，火焰中有温柔。

## (2) 音色与音域

- 音色： 粗粝强力的女低音，中低音区最有辨识度；主音色为强力胸声，辅音色为气声低语；禁音色为甜美圆润与歌剧式花腔。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深，起音直接，收尾拖长或戛然而止；颤音自然而宽；《At Last》以缓慢抒情与强音推进为标记，《I'd Rather Go Blind》以绝望的副歌为标记。`artifact`

## (4) 咬字与语言

- 咬字：美式发音清晰，辅音重；重音落在情感词上；换气点短促。`artifact`

## (5) 节奏与即兴

- 节奏：灵魂与布鲁斯节拍上拖拍，乐句如波浪起伏；即兴以尾段加花与呼喊为主。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 灵魂布鲁斯抒情歌（如《At Last》一类）
- 绝望副歌与强力推进（如《I'd Rather Go Blind》）
- 口语化主歌接爆发副歌的对照
- 福音粗粝感的演唱
- 不该唱：`No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice, no detached cool delivery`
- Negative prompt: `No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice, no detached cool delivery`

## (7) 测试提示词示例（现代题材：雨夜的出租车）

- Prompt: `Sing in the style of Etta James, a song about a taxi ride through a rainy modern city at night. Raw powerful contralto, gospel grit, conversational verses building into desperate choruses, every line sung as if it cost something, tenderness inside fire.`
- 中文对照：詹姆斯风格：唱一首关于雨夜出租车的歌。粗粝强力的女低音，福音的粗粝感，口语化主歌 渐强至绝望的副歌，每句都如付出了代价，火焰中有温柔。
- Negative: `No sweet rounded pop tone, no operatic coloratura, no mumbled diction, no thin head voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
