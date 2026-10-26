# Sarah Vaughan — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Sarah Vaughan: rich contralto-to-soprano range, velvet vibrato, bebop agility, effortless leaps, warm improvisation`
- ZH: 沃恩风格：从女低音到女高音的宽广音域，天鹅绒般的颤音，比波普式的敏捷，毫不费力的跳跃，温暖的即兴。

## (2) 音色与音域

- 音域宽广，音色天鹅绒般温暖；主音色为温暖的爵士女声，辅音色为拟声的乐器感，禁音色为单薄的头声与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息深厚，起音干净，收尾多渐弱；唱腔：音程跳跃毫不费力，装饰音丰富，颤音天鹅绒般。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰温暖，元音圆润；拟声段落音节清晰。`artifact`

## (5) 节奏与即兴

- 比波普式的敏捷，乐句如萨克斯独奏；摇摆感强。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：比波普标准曲（《Lullaby of Birdland》《Misty》《Tenderly》）、拟声与装饰音即兴、大乐队摇摆曲、抒情慢板、音程跳跃的华彩段落。
- 不该唱：`No thin head voice, no straight stiff phrasing, no breathy whisper, no operatic blast, no shouted climax`
- Negative prompt: `No thin head voice, no straight stiff phrasing, no breathy whisper, no operatic blast, no shouted climax`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `Sing in the style of Sarah Vaughan, a song about a cup of coffee cooling on a windowsill in the morning. Rich wide range, velvet vibrato, bebop agility, effortless leaps, warm improvisation, small jazz combo.`
- 中文对照：沃恩风格：唱一首关于清晨一杯咖啡放在窗台上变凉的歌。宽广的音域，天鹅绒般的颤音，比波普式的敏捷，毫不费力的跳跃，温暖的即兴，小型爵士乐队伴奏。
- Negative: `No thin head voice, no straight stiff phrasing, no breathy whisper, no operatic blast, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
