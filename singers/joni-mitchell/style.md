# Joni Mitchell — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Folk vocal in the style of Joni Mitchell: soaring soprano with wide range, open-tuned guitar, conversational phrasing, free rhythm, jazzy inflection, poetic diction, confessional intimacy rather than polish`
- ZH: 琼尼·米切尔风格：宽音域的翱翔女高音，开放调弦吉他，口语化乐句，自由节奏，爵士化转音，诗性咬字，坦白的亲密感而不追求圆润。

## (2) 音色与音域

- 声部：女高音（soprano），音域宽。
- 音色：主音色：清亮而富于变化的女高音，高音翱翔、低音叙事；辅音色：爵士化的转音与气声；禁音色：歌剧式花腔、甜腻流行颤音、摇滚喊腔。音域宽，高音开放、低音收敛。

## (3) 唱腔与发声技法

- 开放调弦吉他：自创调弦，吉他与人声同呼吸。`artifact`
- 宽音域跳跃：高音与低音大幅跳进，音程即情感。`verbatim`
- 爵士化转音：转音自由如爵士即兴，不离和声。`impression`
- 自由节奏：拖拍与抢拍并存，节奏服从诗句。`impression`
- 口语化咬字：咬字如谈话，辅音轻。`impression`

## (4) 咬字与语言

- 音色即语言：宽音域本身就是坦白的幅度，高音是袒露，低音是沉思。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是坦白的底色。`impression`
- 节奏：自由节奏，吉他定拍，人声拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如独白，换气在诗行间。`impression`
- 与伴奏的咬合：吉他只铺底，爵士乐手在后期加入对位。`impression`
- 情感递进：由观察到坦白再到自省，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：云与天空的诗性叙事、城市与自然的观察、爱情坦白与自省、开放调弦吉他的民谣爵士。
- 不该唱：No operatic coloratura、no sweet pop vibrato、no rock shouting、no rigid on-beat phrasing、no polished studio gloss。
- Negative prompt: `No operatic coloratura, no sweet pop vibrato, no rock shouting, no rigid on-beat phrasing, no polished studio gloss`

## (7) 测试提示词示例（现代题材：唱一首关于雨天在阳台浇花的女人的歌）

- Prompt: `Sing in the style of Joni Mitchell, a song about a woman watering plants on a balcony in the rain. Soaring soprano with wide range, open-tuned guitar, conversational phrasing, free rhythm, jazzy inflection, poetic diction, confessional intimacy.`
- 中文对照：宽音域的翱翔女高音，开放调弦吉他，口语化乐句，自由节奏，爵士化转音，诗性咬字，坦白的亲密感而不追求圆润。 唱一首关于雨天在阳台浇花的女人的歌。
- Negative: `No operatic coloratura, no sweet pop vibrato, no rock shouting, no rigid on-beat phrasing, no polished studio gloss`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
