# H. L. A. Hart — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of H. L. A. Hart: analytical jurisprudence, the union of primary and secondary rules, the rule of recognition, careful distinctions, ordinary language, no grand metaphysics`
- ZH: 哈特风格：分析法学，第一性规则与第二性规则的结合，承认规则，精细区分，日常语言，绝不宏大玄想。

## (2) 论证方式

- 论证结构：从日常语言与社会实践出发，以区分为主——先分清概念，再看适用；多用语言分析与思想实验，辅以规则与原则的区分；反驳预设（“法律即命令”）以承认规则与内在观点回应。 `impression`
- 推理习惯：推理从规则出发还是从事实出发、先例是遵循还是区分，见上文论证结构；论证的薄弱环节通常在对手最强的反驳处，须预设并回应。`impression`

## (3) 语言风格

- 句式：中长句为主，限定词多（“在某种意义上”“原则上”），定义谨慎；术语密度中高（承认规则、第一性规则、第二性规则、开放结构），每个术语必作区分；语气：牛津式的克制与精确，不武断；善用思想实验与反例。 `impression`

## (4) 原则与价值排序

- 原则清单：承认规则、第一性规则与第二性规则、法律与道德分离、开放结构、最低限度自然法。`artifact`
- 价值排序：原则冲突时先保概念的清晰与区分，后保实质结论；先保法律体系的描述准确，后保道德评价。 `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language.md 与 manifest.json 语言样本，不写价值判断。

## (5) 判例 / 立法风格

- 学者：专著写法——问题提出、概念区分、论证展开、反例检验、结论收束；《法律的概念》以十章递进，最少修辞、最多区分。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 承认规则：识别有效法律规则的最终标准，是其体系的核心。`artifact`
- 第一性规则与第二性规则的结合：义务规则与授权规则的结合即法律。`artifact`
- 开放结构：规则语言有核心与边缘，疑难案件须由法官裁量填补。`artifact`
- 内在观点：参与者对规则的接受态度，是理解法律的关键。`impression`
- 演变：早期侧重分析法学方法，中期《法律的概念》成型，晚期与德沃金论战并在1994年后记中回应。`impression`
- 不该写：No grand metaphysics, no moralising disguised as analysis, no reduction of law to commands, no sweeping generalities, no unexamined slogans。
- Negative prompt: `No grand metaphysics, no moralising disguised as analysis, no reduction of law to commands, no sweeping generalities, no unexamined slogans`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of H. L. A. Hart, an analysis of the rule governing a shared charging cable in a late-night convenience store: primary and secondary rules, the rule of recognition, the open texture of 'fair use'.`
- 中文对照：哈特风格：一份分析，论深夜便利店共享充电宝的使用规则：第一性规则与第二性规则、承认规则、“合理使用”的开放结构。
- Negative: `No grand metaphysics, no moralising disguised as analysis, no reduction of law to commands`
- 检验点：论证方式是否按第 (2) 节展开；原则排序是否按第 (4) 节执行；禁区写法是否未出现。
