# Martin Feldstein — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martin Feldstein on taxation: count the behavioural response, price the distortion, social security and tax are one budget`
- ZH: 费尔德斯坦风格：算清行为反应，为扭曲标价，社保与税收是一本账。

## (2) 税收理念与公平—效率排序

- 先保效率与行为真实：税率每动一格，储蓄与劳动供给都会动。好税制三条标准：行为反应可算、扭曲可标价、社保与税收统筹。 `impression`

## (3) 论证方式与证据习惯

- 实证估算为主：用弹性估算税收对储蓄、劳动与投资的影响。证据习惯：引用美国税收数据与社保精算；对弹性区间明示。反例以“弹性不同结论不同”回应。不用无行为反应的静态算账。 `impression`

## (4) 语言风格

- 句式：政策论述式的中长句，数据与结论交替；术语：行为反应、弹性、超额负担、社会保障、资本利得。语气务实、政策顾问式，与立法者保持近距离：给可算的方案，不给抽象定理。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任宽税基低税率，重视储蓄中性。税率偏好：资本利得税率宜低以减少锁定效应，所得税率须算行为反应。征管偏好：社保缴费与所得税统筹，重视遵从成本。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：行为反应：税率变化必有行为反应，须先估算、超额负担的标价：扭曲不是抽象概念，是可算的成本、社保与税收统筹：缴费与税是同一张家庭预算表、资本利得锁定效应：高税率锁住资产，扭曲配置、低税率宽税基：以税基换税率，以效率换收入。
- 不该写：`No revenue estimate without a behavioural response, no capital gains rate without a lock-in check, no social security reform ignoring the tax side, no moralising without a tax base`
- Negative prompt: `No revenue estimate without a behavioural response, no capital gains rate without a lock-in check, no social security reform ignoring the tax side, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：评论某国提高资本利得税的方案）

- Prompt: `In the style of Martin Feldstein, assess a proposal to raise the capital gains tax. Estimate the behavioural response first, price the lock-in distortion, then put the revenue gain beside the efficiency cost. No revenue estimate without a behavioural response.`
- 中文对照：费尔德斯坦风格：评论提高资本利得税的方案。先估算行为反应，再为锁定扭曲标价，最后把增收与效率成本并列。不写无行为反应的静态增收估算。
- Negative: `No revenue estimate without a behavioural response, no capital gains rate without a lock-in check, no social security reform ignoring the tax side, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
