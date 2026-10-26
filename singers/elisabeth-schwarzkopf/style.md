# Elisabeth Schwarzkopf — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Lyric soprano in the style of Elisabeth Schwarzkopf: silvery refined soprano, exquisite diction, Mozartian grace, Straussian glow, polished studio elegance`
- ZH: 施瓦茨科普夫风格：银亮精致的抒情女高音，咬字精美，莫扎特式优雅，施特劳斯式光辉，录音室打磨的优雅。

## (2) 音色与音域

- 抒情女高音，音色银亮精致；主音色为银亮的抒情女高音，辅音色为弱音的轻盈，禁音色为戏剧性的胸声吼叫与粗粝边缘。`artifact`

## (3) 唱腔与发声技法

- 发声：气息细腻，起音干净，收尾多渐弱；唱腔：弱音层次多，花腔轻盈，颤音细腻。`artifact`

## (4) 咬字与语言

- 德语咬字极其清晰，元音纯净；换气点藏在乐句呼吸处。`artifact`

## (5) 节奏与即兴

- 乐句优雅，速度从容；慢板更沉，快板更轻。`artifact`

## (6) 该唱什么 / 不该唱什么

- 该唱：莫扎特女主角（《玫瑰骑士》元帅夫人、《魔笛》帕米娜）、施特劳斯艺术歌曲（《最后四首歌》《清晨》）、舒伯特与沃尔夫艺术歌曲、轻歌剧曲目、录音室打磨的抒情段落。
- 不该唱：`No dramatic chest belt, no rough edge, no jazz phrasing, no breathy pop tone, no heavy vibrato`
- Negative prompt: `No dramatic chest belt, no rough edge, no jazz phrasing, no breathy pop tone, no heavy vibrato`

## (7) 测试提示词示例（现代题材：共享单车）

- Prompt: `Sing in the style of Elisabeth Schwarzkopf, a song about riding a shared bicycle through a city in the morning. Silvery refined soprano, exquisite diction, Mozartian grace, Straussian glow, light orchestral accompaniment.`
- 中文对照：施瓦茨科普夫风格：唱一首关于清晨骑共享单车穿过城市的歌。银亮精致的抒情女高音，咬字精美，莫扎特式优雅，施特劳斯式光辉，轻型管弦乐伴奏。
- Negative: `No dramatic chest belt, no rough edge, no jazz phrasing, no breathy pop tone, no heavy vibrato`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
