# Orhan Pamuk — 写作风格规格 style.md（给文本模型）

> 只描述文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Orhan Pamuk: melancholic Istanbul, layered first-person and shifting narrators, East-West mirrors, objects that remember, long sentences with parentheses`
- ZH: 帕慕克风格：忧郁的伊斯坦布尔，多层第一人称与轮换叙述者，东西之镜，会记忆的物件，带括号的长句。

## (2) 句式与节奏

- 长句为主，括号插入多；细节铺陈，节奏缓慢而绵密。
- 节奏：段落长度与章节切分见 technique.md。

## (3) 词汇与意象

- 常用词域：伊斯坦布尔、忧郁（huzun）、细密画、雪、博物馆、物件、镜子；土耳其语与西方词汇并置。
- 意象：伊斯坦布尔废墟之美、细密画、雪、博物馆里的旧物、东西交界的桥。
- 禁词 / 禁意象：见第 (6) 节 Negative prompt。

## (4) 叙事视角与结构

- 视角：多声部：第一人称轮换叙述（《我的名字叫红》连死者、狗、颜色都开口说话）。`impression`
- 结构：多视角拼贴、双线并行；开头多为物件或场景切入，结尾开放。
- 对话：对话与独白交织，人物常以长段自白辩论；东西方的争论借人物之口展开。

## (5) 语气与距离

- 忧郁、博学；与读者如博物馆导览般细说。

## (6) 该写什么 / 不该写什么

- 该写：伊斯坦布尔（废墟之美、东西交界）、细密画与东西之争（《我的名字叫红》的核心）、雪（封闭小城中的政治与爱情）、博物馆与旧物（记忆的容器）。
- 不该写：风格上的禁区，见 Negative prompt。
- Negative prompt: `No brisk plot, no flat reportage, no single authoritative voice, no short clipped prose`

## (7) 测试提示词示例（现代题材：一个人在机场延误一夜）

- Prompt: `In the style of Orhan Pamuk, a man spends a night delayed at an airport. Long sentences with parentheses. Objects remember things. East and West mirror each other. Melancholy, unhurried.`
- 中文对照：帕慕克风格，一个人在机场延误一夜。带括号的长句。物件会记忆。东方与西方互为镜像。忧郁，不匆忙。
- Negative: 见第 (6) 节。
- 检验点：换了现代题材后，句式、意象、语气是否还是此人；若变成通用散文，即未通过。
