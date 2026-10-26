# Julio Cortázar — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Julio Cortázar: playful structural games, the reader as co-author, jazz rhythm, Buenos Aires and Paris, the fantastic erupting into the everyday`
- ZH: 科塔萨尔风格：游戏般的结构实验，读者即合著者，爵士节奏，布宜诺斯艾利斯与巴黎，奇幻闯入日常。

## (2) 句式与节奏

- 爵士节奏，句式跳跃；括号与破折号多；长句与短句交错如即兴演奏。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：跳房子、走廊、镜子、爵士、巴黎、布宜诺斯艾利斯；日常词与游戏词并置。
- 意象：跳房子、走廊、镜子、爵士、通道；日常空间突然变成入口。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：多视角，第一、第二、第三人称实验；读者被直接点名。
- 结构：可跳读结构（《跳房子》两种读法）；短篇以日常切入、奇幻收束。
- 对话：对话跳跃、游戏化，常被叙述者打断与重组；独白与对话界限模糊。

## (5) 语气与距离

- 游戏、轻盈；既严肃又顽皮。

## (6) 该写什么 / 不该写什么

- 该写：跳房子（游戏即结构）、走廊与通道（现实之间的缝隙）、爵士（即兴与自由）、克罗诺皮奥与法玛（两种生存方式的寓言）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No linear plot, no explanation of the fantastic, no solemn realism, no single authoritative voice`

## (7) 测试提示词示例（现代题材：手机没电的一天）

- Prompt: `In the style of Julio Cortázar, a day without a charged phone. Jazz rhythm. The reader is invited to jump chapters. The fantastic erupts into the everyday. No explanation.`
- 中文对照：科塔萨尔风格，手机没电的一天。爵士节奏。邀请读者跳章阅读。奇幻闯入日常。不作解释。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
