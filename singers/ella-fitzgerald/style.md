# Ella Fitzgerald — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Ella Fitzgerald: pure clear voice, flawless intonation, scat like a horn, effortless swing, warm diction, endless invention`
- ZH: 菲茨杰拉德风格：纯净清澈的嗓音，音准无瑕，拟声如号角，摇摆毫不费力，咬字温暖，即兴无穷。

## (2) 音色与音域

- 纯净清澈，音色温暖，音域宽广；主音色为纯净的爵士女声，辅音色为拟声的乐器感，禁音色为沙哑的低吼与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深厚，起音干净，收尾多渐弱；唱腔：拟声唱法（scat）如乐器独奏，装饰音丰富，颤音均匀。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰温暖，元音圆润；拟声段落音节清晰如乐器。`artifact`

## (5) 节奏与即兴

- 摇摆感强，乐句流畅；拟声段落节奏如比波普独奏。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：爵士标准曲（《Summertime》《Cheek to Cheek》）、拟声即兴（scat）段落、歌集系列（Gershwin、Cole Porter、Rodgers & Hart Song Books）、与爵士乐队的呼应段落、大乐队摇摆曲。
- 不该唱：`No breathy whisper, no rough growl, no straight stiff phrasing, no operatic vibrato, no shouted climax`
- Negative prompt: `No breathy whisper, no rough growl, no straight stiff phrasing, no operatic vibrato, no shouted climax`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of Ella Fitzgerald, a song about a small Yorkshire terrier sitting on a subway seat. Pure clear voice, flawless intonation, scat like a horn, effortless swing, warm diction, small jazz combo.`
- 中文对照：菲茨杰拉德风格：唱一首关于一只约克夏犬坐在地铁座位上的歌。纯净清澈的嗓音，音准无瑕，拟声如号角，摇摆毫不费力，咬字温暖，小型爵士乐队伴奏。
- Negative: `No breathy whisper, no rough growl, no straight stiff phrasing, no operatic vibrato, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
