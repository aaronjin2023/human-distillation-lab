# Luciano Pavarotti — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric tenor in the style of Luciano Pavarotti: bright open tenor, ringing high C, generous legato, sunny warmth, effortless high notes, Italianate phrasing`
- ZH: 帕瓦罗蒂风格：明亮开放的男高音，高音 C 辉煌，连音宽宏，音色阳光温暖，高音毫不费力，意大利式乐句。

## (2) 音色与音域

- 明亮开放的男高音，高音 C 辉煌，音色阳光饱满；主音色为明亮的抒情男高音，辅音色为弱音的柔和，禁音色为气声耳语与暗沉的覆盖音色。`artifact`

## (3) 唱腔与发声技法

- 发声：气息支撑深厚，起音明亮，收尾多辉煌渐强；唱腔：legato 流畅，高音渐强（crescendo）后收束，颤音均匀。`artifact`

## (4) 咬字与语言

- 意大利语元音圆润，咬字清晰而歌唱化；那不勒斯歌曲咬字带口语暖意；换气点留在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 速度稳定，乐句宽广，rubato 节制；高音前常有轻微的蓄势停顿。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：普契尼咏叹调（《今夜无人入睡》《星光灿烂》）、威尔第男高音咏叹调（《女人善变》）、那不勒斯歌曲（《我的太阳》）、歌剧重唱与音乐会返场曲、三大男高音音乐会曲目。
- 不该唱：`No breathy whisper, no jazz swing, no rough rock shouting, no mumbled diction, no thin head voice, no dark covered tone`
- Negative prompt: `No breathy whisper, no jazz swing, no rough rock shouting, no mumbled diction, no thin head voice, no dark covered tone`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of Luciano Pavarotti, a song about a small Yorkshire terrier sitting on a subway seat. Bright open tenor, ringing high notes, legato phrasing, full breath support, warm orchestral accompaniment, joyful and generous.`
- 中文对照：帕瓦罗蒂风格：唱一首关于一只约克夏犬坐在地铁座位上的歌。明亮开放的男高音，高音辉煌，连音宽宏，气息饱满，管弦乐伴奏，欢快而慷慨。
- Negative: `No breathy whisper, no jazz swing, no rough rock shouting, no mumbled diction, no thin head voice, no dark covered tone`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
