# Ferdowsi — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ferdowsi: stately epic couplets, heroic deeds, kings and fate, plain Persian diction, moral reflection between battles`
- ZH: 菲尔多西风格：庄严的史诗对句，英雄事迹、君王与命运，质朴的波斯语，战斗之间的道德沉思。

## (2) 句式与节奏

- 对句（联句）为基本单位，句式工整、庄重；套语与重复句式多，节奏如行军。
- 节奏：段落长度与章节切分见 technique.md；诗的行断与韵律见 technique.md。

## (3) 词汇与意象

- 常用词域：王冠、宝剑、战马、王座、命运、荣誉；语言质朴，少用阿拉伯语借词（有意为之）。`artifact`
- 意象：王冠与宝剑、战马、七重考验、父子相残（鲁斯坦与苏赫拉布）；意象来自神话与王朝谱系。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：全知史诗叙述者，偶以道德感慨插入。
- 结构：王朝谱系结构：神话时代—英雄时代—历史时代；每王一传，故事联缀。
- 对话：史诗以人物对话（君王、英雄的誓言与辩论）推进情节，对话庄重、格言化。

## (5) 语气与距离

- 庄严、悲怆；对英雄既赞美又哀悼。

## (6) 该写什么 / 不该写什么

- 该写：鲁斯坦（最伟大的英雄，七试、误杀亲子苏赫拉布）、王权与命运（得之则兴，失之则亡）、善恶之争（光明与黑暗、伊朗与图兰的对立）、父子、君臣的悲剧（英雄常死于亲人之手）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No colloquial slang, no irony, no fragmented modernism, no private lyricism, no short clipped prose`

## (7) 测试提示词示例（现代题材：一个外卖骑手深夜送餐穿越城市）

- Prompt: `In the style of Ferdowsi, a delivery rider crosses the city late at night, as a hero crosses a desert. Long stately couplets. His scooter is his horse. Fate watches from above. No irony.`
- 中文对照：菲尔多西风格，一个外卖骑手深夜穿越城市送餐，如英雄穿越沙漠。庄严的长对句。电动车是他的战马。命运在上俯瞰。没有反讽。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
