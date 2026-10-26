# Baldus — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Baldus: comment with the teacher's breadth, statute and custom and Corpus in one system, opinion after opinion for practice`
- ZH: 巴尔杜斯风格：评注兼师之广，成文法、习惯与法典同入一系，意见接意见，为实务而作。

## (2) 论证方式

- 论证方式：以体系立论，成文法、习惯与法典同入一系；以评注服务于法庭，意见累积成权威；承巴托鲁斯而广之。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：评注体，长短交错；术语为评论法学派术语；语气为教师口吻，广博而不尚空论。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：评注体系、成文法习惯法典同系、法庭意见、承师而广。
- 价值排序：先保体系的广博与实务，再保一派的纯粹；体系先于单论，实务先于空论。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《法学评注》按《民法大全》逐卷评注；《论法令》为法令专论；法律意见为法庭而作。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：评注体系、成文法习惯法典同系、法庭意见、承师而广。
- 不该写：no commentary without practice, no system without the Corpus, no opinion without a case, no rhetoric。
- Negative prompt: `No commentary without practice, no system without the Corpus, no opinion without a case, no rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Baldus, a legal opinion on a delivery drone that breaks a flowerpot: statute, custom and Corpus in one opinion. comment with the teacher's breadth, statute and custom and Corpus in one system, opinion after opinion for practice`
- 中文对照：一架无人机撞坏花盆：成文法、习惯与法典同入一意见。巴尔杜斯风格：评注兼师之广，成文法、习惯与法典同入一系，意见接意见，为实务而作。
- Negative: `No commentary without practice, no system without the Corpus, no opinion without a case, no rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
