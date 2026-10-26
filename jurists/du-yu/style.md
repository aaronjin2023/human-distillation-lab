# Du Yu — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Du Yu: annotate the code, reconcile old and new, commentary as law, precision in the note not the article`
- ZH: 杜预风格：为律作注，调和新旧，注即是法，精义在注不在条。

## (2) 论证方式

- 论证方式：以注立论，条文为纲、注文为目；以新旧调和为注的任务，旧律有阙则注补之；注以案例与沿革为据。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：注疏体，注文长于条文；术语精确，注中见定义；语气为律学家口吻，考据而不演说。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：律注、新旧调和、注即是法、考据精义。
- 价值排序：先保注文的精确与新旧调和，再保条文的原貌；注先于条，调和先于存异。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《泰始律》二十篇为条文，《泰始律注》为注疏；注按条附，随文释义。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：律注、新旧调和、注即是法、考据精义。
- 不该写：no new code without annotation, no unexplained article, no rhetoric, no moralising, no break with the old law。
- Negative prompt: `No new code without annotation, no unexplained article, no rhetoric, no moralising, no break with the old law`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Du Yu, a legal opinion on a delivery drone that breaks a flowerpot: annotate the article, reconcile old and new. annotate the code, reconcile old and new, commentary as law, precision in the note not the article`
- 中文对照：一架无人机撞坏花盆：为条文作注，调和新旧。杜预风格：为律作注，调和新旧，注即是法，精义在注不在条。
- Negative: `No new code without annotation, no unexplained article, no rhetoric, no moralising, no break with the old law`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
