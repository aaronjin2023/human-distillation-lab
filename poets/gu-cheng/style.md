# Gu Cheng — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gu Cheng: Misty School verse, black eyes seeking light in the dark night, you looking at me and at the clouds, far and near reversed, childlike images carrying adult sorrow, no explanation, lucid and strange`
- ZH: 顾城风格：朦胧诗，黑夜给了我黑色的眼睛，远和近颠倒，童稚意象承载成人之悲，绝无解释，清明而奇异。

## (2) 意象

- 主意象：黑夜、黑色的眼睛、远和近、弧线
- 辅意象：云、草、种子、风、叶子
- 禁意象：直白说教、铺张排比、口语俗词
- 密度：疏朗：意象童稚，一景一意，留白极大
- 来源：童年意象、自然、梦境
`impression`

## (3) 韵律与句式

- 韵律：现代自由体，短行居多，断行讲究，押韵自由
- 句式：短句为主，长短交错，跨行跳跃，少倒装
- 节奏：缓慢而奇异，呼吸均匀，顿挫在远近颠倒处
`impression`

## (4) 语言密度与词汇

- 词汇：童稚词域：黑夜、眼睛、云、草、种子；动词多看、寻、结、摇；少沉重词
- 密度：每行信息量低，一景一句，留白极大
- 禁词：直白说教、铺张排比、口语俗词、豪放壮语
`impression`

## (5) 结构习惯

- 诗体：现代抒情短诗；结构为童稚意象起兴 → 远近颠倒 → 奇异收束
- 开头：以童稚意象直入（黑夜给了我黑色的眼睛）
- 结尾：以奇异收束，不解释
- 视角：第一人称童稚者
- 推进：意象 → 颠倒 → 收束，层层见奇
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 黑夜黑眼睛
- 远和近颠倒
- 童稚意象
- 短行留白
- 奇异收束
- 不该写：
- 直白说教
- 铺张排比
- 口语俗词
- 豪放壮语
- 解释说明
- Negative prompt: `No direct preaching, no lavish parallelism, no colloquial diction, no grand heroic diction, no explanation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gu Cheng, a person buys oden at a convenience store late at night. Misty School verse, black eyes seeking light in the dark night, you looking at me and at the clouds, far and near reversed, childlike images carrying adult sorrow, no explanation, lucid and strange`
- 中文对照：顾城风格：一个人在深夜便利店买关东煮。顾城风格：朦胧诗，黑夜给了我黑色的眼睛，远和近颠倒，童稚意象承载成人之悲，绝无解释，清明而奇异。
- Negative: `No direct preaching, no lavish parallelism, no colloquial diction, no grand heroic diction, no explanation`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
