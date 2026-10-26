# Leonard Cohen — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Folk vocal in the style of Leonard Cohen: deep spoken-sung baritone, near-whisper delivery, slow deliberate phrasing, minimal vibrato, poetic diction, female backing vocals as counterpoint, prayer-like restraint rather than climax`
- ZH: 莱昂纳德·科恩风格：低沉的说唱式男低音，近乎耳语的演唱，缓慢而有意的乐句，极少颤音，诗性咬字，女声和声作对位，祈祷般的克制而不追求高潮。

## (2) 音色与音域

- 声部：男低音（bass-baritone），常用低音区。
- 音色：主音色：低沉、沙哑、近乎耳语的男低音；辅音色：女声和声的清亮对位；禁音色：明亮高音、摇滚喊腔、甜美颤音。音域以低音区为叙事主场，高音区几乎不用。

## (3) 唱腔与发声技法

- 说唱式演唱：半说半唱，旋律服从诗句重音。`verbatim`
- 耳语式气声：近距离麦克风，气息声即语言的一部分。`verbatim`
- 缓慢乐句：速度极慢，停顿即意义。`impression`
- 女声对位：女声和声与主唱构成问答。`artifact`
- 极少颤音：直声为主，颤音只在句尾轻现。`impression`

## (4) 咬字与语言

- 音色即语言：低沉耳语音色本身就是祈祷与忏悔的距离感。`impression`
- 力度：弱力度为主，全曲几乎不抬高潮，克制是本体。`impression`
- 节奏：自由节奏，拖拍明显，停顿长于音符。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长停顿如诗行间的空白，换气即标点。`impression`
- 与伴奏的咬合：吉他与键盘只铺底，女声和声作对位。`impression`
- 情感递进：由低语到倾诉，不跳级、不爆发。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：宗教与爱情交织的诗性叙事、耳语式低音演唱、女声和声对位的民谣、忏悔与救赎主题的慢歌。
- 不该唱：No bright high notes、no rock shouting、no sentimental climax、no wide operatic vibrato、no fast patter delivery。
- Negative prompt: `No bright high notes, no rock shouting, no sentimental climax, no wide operatic vibrato, no fast patter delivery`

## (7) 测试提示词示例（现代题材：唱一首关于清晨天台上喂流浪猫的男人的歌）

- Prompt: `Sing in the style of Leonard Cohen, a song about a man feeding a stray cat on a rooftop at dawn. Deep spoken-sung baritone, near-whisper delivery, slow deliberate phrasing, minimal vibrato, poetic diction, female backing vocals as counterpoint.`
- 中文对照：低沉的说唱式男低音，近乎耳语的演唱，缓慢而有意的乐句，极少颤音，诗性咬字，女声和声作对位，祈祷般的克制而不追求高潮。 唱一首关于清晨天台上喂流浪猫的男人的歌。
- Negative: `No bright high notes, no rock shouting, no sentimental climax, no wide operatic vibrato, no fast patter delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
