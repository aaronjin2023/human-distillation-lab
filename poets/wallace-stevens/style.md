# Wallace Stevens — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wallace Stevens: imagination against reality, the blackbird in thirteen ways, the jar on a hill in Tennessee, the emperor of ice-cream, abstraction made sensuous, the supreme fiction`
- ZH: 史蒂文斯风格：想象对现实，黑鸟的十三种看法，田纳西山上的坛子，冰淇淋的皇帝，抽象变得可感，至上的虚构。

## (2) 意象

- 黑鸟（十三种看法，想象的棱镜）
- 坛子（秩序对荒野）
- 冰淇淋的皇帝（生与死的并置）
- 棕榈与蓝吉他（色彩与音乐）
- 雪山与移动（《看黑鸟》的雪山）
- 禁意象：直白的抒情告白、琐碎的日常絮叨
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 自由体与空白体交错：《风琴》以短章并置，句式断裂、意象跳接；《看黑鸟》以十三节短章，每节一看法；晚期以长句冥想推进；整体由并置的短章向冥想的长句演变。

## (4) 语言密度与词汇

- 词汇：抽象词（想象、现实、虚构）极密，但每词借黑鸟、坛子、冰淇淋落地；色彩词（蓝、绿、金）与音乐词并置；禁词：直白告白词、琐碎絮叨词、煽情词。

## (5) 结构习惯

- 短章并置：《看黑鸟》十三节，每节一看法，顺序即意义；单篇多以一物（坛子、黑鸟）起兴，并置—对照—翻转；晚期以冥想长句推进，结尾多为悖论收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 黑鸟、坛子、冰淇淋的意象
- 短章并置与多看法
- 抽象借物落地的结构
- 悖论式收束
- 不该写：
- 直白抒情告白
- 琐碎日常絮叨
- 煽情的爆发
- 无物支撑的抽象议论
- Negative prompt: `No direct lyrical confession, no trivial daily chatter, no sentimental outburst, no abstract discourse without a thing, no single fixed viewpoint, no explaining the image`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Wallace Stevens, a small Yorkshire terrier sits on a subway seat at night. Thirteen ways of looking at the dog, the jar on a hill in the carriage, the emperor of ice-cream among commuters, imagination against reality, a paradoxical close.`
- 中文对照：史蒂文斯风格：一只约克夏犬深夜坐在地铁座位上。看狗的十三种方法，车厢山上的坛子，乘客中的冰淇淋皇帝，想象对现实，悖论式收束。
- Negative: `No direct confession, no trivial chatter, no sentimental outburst, no imageless abstraction, no single viewpoint, no explaining the image`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
