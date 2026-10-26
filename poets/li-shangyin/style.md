# Li Shangyin — 诗歌风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Shangyin: dense late-Tang verse, untitled poems, brocade zither and spring silkworms, allusion upon allusion, beauty that refuses explanation, no plain statement, exquisite and obscure`
- ZH: 李商隐风格：晚唐密丽，无题诗，锦瑟春蚕，典故层层，美而不解，绝无直言，绮丽而晦涩。

## (2) 意象

- 主意象：锦瑟、春蚕、蜡炬、巴山夜雨、碧海青天
- 辅意象：庄生晓梦、望帝春心、沧海月明
- 禁意象：直白陈述、平淡田园、豪放壮语
- 密度：极高密度：典故层层，一句多典，意象绵密
- 来源：典故、神话、爱情、咏史
`impression`

## (3) 韵律与句式

- 韵律：七言律绝为主，对仗极工，平仄精严，押韵绵密
- 句式：句式绵密，对仗极工，倒装顿挫，跨行少，句句着力
- 节奏：缓慢绵密，呼吸深长，顿挫在典故转换处
`impression`

## (4) 语言密度与词汇

- 词汇：绮丽词域：锦瑟、春蚕、蜡炬、沧海；动词多托、寄、忆、望；少口语
- 密度：每行信息量极高，一句多典，修饰语占比高
- 禁词：直白陈述、平淡田园、豪放壮语、口语俗词
`impression`

## (5) 结构习惯

- 诗体：七言律绝 / 无题组诗；结构为密典起兴 → 层层铺写 → 惘然收束
- 开头：以密典直入（锦瑟无端五十弦）
- 结尾：以惘然收束（只是当时已惘然），不解不答
- 视角：第一人称惘然者
- 推进：密典 → 再密典 → 惘然，层层加深
`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 无题诗
- 锦瑟春蚕
- 典故层层
- 绮丽绵密
- 惘然收束
- 不该写：
- 直白陈述
- 平淡田园
- 豪放壮语
- 口语俗词
- 直白议论
- Negative prompt: `No plain statement, no flat pastoral, no grand heroic diction, no colloquial diction, no direct preaching`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Shangyin, a letter to oneself ten years from now. dense late-Tang verse, untitled poems, brocade zither and spring silkworms, allusion upon allusion, beauty that refuses explanation, no plain statement, exquisite and obscure`
- 中文对照：李商隐风格：一封写给十年后自己的信。李商隐风格：晚唐密丽，无题诗，锦瑟春蚕，典故层层，美而不解，绝无直言，绮丽而晦涩。
- Negative: `No plain statement, no flat pastoral, no grand heroic diction, no colloquial diction, no direct preaching`
- 检验点：意象、韵律、结构、收束是否符合第 (2)–(6) 节；禁区写法是否出现。
