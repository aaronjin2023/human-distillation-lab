# ABBA — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Pop vocal in the style of ABBA: bright intertwined harmonies, two female leads in close harmony, male voices underneath, crystalline diction, joyful disco lift, bittersweet melancholy inside the sparkle`
- ZH: ABBA 风格：明亮交织的和声，两位女主唱的近距离和声，男声在下托底，清澈咬字，欢快的迪斯科上扬，闪耀中有苦涩的忧郁。

## (2) 音色与音域

- 音色：明亮的女声和声为主，男声低音托底；主音色为双女主唱的和声，辅音色为男声和声；禁音色为沙哑撕裂与含混低语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息平稳，起音干脆，收尾拖长渐弱；和声声部音准统一；《Dancing Queen》以和声上扬与迪斯科节奏为标记。`artifact`

## (4) 咬字与语言

- 咬字：瑞典口音底色的英语发音，元音亮、辅音清晰；重音落在节奏点上；换气点统一。`artifact`

## (5) 节奏与即兴

- 节奏：迪斯科节拍上精准切分，和声乐句与节拍严丝合缝；即兴少，以和声编排制造变化。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：
- 迪斯科流行歌与和声交织的副歌（如《Dancing Queen》一类）
- 双女主唱近距离和声的演唱
- 欢快副歌中苦涩忧郁的对照
- 男女声交织的层次推进
- 不该唱：`No raspy growl, no mumbled diction, no operatic vibrato, no soloistic showboating, no loose off-beat phrasing`
- Negative prompt: `No raspy growl, no mumbled diction, no operatic vibrato, no soloistic showboating, no loose off-beat phrasing`

## (7) 测试提示词示例（现代题材：地铁里的约克夏犬）

- Prompt: `Sing in the style of ABBA, a song about a small Yorkshire terrier sitting on a subway seat. Bright intertwined harmonies, two female leads in close harmony, male voices underneath, crystalline diction, joyful disco lift, bittersweet melancholy inside the sparkle.`
- 中文对照：ABBA 风格：唱一首关于地铁里约克夏犬的歌。明亮交织的和声，两位女主唱近距离和声，男声在下托底，清澈咬字，欢快的迪斯科上扬，闪耀中有苦涩的忧郁。
- Negative: `No raspy growl, no mumbled diction, no operatic vibrato, no soloistic showboating`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
