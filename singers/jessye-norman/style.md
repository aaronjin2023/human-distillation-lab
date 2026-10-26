# Jessye Norman — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Dramatic soprano in the style of Jessye Norman: majestic dark soprano, cathedral resonance, regal phrasing, spiritual depth, immense dynamic range`
- ZH: 诺曼风格：庄严深沉的女高音，教堂般的共鸣，帝王般的乐句，灵歌的深度，极大的强弱幅度。

## (2) 音色与音域

- 女高音音色庄严深沉，共鸣如教堂，音域宽广；主音色为深沉的戏剧女高音，辅音色为弱音的私语，禁音色为轻飘的花腔与气声耳语。`artifact`

## (3) 唱腔与发声技法

- 发声：气息极深，起音庄重，收尾多渐弱；唱腔：弱音到强音幅度极大，乐句庄严，颤音适中。`artifact`

## (4) 咬字与语言

- 德语、法语、英语多语咬字清晰；重音落在词义与诗意上；换气点留在长乐句的呼吸处。`artifact`

## (5) 节奏与即兴

- 速度从容庄重，乐句长；慢板更沉，高潮处不抢拍。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：瓦格纳与施特劳斯女主角（伊索尔德、阿里阿德涅）、马勒与施特劳斯艺术歌曲（《最后四首歌》）、美国灵歌、音乐会咏叹调、巴托克《蓝胡子城堡》中的朱迪丝。
- 不该唱：`No light soubrette sparkle, no breathy whisper, no jazz scat, no clipped coloratura, no casual pop phrasing`
- Negative prompt: `No light soubrette sparkle, no breathy whisper, no jazz scat, no clipped coloratura, no casual pop phrasing`

## (7) 测试提示词示例（现代题材：雨夜外卖员）

- Prompt: `Sing in the style of Jessye Norman, a song about a delivery rider crossing a rainy city at night. Majestic dark soprano, cathedral resonance, regal phrasing, immense dynamic range, warm orchestral accompaniment.`
- 中文对照：诺曼风格：唱一首关于深夜雨中外卖员穿过城市的歌。庄严深沉的女高音，教堂般的共鸣，帝王般的乐句，极大的强弱幅度，管弦乐伴奏。
- Negative: `No light soubrette sparkle, no breathy whisper, no jazz scat, no clipped coloratura, no casual pop phrasing`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
