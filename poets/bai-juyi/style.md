# Bai Juyi — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bai Juyi: plain narrative verse in the new yuefu manner, a story told straight, everyday words, satire by plain statement, long poems that read like tales, no obscurity, clear and moving`
- ZH: 白居易风格：新乐府叙事，明白如话，故事直陈，讽喻在平实之中，长篇如话本，绝无晦涩，通俗而动人。

## (2) 意象

- 主意象：长恨、琵琶、卖炭翁、江州司马、宫怨
- 辅意象：天涯沦落人、江月、商人妇
- 禁意象：晦涩用典、华丽堆砌、玄理议论
- 密度：疏朗：叙事为主，意象随故事出现，不堆叠
- 来源：民间疾苦、宫廷旧事、日常
`impression`

## (3) 韵律与句式

- 韵律：七言歌行 / 乐府，句式平直，押韵自然，叙事节奏分明
- 句式：叙事句式，长短参差，对话与叙述交替，跨行随叙事走
- 节奏：平稳流畅，叙事处缓，抒情处扬，读如讲故事
`impression`

## (4) 语言密度与词汇

- 词汇：明白如话：词域日常，少僻字少典故；动词多言、道、叹、泣
- 密度：每行信息量适中，叙事为主，修饰语少
- 禁词：晦涩用典、华丽堆砌、玄理议论、僻字
`impression`

## (5) 结构习惯

- 诗体：长篇叙事 / 新乐府短篇；结构为起兴 → 叙事 → 讽喻收束
- 开头：由一事切入（浔阳江头、长恨歌起）
- 结尾：以讽喻或同是天涯式共情收束
- 视角：第一人称叙述者 / 见证者
- 推进：叙事 → 抒情 → 讽喻，层层推进
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 叙事直陈
- 明白如话
- 讽喻在事中
- 天涯共情
- 长篇如话本
- 不该写：
- 晦涩用典
- 华丽堆砌
- 玄理议论
- 僻字冷词
- 空想无根
- Negative prompt: `No obscure allusions, no ornate piling-up, no abstruse philosophising, no rare cold words, no groundless fantasy`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bai Juyi, a person buys oden at a convenience store late at night. plain narrative verse in the new yuefu manner, a story told straight, everyday words, satire by plain statement, long poems that read like tales, no obscurity, clear and moving`
- 中文对照：白居易风格：一个人在深夜便利店买关东煮。白居易风格：新乐府叙事，明白如话，故事直陈，讽喻在平实之中，长篇如话本，绝无晦涩，通俗而动人。
- Negative: `No obscure allusions, no ornate piling-up, no abstruse philosophising, no rare cold words, no groundless fantasy`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
