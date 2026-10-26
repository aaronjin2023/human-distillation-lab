# Homer — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处，译文一律不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Homer: epic hexameter, formulaic epithets, wine-dark sea and rosy-fingered dawn, simile piled on simile, gods and men in the same breath`
- ZH: 荷马风格：史诗六音步，程式化修饰语，酒色的海与玫瑰色手指的黎明，明喻叠着明喻，神与人在同一口气里。

## (2) 意象

- 主意象：酒色的海、玫瑰色手指的黎明、青铜、盾牌、归家；辅意象：橄榄树、猪、风、星；禁意象：内心独白式抒情、抽象议论；密度高，意象多取自自然与器物，程式化重复。

## (3) 韵律与句式

- 六音步（hexameter）长行，行长稳定、庄重；句式以程式化修饰语（“足智多谋的奥德修斯”）与长明喻为主；节奏如吟唱，快慢平稳，朗读时有重复的呼吸。

## (4) 语言密度与词汇

- 词汇程式化而庄重：修饰语固定搭配；动词有力；名词多为器物与自然；禁词：口语俚语、抽象大词。

## (5) 结构习惯

- 史诗式结构：开篇呼告缪斯，中途倒叙，结尾收束；《伊利亚特》以愤怒开场，《奥德赛》以归家收束；视角为第三人称全知；推进靠情节与明喻交替。

## (6) 该写什么 / 不该写什么

- 该写：酒色的海、玫瑰色手指的黎明、青铜与盾牌；程式化修饰语、长明喻、开篇呼告；神与人同场的史诗场面。
- 不该写：风格上的禁区——modern interior monologue, no abstract discourse without an image, no colloquial diction, no fragmented free verse, no ironic detachment。
- Negative prompt: `No modern interior monologue, no abstract discourse without an image, no colloquial diction, no fragmented free verse, no ironic detachment`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Homer, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. Epic hexameter, formulaic epithets, wine-dark sea, long similes, gods and men in the same breath.`
- 中文对照：荷马风格：一只约克夏犬深夜坐在地铁座位上。史诗六音步，程式化修饰语，酒色的海，长明喻，神与人在同一口气里。
- Negative: `No modern interior monologue, no abstract discourse without an image, no colloquial diction, no fragmented free verse, no ironic detachment`
- 检验点：意象是否对位；韵律与句式是否成立；结尾是否按该诗人的收束习惯处理。
