# Mel Tormé — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Jazz vocal in the style of Mel Tormé: velvet tenor, flawless intonation, scat virtuosity, effortless swing, the Velvet Fog`
- ZH: 托梅风格：天鹅绒般的男高音，音准无瑕，拟声的炫技，摇摆毫不费力，天鹅绒迷雾。

## (2) 音色与音域

- 男高音天鹅绒般温暖，音色纯净；主音色为天鹅绒般的男高音，辅音色为拟声的乐器感，禁音色为粗粝的低吼与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息深厚，起音干净，收尾多渐弱；唱腔：拟声唱法（scat）炫技，装饰音丰富，颤音均匀。`artifact`

## (4) 咬字与语言

- 美式英语咬字清晰温暖，元音圆润；拟声段落音节清晰如乐器。`artifact`

## (5) 节奏与即兴

- 摇摆毫不费力，乐句流畅；拟声段落节奏如比波普独奏。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：爵士标准曲（《Blue Moon》《Comin' Home Baby》）、圣诞歌曲（《The Christmas Song》）、拟声即兴段落、大乐队摇摆曲、抒情慢板。
- 不该唱：`No rough growl, no breathy whisper, no operatic blast, no straight stiff phrasing, no shouted climax`
- Negative prompt: `No rough growl, no breathy whisper, no operatic blast, no straight stiff phrasing, no shouted climax`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `Sing in the style of Mel Tormé, a song about riding a shared bicycle through a city in the morning. Velvet tenor, flawless intonation, scat virtuosity, effortless swing, warm diction, big band.`
- 中文对照：托梅风格：唱一首关于清晨骑共享单车穿过城市的歌。天鹅绒般的男高音，音准无瑕，拟声的炫技，摇摆毫不费力，咬字温暖，大乐队伴奏。
- Negative: `No rough growl, no breathy whisper, no operatic blast, no straight stiff phrasing, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
