# Tony Bennett — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz-pop vocal in the style of Tony Bennett: warm baritone, bel canto breath control, clear diction, swing ease, painterly phrasing, lifelong elegance`
- ZH: 贝内特风格：温暖的男中音，美声式的气息控制，咬字清晰，摇摆从容，画家般的乐句，终身的优雅。

## (2) 音色与音域

- 男中音温暖，音色带美声的支撑；主音色为温暖的男中音，辅音色为弱音的亲密，禁音色为摇滚式的喊叫与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息控制如美声，起音干净，收尾多渐弱；唱腔：乐句如绘画，装饰音克制，颤音适中。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰，口语化；重音落在词义上；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 摇摆从容，乐句随呼吸而非小节；与爵士乐手咬合紧密。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：流行标准曲（《I Left My Heart in San Francisco》《The Way You Look Tonight》）、与爵士乐手的二重唱（《Body and Soul》与艾米·怀恩豪斯）、大乐队摇摆曲、抒情慢板、晚期二重唱专辑曲目。
- 不该唱：`No rock shouting, no breathy whisper, no operatic blast, no rushed phrasing, no sloppy diction`
- Negative prompt: `No rock shouting, no breathy whisper, no operatic blast, no rushed phrasing, no sloppy diction`

## (7) 测试提示词示例（现代题材：地铁末班车）

- Prompt: `Sing in the style of Tony Bennett, a song about the last subway train of the night. Warm baritone, bel canto breath control, clear diction, swing ease, painterly phrasing, small jazz combo.`
- 中文对照：贝内特风格：唱一首关于深夜末班地铁的歌。温暖的男中音，美声式的气息控制，咬字清晰，摇摆从容，画家般的乐句，小型爵士乐队伴奏。
- Negative: `No rock shouting, no breathy whisper, no operatic blast, no rushed phrasing, no sloppy diction`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
