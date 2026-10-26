# Mario Vargas Llosa — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mario Vargas Llosa: shifting narrators and times, dialogue-driven scenes, power and desire, precise psychological realism, the novel as a total world`
- ZH: 巴尔加斯·略萨风格：轮换的叙述者与时间，对话驱动的场景，权力与欲望，精确的心理现实主义，小说即一个完整的世界。

## (2) 句式与节奏

- 对话密集，时空跳切；长句与对话短句交错；节奏快而密。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：军校、酒吧、利马街头、权力、欲望、谎言；词汇精确，少用抒情。
- 意象：军校、酒吧、利马街头、对话中的权力；空间即权力结构。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：多视角，时空跳切；同一事件多角度重述。
- 结构：多线交织、时空跳切；开头多为对话场景切入，结尾常以对话收束。
- 对话：对话即权力，人物在对话中暴露与伪装；多声部对话并行，叙述者退后。

## (5) 语气与距离

- 冷峻、犀利；既现实又思辨。

## (6) 该写什么 / 不该写什么

- 该写：军校（权力的微缩模型）、酒吧与对话（真相的场所）、利马（阶层与欲望的城市）、谎言与真相（叙述的永恒辩题）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No magic, no lyricism for its own sake, no single voice, no sentimental ending`

## (7) 测试提示词示例（现代题材：一个人在机场延误一夜）

- Prompt: `In the style of Mario Vargas Llosa, a man spends a night delayed at an airport. Dialogue-driven scenes. Shifting narrators and times. Power and desire in every conversation. No magic.`
- 中文对照：巴尔加斯·略萨风格，一个人在机场延误一夜。对话驱动的场景。轮换的叙述者与时间。每段对话里都有权力与欲望。没有魔幻。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
