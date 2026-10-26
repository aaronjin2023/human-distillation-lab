# Virginia Woolf — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Virginia Woolf: stream of consciousness in waves, a single day holding a whole life, free indirect thought, images of light and water, the moment of being, sentences that rise and fall like breath`
- ZH: 伍尔夫风格：波浪般的意识流，一天装下整个人生，自由间接的思想，光与水的意象，‘存在的瞬间’，句子如呼吸般起伏。

## (2) 句式与节奏

句长：长短交错如波浪——长句绵延、意象层叠，随后以短句收束（‘她要自己去买花’）；分号与逗号构成呼吸，括号插入联想。节奏：单日结构（《达洛维夫人》一天、《到灯塔去》分‘窗—岁月流逝—灯塔’三段），时间靠意识的潮汐推进而非情节；‘岁月流逝’一节以十年的战争与死亡压缩成十余页，节奏骤然加快。`verbatim`

## (3) 词汇与意象

词汇：日常词（花、帽子、窗、灯塔）与抽象词（存在、瞬间、意识）并置；光、水、海、花的意象极密。意象群：花（达洛维夫人的花）、窗（内外世界的边界）、灯塔（到达不了又必须到达的目标）、海浪（《海浪》的结构本身）、存在的瞬间（moment of being）。禁词/禁意象：不用全知叙述者的解释，不用情节驱动的悬念，不用直白的道德评判。`impression`/`artifact`

## (4) 叙事视角与结构

视角：自由间接引语 + 多视角轮换，同一事件（达洛维夫人的宴会）在不同人物意识中折射；叙述者不固定，意识在人物之间流动如潮水。结构：单日环形、意识流的三段式、传记戏拟（《奥兰多》三百年）；开头多为一个日常决定（‘她要自己去买花’），结尾多为顿悟或到达（灯塔终于到达）。对话：对话常被内心独白淹没，人物说出口的远少于想到的。`verbatim`

## (5) 语气与距离

语气：抒情、敏锐、带忧郁的清醒；对人物的态度是共情的凝视；与读者的距离是邀约式的——请读者进入意识的潮汐。反讽是轻柔的，悲悯是主调。`impression`（学界共识）

## (6) 该写什么 / 不该写什么

- 该写：该写：一个普通日的意识潮汐；光、水、花、窗的意象；存在的瞬间；多视角下的同一事件；女性内心的自由与压抑；时间如何在一日中展开。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No omniscient explanation, no plot-driven suspense, no direct moralising, no flat reportage, no heroic action scenes`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Virginia Woolf, a small Yorkshire terrier sits on a subway seat. Free indirect thought flows between the dog, the woman opposite, and the man by the door. Light through the window, the hum of the train, a moment of being. One ordinary ride holds a whole life.`
- 中文对照：伍尔夫风格，一只小约克夏犬坐在地铁座位上。自由间接的思想在狗、对面的女人与门边的男人之间流动；窗外的光、列车的轰鸣、一个存在的瞬间；一次普通的乘车装下整个人生。
- Negative: `omniscient explanation, plot-driven suspense, direct moralising, flat reportage, heroic action scenes`
- 检验点：写出的文本是否‘一读即是此人’而不是‘情节对了、语言不对’；禁区是否出现（见第 (6) 节）；现代题材是否被风格同化而不是风格被题材冲淡。
