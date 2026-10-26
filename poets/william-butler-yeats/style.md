# William Butler Yeats — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Butler Yeats: Irish myth and the gyre, the tower and the swan, Byzantium's gold bird, early Celtic twilight giving way to a hard late plainness, ceremony and passion held in one stanza`
- ZH: 叶芝风格：爱尔兰神话与盘旋，塔与天鹅，拜占庭的金鸟，早期的凯尔特暮色让位于晚期坚硬的朴素，仪式与激情同在一节诗里。

## (2) 意象

- 塔（晚期立足点：塔楼即自我）
- 盘旋与陀螺（历史的盘旋上升）
- 天鹅与野天鹅（《库尔的野天鹅》）
- 拜占庭金鸟（超越肉身的艺术）
- 玫瑰与苇间风（早期暮色）
- 禁意象：轻佻的都市风情、琐碎的日常
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 早期多用民谣体与挽歌体，音乐性强；中期以十四行诗与八行体求庄重；晚期以短促的四行体与对句求坚硬；句式多为长句盘旋后短句收束，如陀螺收紧。

## (4) 语言密度与词汇

- 词汇：神话词（库丘林、爱尔兰诸神）与日常词（塔、石、梯）并置；抽象词（激情、仪式、幻象）借具体意象落地；禁词：轻佻俚语、无根的抽象议论。

## (5) 结构习惯

- 单篇多以一景（塔、天鹅、拜占庭）起兴，神话与现实对照，末节以格言式收束；组诗《塔》《盘旋的楼梯》以塔为轴心编排；晚期多用对句与问答体。

## (6) 该写什么 / 不该写什么

- 该写：
- 爱尔兰神话与盘旋的历史观
- 塔、天鹅、拜占庭金鸟的意象
- 仪式与激情的对照
- 格言式收束
- 不该写：
- 轻佻都市风情
- 琐碎日常絮叨
- 无意象支撑的抽象议论
- 温情的安慰收束
- Negative prompt: `No frivolous urban chic, no trivial daily chatter, no abstract discourse without an image, no sentimental consolation, no loose formless free verse`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of William Butler Yeats, a small Yorkshire terrier sits on a subway seat at night. The tower of the carriage, the gyre of the crowd, the dog as a small golden bird of Byzantium, ceremony and passion in one stanza, an aphoristic close.`
- 中文对照：叶芝风格：一只约克夏犬深夜坐在地铁座位上。车厢如塔，人群如盘旋，狗是拜占庭的一只小金鸟，仪式与激情同在一节诗里，格言式收束。
- Negative: `No frivolous chic, no trivial chatter, no imageless abstraction, no sentimental consolation, no formless verse`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
