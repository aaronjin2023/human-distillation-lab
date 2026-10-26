# Renata Tebaldi — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric-spinto soprano in the style of Renata Tebaldi: warm golden soprano, velvet legato, radiant pianissimo, Verdian and Puccinian heroines, voice of an angel`
- ZH: 泰巴尔迪风格：金黄温暖的女高音，天鹅绒般的连音，辉煌的弱音，威尔第与普契尼女主角，天使之声。

## (2) 音色与音域

- 女高音音色金黄温暖，legato 如天鹅绒；主音色为金黄的抒情—戏剧女高音，辅音色为弱音的辉煌，禁音色为钢铁般的边缘音色与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息深厚，起音圆润，收尾多渐弱；唱腔：连音绵长，弱音辉煌，高音圆润。`artifact`

## (4) 咬字与语言

- 意大利语咬字圆润清晰，元音饱满；换气点留在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 乐句宽广，速度从容；慢板更沉，高潮处不抢拍。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：普契尼女主角（托斯卡、蝴蝶夫人、咪咪）、威尔第抒情女主角（阿依达、薇奥莱塔、莱奥诺拉）、意大利歌剧咏叹调、音乐会曲目、弱音辉煌的抒情段落。
- 不该唱：`No steely edge, no coloratura chatter, no breathy whisper, no jazz swing, no harsh chest voice`
- Negative prompt: `No steely edge, no coloratura chatter, no breathy whisper, no jazz swing, no harsh chest voice`

## (7) 测试提示词示例（现代题材：手机没电）

- Prompt: `Sing in the style of Renata Tebaldi, a song about a phone running out of battery on a long journey home. Warm golden soprano, velvet legato, radiant pianissimo, long generous line, warm orchestral accompaniment.`
- 中文对照：泰巴尔迪风格：唱一首关于长途回家路上手机没电的歌。金黄温暖的女高音，天鹅绒般的连音，辉煌的弱音，连音宽宏，管弦乐伴奏。
- Negative: `No steely edge, no coloratura chatter, no breathy whisper, no jazz swing, no harsh chest voice`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
