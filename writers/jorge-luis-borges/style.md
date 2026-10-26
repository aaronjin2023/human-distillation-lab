# Jorge Luis Borges — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jorge Luis Borges: erudite playful essays disguised as stories, labyrinths, mirrors, doubles and infinite libraries, precise sentences, false footnotes, metaphysical detective plots`
- ZH: 博尔赫斯风格：伪装成小说的博学随笔，迷宫、镜子、分身与无限图书馆，精确的句子，伪注脚，形而上的侦探情节。

## (2) 句式与节奏

- 精确短句与长从句交错；伪注脚、引文、书目体；句式冷静而博学。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：迷宫、镜子、图书馆、老虎、刀、时间、无限；典故横跨东西古今。
- 意象：迷宫、镜子、图书馆、老虎、刀、分身；意象即哲学命题。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：第一人称博学者，时而不可靠叙述者；偶用第三人称。
- 结构：短篇为主，伪论文、伪书评、侦探结构；开头多为引文或书目切入，结尾翻转。
- 对话：小说以对话与议论推进，人物对答多为哲学辩论；独白（叙述者的博学独白）常压倒对话。

## (5) 语气与距离

- 博学、游戏、冷静；既严肃又顽皮。

## (6) 该写什么 / 不该写什么

- 该写：迷宫（时间、空间与文本的迷宫）、镜子与分身（自我复制的恐惧与游戏）、图书馆（无限的书与无限的时间）、老虎与刀（暴力与美的短暂意象）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No realism, no sentimentality, no long psychological portrait, no plot for its own sake`

## (7) 测试提示词示例（现代题材：一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Jorge Luis Borges, a small Yorkshire terrier sits on a subway seat. A labyrinth of mirrors. A false footnote. The dog may be a double. Precise sentences. No sentimentality.`
- 中文对照：博尔赫斯风格，一只小约克夏犬坐在地铁座位上。镜子的迷宫。一条伪注脚。这只狗可能是一个分身。精确的句子。没有感伤。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
