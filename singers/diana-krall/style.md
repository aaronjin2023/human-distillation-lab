# Diana Krall — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Diana Krall: cool contralto, piano-bar intimacy, restrained swing, breathy warmth, unhurried phrasing`
- ZH: 克劳尔风格：冷静的女低音，钢琴酒吧式的亲密，克制的摇摆，气声的暖意，从容的乐句。

## (2) 音色与音域

- 女低音冷静，音色带气声的暖意；主音色为冷静的女低音，辅音色为钢琴般的乐句感，禁音色为力量型高音与歌剧式的颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气声起音，收尾多渐弱；唱腔：乐句如钢琴，装饰音克制，颤音稀疏。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰，口语化；换气点留在句尾，制造悬念。`artifact`

## (5) 节奏与即兴

- 摇摆克制，乐句从容；与钢琴咬合紧密。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：爵士标准曲（《The Look of Love》《Cry Me a River》《Let's Fall in Love》）、钢琴自弹自唱曲目、波萨诺瓦式轻摇摆、深夜抒情慢板、钢琴酒吧式的亲密段落。
- 不该唱：`No powerful belting, no operatic vibrato, no rushed phrasing, no rough growl, no shouted climax`
- Negative prompt: `No powerful belting, no operatic vibrato, no rushed phrasing, no rough growl, no shouted climax`

## (7) 测试提示词示例（现代题材：深夜便利店）

- Prompt: `Sing in the style of Diana Krall, a song about a woman buying coffee at a convenience store late at night. Cool contralto, piano-bar intimacy, restrained swing, breathy warmth, unhurried phrasing, piano and small jazz combo.`
- 中文对照：克劳尔风格：唱一首关于深夜在便利店买咖啡的女人的歌。冷静的女低音，钢琴酒吧式的亲密，克制的摇摆，气声的暖意，从容的乐句，钢琴与小型爵士乐队伴奏。
- Negative: `No powerful belting, no operatic vibrato, no rushed phrasing, no rough growl, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
