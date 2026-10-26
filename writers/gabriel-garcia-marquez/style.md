# Gabriel García Márquez — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gabriel García Márquez: long looping sentences, magical events told as fact, Macondo as the world, solitude and circular time, the epic of one family`
- ZH: 马尔克斯风格：绵长的循环长句，魔幻事件当作事实来讲，马孔多即世界，孤独与循环的时间，一个家族的史诗。

## (2) 句式与节奏

- 长句绵延，时间跳跃；从句层层嵌套；一句可写尽数代人。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：冰、黄色蝴蝶、马孔多、雨、香蕉、家族、预言；日常词与魔幻词同句出现。
- 意象：冰、黄色蝴蝶、马孔多、连绵的雨、飞升的美人；魔幻即日常。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：全知视角，祖母讲故事的口吻；预言式开头（多年以后……）。
- 结构：家族编年，时间循环；开头多为预言式倒叙，结尾常以预言应验收束。
- 对话：对话口语化、夸张，人物在闲谈中说出魔幻之事；独白（全知叙述者的评述）与对话交替。

## (5) 语气与距离

- 庄重、幽默；既史诗又家常。

## (6) 该写什么 / 不该写什么

- 该写：冰（童年与现代性的入口）、黄色蝴蝶（爱情与死亡的信使）、马孔多（虚构小镇即世界）、孤独（家族七代的共同命运）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No realism, no irony, no short clipped prose, no explanation of the magic`

## (7) 测试提示词示例（现代题材：一个外卖骑手深夜穿过城市送餐）

- Prompt: `In the style of Gabriel García Márquez, a delivery rider crosses the city late at night. Long looping sentences. Magical events told as fact. Yellow butterflies follow him. Time is circular.`
- 中文对照：马尔克斯风格，一个外卖骑手深夜穿过城市送餐。绵长的循环长句。魔幻事件当作事实来讲。黄色蝴蝶跟着他。时间是循环的。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
