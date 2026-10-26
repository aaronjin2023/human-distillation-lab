# Elis Regina — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Bossa nova vocal in the style of Elis Regina: fiery contralto, precise Brazilian Portuguese diction, dramatic phrasing, jazz-inflected improvisation, bossa-nova rhythm with MPB fire, emotion that leaps from whisper to cry within a single line`
- ZH: 伊利斯·雷吉娜风格：炽热的女中音，精准的巴西葡语咬字，戏剧化乐句，爵士化即兴，波萨诺瓦节奏与巴西流行音乐的烈火，同一乐句内从耳语跳到哭喊的情感幅度。

## (2) 音色与音域

- 声部：女中音（contralto），音域宽。
- 音色：主音色：炽热、富于弹性、穿透力强的女中音；辅音色：耳语与哭喊的两极；禁音色：美声式圆润、甜腻颤音、摇滚喊腔。音域宽，高音炽热、低音叙事。

## (3) 唱腔与发声技法

- 戏剧化乐句：同一乐句内从耳语跳到哭喊，是声口标记。`verbatim`
- 爵士化即兴：转音自由如爵士即兴，不离和声。`impression`
- 葡语咬字：辅音颗粒清晰，重音落在词义上。`impression`
- 波萨节奏：人声踩在轻盈的桑巴节奏上。`artifact`
- 现场一次成形：现场录音少补录，情感幅度即真实。`impression`

## (4) 咬字与语言

- 音色即语言：炽热音色本身就是情感的幅度。`impression`
- 力度：由耳语到哭喊，幅度为波萨之最。`impression`
- 节奏：轻盈的桑巴节拍，人声拖拍与抢拍并存。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如独白，换气在句间。`impression`
- 与伴奏的咬合：吉他与钢琴只铺底，不抢人声。`impression`
- 情感递进：由低语到哭喊，层层推进，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：波萨诺瓦与巴西流行音乐、戏剧幅度的抒情、爵士化即兴、意象罗列的叙事。
- 不该唱：No operatic roundness、no sweet pop vibrato、no mumbled diction、no rock shouting、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于在公交站长椅上等雨停的女人的歌）

- Prompt: `Sing in the style of Elis Regina, a song about a woman waiting for the rain to stop on a bus stop bench. Fiery contralto, precise Brazilian Portuguese diction, dramatic phrasing, jazz-inflected improvisation, bossa-nova rhythm, emotion leaping from whisper to cry within a single line.`
- 中文对照：炽热的女中音，精准的巴西葡语咬字，戏剧化乐句，爵士化即兴，波萨诺瓦节奏与巴西流行音乐的烈火，同一乐句内从耳语跳到哭喊的情感幅度。 唱一首关于在公交站长椅上等雨停的女人的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
