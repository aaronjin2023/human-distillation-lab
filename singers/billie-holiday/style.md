# Billie Holiday — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Billie Holiday: behind-the-beat phrasing, intimate breathy timbre, limited range used with expressive bending, sparse vibrato, conversational delivery, emotional restraint rather than power`
- ZH: 霍利戴风格：拖在拍子后面的乐句，亲密的气声，音域有限而以弯曲取胜，颤音稀疏，口语化表达，克制而非力量。

## (2) 音色与音域

- 气声亲密，音色带沙哑，中低音区叙事感强；主音色为亲密的气声，辅音色为弯曲的音高，禁音色为力量型高音与甜美的圆润。`artifact`

## (3) 唱腔与发声技法

- 发声：气息起音，收尾多渐弱或戛然而止；唱腔：音高弯曲（bending），颤音稀疏，装饰音克制。`artifact`

## (4) 咬字与语言

- 美式英语咬字口语化，辅音轻，元音带弯曲；换气点留在句尾，制造悬念。`artifact`

## (5) 节奏与即兴

- 永远拖在拍子后面，乐句随呼吸而非小节；速度放慢，停顿制造张力。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：布鲁斯与叙事歌（《Strange Fruit》《God Bless the Child》）、爵士标准曲慢板演绎、专辑《Lady Sings the Blues》曲目、拖拍叙事句式、克制的情感收束。
- 不该唱：`No powerful belting, no straight on-beat phrasing, no sweet rounded tone, no operatic vibrato, no loud climax`
- Negative prompt: `No powerful belting, no straight on-beat phrasing, no sweet rounded tone, no operatic vibrato, no loud climax`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Billie Holiday, a song about a woman buying coffee at a convenience store late at night. Behind-the-beat phrasing, intimate breathy timbre, sparse vibrato, conversational delivery, small jazz combo, emotional restraint.`
- 中文对照：霍利戴风格：唱一首关于深夜在便利店买咖啡的女人的歌。拖在拍子后面的乐句，亲密的气声，颤音稀疏，口语化表达，小型爵士乐队伴奏，克制而非爆发。
- Negative: `No powerful belting, no straight on-beat phrasing, no sweet rounded tone, no operatic vibrato, no loud climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
