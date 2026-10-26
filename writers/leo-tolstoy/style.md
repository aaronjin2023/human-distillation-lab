# Leo Tolstoy — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tolstoy: the whole of life in one family, history through a drawing room, free indirect thought, the search for meaning in ordinary days, no hero without doubt`
- ZH: 托尔斯泰风格：一家之中见整个人生，客厅里的历史，自由间接的思想，日常中的意义追寻，没有不怀疑的英雄。

## (2) 句式与节奏

- 句式：句长：长句为主，从句层层嵌套，思想在句中生长；短句只用在收束的断言处。
- 节奏：节奏：缓慢而辽阔——一章可写一日，一部可写十年；战争与和平、客厅与战场交替。

## (3) 词汇与意象

- 词汇：词汇：家庭、土地、战争、信仰、爱、死；爱用日常词写宏大命题。
- 意象：意象群：客厅与舞会、战场与雪、田野与收割、火车与死亡、家庭与餐桌。
- 禁词/禁意象：禁词/禁意象：不写快节奏的情节，不用廉价的激情，不写单一的讽刺。

## (4) 叙事视角与结构

- 视角：叙事视角：全知而深入的第三人称，自由间接引语让叙述滑入人物内心；视角在人物之间流动，读者须不断调整站位。
- 结构：结构：多线并行，家庭与历史交织；开头多为一句断言或一个场景，结尾以哲理收束（《战争与和平》的尾声）。

## (5) 语气与距离

- 语气：语气：庄重、悲悯而追问；与人物的距离如导师——爱他们，也审判他们。

## (6) 该写什么 / 不该写什么

- 该写：该写：家庭与历史、自由间接思想、日常中的意义、怀疑的英雄。
- 不该写：不该写：快节奏情节、廉价激情、单一讽刺。
- Negative prompt: `No fast-paced plot, no cheap passion, no one-sided satire, no flat heroism`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Tolstoy, a small Yorkshire terrier sits on a subway seat, and the whole of life passes in one carriage. Free indirect thought. History through an ordinary day. No hero without doubt.`
- 中文对照：托尔斯泰风格，一只小约克夏犬坐在地铁座位上，整个人生在一节车厢里经过。自由间接的思想，日常中的历史，没有不怀疑的英雄。
- Negative: `fast-paced plot, cheap passion, one-sided satire, flat heroism`
- 检验点：写出的文本是否一读即是该作家的声音，而不是通用散文；禁区是否出现（见第 (6) 节）。
