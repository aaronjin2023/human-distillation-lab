# Celia Cruz — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Salsa vocal in the style of Celia Cruz: powerful contralto, ¡Azúcar! cry, call-and-response soneo improvisation, Cuban Spanish diction, montuno rhythm, brass and percussion, celebration and joy rather than lament`
- ZH: 西莉亚·克鲁斯风格：有力的女中音，“¡Azúcar!”呼喊，呼应式索内奥即兴，古巴西语咬字，蒙图诺节奏，铜管与打击乐，欢庆与喜悦而非哀诉。

## (2) 音色与音域

- 声部：女中音（contralto），常用中音区。
- 音色：主音色：有力、明亮、富于穿透力的女中音；辅音色：“¡Azúcar!”的呼喊；禁音色：美声式圆润、甜腻颤音、摇滚喊腔。音域以中音区为叙事主场，高音区以呼喊攀升。

## (3) 唱腔与发声技法

- “¡Azúcar!”呼喊：标志性呼喊，是声口标记。`verbatim`
- 索内奥即兴：蒙图诺段落的即兴呼应，落点清晰。`verbatim`
- 古巴西语咬字：辅音颗粒清晰，重音落在节奏上。`impression`
- 蒙图诺节奏：人声踩在蒙图诺节奏上，身体感强。`artifact`
- 铜管与打击乐：伴奏定节奏，人声在其上即兴。`impression`

## (4) 咬字与语言

- 音色即语言：有力音色本身就是欢庆的幅度。`impression`
- 力度：中强力度为主，欢庆时抬高，不煽情。`impression`
- 节奏：蒙图诺节拍，人声与打击乐咬合紧密。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如呼喊，换气在句间。`impression`
- 与伴奏的咬合：铜管与打击乐构成呼应，人声居中。`impression`
- 情感递进：由欢庆到狂喜，层层推进。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：欢庆的萨尔萨、“¡Azúcar!”呼喊、蒙图诺段落的索内奥即兴、古巴节奏与舞蹈。
- 不该唱：No operatic roundness、no sweet pop vibrato、no sentimental outburst、no mumbled diction、no flat monotone delivery。
- Negative prompt: `No operatic roundness, no sweet pop vibrato, no sentimental outburst, no mumbled diction, no flat monotone delivery`

## (7) 测试提示词示例（现代题材：唱一首关于夜市摊主边炸大蕉边跳舞的歌）

- Prompt: `Sing in the style of Celia Cruz, a song about a street food stall owner dancing while frying plantains at a night market. Powerful contralto, ¡Azúcar! cry, call-and-response soneo improvisation, Cuban Spanish diction, montuno rhythm, brass and percussion, celebration and joy.`
- 中文对照：有力的女中音，“¡Azúcar!”呼喊，呼应式索内奥即兴，古巴西语咬字，蒙图诺节奏，铜管与打击乐，欢庆与喜悦而非哀诉。 唱一首关于夜市摊主边炸大蕉边跳舞的歌。
- Negative: `No operatic roundness, no sweet pop vibrato, no sentimental outburst, no mumbled diction, no flat monotone delivery`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
