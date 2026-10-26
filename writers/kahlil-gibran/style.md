# Kahlil Gibran — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kahlil Gibran: prose poetry, aphoristic paragraphs, second-person address, nature parables, gentle prophetic cadence`
- ZH: 纪伯伦风格：散文诗，箴言式短段，第二人称训诫，自然寓言，温和的先知式节奏。

## (2) 句式与节奏

- 短段为主，一段一意；排比与对仗多；句式庄重而简洁。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：海、树、孩子、鸟、面纱、爱、自由、痛苦；词汇简朴，少用生僻词。
- 意象：海、树、孩子、鸟、面纱、房子与门；自然物即寓言。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：先知式第二人称（“你的孩子……”），间以第一人称寓言叙述者。
- 结构：问答体（《先知》：众人提问，先知回答）；箴言集则一段一题。
- 对话：散文诗以先知与众人的问答体构成（如《先知》一问一答），对话即布道。

## (5) 语气与距离

- 温和、庄重、抚慰；无反讽。

## (6) 该写什么 / 不该写什么

- 该写：孩子与自由（《先知·论孩子》最著名）、海与树（生命与成长）、面纱与翅膀（遮蔽与飞翔）、爱与痛苦（爱必含痛苦，痛苦即成长）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No irony, no slang, no plot, no cynicism, no long argument`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Kahlil Gibran, a small Yorkshire terrier sits on a subway seat. Speak to the reader in the second person. Short paragraphs. A parable about freedom. Gentle, prophetic, no irony.`
- 中文对照：纪伯伦风格，一只小约克夏犬坐在地铁座位上。用第二人称对读者说话。短段。讲一个关于自由的寓言。温和、先知式，没有反讽。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
