# Héctor Lavoe — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Salsa vocal in the style of Héctor Lavoe: street-wise tenor, soneo improvisation, Puerto Rican Spanish diction, bolero tenderness inside salsa fire, montuno rhythm, brass and percussion, a singer who tells his own story in every song`
- ZH: 埃克托·拉沃风格：街头智慧的男高音，索内奥即兴，波多黎各西语咬字，萨尔萨烈火中的波莱罗柔情，蒙图诺节奏，铜管与打击乐，每首歌都在讲自己的故事。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：街头感、富于弹性的男高音；辅音色：波莱罗式的柔情；禁音色：美声式圆润、甜腻颤音、摇滚喊腔。音域以中音区为叙事主场，高音区以即兴攀升。

## (3) 唱腔与发声技法

- 索内奥即兴：蒙图诺段落的即兴呼应，落点清晰。`verbatim`
- 街头咬字：波多黎各西语辅音直接，重音落在节奏上。`impression`
- 波莱罗柔情：慢歌以柔情收束，与快歌的烈火对照。`verbatim`
- 蒙图诺节奏：人声踩在蒙图诺节奏上，身体感强。`artifact`
- 现场一次成形：现场录音少补录，即兴即真实。`impression`

## (4) 咬字与语言

- 音色即语言：街头音色本身就是自述的可信度。`impression`
- 力度：中强力度为主，快歌抬高、慢歌收低，对照鲜明。`impression`
- 节奏：蒙图诺节拍，人声与打击乐咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如街头讲述，换气在句间。`impression`
- 与伴奏的咬合：铜管与打击乐构成呼应，人声居中。`impression`
- 情感递进：由讲述到即兴再到柔情，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：歌手的自述、蒙图诺段落的索内奥即兴、波莱罗柔情慢歌、街头叙事的萨尔萨。
- 不该唱：No operatic roundness、no sweet pop vibrato、no sentimental outburst、no mumbled diction、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no sentimental outburst, no mumbled diction, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于在同一个街角卖了四十年报纸的报贩的歌）

- Prompt: `Sing in the style of Héctor Lavoe, a song about a newspaper vendor who has sold papers on the same corner for forty years. Street-wise tenor, soneo improvisation, Puerto Rican Spanish diction, bolero tenderness inside salsa fire, montuno rhythm, brass and percussion.`
- 中文对照：街头智慧的男高音，索内奥即兴，波多黎各西语咬字，萨尔萨烈火中的波莱罗柔情，蒙图诺节奏，铜管与打击乐，每首歌都在讲自己的故事。 唱一首关于在同一个街角卖了四十年报纸的报贩的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no sentimental outburst, no mumbled diction, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
