# Shakira — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Latin pop vocal in the style of Shakira: distinctive nasal-tinged contralto, Arabic-influenced melisma, bilingual Spanish-English delivery, dance rhythm, belly-dance phrasing, yodel-like leaps, playful and sensual rather than polished`
- ZH: 夏奇拉风格：独特的鼻音女中音，阿拉伯风味转音，西英双语演唱，舞曲节奏，肚皮舞式乐句，约德尔式跳音，俏皮而性感，不追求圆润。

## (2) 音色与音域

- 声部：女中音（contralto），音域宽。
- 音色：主音色：鼻音、富于弹性、辨识度极高的女中音；辅音色：阿拉伯风味转音与约德尔式跳音；禁音色：美声式圆润、甜腻颤音、摇滚喊腔。音域宽，高音跳跃、低音叙事。

## (3) 唱腔与发声技法

- 鼻音声口：鼻音是声口标记，辨识度极高。`verbatim`
- 阿拉伯风味转音：melisma 带微分音弯曲。`impression`
- 双语演唱：西语与英语切换自然，重音各归其位。`artifact`
- 约德尔式跳音：高音与低音大幅跳进。`verbatim`
- 舞曲节奏：人声踩在拉丁舞曲节奏上，身体感强。`impression`

## (4) 咬字与语言

- 音色即语言：鼻音本身就是俏皮的标记。`impression`
- 力度：中强力度为主，舞曲时抬高，不煽情。`impression`
- 节奏：拉丁舞曲节拍，人声与打击乐咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如舞蹈，换气在句间。`impression`
- 与伴奏的咬合：打击乐与铜管构成呼应，人声居中。`impression`
- 情感递进：由俏皮到热烈，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：拉丁舞曲、西英双语爱情歌、阿拉伯风味转音、欢庆主题的体育歌曲。
- 不该唱：No operatic roundness、no sweet pop vibrato、no rock shouting、no mumbled diction、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no rock shouting, no mumbled diction, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于午夜等单的外卖骑手边等边跳舞的歌）

- Prompt: `Sing in the style of Shakira, a song about a food delivery rider dancing while waiting for an order at midnight. Distinctive nasal-tinged contralto, Arabic-influenced melisma, bilingual Spanish-English delivery, dance rhythm, belly-dance phrasing, playful and sensual.`
- 中文对照：独特的鼻音女中音，阿拉伯风味转音，西英双语演唱，舞曲节奏，肚皮舞式乐句，约德尔式跳音，俏皮而性感，不追求圆润。 唱一首关于午夜等单的外卖骑手边等边跳舞的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no rock shouting, no mumbled diction, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
