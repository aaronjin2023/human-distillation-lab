# G.E.M. — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandopop vocal in the style of G.E.M.: powerful soprano with wide range, precise Mandarin diction, dramatic phrasing, R&B melisma, rock energy with ballad tenderness, emotion that leaps from whisper to belt within a single line`
- ZH: 邓紫棋风格：宽音域的有力女高音，精准的国语咬字，戏剧化乐句，R&B 转音，摇滚能量与抒情柔情并存，同一乐句内从耳语跳到强音的情感幅度。

## (2) 音色与音域

- 声部：女高音（soprano），音域宽。
- 音色：主音色：有力、富于弹性、穿透力强的女高音；辅音色：耳语与强音的两极；禁音色：美声式圆润、甜腻颤音、含混咬字。音域宽，高音有力、低音叙事。

## (3) 唱腔与发声技法

- 宽音域跳跃：高音与低音大幅跳进，音程即情感。`verbatim`
- R&B 转音：转音自由如 R&B 即兴，不离和声。`impression`
- 戏剧化乐句：同一乐句内从耳语跳到强音，是声口标记。`verbatim`
- 国语咬字：字正腔圆，辅音清晰。`impression`
- 摇滚能量：快歌以摇滚能量驱动，人声踩在节拍上。`impression`

## (4) 咬字与语言

- 音色即语言：有力音色本身就是情感的幅度。`impression`
- 力度：由耳语到强音，幅度大。`impression`
- 节奏：流行节拍，快歌踩拍、慢歌拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：长乐句如独白，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由低语到强音，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：宽音域抒情、泡沫与距离的叙事、R&B 转音、戏剧幅度的慢歌。
- 不该唱：No operatic roundness、no sweet pop vibrato、no mumbled diction、no rock shouting、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于黄昏时分女孩在天台吹肥皂泡的歌）

- Prompt: `Sing in the style of G.E.M., a song about a girl blowing soap bubbles on a rooftop at dusk. Powerful soprano with wide range, precise Mandarin diction, dramatic phrasing, R&B melisma, rock energy with ballad tenderness, emotion leaping from whisper to belt within a single line.`
- 中文对照：宽音域的有力女高音，精准的国语咬字，戏剧化乐句，R&B 转音，摇滚能量与抒情柔情并存，同一乐句内从耳语跳到强音的情感幅度。 唱一首关于黄昏时分女孩在天台吹肥皂泡的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no mumbled diction, no rock shouting, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
