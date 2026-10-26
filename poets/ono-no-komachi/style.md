# Ono no Komachi — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ono no Komachi: Heian waka, the colour of flowers fading in vain, a woman's love held in five-seven-five-seven-seven, longing without end, no excess, exquisite and fleeting`
- ZH: 小野小町风格：平安和歌，花之色空移，女子之恋在五七五七七中，思而不尽，绝无铺张，精致而倏忽。

## (2) 意象

- 主意象：花之色、长夜、梦、泪
- 辅意象：月、雨、衣、袖
- 禁意象：豪放壮语、铺张排比、直白议论
- 密度：疏朗：意象小而精，一首一意，留白极大
- 来源：宫廷风物、四季、恋歌
`impression`

## (3) 韵律与句式

- 韵律：和歌（五七五七七），音数精严，挂词见长
- 句式：短句为主，五七调滚动，挂词与缘语并用
- 节奏：缓慢而倏忽，呼吸均匀，顿挫在挂词处
`impression`

## (4) 语言密度与词汇

- 词汇：精致词域：花、色、梦、泪；动词多思、恋、泣、望；少华丽词
- 密度：每行信息量低，一首一意，留白极大
- 禁词：豪放壮语、铺张排比、直白议论、口语俗词
`impression`

## (5) 结构习惯

- 诗体：和歌（五七五七七）；结构为花色起兴 → 恋思铺写 → 倏忽收束
- 开头：以花色直入（花の色はうつりにけりな）
- 结尾：以 倏忽收束，不解释
- 视角：第一人称女子歌者
- 推进：花色 → 恋思 → 收束，层层见倏忽
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 花之色
- 五七五七七
- 挂词缘语
- 女子恋歌
- 倏忽收束
- 不该写：
- 豪放壮语
- 铺张排比
- 直白议论
- 口语俗词
- 解释说明
- Negative prompt: `No grand heroic diction, no lavish parallelism, no direct preaching, no colloquial diction, no explanation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ono no Komachi, a person buys oden at a convenience store late at night. Heian waka, the colour of flowers fading in vain, a woman's love held in five-seven-five-seven-seven, longing without end, no excess, exquisite and fleeting`
- 中文对照：小野小町风格：一个人在深夜便利店买关东煮。小野小町风格：平安和歌，花之色空移，女子之恋在五七五七七中，思而不尽，绝无铺张，精致而倏忽。
- Negative: `No grand heroic diction, no lavish parallelism, no direct preaching, no colloquial diction, no explanation`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
