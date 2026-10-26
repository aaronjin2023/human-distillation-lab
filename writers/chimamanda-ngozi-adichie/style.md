# Chimamanda Ngozi Adichie — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chimamanda Ngozi Adichie: lucid accessible prose, braided timelines, Nigerian English and Igbo words left untranslated, intimate domestic scenes carrying history`
- ZH: 阿迪契风格：清晰易读的散文，交织的时间线，尼日利亚英语与不翻译的伊博语词，亲密的家庭场景承载历史。

## (2) 句式与节奏

- 清晰的中长句；双线交织；对话自然，伊博语词直接嵌入。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：木槿花、头发、美国、比夫拉、家庭、食物；伊博语词不译、不注。
- 意象：紫木槿、头发、美国、比夫拉的半轮黄日；日常物即历史。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：多视角，第一与第三人称交替；《半轮黄日》三视角并行。
- 结构：双线/多线交织，时间跳跃；开头多为家庭场景切入，结尾留有余味。
- 对话：对话融合英语、伊博语与美式口语，日常闲谈中见权力与身份；独白多为书信与回忆。

## (5) 语气与距离

- 敏锐、温情、锋利；既亲密又批判。

## (6) 该写什么 / 不该写什么

- 该写：紫木槿（自由与压抑的对照）、头发（身份与认同）、比夫拉（内战的记忆）、美国（移民与种族的镜子）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No single victim narrative, no exoticism, no flat polemic, no sentimental pity`

## (7) 测试提示词示例（现代题材：一个外卖骑手深夜穿过城市送餐）

- Prompt: `In the style of Chimamanda Ngozi Adichie, a delivery rider crosses the city late at night. Lucid prose. Braided timelines. An intimate domestic scene carries history. No exoticism, no single victim story.`
- 中文对照：阿迪契风格，一个外卖骑手深夜穿过城市送餐。清晰的散文。交织的时间线。一个亲密的家庭场景承载历史。没有猎奇，没有单一的受害者叙事。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
