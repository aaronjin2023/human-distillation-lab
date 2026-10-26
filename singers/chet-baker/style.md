# Chet Baker — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Cool jazz vocal in the style of Chet Baker: fragile intimate tenor, whispered trumpet-like phrasing, behind-the-beat cool, vulnerable honesty, minimal vibrato`
- ZH: 贝克风格：脆弱亲密的男高音，耳语般的小号式乐句，拖拍的冷静，易碎的诚实，颤音极少。

## (2) 音色与音域

- 男高音脆弱亲密，音色带耳语感；主音色为脆弱的冷爵士男高音，辅音色为小号般的乐句感，禁音色为力量型高音与甜美的圆润。`artifact`

## (3) 唱腔与发声技法

- 发声：气声起音，收尾多渐弱；唱腔：乐句如小号，颤音极少，装饰音克制。`artifact`

## (4) 咬字与语言

- 美式英语咬字轻柔，口语化；换气点留在句尾，制造悬念。`artifact`

## (5) 节奏与即兴

- 拖拍的冷静，乐句随呼吸而非小节；速度放慢。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：冷爵士标准曲（《My Funny Valentine》《Time After Time》）、自弹自唱式抒情曲、与小号呼应的演唱段落、深夜慢板、耳语般的亲密段落。
- 不该唱：`No powerful belting, no operatic vibrato, no straight on-beat phrasing, no rough growl, no loud climax`
- Negative prompt: `No powerful belting, no operatic vibrato, no straight on-beat phrasing, no rough growl, no loud climax`

## (7) 测试提示词示例（现代题材：深夜出租车）

- Prompt: `Sing in the style of Chet Baker, a song about a taxi ride through a sleeping city late at night. Fragile intimate tenor, whispered trumpet-like phrasing, behind-the-beat cool, vulnerable honesty, minimal vibrato, small jazz combo.`
- 中文对照：贝克风格：唱一首关于深夜出租车穿过沉睡城市的歌。脆弱亲密的男高音，耳语般的小号式乐句，拖拍的冷静，易碎的诚实，颤音极少，小型爵士乐队伴奏。
- Negative: `No powerful belting, no operatic vibrato, no straight on-beat phrasing, no rough growl, no loud climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
