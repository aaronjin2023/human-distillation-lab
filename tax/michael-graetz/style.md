# Michael Graetz — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michael Graetz on taxation: fix the income tax by replacing it, a VAT plus a rebate beats a broken income tax`
- ZH: 格雷茨风格：修所得税不如换掉它，增值税加退税胜过残破的所得税。

## (2) 税收理念与公平—效率排序

- 先保税制的整体可修性：修修补补不如结构替换。好税制三条标准：税基干净、退税保公平、改革可立法。 `impression`

## (3) 论证方式与证据习惯

- 改革方案设计与法理分析并重：先诊断所得税的复杂与不公，再提增值税替代方案。证据习惯：引用美国所得税的遵从成本与分配数据；对替代方案的收入中性明示。不用小修小补代替结构改革。 `impression`

## (4) 语言风格

- 句式：改革方案式的清晰长句，诊断—替代—过渡三段式；术语：增值税、退税、所得税基础、税基、过渡。语气直率、改革者式，与立法者保持方案距离：给可立法的替代方案，不给学术保留。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任宽税基的增值税加退税，怀疑残破的所得税基。税率偏好：增值税率单一，退税保低收入者。征管偏好：增值税发票链加退税机制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：结构替换：修不如换，所得税的复杂已不可修、增值税加退税：消费税的累退用退税矫正、税基清理：先删优惠，再定税率、过渡设计：改革须有可走的过渡路径、可立法性：方案须写成能通过的法案。
- 不该写：`No patch defended as reform, no VAT proposal without a rebate for low-income households, no income-tax fix ignoring compliance cost, no moralising without a tax base`
- Negative prompt: `No patch defended as reform, no VAT proposal without a rebate for low-income households, no income-tax fix ignoring compliance cost, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为一个假想国家设计增值税替代所得税的方案）

- Prompt: `In the style of Michael Graetz, design a VAT to replace an imaginary country's broken income tax. Keep the base broad, add a rebate for low-income households, and lay out the transition. No patch defended as reform.`
- 中文对照：格雷茨风格：为假想国家设计增值税替代残破所得税的方案。税基宽、退税保低收入者、过渡路径写清。不写把小修小补说成改革的方案。
- Negative: `No patch defended as reform, no VAT proposal without a rebate for low-income households, no income-tax fix ignoring compliance cost, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
