# Nina Simone — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz-soul vocal in the style of Nina Simone: deep contralto, classical piano roots, gospel fire, protest intensity, unpredictable phrasing, raw honesty`
- ZH: 妮娜·西蒙风格：深沉的女低音，古典钢琴的根基，福音的火焰，抗议的强度，不可预测的乐句，原始的诚实。

## (2) 音色与音域

- 女低音深沉，音色带古典与福音的双重质感；主音色为深沉的女低音，辅音色为钢琴般的乐句感，禁音色为甜美的流行音色与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：胸声为主，起音果断，收尾或渐弱或戛然而止；唱腔：古典钢琴式的前奏与间奏，福音式的高潮，装饰音克制。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰，口语化；重音落在词义与抗议上；换气点随乐句呼吸。`artifact`

## (5) 节奏与即兴

- 乐句不可预测，速度随情绪变化；与钢琴咬合紧密。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：灵魂与民谣抗议歌（《Mississippi Goddam》《Feeling Good》《I Put a Spell on You》）、古典钢琴式的前奏与间奏、福音式的高潮段落、现场即兴延展、口语化叙事句式。
- 不该唱：`No sweet pop polish, no straight on-beat phrasing, no light soubrette tone, no detached delivery, no operatic vibrato`
- Negative prompt: `No sweet pop polish, no straight on-beat phrasing, no light soubrette tone, no detached delivery, no operatic vibrato`

## (7) 测试提示词示例（现代题材：雨夜外卖员）

- Prompt: `Sing in the style of Nina Simone, a song about a delivery rider crossing a rainy city at night. Deep contralto, classical piano roots, gospel fire, unpredictable phrasing, raw honesty, piano and small band.`
- 中文对照：妮娜·西蒙风格：唱一首关于深夜雨中外卖员穿过城市的歌。深沉的女低音，古典钢琴的根基，福音的火焰，不可预测的乐句，原始的诚实，钢琴与小型乐队伴奏。
- Negative: `No sweet pop polish, no straight on-beat phrasing, no light soubrette tone, no detached delivery, no operatic vibrato`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
