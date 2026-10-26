# Mark Twain — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mark Twain: vernacular American voice, deadpan humour, the river as freedom, episodic picaresque, irony aimed at respectability`
- ZH: 马克·吐温风格：美国口语，冷面幽默，河流即自由，插曲式流浪汉小说，反讽对准体面人。

## (2) 句式与节奏

- 口语化短句与长句交错；方言拼写；反讽句作收束。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：密西西比河、木筏、小镇、体面人、骗子；口语与方言词汇密集。
- 意象：密西西比河、木筏、小镇、洞穴；河流即自由。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称少年（哈克）与全知视角交替；《汤姆·索亚》为第三人称。
- 结构：插曲式：一段一冒险，串珠而成；开头多为小镇场景切入，结尾常以反讽收束。
- 对话：方言对话是风格本体，人物说什么、怎么说即人物是谁；独白（哈克的内心独白）与对话交替。

## (5) 语气与距离

- 幽默、讽刺；既亲切又刻薄。

## (6) 该写什么 / 不该写什么

- 该写：密西西比河（自由与逃亡）、木筏（漂流的家）、小镇（体面社会的缩影）、骗子与体面人（美国的两种面孔）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No high diction, no sentimentality, no solemn moralising, no purple prose`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Mark Twain, a small Yorkshire terrier sits on a subway seat. Vernacular American voice. Deadpan humour. The river is now a subway line. Irony aimed at respectable people.`
- 中文对照：马克·吐温风格，一只小约克夏犬坐在地铁座位上。美国口语。冷面幽默。河流如今是一条地铁线。反讽对准体面人。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
