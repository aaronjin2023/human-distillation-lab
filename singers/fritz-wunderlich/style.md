# Fritz Wunderlich — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric tenor in the style of Fritz Wunderlich: radiant German tenor, crystal diction, effortless Mozartian grace, warm Lieder intimacy, tragically brief career`
- ZH: 文德里希风格：明亮的德国男高音，咬字如水晶，莫扎特式毫不费力的优雅，艺术歌曲的暖意，短暂而辉煌的生涯。

## (2) 音色与音域

- 抒情男高音，音色明亮温暖；主音色为明亮的抒情男高音，辅音色为艺术歌曲的亲密，禁音色为英雄式的轰鸣与暗沉的覆盖音色。`artifact`

## (3) 唱腔与发声技法

- 发声：气息轻盈，起音干净，收尾多渐弱；唱腔：高音轻松，颤音细腻，装饰音精确。`artifact`

## (4) 咬字与语言

- 德语咬字极其清晰，元音纯净；意大利语咬字同样清晰；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 乐句轻盈，速度灵动；莫扎特段落节奏精确，艺术歌曲段落随诗歌呼吸。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：莫扎特男主角（塔米诺、唐·奥塔维奥）、舒伯特艺术歌曲（《美丽的磨坊女》）、轻歌剧与德国艺术歌曲、巴赫与亨德尔清唱剧、音乐会咏叹调。
- 不该唱：`No heroic weight, no dark cover, no jazz swing, no breathy pop tone, no shouted climax`
- Negative prompt: `No heroic weight, no dark cover, no jazz swing, no breathy pop tone, no shouted climax`

## (7) 测试提示词示例（现代题材：凌晨的面包房）

- Prompt: `Sing in the style of Fritz Wunderlich, a song about a bakery opening before dawn. Radiant tenor, crystal diction, effortless Mozartian grace, warm intimacy, light orchestral accompaniment.`
- 中文对照：文德里希风格：唱一首关于黎明前开门的面包房的歌。明亮的男高音，咬字如水晶，莫扎特式毫不费力的优雅，暖意亲密，轻型管弦乐伴奏。
- Negative: `No heroic weight, no dark cover, no jazz swing, no breathy pop tone, no shouted climax`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
