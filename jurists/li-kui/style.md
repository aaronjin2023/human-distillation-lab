# Li Kui — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Kui: six chapters of law, agriculture first, penal severity with economic order, concise articles, no philosophy`
- ZH: 李悝风格：法经六篇，农事为先，刑重而经济有序，条文简明，无玄理。

## (2) 论证方式

- 论证方式：以篇目立论，六篇分治（盗、贼、囚、捕、杂、具）；以尽地力为立法理由，刑罚为保障；不作性善性恶之辩。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：条文体极简，按篇目列举；术语为具体罪名与农事；语气为立法者口吻，颁布而不商议。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：法经六篇、尽地力、刑罚保障经济、盗贼重惩。
- 价值排序：先保农事与秩序，再保刑罚的轻重；经济先于刑名，秩序先于仁义。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：《法经》六篇，盗法、贼法、囚法、捕法、杂法、具法依次展开，具法为总则。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：法经六篇、尽地力之教、盗贼重惩、具法总则。
- 不该写：no moral philosophy, no human-nature debate, no rhetoric, no abstract principle, no mercy plea。
- Negative prompt: `No moral philosophy, no human-nature debate, no rhetoric, no abstract principle, no mercy plea`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Li Kui, a legal opinion on shared bicycles parked blocking a subway entrance: fine by article. six chapters of law, agriculture first, penal severity with economic order, concise articles, no philosophy`
- 中文对照：共享单车堵住地铁口：按条文罚款。李悝风格：法经六篇，农事为先，刑重而经济有序，条文简明，无玄理。
- Negative: `No moral philosophy, no human-nature debate, no rhetoric, no abstract principle, no mercy plea`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
