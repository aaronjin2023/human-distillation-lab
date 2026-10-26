# Edgar Allan Poe — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edgar Allan Poe: musical incantation, repetition and refrain, dread and beauty, the single effect, rooms, bells and ravens`
- ZH: 坡风格：音乐般的咒语，重复与叠句，恐怖与美，单一效果，房间、钟与乌鸦。

## (2) 句式与节奏

- 音乐性长句，重复与叠句多；节奏如钟声，渐强至高潮。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：乌鸦、钟、古宅、深夜、美、死亡；词汇华美而阴郁。
- 意象：乌鸦、钟、古宅、深夜、美人之死；意象高度重复。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称偏执叙述者；偶用第三人称。
- 结构：单一效果结构：全篇服务于一个情绪高潮；开头即定调，结尾收束于一声叠句。
- 对话：小说对话多为独白式倾诉（叙述者对读者的自白），人物对答短促、服务于悬念。

## (5) 语气与距离

- 阴郁、迷人；既恐怖又美丽。

## (6) 该写什么 / 不该写什么

- 该写：乌鸦（不祥的信使与叠句）、钟（时间的音乐）、古宅（家族与精神的废墟）、美人之死（美与恐怖的合一）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No daylight realism, no humour, no loose structure, no plain prose`

## (7) 测试提示词示例（现代题材：一封写给十年后自己的信）

- Prompt: `In the style of Edgar Allan Poe, a letter to yourself ten years from now. Musical repetition. A refrain returns. Dread and beauty in the same room. One single effect.`
- 中文对照：坡风格，一封写给十年后自己的信。音乐般的重复。一句叠句反复回来。恐怖与美在同一间屋里。只有一个效果。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
