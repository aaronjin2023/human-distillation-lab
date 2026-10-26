# Nat King Cole — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz-pop vocal in the style of Nat King Cole: velvet baritone, intimate warmth, piano-like phrasing, effortless swing, gentle diction`
- ZH: 纳·金·科尔风格：天鹅绒般的男中音，亲密的暖意，钢琴般的乐句，毫不费力的摇摆，温柔的咬字。

## (2) 音色与音域

- 男中音天鹅绒般温暖，音色亲密；主音色为温暖的男中音，辅音色为钢琴般的乐句感，禁音色为粗粝的低吼与歌剧式的颤音。`artifact`

## (3) 唱腔与发声技法

- 发声：气息深厚，起音柔和，收尾多渐弱；唱腔：乐句如钢琴，装饰音克制，颤音适中。`artifact`

## (4) 咬字与语言

- 美式英语咬字温柔清晰，元音圆润；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 摇摆感毫不费力，乐句流畅；与三重奏咬合紧密。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：流行标准曲（《Unforgettable》《Mona Lisa》）、圣诞歌曲（《The Christmas Song》）、三重奏时期的摇摆曲、抒情情歌、钢琴自弹自唱曲目。
- 不该唱：`No rough growl, no operatic vibrato, no breathy whisper, no rushed phrasing, no shouted climax`
- Negative prompt: `No rough growl, no operatic vibrato, no breathy whisper, no rushed phrasing, no shouted climax`

## (7) 测试提示词示例（现代题材：凌晨机场）

- Prompt: `Sing in the style of Nat King Cole, a song about a traveller waiting alone at an airport before dawn. Velvet baritone, intimate warmth, piano-like phrasing, effortless swing, gentle diction, small jazz combo.`
- 中文对照：纳·金·科尔风格：唱一首关于黎明前独自在机场等候的旅人的歌。天鹅绒般的男中音，亲密的暖意，钢琴般的乐句，毫不费力的摇摆，温柔的咬字，小型爵士乐队伴奏。
- Negative: `No rough growl, no operatic vibrato, no breathy whisper, no rushed phrasing, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
