# Jussi Björling — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric tenor in the style of Jussi Björling: silvery Swedish tenor, effortless high notes, warm Italianate phrasing, flawless legato, unforced beauty`
- ZH: 比约林风格：银亮的瑞典男高音，高音毫不费力，意大利式暖意乐句，连音无缝，毫不费力的美。

## (2) 音色与音域

- 抒情男高音，音色银亮温暖，高音毫不费力；主音色为银亮的抒情男高音，辅音色为弱音的柔和，禁音色为英雄式的轰鸣与暗沉的覆盖音色。`artifact`

## (3) 唱腔与发声技法

- 发声：气息流畅，起音轻盈，收尾多渐弱；唱腔：legato 无缝，高音自然开放，颤音均匀。`artifact`

## (4) 咬字与语言

- 意大利语咬字优美，瑞典口音极轻；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 乐句流畅，速度自然；rubato 节制，为旋律服务。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：普契尼男主角（鲁道夫、《今夜无人入睡》）、威尔第抒情男高音（公爵、阿尔弗雷德）、法国与俄罗斯歌剧抒情段落、艺术歌曲与瑞典民歌、音乐会咏叹调。
- 不该唱：`No heroic blast, no breathy whisper, no jazz phrasing, no rough edge, no dark covered tone`
- Negative prompt: `No heroic blast, no breathy whisper, no jazz phrasing, no rough edge, no dark covered tone`

## (7) 测试提示词示例（现代题材：深夜便利店的关东煮）

- Prompt: `Sing in the style of Jussi Björling, a song about oden simmering at a convenience store late at night. Silvery tenor, effortless high notes, warm Italianate phrasing, flawless legato, light orchestral accompaniment.`
- 中文对照：比约林风格：唱一首关于深夜便利店里关东煮咕嘟作响的歌。银亮的男高音，高音毫不费力，意大利式暖意乐句，连音无缝，轻型管弦乐伴奏。
- Negative: `No heroic blast, no breathy whisper, no jazz phrasing, no rough edge, no dark covered tone`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
