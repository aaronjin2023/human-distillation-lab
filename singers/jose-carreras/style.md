# José Carreras — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric tenor in the style of José Carreras: warm Mediterranean tenor, tender legato, emotional directness, Puccinian lyricism, heartfelt phrasing`
- ZH: 卡雷拉斯风格：地中海式温暖的男高音，柔和的连音，情感的直接，普契尼式抒情，发自内心的乐句。

## (2) 音色与音域

- 抒情男高音，音色地中海式温暖；主音色为温暖的抒情男高音，辅音色为弱音的细腻，禁音色为钢铁般的英雄音色与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息深厚，起音柔和，收尾多渐弱；唱腔：legato 柔和，高音带情感，弱音细腻。`artifact`

## (4) 咬字与语言

- 西班牙语与意大利语咬字清晰，元音圆润；换气点留在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 乐句抒情，速度从容；慢板更沉，高潮处不抢拍。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：普契尼男主角（鲁道夫、卡瓦拉多西、平克顿）、威尔第抒情男高音（阿尔弗雷德、公爵）、法国歌剧、音乐会与三大男高音曲目、抒情咏叹调的弱音段落。
- 不该唱：`No steely heroic blast, no breathy whisper, no jazz swing, no coloratura chatter, no rough rock edge`
- Negative prompt: `No steely heroic blast, no breathy whisper, no jazz swing, no coloratura chatter, no rough rock edge`

## (7) 测试提示词示例（现代题材：窗台上的咖啡）

- Prompt: `Sing in the style of José Carreras, a song about a cup of coffee cooling on a windowsill in the morning. Warm Mediterranean tenor, tender legato, emotional directness, Puccinian lyricism, light orchestral accompaniment.`
- 中文对照：卡雷拉斯风格：唱一首关于清晨一杯咖啡放在窗台上变凉的歌。地中海式温暖的男高音，柔和的连音，情感的直接，普契尼式抒情，轻型管弦乐伴奏。
- Negative: `No steely heroic blast, no breathy whisper, no jazz swing, no coloratura chatter, no rough rock edge`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
