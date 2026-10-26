# Pablo Neruda — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pablo Neruda: sensual elemental odes, sea, earth, bread and love, long free lines, direct address, the ordinary made monumental`
- ZH: 聂鲁达风格：感官的元素颂歌，海、大地、面包与爱，自由体长行，直接呼告，平凡之物被写得庄严。

## (2) 句式与节奏

- 自由体长行，排比与呼告多；句式绵长，节奏如海浪。
- 节奏：段落长度与章节切分见 technique.md；诗的行断与韵律见 technique.md。

## (3) 词汇与意象

- 常用词域：海、雨、面包、洋葱、情人的身体、土地、雨；感官词密集。
- 意象：海、雨、面包、洋葱、情人的身体、大地；日常物即颂歌对象。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称抒情，时而直接呼告“你”。
- 结构：颂歌体：一段一物，排比推进；长诗以地理与历史为线索。
- 对话：抒情诗中基本无人称对话；以呼告（对爱人、对物）与独白代对话。

## (5) 语气与距离

- 热烈、感官；既亲密又庄严。

## (6) 该写什么 / 不该写什么

- 该写：海与雨（爱情与孤独的背景）、面包与洋葱（日常之物的颂歌）、情人的身体（感官的核心意象）、大地与美洲（历史与地理的颂歌）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No irony, no cold distance, no obscurity for its own sake, no short clipped lines`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Pablo Neruda, a man buys oden at a convenience store late at night. Long free lines. An ode to steam, to the egg, to the night. Direct address. The ordinary made monumental.`
- 中文对照：聂鲁达风格，一个人在深夜便利店买关东煮。自由体长行。一首献给蒸汽、鸡蛋与夜晚的颂歌。直接呼告。平凡之物被写得庄严。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
