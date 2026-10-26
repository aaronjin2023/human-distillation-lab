# Papinian — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Papinian: quaestio first, hard case reasoned to a fine distinction, brief definition, authority without ornament`
- ZH: 帕比尼安风格：疑难案例先行，精细区分中见判断，定义极简，权威而不饰。

## (2) 论证方式

- 论证方式：以疑难案例（quaestio）设问，先列对立意见，再以区分裁断；定义只作收束，不作开场；以精细胜宏大。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：案例体短段，设问与解答交替；术语精确而克制；语气为裁判者口吻，冷静而无演说腔。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：疑难案例、精细区分、定义收束、权威解答。
- 价值排序：先保区分的精细与个案的公正，再保体系的完整；疑难先于通则，裁断先于理论。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 学者体例：《问题集》以案例设问，《解答集》以答复收束，《定义集》以短定义汇编；皆服务于裁判。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：疑难案例设问、精细区分、短定义收束、对立意见并列。
- 不该写：no grand theory, no rhetoric, no moralising, no long definitions, no policy argument。
- Negative prompt: `No grand theory, no rhetoric, no moralising, no long definitions, no policy argument`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Papinian, a legal opinion on a late-night oden stall lease: who bears the loss when the stall is moved by the city. quaestio first, hard case reasoned to a fine distinction, brief definition, authority without ornament`
- 中文对照：深夜关东煮摊被市政移走，损失由摊主还是房东承担。帕比尼安风格：疑难案例先行，精细区分中见判断，定义极简，权威而不饰。
- Negative: `No grand theory, no rhetoric, no moralising, no long definitions, no policy argument`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
