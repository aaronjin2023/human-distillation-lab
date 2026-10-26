# Langston Hughes — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Langston Hughes: blues and jazz as metre, the dream deferred, I too sing America, plain speech with swing, the river deep as the soul, Harlem night as home`
- ZH: 休斯风格：蓝调与爵士即格律，梦想被推迟，我也歌唱美国，平实的语言带摇摆，河流深如灵魂，哈莱姆之夜即家园。

## (2) 意象

- 河流（《黑人谈河流》：灵魂深如河）
- 蓝调与爵士（节奏即意义）
- 梦想（被推迟的梦）
- 哈莱姆之夜（家园）
- 火车与夜（流浪与归来）
- 禁意象：欧洲的典雅、抽象的大词、温情的安慰
- 密度：见上，意象密度与来源按各条写明，不编造词频数字。

## (3) 韵律与句式

- 蓝调与爵士节奏：以布鲁斯的十二小节与爵士的即兴为格律，短行、重复、呼应；《疲倦的布鲁斯》以歌词体推进；《蒙太奇》以蒙太奇跳接；整体节奏由歌谣的摇摆向蒙太奇的跳接演变。

## (4) 语言密度与词汇

- 词汇：日常口语词极准（河、梦、夜、火车），蓝调词（疲倦、摇摆）与爵士词并置；抽象词（梦想、自由）借河流落地；禁词：欧洲典雅词、抽象大词、温和安慰语。

## (5) 结构习惯

- 歌词体：以一曲（蓝调、爵士）起兴，重复—变奏—收束；《蒙太奇》以短章跳接，场景并置；单篇多以一景（河、夜）起兴，结尾多为梦想的追问而非收束。

## (6) 该写什么 / 不该写什么

- 该写：
- 蓝调与爵士的节奏
- 河流、梦想、哈莱姆的意象
- 平实口语的摇摆
- 梦想的追问收束
- 不该写：
- 欧洲典雅与抽象大词
- 温和安慰
- 直白说教
- 冗长铺陈
- Negative prompt: `No European elegance, no grand abstract words, no mild consolation, no direct preaching, no long explanatory passages, no verse without swing`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Langston Hughes, a small Yorkshire terrier sits on a subway seat at night. Blues and jazz as metre, the river deep as the soul, I too sing the subway, the dream deferred among commuters, plain speech with swing.`
- 中文对照：休斯风格：一只约克夏犬深夜坐在地铁座位上。蓝调与爵士即格律，河流深如灵魂，我也歌唱地铁，梦想在乘客中被推迟，平实的语言带摇摆。
- Negative: `No European elegance, no grand abstractions, no mild consolation, no preaching, no long passages, no verse without swing`
- 检验点：意象、韵律与收束是否按上文成立；Negative prompt 的禁区是否被守住。
