# Xue Tao — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xue Tao: delicate five- and seven-character verse, river wind and moonlit mountains, restrained longing, precise small images, a woman's voice speaking plainly and finely, no excess, clear and cool`
- ZH: 薛涛风格：清丽小诗，江风月色，含蓄寄情，意象小而精，女子声口直白而细腻，绝无铺张，清峭而凉。

## (2) 意象

- 主意象：锦江、风、月、山色、蒹葭
- 辅意象：离梦、霜、关塞、旧诗
- 禁意象：豪放壮语、铺张排比、直白艳情
- 密度：疏朗：意象小而精，一景一意
- 来源：锦江实景、离别日常
`impression`

## (3) 韵律与句式

- 韵律：五言 / 七言律绝，句式工整，平仄稳健
- 句式：短句平直，少倒装，少跨行，句句落地
- 节奏：缓慢清凉，呼吸均匀
`impression`

## (4) 语言密度与词汇

- 词汇：清丽词域：风、月、霜、江；动词多寄、望、忆、别；少僻字
- 密度：每行信息量低，一景一句
- 禁词：豪放壮语、铺张排比、直白艳情、僻典
`impression`

## (5) 结构习惯

- 诗体：短篇抒情 / 寄赠诗；结构为写景 → 寄情 → 含蓄收束
- 开头：直入眼前之景（锦江、风）
- 结尾：以含蓄寄情收束，不直言
- 视角：第一人称女子自述
- 推进：景 → 情 → 寄，层层淡出
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 锦江风月
- 含蓄寄情
- 小而精的意象
- 清丽短句
- 女子声口
- 不该写：
- 豪放壮语
- 铺张排比
- 直白艳情
- 堆砌典故
- 激烈议论
- Negative prompt: `No grand heroic diction, no lavish parallelism, no blunt eroticism, no piled-up allusions, no heated argument`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xue Tao, a letter to oneself ten years from now. delicate five- and seven-character verse, river wind and moonlit mountains, restrained longing, precise small images, a woman's voice speaking plainly and finely, no excess, clear and cool`
- 中文对照：薛涛风格：一封写给十年后自己的信。薛涛风格：清丽小诗，江风月色，含蓄寄情，意象小而精，女子声口直白而细腻，绝无铺张，清峭而凉。
- Negative: `No grand heroic diction, no lavish parallelism, no blunt eroticism, no piled-up allusions, no heated argument`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
