# Su Shi — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Su Shi: bold and unconstrained ci, great river flowing east, moonlight shared across a thousand miles, ten years of life and death in one line, philosophy worn lightly, no narrowness, expansive and humane`
- ZH: 苏轼风格：豪放词，大江东去，千里共婵娟，十年生死两茫茫，哲理举重若轻，绝无局促，旷达而深情。

## (2) 意象

- 主意象：大江、明月、赤壁、十年、东坡
- 辅意象：清风、江水、故国、人生如梦
- 禁意象：狭窄闺情、直白说教、晦涩用典
- 密度：疏密相间：意象宏大而句式疏朗，一景一意
- 来源：赤壁实景、人生际遇、典故
`impression`

## (3) 韵律与句式

- 韵律：词牌依谱，长短句参差，上下片分工分明，押韵豪放
- 句式：长短句交错，问句叠出，跨行随词意走，倒装豪放
- 节奏：旷达舒展，呼吸绵长，顿挫在上下片转折处
`impression`

## (4) 语言密度与词汇

- 词汇：豪放词域：大江、千古、明月、人生；动词多望、叹、归、笑；少僻字
- 密度：每行信息量适中，一景一句，哲理在末句点出
- 禁词：狭窄闺情、直白说教、晦涩用典、琐碎絮叨
`impression`

## (5) 结构习惯

- 诗体：词（豪放）；结构为上片写景 → 下片抒情议论 → 旷达收束
- 开头：以大景直入（大江东去、明月几时有）
- 结尾：以旷达收束（人生如梦、一樽还酹江月）
- 视角：第一人称旷达者
- 推进：大景 → 人事 → 哲理，层层放开
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 大江明月
- 豪放长短句
- 上下片转折
- 哲理举重若轻
- 旷达收束
- 不该写：
- 狭窄闺情
- 直白说教
- 晦涩用典
- 琐碎絮叨
- 局促小调
- Negative prompt: `No narrow boudoir sentiment, no direct preaching, no obscure allusions, no petty chatter, no cramped trifles`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Su Shi, a person buys oden at a convenience store late at night. bold and unconstrained ci, great river flowing east, moonlight shared across a thousand miles, ten years of life and death in one line, philosophy worn lightly, no narrowness, expansive and humane`
- 中文对照：苏轼风格：一个人在深夜便利店买关东煮。苏轼风格：豪放词，大江东去，千里共婵娟，十年生死两茫茫，哲理举重若轻，绝无局促，旷达而深情。
- Negative: `No narrow boudoir sentiment, no direct preaching, no obscure allusions, no petty chatter, no cramped trifles`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
