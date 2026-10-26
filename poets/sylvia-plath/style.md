# Sylvia Plath — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sylvia Plath: compressed rage in bright images, bees and mirrors, Daddy as a black shoe, Lady Lazarus rising from the ash, domestic horror made mythic, nothing soft`
- ZH: 普拉斯风格：明亮意象中的压缩愤怒，蜜蜂与镜子，爸爸是一只黑鞋子，拉撒路夫人从灰烬中升起，家居恐怖被写成神话，毫无柔软。

## (2) 意象

- 蜜蜂（蜂之组诗：秩序与蜇）
- 镜子（《镜子》：真实的冷）
- 爸爸与黑鞋（《爸爸》的压迫）
- 灰烬与升起（拉撒路夫人）
- 月与血（《爱丽尔》的明亮）
- 禁意象：温情的安慰、轻佻的俏皮、抽象的大词
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 短行、急促、意象跳接：《爱丽尔》以短行奔涌，节奏如心跳；《巨像》以格律较工整的短诗；晚期句式更短、更密，感叹与断言交替；整体由《巨像》的工整向《爱丽尔》的奔涌演变。

## (4) 语言密度与词汇

- 词汇：明亮意象词极密（蜜、镜、月、血），动词多为暴力态（蜇、烧、升）；抽象词（愤怒、压迫）借蜜蜂与镜子落地；禁词：温情安慰词、轻佻俏皮词、抽象大词。

## (5) 结构习惯

- 单篇多以一物（蜜蜂、镜子）起兴，意象并置—愤怒迸发—神话收束；《爱丽尔》以组诗推进，蜂之组诗为轴；结尾多为升起或戛然而止的爆发。

## (6) 该写什么 / 不该写什么

- 该写：
- 蜜蜂、镜子、爸爸的意象
- 短行奔涌的节奏
- 家居恐怖的神话化
- 升起或戛然而止的收束
- 不该写：
- 温情安慰与轻佻俏皮
- 抽象大词
- 直白说教
- 冗长铺陈
- Negative prompt: `No sentimental consolation, no flippant quips, no grand abstract words, no direct preaching, no long explanatory passages, no softening of the rage`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Sylvia Plath, a small Yorkshire terrier sits on a subway seat at night. Compressed rage in bright images, bees and mirrors in the carriage, Daddy as a black shoe, the dog as Lady Lazarus rising from the ash, nothing soft.`
- 中文对照：普拉斯风格：一只约克夏犬深夜坐在地铁座位上。明亮意象中的压缩愤怒，车厢里的蜜蜂与镜子，爸爸是一只黑鞋子，狗是拉撒路夫人从灰烬中升起，毫无柔软。
- Negative: `No sentimental consolation, no flippant quips, no grand abstractions, no preaching, no long passages, no softening of the rage`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
