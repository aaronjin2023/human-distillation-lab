# James Dean — 表演风格规格 style.md（给视频模型）

> 只描述表演，不描述人生。引用台词时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Dean: restless Method youth, mumbled lines that break and restart, hunched shoulders, sudden bursts of anger and tenderness, a boy who cannot sit still`
- ZH: 詹姆斯·迪恩风格：不安的方法派青年，台词含混、断了又续，耸肩驼背，愤怒与温柔突然爆发，一个坐不住的少年。

## (2) 形体

- 耸肩、驼背、双手插兜；走路踢踢踏踏、突然停下；坐姿蜷缩、常蹲在地上；爆发时全身弹起，温柔时突然静止。`impression`

## (3) 台词

- 含混低语、句子断了又续、重复开头；语速忽快忽慢；哭腔与怒吼只在顶点出现。`impression`

## (4) 表情与眼神

- 眼神游移、突然直视；眉头紧锁、嘴角下撇；笑是短暂的、带点羞涩的。`impression`

## (5) 角色类型

- 常演角色：叛逆青年（吉姆、卡尔）；被父亲误解的儿子（《伊甸之东》）；野心勃勃的穷小子（《巨人》杰特）。
- 类型突破：三部主演即全部代表作：从《伊甸之东》的求爱到《巨人》的野心，24 岁去世使风格定格为“永恒的青年”。`artifact`
- 禁演类型：几乎不演成熟稳重的中年人、不演字正腔圆的正剧、不演讨好观众的英雄。`impression`

## (6) 该演什么 / 不该演什么

- 该演：含混断续的台词、耸肩驼背的形体、突然的爆发与温柔、蜷缩的坐姿、游移又直视的眼神。
- 不该演：字正腔圆的舞台腔、成熟稳重的中年人、讨好观众的英雄气、解释性独白。
- Negative prompt: `No theatrical declamation, no settled middle-aged authority, no crowd-pleasing heroics, no explanatory monologue`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of James Dean, a food delivery rider waits for an order on a rainy night, hunched shoulders, hands in pockets, mumbled lines that break and restart, sudden tenderness`
- 中文对照：詹姆斯·迪恩风格：一位外卖骑手在雨夜等单，耸肩驼背，双手插兜，台词含混、断了又续，突然的温柔。
- Negative: `No theatrical declamation, no settled middle-aged authority, no crowd-pleasing heroics, no explanatory monologue`
- 检验点：形体、台词、表情三项是否同时成立；风格迁移后是否仍可辨认出是此人。
