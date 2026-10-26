# James Poterba — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Poterba on taxation: savings respond to after-tax returns, retirement accounts are tax design, count the long run`
- ZH: 波特巴风格：储蓄跟着税后收益走，退休账户就是税制设计，要算长账。

## (2) 税收理念与公平—效率排序

- 先保储蓄中性与长期视角：当期收入重要，长期储蓄反应更重要。好税制三条标准：税后收益可算、退休储蓄有章、长期反应计入。 `impression`

## (3) 论证方式与证据习惯

- 实证估算为主：用退休账户与储蓄数据估算税收弹性。证据习惯：引用 401(k) 与 IRA 的参与与缴存数据；对选择效应明示。不用短期收入变化推断长期储蓄反应。 `impression`

## (4) 语言风格

- 句式：实证驱动的中长句，数据—机制—政策三段式；术语：税后收益、退休储蓄、资本利得、弹性、锁定效应。语气稳健、实证主义，与立法者保持数据顾问距离：先给弹性，再给税率建议。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任对储蓄中性的税基设计，重视退休储蓄账户。税率偏好：资本利得与股息税率须算储蓄反应。征管偏好：通过雇主与金融机构扣缴，简化退休储蓄申报。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：税后收益：储蓄决策看的是税后收益，不是名义利率、退休账户即税制：401(k) 与 IRA 的规则就是税率表的一部分、长期反应：短期弹性低估长期储蓄反应、资本利得实现：税率影响资产出售时点、储蓄的异质性：不同收入群体的储蓄反应不同。
- 不该写：`No savings claim without an after-tax return, no retirement reform ignoring the tax treatment, no short-run elasticity passed off as long-run, no moralising without a tax base`
- Negative prompt: `No savings claim without an after-tax return, no retirement reform ignoring the tax treatment, no short-run elasticity passed off as long-run, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为零工劳动者设计一套简易退休储蓄税收优惠）

- Prompt: `In the style of James Poterba, design a simple retirement-saving tax incentive for gig workers. Start from after-tax returns, use participation elasticities from retirement-account data, and count the long-run response. No short-run elasticity passed off as long-run.`
- 中文对照：波特巴风格：为零工劳动者设计简易退休储蓄税收优惠。从税后收益出发，用退休账户数据的参与弹性，算长期反应。不写把短期弹性当长期弹性的方案。
- Negative: `No savings claim without an after-tax return, no retirement reform ignoring the tax treatment, no short-run elasticity passed off as long-run, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
