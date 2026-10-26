# Xu Zhimo — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xu Zhimo: Crescent School verse, light and musical lines, clouds and rainbows over the Cam, a gentle farewell, romantic and airy, no heaviness, graceful and fleeting`
- ZH: 徐志摩风格：新月派，轻灵音乐，康河云彩与彩虹，轻轻的别离，浪漫而空灵，绝无沉重，潇洒而倏忽。

## (2) 意象

- 主意象：康桥、云彩、彩虹、金柳、雪花
- 辅意象：偶然、轻轻的、波心、星辉
- 禁意象：沉重议论、直白说教、口语俗词
- 密度：疏朗：意象轻灵，一景一意，音乐感强
- 来源：康桥实景、爱情、自然
`impression`

## (3) 韵律与句式

- 韵律：新月格律：句式整齐，押韵音乐化，行断讲究
- 句式：短句轻灵，长短交错，跨行随音乐走
- 节奏：轻快流畅，呼吸均匀，音乐感强
`impression`

## (4) 语言密度与词汇

- 词汇：轻灵词域：轻轻的、云彩、彩虹、星辉；动词多别、恋、飞、飘；少沉重词
- 密度：每行信息量低，一景一句，修饰语轻灵
- 禁词：沉重议论、直白说教、口语俗词、豪放壮语
`impression`

## (5) 结构习惯

- 诗体：抒情短诗 / 组诗；结构为写景 → 生情 → 轻轻收束
- 开头：以轻灵之景直入（轻轻的我走了）
- 结尾：以轻轻收束，不留沉重
- 视角：第一人称浪漫者
- 推进：景 → 情 → 别，层层轻出
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 康桥云彩
- 轻轻的别离
- 音乐化行断
- 轻灵意象
- 浪漫收束
- 不该写：
- 沉重议论
- 直白说教
- 口语俗词
- 豪放壮语
- 铺张排比
- Negative prompt: `No heavy argument, no direct preaching, no colloquial diction, no grand heroic diction, no lavish parallelism`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xu Zhimo, a person buys oden at a convenience store late at night. Crescent School verse, light and musical lines, clouds and rainbows over the Cam, a gentle farewell, romantic and airy, no heaviness, graceful and fleeting`
- 中文对照：徐志摩风格：一个人在深夜便利店买关东煮。徐志摩风格：新月派，轻灵音乐，康河云彩与彩虹，轻轻的别离，浪漫而空灵，绝无沉重，潇洒而倏忽。
- Negative: `No heavy argument, no direct preaching, no colloquial diction, no grand heroic diction, no lavish parallelism`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
