# Wang Wei — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Wei: five-character regulated verse, empty mountains and clear springs, moonlight and pine, stillness with one moving detail, Zen-like emptiness, no noise, serene and luminous`
- ZH: 王维风格：五言律绝，空山清泉，月照松间，静中一动，禅意空寂，不著尘嚣，清朗而空明。

## (2) 意象

- 主意象：空山、明月、松、清泉、鹿柴、秋暝
- 辅意象：白云、青苔、渔舟、莲花
- 禁意象：喧闹市井、艳情、豪言壮语
- 密度：疏朗：意象少而精，一景一意，留白极大
- 来源：辋川实景、自然、禅境
`impression`

## (3) 韵律与句式

- 韵律：五言律绝为主，对仗工整，平仄稳健，押韵清朗
- 句式：短句平直，动静对照（明月照、清泉流），少跨行
- 节奏：极缓极静，呼吸深长，动处一点即止
`impression`

## (4) 语言密度与词汇

- 词汇：清、空、明、静、幽等词域；动词多照、流、归、空；少僻字
- 密度：每行信息量低，一景一句，修饰语极少
- 禁词：喧闹词、艳情词、豪壮词、堆砌典故
`impression`

## (5) 结构习惯

- 诗体：五言律诗 / 绝句；结构为静景 → 一动 → 归静
- 开头：直入静景（空山新雨后）
- 结尾：以归静收束，余音在空处
- 视角：第一人称静观者，偶隐去人称
- 推进：静 → 动 → 静，一动即止
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 空山清泉
- 明月松间
- 静中一动
- 大留白
- 禅意空寂
- 不该写：
- 喧闹市井
- 艳情铺陈
- 豪言壮语
- 堆砌典故
- 直白议论
- Negative prompt: `No noisy bustle, no erotic elaboration, no grand heroic diction, no piled-up allusions, no direct preaching`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wang Wei, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. five-character regulated verse, empty mountains and clear springs, moonlight and pine, stillness with one moving detail, Zen-like emptiness, no noise, serene and luminous`
- 中文对照：王维风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。王维风格：五言律绝，空山清泉，月照松间，静中一动，禅意空寂，不著尘嚣，清朗而空明。
- Negative: `No noisy bustle, no erotic elaboration, no grand heroic diction, no piled-up allusions, no direct preaching`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
