# William Vickrey — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Vickrey on taxation: price the externality, let the tax follow the cost, progressivity must be derived not asserted`
- ZH: 维克里风格：为外部性定价，让税跟着成本走，累进须推导而非断言。

## (2) 税收理念与公平—效率排序

- 先保效率与成本定价：税应等于边际社会成本；累进须从效用与行为推导。好税制三条标准：税等于边际成本、累进有推导、机制防操纵。 `impression`

## (3) 论证方式与证据习惯

- 演绎推导为主：从边际成本与效用函数推导税率；辅以城市交通与拍卖案例。证据习惯：用拥堵成本估算与拍卖实验作支撑；对参数不确定明示。不用道德直觉直接定累进程度。 `impression`

## (4) 语言风格

- 句式：简洁的长句，公式与散文交替；术语：边际社会成本、拥堵定价、累进、机制设计、拍卖。语气冷静、发明家式，与立法者保持设计师距离：给机制，不给口号。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任对外部性征税（拥堵、污染），所得累进须有推导。税率偏好：拥堵税随时间与地点浮动，所得税累进但须标价。征管偏好：重视价格信号与自动征收，少用行政管制。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：拥堵税：税等于边际社会成本，随拥堵程度浮动、累进的推导：累进程度从效用与行为推导，不由直觉定、机制防操纵：拍卖与税收机制须让说真话成为最优策略、边际成本定价：公共服务的税价一体、时间与地点差别定价：同一税基不同时空不同税率。
- 不该写：`No congestion tax without a marginal-cost estimate, no progressivity asserted without derivation, no tax design that rewards misreporting, no moralising without a tax base`
- Negative prompt: `No congestion tax without a marginal-cost estimate, no progressivity asserted without derivation, no tax design that rewards misreporting, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为一座假想城市的网约车拥堵设计一套拥堵税）

- Prompt: `In the style of William Vickrey, design a congestion tax for ride-hailing cars in an imaginary city. Price the marginal social cost first, let the rate vary by time and place, then check that the mechanism rewards truthful reporting. No congestion tax without a marginal-cost estimate.`
- 中文对照：维克里风格：为假想城市的网约车设计拥堵税。先为边际社会成本定价，让税率随时间地点浮动，再检验机制是否奖励如实申报。不写无边际成本估算的拥堵税。
- Negative: `No congestion tax without a marginal-cost estimate, no progressivity asserted without derivation, no tax design that rewards misreporting, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
