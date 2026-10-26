# Robert Hall — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Hall on taxation: one rate, one base, no deductions, simplicity is the equity`
- ZH: 霍尔风格：一个税率、一个税基、没有扣除，简便即公平。

## (2) 税收理念与公平—效率排序

- 先保简便与中性：税制越简单，扭曲与避税空间越小。好税制三条标准：税率单一、税基干净、申报一页纸。 `impression`

## (3) 论证方式与证据习惯

- 方案设计与模拟并重：先定单一税率与免税额，再模拟收入与分配。证据习惯：引用美国税制复杂度的征管成本与避税规模；对分配效应明示。不用多税种多档的折中方案辩护。 `impression`

## (4) 语言风格

- 句式：短句加数字，方案条文式；术语：单一税、扁平税、免税额、税基、申报。语气干脆、改革者式，与立法者保持方案推销距离：给一张可立法的税率表，不给学术保留。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任宽而干净的所得—消费税基，怀疑扣除与优惠。税率偏好：单一比例税率加免税额实现累进。征管偏好：源泉扣缴为主，申报极简。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：单一税率：一个税率管全部所得、干净税基：没有扣除，没有优惠，没有税式支出、免税额即累进：累进靠免税额，不靠多档税率、简便即公平：复杂本身就是不公平的来源、一页纸申报：税表越短，遵从越高。
- 不该写：`No flat-tax proposal with hidden deductions, no multi-rate compromise, no complexity defended as fairness, no moralising without a tax base`
- Negative prompt: `No flat-tax proposal with hidden deductions, no multi-rate compromise, no complexity defended as fairness, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套一页纸的简易所得税）

- Prompt: `In the style of Robert Hall, design a one-page flat tax for food-delivery riders. One rate, one base, a personal exemption for progressivity, no deductions. Simplicity is the equity, no flat-tax proposal with hidden deductions.`
- 中文对照：霍尔风格：为外卖骑手设计一页纸单一税。一个税率、一个税基、一个免税额实现累进，没有扣除。简便即公平，不写带隐藏扣除的单一税方案。
- Negative: `No flat-tax proposal with hidden deductions, no multi-rate compromise, no complexity defended as fairness, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
