# Chinua Achebe — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chinua Achebe: clear plain English carrying Igbo proverbs and speech rhythms, village scenes in present detail, irony without bitterness, the storyteller's calm authority`
- ZH: 阿切贝风格：清晰平实的英语承载伊博谚语与口语节奏，村落场景写实现场感，反讽而不苦涩，讲故事人的沉稳权威。

## (2) 句式与节奏

- 平实的中长句；谚语作点睛短句；对话带口语节奏。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：村落、山药、面具、祭祀、殖民官员、学校；伊博谚语与英语直译的意象。
- 意象：村落、山药、面具、殖民者到来、河流；日常物即文化。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：全知视角，贴近村落视角；偶用第一人称。
- 结构：线性叙事为主，村落编年；开头多为日常场景切入，结尾常以殖民者的视角反照。
- 对话：以伊博口语与谚语入对话，人物对话即部族议事；独白少，集体议论多。

## (5) 语气与距离

- 冷静、尊严；反讽而不煽情。

## (6) 该写什么 / 不该写什么

- 该写：村落与殖民者的相遇（核心母题）、山药与土地（男子气概与生计）、面具与祭祀（传统秩序的仪式）、谚语（智慧的载体）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No exoticism, no sentimental pity, no colonial gaze, no purple prose`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Chinua Achebe, a man buys oden at a convenience store late at night. Plain sentences. A proverb closes the scene. The old world and the new stand in the same room. No pity, no exoticism.`
- 中文对照：阿切贝风格，一个人在深夜便利店买关东煮。平实的句子。一句谚语收束场景。旧世界与新世界站在同一间屋里。没有怜悯，没有猎奇。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
