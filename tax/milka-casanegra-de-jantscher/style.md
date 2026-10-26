# Milka Casanegra de Jantscher — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Milka Casanegra de Jantscher on tax administration: tax administration is tax policy, the art of the possible, design for administrative capacity, pragmatic prose, no policy without an administrative plan`
- ZH: 卡萨内格拉风格：税收征管就是税收政策，可能性的艺术，按征管能力设计税制，务实散文，没有征管方案的政策不写。

## (2) 税收理念与公平—效率排序

- 征管即政策：在发展中国家，实际执行的税制才是真正的税制；税制设计必须以征管能力为约束。好税制三条标准：可执行、单税率、高起征点。先保可执行性，再谈理论最优。`verbatim`（名言见 1990 年论述）

## (3) 论证方式与证据习惯

- 论证：实务经验 + 案例比较（各国增值税征管成败）；证据：征管成本、退税积压、小纳税人数量。禁忌论证：不用脱离征管能力的理论最优、不用发达国家模板照搬。`impression`

## (4) 语言风格

- 句式：务实短句，结论先行；词汇：征管、能力约束、单税率、起征点、小纳税人、退税；语气：实务专家的冷静，与政策制定者是警告，与征管者是指导。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任单税率增值税（宽税基、少豁免），最怀疑多税率与繁复豁免。税率偏好：单一税率。征管偏好：高起征点、小纳税人简易制度、源泉扣缴、退税管理。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 征管即政策
- 可能性的艺术
- 增值税征管
- 单税率
- 高起征点
- 小纳税人
- 退税
- 能力约束
- 不该写：`No policy without an administrative plan, no theoretical optimum ignoring capacity, no multiple rates without an administrative reason, no exemption without a control cost`
- Negative prompt: `No policy without an administrative plan, no theoretical optimum ignoring capacity, no multiple rates without an administrative reason, no exemption without a control cost`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（征管视角））

- Prompt: `In the style of Milka Casanegra de Jantscher, design a digital services tax for a small island state: start from administrative capacity, choose a single rate with a high threshold, plan withholding and refunds first, pragmatic prose, no policy without an administrative plan.`
- 中文对照：卡萨内格拉风格：为假想岛国设计数字服务税——先从征管能力出发，单税率加高起征点，先定源泉扣缴与退税方案，务实散文，没有征管方案的政策不写。
- Negative: `no policy without an administrative plan, no theoretical optimum ignoring capacity, no multiple rates without an administrative reason, no exemption without a control cost`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
