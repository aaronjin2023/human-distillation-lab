# Vicente Fernández — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Ranchera vocal in the style of Vicente Fernández: powerful mariachi tenor, crying falsetto breaks, Mexican Spanish diction, trumpet and violin, macho tenderness, a song as a toast shouted to the whole cantina`
- ZH: 比森特·费尔南德斯风格：有力的马里亚奇男高音，哭腔式假声断裂，墨西哥西语咬字，小号与小提琴，硬汉柔情，歌如向整个酒馆举杯的祝酒。

## (2) 音色与音域

- 声部：男高音（tenor），音域宽。
- 音色：主音色：有力、明亮、富于穿透力的男高音；辅音色：哭腔式假声断裂；禁音色：美声式圆润、甜腻颤音、摇滚喊腔。音域宽，高音以哭腔攀升、低音叙事。

## (3) 唱腔与发声技法

- 哭腔式假声：高音处假声断裂，是声口标记。`verbatim`
- 马里亚奇伴奏：小号与小提琴铺底，人声在其上叙事。`artifact`
- 墨西哥西语咬字：辅音硬朗，重音落在节奏上。`impression`
- 现场一次成形：现场录音少补录，豪情即真实。`impression`
- 长乐句气息：长乐句一气呵成，换气极隐蔽。`impression`

## (4) 咬字与语言

- 音色即语言：有力音色本身就是豪情的幅度。`impression`
- 力度：中强力度为主，高潮处抬高，不煽情。`impression`
- 节奏：兰切拉节拍，人声与马里亚奇咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如祝酒，换气在句间。`impression`
- 与伴奏的咬合：小号与小提琴构成呼应，人声居中。`impression`
- 情感递进：由讲述到豪情，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：兰切拉豪情歌曲、哭腔式假声抒情、王者自述、马里亚奇伴奏的叙事。
- 不该唱：No operatic roundness、no sweet pop vibrato、no mumbled diction、no rock shouting、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于午夜出租车司机为乘客唱歌的歌）

- Prompt: `Sing in the style of Vicente Fernández, a song about an old taxi driver singing to his passengers at midnight. Powerful mariachi tenor, crying falsetto breaks, Mexican Spanish diction, trumpet and violin, macho tenderness, a song as a toast shouted to the whole cantina.`
- 中文对照：有力的马里亚奇男高音，哭腔式假声断裂，墨西哥西语咬字，小号与小提琴，硬汉柔情，歌如向整个酒馆举杯的祝酒。 唱一首关于午夜出租车司机为乘客唱歌的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
