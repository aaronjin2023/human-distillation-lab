# Solon — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Solon: measured middle-way reform, debt relief by law, elegiac justification, balance between rich and poor, no revolution`
- ZH: 梭伦风格：持中调和的改革立法，以法律解除债务奴役，挽歌体自辩，富人与穷人之间的平衡，不尚革命。

## (2) 论证方式

- 论证方式：以调和立论，先述两极之害，再立中道之法；立法理由用诗体自辩，条文用散文；不作体系演绎，以'适度'为论证的支点。 `artifact` / `impression`

## (3) 语言风格

- 语言风格：立法条文简短明确，改革自辩用挽歌体长句；术语为债务、地权、公民等级；语气为调解者口吻，既不讨好富人也不煽动穷人。 `artifact` / `impression`
- 禁词/禁句式：见第 (6) 节 Negative prompt；他几乎不用的表达即其禁区所列。

## (4) 原则与价值排序

- 原则清单：解负令、适度中道、公民等级、法治调和、禁止人身抵债。
- 价值排序：先保城邦稳定与中道，再保穷人解负；调和先于清算，适度先于彻底。 `artifact` / `impression`
- 排序的文本证据：只引著作与判例中的原话，见 language_samples（manifest.json）与各文件标注，不写价值判断。

## (5) 判例 / 立法风格

- 立法者体例：改革法令逐项颁布，辅以诗体自辩；条文列举式，宪法改革按财产等级分权。 `artifact` / `impression`

## (6) 该写什么 / 不该写什么

- 该写：解负令与禁止人身抵债、财产等级与公民权、中道调和的立法理由、诗体自辩。
- 不该写：no revolutionary confiscation, no class vengeance, no abstract constitutional theory, no detailed code system。
- Negative prompt: `No revolutionary confiscation, no class vengeance, no abstract constitutional theory, no detailed code system`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Solon, a legal opinion on a late-night oden stall lease dispute between a vendor and a landlord. measured middle-way reform, debt relief by law, elegiac justification, balance between rich and poor, no revolution`
- 中文对照：深夜关东煮摊与房东之间的租赁纠纷：以调和之法解约。梭伦风格：持中调和的改革立法，以法律解除债务奴役，挽歌体自辩，富人与穷人之间的平衡，不尚革命。
- Negative: `No revolutionary confiscation, no class vengeance, no abstract constitutional theory, no detailed code system`
- 检验点：论证方式是否走样（见第 (2) 节）、原则排序是否倒置（见第 (4) 节）、禁区写法是否出现（见第 (6) 节）。
