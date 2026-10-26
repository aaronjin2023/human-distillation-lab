# Jay Chou — 演唱风格规格 style.md（给音频模型）

> 只描述声音，不描述人生。引用歌词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `Mandopop vocal in the style of Jay Chou: laid-back mumbled tenor, R&B phrasing with Chinese pentatonic melody, fast rap-like delivery mixed with ballad tenderness, precise Mandarin diction under the mumble, a song as a cool aside rather than a declaration`
- ZH: 周杰伦风格：慵懒含混的男高音，R&B 乐句与中国五声音阶旋律，快嘴说唱与抒情柔情并存，含混之下的精准国语咬字，歌如酷酷的旁白而非宣告。

## (2) 音色与音域

- 声部：男高音（tenor），常用中音区。
- 音色：主音色：慵懒、含混、富于弹性的男高音；辅音色：快嘴说唱与抒情柔情；禁音色：美声式圆润、摇滚喊腔、甜腻颤音。音域以中音区为叙事主场，高音区轻收。

## (3) 唱腔与发声技法

- 含混咬字：咬字含混是声口标记，但重音仍落在词义上。`verbatim`
- R&B 乐句：转音自由如 R&B 即兴，不离和声。`impression`
- 五声音阶旋律：旋律带中国五声音阶的骨架。`artifact`
- 快嘴说唱：快歌以说唱驱动，人声踩在节拍上。`impression`
- 抒情柔情：慢歌以柔情收束，与快歌对照。`impression`

## (4) 咬字与语言

- 音色即语言：慵懒音色本身就是酷的距离感。`impression`
- 力度：中弱力度为主，高潮只抬半格，克制是酷的底色。`impression`
- 节奏：R&B 节拍，快歌踩拍、慢歌拖拍。`impression`

- 换气：换气点选择、气口长短、是否用换气制造停顿与悬念——见 language.md。

## (5) 节奏与即兴

- 乐句呼吸：短乐句如旁白，换气在句间。`impression`
- 与伴奏的咬合：乐队只铺底，不抢人声。`impression`
- 情感递进：由慵懒到柔情，不跳级。`impression`

## (6) 该唱什么 / 不该唱什么

- 该唱：中国风流行歌、R&B 乐句的抒情、快嘴说唱、童年与故乡的叙事。
- 不该唱：No operatic roundness、no rock shouting、no sweet pop vibrato、no crystal-clear diction、no sentimental outburst。
- Negative prompt: `No operatic roundness, no rock shouting, no sweet pop vibrato, no crystal-clear diction, no sentimental outburst`

## (7) 测试提示词示例（现代题材：唱一首关于黄昏时分乡村屋顶上放风筝的男孩的歌）

- Prompt: `Sing in the style of Jay Chou, a song about a boy flying a kite on a rooftop in a village at dusk. Laid-back mumbled tenor, R&B phrasing with Chinese pentatonic melody, fast rap-like delivery mixed with ballad tenderness, precise Mandarin diction under the mumble.`
- 中文对照：慵懒含混的男高音，R&B 乐句与中国五声音阶旋律，快嘴说唱与抒情柔情并存，含混之下的精准国语咬字，歌如酷酷的旁白而非宣告。 唱一首关于黄昏时分乡村屋顶上放风筝的男孩的歌。
- Negative: `No operatic roundness, no rock shouting, no sweet pop vibrato, no crystal-clear diction, no sentimental outburst`
- 检验点：风格是否可辨（音色、唱腔、咬字三者至少两项成立），而不是只贴一个歌手名字；现代题材是否被风格“吃掉”而不是原样照搬。
