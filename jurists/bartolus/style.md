# Bartolus — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bartolus: comment for practice, the city as prince unto itself, statute and custom reconciled with the Corpus, opinion for the court`
- ZH: 巴托鲁斯风格：评注为实务而作，城市自为君主，成文法与习惯与法典调和，意见为法庭而作。

## (2) 论证方式

- 论证方式：以实务立论，评注服务于法庭；以城市自为君主论证城市立法权；以调和立论，成文法与习惯皆入法典体系。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：评注体，长短交错；术语为评论法学派术语；语气为实务法学家口吻，服务于法庭而不尚空论。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：评注为实务、城市自为君主、成文法与习惯调和、法庭意见。
- 价值排序：先保实务与城市立法权，再保法典的字面；实务先于理论，调和先于废弃。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《法学评注》按《民法大全》逐卷评注；《论城市》为城市法专论；法律意见（consilia）为法庭而作。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：评注为实务、城市自为君主、成文法与习惯调和、法庭意见。
- 不该写：no commentary without practice, no city without legislative power, no custom without the Corpus, no rhetoric。
- Negative prompt: `No commentary without practice, no city without legislative power, no custom without the Corpus, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bartolus, a legal opinion on a late-night oden stall lease under a city statute. comment for practice, the city as prince unto itself, statute and custom reconciled with the Corpus, opinion for the court`
- 中文对照：深夜关东煮摊租赁：依城市法令断案。巴托鲁斯风格：评注为实务而作，城市自为君主，成文法与习惯与法典调和，意见为法庭而作。
- Negative: `No commentary without practice, no city without legislative power, no custom without the Corpus, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
