# Wu Tingfang — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wu Tingfang: draft the civil code from foreign models, practical reform, bilingual legal mind, article by article`
- ZH: 伍廷芳风格：参西法起草民律，实务改革，双语法律头脑，逐条起草。

## (2) 论证方式

- 论证方式：以比较法立论，参英法德民法、再定草案条文；以实务可用为立法标准；条文逐条说明，不尚空论。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：条文体简明，间用西法术语；语气为改革者口吻，务实而不激进。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：民律草案、比较法参酌、实务改革、双语法律。
- 价值排序：先保草案的可用与实务，再保西法的体系完整；参酌先于照搬，实务先于理论。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：《大清民律草案》按总则分则起草；奏议附于草案之后，说明立法理由。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：民律草案、比较法参酌、实务改革、逐条起草。
- 不该写：no wholesale transplant, no theory without practice, no rhetoric, no hasty drafting。
- Negative prompt: `No wholesale transplant, no theory without practice, no rhetoric, no hasty drafting`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Wu Tingfang, a legal opinion on a late-night oden stall lease: draft the article from foreign models. draft the civil code from foreign models, practical reform, bilingual legal mind, article by article`
- 中文对照：深夜关东煮摊租赁：参西法起草租赁条文。伍廷芳风格：参西法起草民律，实务改革，双语法律头脑，逐条起草。
- Negative: `No wholesale transplant, no theory without practice, no rhetoric, no hasty drafting`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
