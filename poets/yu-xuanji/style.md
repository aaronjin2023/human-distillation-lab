# Yu Xuanji — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yu Xuanji: frank and direct late-Tang verse, a woman speaking in her own voice, longing and resentment held in clear images, river mist and autumn leaves, no veil, passionate and lucid`
- ZH: 鱼玄机风格：晚唐直抒，女子自道其声，怨而不晦，江雾秋叶，情真而语直，不加遮掩，炽烈而清明。

## (2) 意象

- 主意象：江陵、愁望、秋叶、江雾、子安
- 辅意象：离别、相思、山居、夜雨
- 禁意象：豪放壮语、铺张排比、晦涩用典
- 密度：疏朗：意象小而精，一景一意，情在景外
- 来源：江陵实景、寄情日常
`impression`

## (3) 韵律与句式

- 韵律：五言 / 七言律绝，句式工整，平仄稳健
- 句式：短句平直，少倒装，少跨行，句句落地
- 节奏：缓慢而炽烈，呼吸均匀，情到处微扬
`impression`

## (4) 语言密度与词汇

- 词汇：直白词域：愁、望、寄、忆；动词多望、寄、思、别；少僻字
- 密度：每行信息量低，一景一句
- 禁词：豪放壮语、铺张排比、晦涩用典、直白艳情
`impression`

## (5) 结构习惯

- 诗体：短篇抒情 / 寄赠诗；结构为写景 → 寄情 → 直抒收束
- 开头：直入眼前之景（江陵愁望）
- 结尾：以直抒收束，不遮掩
- 视角：第一人称女子自述
- 推进：景 → 情 → 直抒，层层见真
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 女子自道
- 江陵愁望
- 直抒寄情
- 小而精的意象
- 清丽短句
- 不该写：
- 豪放壮语
- 铺张排比
- 晦涩用典
- 直白艳情
- 遮掩含糊
- Negative prompt: `No grand heroic diction, no lavish parallelism, no obscure allusions, no blunt eroticism, no evasive vagueness`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Yu Xuanji, a small Yorkshire terrier sits on a subway seat at night, watched by commuters. frank and direct late-Tang verse, a woman speaking in her own voice, longing and resentment held in clear images, river mist and autumn leaves, no veil, passionate and lucid`
- 中文对照：鱼玄机风格：一只约克夏犬深夜坐在地铁座位上，乘客们看着它。鱼玄机风格：晚唐直抒，女子自道其声，怨而不晦，江雾秋叶，情真而语直，不加遮掩，炽烈而清明。
- Negative: `No grand heroic diction, no lavish parallelism, no obscure allusions, no blunt eroticism, no evasive vagueness`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
