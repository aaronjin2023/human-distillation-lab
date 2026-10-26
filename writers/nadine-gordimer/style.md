# Nadine Gordimer — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nadine Gordimer: precise interior prose, white South African conscience under pressure, short scenes, moral ambiguity, the political inside the domestic`
- ZH: 戈迪默风格：精确的内心散文，重压下的白人南非良知，短场景，道德暧昧，政治藏在家庭内部。

## (2) 句式与节奏

- 内省长句与短场景切换；自由间接引语多；句式精确，少用抒情。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：郊区住宅、矿山、隔离区边界、花园、仆人、护照；日常物即政治。
- 意象：郊区住宅、矿山、隔离区边界、花园；空间即种族秩序。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：限知视角与自由间接引语；视角常贴近白人主人公的内心。
- 结构：短场景并置；开头多为家庭场景切入，结尾开放，道德问题不作结论。
- 对话：对话克制、潜台词多，人物在对话中回避与试探；独白（内心独白）与对话并置。

## (5) 语气与距离

- 冷峻、克制；同情而不宽恕。

## (6) 该写什么 / 不该写什么

- 该写：郊区住宅与花园（白人生活的体面外壳）、矿山与隔离区（被隔开的另一个南非）、护照与边境（身份与流亡）、七月的人民（秩序颠倒之后的家庭）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No slogans, no heroes, no neat moral, no exotic landscape writing`

## (7) 测试提示词示例（现代题材：一个人在机场延误一夜）

- Prompt: `In the style of Nadine Gordimer, a man spends a night delayed at an airport. Short scenes. Precise interior prose. The political inside the domestic. No slogan, no hero, no neat moral.`
- 中文对照：戈迪默风格，一个人在机场延误一夜。短场景。精确的内心散文。政治藏在家庭内部。没有口号，没有英雄，没有现成的道德结论。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
