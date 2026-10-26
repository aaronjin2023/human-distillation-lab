# Frank Sinatra — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz-pop vocal in the style of Frank Sinatra: smooth baritone, conversational phrasing, perfect breath control, behind-the-beat ease, Rat Pack cool, storyteller's timing`
- ZH: 辛纳屈风格：顺滑的男中音，口语化乐句，完美的气息控制，拖拍的从容，潇洒冷静，讲故事般的时机。

## (2) 音色与音域

- 男中音顺滑，音色温暖，音域集中于中声区；主音色为顺滑的男中音，辅音色为弱音的亲密，禁音色为摇滚式的喊叫与歌剧式的颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息控制完美，起音干净，收尾多渐弱；唱腔：乐句如说话，装饰音克制，颤音适中。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰，口语化；重音落在词义上；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 拖拍的从容，乐句随呼吸而非小节；与大乐队咬合稳健。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：流行标准曲（《My Way》《New York, New York》《Fly Me to the Moon》）、萨洛恩歌曲与百老汇曲目、与大乐队合作的摇摆曲、深夜抒情慢板、讲故事般的叙事句式。
- 不该唱：`No rock shouting, no operatic vibrato, no breathy whisper, no rushed phrasing, no sloppy diction`
- Negative prompt: `No rock shouting, no operatic vibrato, no breathy whisper, no rushed phrasing, no sloppy diction`

## (7) 测试提示词示例（现代题材：深夜拉面店）

- Prompt: `Sing in the style of Frank Sinatra, a song about a man eating ramen alone at a late-night noodle shop. Smooth baritone, conversational phrasing, perfect breath control, behind-the-beat ease, big band swing.`
- 中文对照：辛纳屈风格：唱一首关于深夜独自在拉面店吃面的男人的歌。顺滑的男中音，口语化乐句，完美的气息控制，拖拍的从容，大乐队摇摆伴奏。
- Negative: `No rock shouting, no operatic vibrato, no breathy whisper, no rushed phrasing, no sloppy diction`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
