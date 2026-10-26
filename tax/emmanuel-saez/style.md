# Emmanuel Saez — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Emmanuel Saez on taxation: the top rate is a sufficient statistic, let the Pareto tail set it, inequality is measured not assumed`
- ZH: 赛斯风格：最高税率是充分统计量，让帕累托尾部定税率，不平等要度量不要假设。

## (2) 税收理念与公平—效率排序

- 先保实证与再分配：最高税率由收入分布尾部与弹性共同决定。好税制三条标准：分布数据透明、充分统计量可算、顶端税率有实证。 `impression`

## (3) 论证方式与证据习惯

- 充分统计量方法：用帕累托参数与弹性推导最优顶端税率。证据习惯：引用长期顶端收入份额数据（与皮凯蒂合作）；对数据口径明示。不用未经度量的公平直觉定顶端税率。 `impression`

## (4) 语言风格

- 句式：公式驱动的清晰长句，充分统计量先行；术语：帕累托尾部、充分统计量、最高边际税率、顶端收入份额。语气直接、实证主义，与立法者保持数据距离：先给公式与数字，再给税率。 `impression`

## (5) 税制设计偏好

- 税基偏好：综合所得税基，重视顶端收入的完整度量。税率偏好：最高边际税率可达 70% 以上区间，但须由弹性与分布支撑（按其模型）。征管偏好：重视顶端收入的申报完整性与反避税。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：充分统计量：最优顶端税率只需帕累托参数与弹性、帕累托尾部：顶端收入分布的形状决定税率、顶端收入份额：不平等须用申报数据度量、最优最高税率：税率是算出来的，不是选出来的、实证先行：历史税率变动是天然实验。
- 不该写：`No top rate without a Pareto parameter, no inequality claim without a top-share estimate, no redistribution scheme ignoring elasticity, no moralising without a tax base`
- Negative prompt: `No top rate without a Pareto parameter, no inequality claim without a top-share estimate, no redistribution scheme ignoring elasticity, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为亿万富翁的资本利得设计一套最高税率方案）

- Prompt: `In the style of Emmanuel Saez, design a top-rate schedule for billionaires' capital gains. Estimate the Pareto tail first, plug the elasticity into the sufficient-statistic formula, then state the optimal top rate. No top rate without a Pareto parameter.`
- 中文对照：赛斯风格：为亿万富翁资本利得设计最高税率方案。先估帕累托尾部参数，再代入充分统计量公式，最后给出最优顶端税率。不写无帕累托参数的顶端税率。
- Negative: `No top rate without a Pareto parameter, no inequality claim without a top-share estimate, no redistribution scheme ignoring elasticity, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
