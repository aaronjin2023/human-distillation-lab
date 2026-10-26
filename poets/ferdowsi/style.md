# Ferdowsi — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原诗时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ferdowsi: heroic epic in rhymed couplets, kings and champions, rustling banners and single combat, fate turning on one blow, solemn and vast as a plain at dawn`
- ZH: 菲尔多西风格：英雄史诗，对句体，王与勇士，旌旗猎猎与单挑决斗，命运系于一击，庄严辽阔如黎明平原

## (2) 意象

- 主意象：王座、宝剑、战马、旌旗、荒原；辅意象：酒宴、猎鹰、星辰、古波斯宫廷；禁意象：市井琐碎、内心独白式抒情；密度中等，意象来自神话、王朝史与口头传统。`impression`

## (3) 韵律与句式

- 对句体（masnavi 式双行押韵），句长整齐，排比铺陈；战斗场面短句加速，抒情处放缓；节奏如战鼓，行断整齐，少跨行。`impression`

## (4) 语言密度与词汇

- 词汇：王朝、血统、荣誉、命运等宏大词域；动词尚武（挥剑、驰马、夺旗）；善用程式化套语与谱系列举；禁词：口语俚语、现代抽象词、琐碎日常词。`impression`

## (5) 结构习惯

- 长篇史诗分王朝纪传，篇章以王统推进；开头多为创世或登基，结尾以哀悼或预言收束；视角全知叙事，间有英雄独白；推进靠谱系与战事递进。`impression`

## (6) 该写什么 / 不该写什么

- 该写：英雄史诗对句、王统与谱系推进、单挑决斗场面、命运与荣誉主题。
- 不该写：市井琐碎日常、内心独白式抒情、现代口语与抽象词、碎片化拼贴。
- Negative prompt: `No mundane everyday chatter, no introspective free-verse lyricism, no modern slang and abstract jargon, no fragmented collage, no sentimental romance without fate`

## (7) 测试提示词示例（现代题材：一封写给十年后自己、从未寄出的信）

- Prompt: `In the style of Ferdowsi, a letter to oneself ten years from now, never sent. Heroic epic couplets, the writer as a champion facing fate, banners and a single decisive blow, solemn and vast.`
- 中文对照：菲尔多西风格：一封写给十年后自己、从未寄出的信。英雄史诗对句，写信人如直面命运的勇士，旌旗与决定性一击，庄严辽阔
- Negative: `No mundane everyday chatter, no introspective free-verse lyricism, no modern slang and abstract jargon, no fragmented collage, no sentimental romance without fate`
- 检验点：意象、韵律与收束是否符合本诗人的风格；禁区写法是否出现。
