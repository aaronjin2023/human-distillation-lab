# Homer — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Homer: dactylic hexameter, formulaic epithets, extended similes, in medias res, gods and men in one frame, wrath and wandering, grandeur without irony`
- ZH: 荷马风格：六音步长句，程式化套语，明喻层层铺展，半路切入，神与人同框，愤怒与漂泊，庄严而不反讽。

## (2) 句式与节奏

- 句式：句长：六音步（dactylic hexameter）的长句为主，句式庄重而绵延；程式化套语（如玫瑰色手指的黎明）反复出现，是口头吟诵的节拍器。
- 节奏：节奏：吟诵式，慢—快—慢：目录与铺陈缓慢，战斗与风暴急促，宴饮与告别回落；明喻一出，时间仿佛停住。

## (3) 词汇与意象

- 词汇：词汇：程式化 epithet（足智多谋的奥德修斯、捷足的阿喀琉斯）、身体与器物名词极具体、神名与地名密集；不用抽象议论，意义全在行动与比喻里。
- 意象：意象群：愤怒与命运、海与归家、宴饮与赠礼、盔甲与盾牌、黎明与黑夜、神的干预与人的抉择；明喻多取自自然（狮子、风暴、蜜蜂、火焰）。
- 禁词/禁意象：禁词/禁意象：不写内心独白式的现代心理分析，不用反讽与解构，不写抽象概念的长篇议论。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而超然的吟诵者视角，时而贴近人物、时而拉远到神界；人神双线并行，神的争吵与人的战争互为镜像。
- 结构：结构：半路切入（in medias res），再以插叙补前史；《伊利亚特》只写特洛伊战争最后数周，《奥德赛》以归家为线串起十年漂泊；环形结构，首尾呼应。

## (5) 语气与距离

- 语气：语气：庄严、悲悯而超然，对希腊人与特洛伊人一视同仁；不审判，只呈现命运的重量。

## (6) 该写什么 / 不该写什么

- 该写：该写：愤怒与荣誉、归家与漂泊、神人交锋、宴饮与赠礼、明喻铺展、目录式铺陈。
- 不该写：不该写：现代心理独白、反讽解构、抽象议论、快节奏情节推进。
- Negative prompt: `No modern psychological monologue, no irony or deconstruction, no abstract philosophical digression, no fast-paced plot suspense`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Homer, a small Yorkshire terrier sits on a subway seat, as the crowd flows around him like a river around a rock. Extended simile. Formulaic epithets. Gods and men in one frame. No irony.`
- 中文对照：荷马风格，一只小约克夏犬坐在地铁座位上，人群如河水绕过岩石般从它身边流过。铺展的明喻，程式化套语，神与人同框，不反讽。
- Negative: `modern psychological monologue, irony, abstract digression, fast-paced suspense`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
