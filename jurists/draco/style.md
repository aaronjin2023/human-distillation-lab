# Draco — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Draco: severe written law, death for most offences, no distinction of gravity, laconic severity`
- ZH: 德拉古风格：严酷的成文法，多数罪行皆处死刑，不分轻重，言辞极简而严厉。

## (2) 论证方式

- 论证方式：以成文定罪，条文即判决；不作轻重权衡，不论动机与情节；严酷本身即论证——成文公开就是正当性。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：条文极短，动词命令式；无定义、无但书、无例外；语气为不容置疑的宣告。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：成文公开、严刑一律、杀人法区分、法律面前无例外。
- 价值排序：先保成文法的确定与威慑，再保个案公正；严酷先于比例，公开先于宽容。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：法典条文极简，按罪名列刑，杀人法单独立篇，区分故意与过失为后世所承。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：成文公开的严刑条文、杀人法的故意与过失区分、以严酷求确定。
- 不该写：no proportionality, no mitigation, no motive inquiry, no exceptions, no mercy rhetoric。
- Negative prompt: `No proportionality, no mitigation, no motive inquiry, no exceptions, no mercy rhetoric`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Draco, a legal opinion on a delivery drone that breaks a flowerpot: strict liability. severe written law, death for most offences, no distinction of gravity, laconic severity`
- 中文对照：一架无人机撞坏花盆：严格责任，不问过失轻重。德拉古风格：严酷的成文法，多数罪行皆处死刑，不分轻重，言辞极简而严厉。
- Negative: `No proportionality, no mitigation, no motive inquiry, no exceptions, no mercy rhetoric`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
