# Xiao He — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Xiao He: nine chapters of law, take the Qin law and cut the harsh, order first, concise articles for a new dynasty`
- ZH: 萧何风格：九章律，取秦律而去其苛，秩序为先，条文简明，为新朝立法。

## (2) 论证方式

- 论证方式：以九章立论，取秦律之体、去其苛刑；以秩序为立法理由，不作理论辩护；条文按盗、贼、囚、捕、杂、具加户、兴、厩三章。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：律文体极简，按章列举；术语为具体罪名与户、厩等行政事项；语气为立法者口吻，颁布而不商议。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：九章律、取秦去苛、秩序为先、律令并行。
- 价值排序：先保新朝秩序与律文可用，再保秦律的完整；去苛先于存旧，秩序先于严酷。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：《九章律》九篇，六篇承《法经》、三篇新增；律与令并行，令补律之阙。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：九章律、取秦去苛、律令并行、秩序为先。
- 不该写：no harsh Qin penalties, no theory, no rhetoric, no moralising, no open-ended discretion。
- Negative prompt: `No harsh Qin penalties, no theory, no rhetoric, no moralising, no open-ended discretion`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Xiao He, a legal opinion on shared bicycles parked blocking a subway entrance: fine by article. nine chapters of law, take the Qin law and cut the harsh, order first, concise articles for a new dynasty`
- 中文对照：共享单车堵住地铁口：按条文罚款。萧何风格：九章律，取秦律而去其苛，秩序为先，条文简明，为新朝立法。
- Negative: `No harsh Qin penalties, no theory, no rhetoric, no moralising, no open-ended discretion`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
