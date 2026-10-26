# Ernest Hemingway — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ernest Hemingway: short declarative sentences, sparse adjectives, concrete nouns, understated emotion, dialogue-driven, iceberg theory, no ornament`
- ZH: 海明威风格：短促的陈述句，形容词稀少，具体的名词，克制的情感，对话驱动，冰山理论，没有装饰。

## (2) 句式与节奏

- 短句、电报体；并列句多，从句少；对话短促，留白多。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：海、雪、酒、斗牛、枪、雨、鱼；具体名词，形容词稀少。
- 意象：海、雪、酒、斗牛、枪、雨；具体物即情感。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第三人称限知为主，间用第一人称；视角贴近人物行动。
- 结构：场景并置，省略过渡；开头多为场景切入，结尾戛然而止。
- 对话：对话即全部，叙述退后；人物只说事实与短句，潜台词在停顿里，独白几乎不用。

## (5) 语气与距离

- 冷峻、克制；情感藏在水面之下。

## (6) 该写什么 / 不该写什么

- 该写：海与鱼（孤独的搏斗）、雪与雨（洁净与寒冷）、酒与斗牛（仪式与勇气）、战争（创伤与克制）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No ornate adjectives, no long explanatory passages, no sentimental happy ending, no direct moralising`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Ernest Hemingway, a man buys oden at a convenience store late at night in a modern city. Short declarative sentences. Concrete nouns. Dialogue only. No adjectives. The cold outside, the steam inside. Nothing explained.`
- 中文对照：海明威风格，一个人在深夜便利店买关东煮。短促的陈述句。具体的名词。只有对话。没有形容词。外面冷，里面有蒸汽。什么都不解释。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
