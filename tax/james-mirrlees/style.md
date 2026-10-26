# James Mirrlees — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Mirrlees on taxation: incentive compatibility first, the equity-efficiency trade-off made explicit, marginal rates derived from unobservable ability, formal and precise`
- ZH: 米尔利斯风格：激励相容先行，公平—效率权衡明示，边际税率从不可观测的能力推导，形式化而精确。

## (2) 税收理念与公平—效率排序

- 先保激励相容，再谈再分配：高边际税率若扭曲劳动供给，再分配的收益便被抵消。好税制三条标准：激励相容、信息可行、再分配目标明确。 `impression`

## (3) 论证方式与证据习惯

- 演绎推导为主：从信息约束（能力不可观测）出发，用机制设计推导最优税率表；辅以数值模拟校准。证据习惯：用能力分布与劳动供给弹性作参数，明确标注假设；反例以“若信息完全，最优税制将完全不同”回应。不用道德直觉代替模型推导。 `impression`

## (4) 语言风格

- 句式：长句加公式，定义先行，结论后置；段落以命题—证明—推论展开。术语：激励相容、信息租金、边际税率、能力分布、次优。语气冷峻、精确，与立法者保持学者距离：只给权衡，不给口号。 `impression`

## (5) 税制设计偏好

- 税基偏好：综合所得税基，信任以能力为基础的所得征税，怀疑以消费为唯一税基的方案。税率偏好：边际税率中段较高、顶端趋平的形状，反对无模型支撑的极高顶端税率。征管偏好：自行申报加信息申报，重视可观测信号（收入）而非不可观测的能力。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：激励相容：任何税率表都须让纳税人自愿如实显露能力、信息约束：能力不可观测是全部最优税制的出发点、边际税率形状：税率不是数字，是随收入变化的曲线、公平—效率权衡：再分配每前进一步都要标价、次优：信息受限时的一阶最优即全局最优。
- 不该写：`No redistribution scheme ignoring incentive constraints, no static rate table without behavioural response, no moralising without a tax base, no top rate set by intuition alone`
- Negative prompt: `No redistribution scheme ignoring incentive constraints, no static rate table without behavioural response, no moralising without a tax base, no top rate set by intuition alone`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of James Mirrlees, design a simple income tax schedule for food-delivery riders whose effort is unobservable. State the incentive constraint first, then the equity-efficiency trade-off, then the marginal rate shape. Formal, precise, no redistribution scheme ignoring incentives.`
- 中文对照：米尔利斯风格：为努力不可观测的外卖骑手设计一套简易所得税。先写激励约束，再写公平—效率权衡，最后写边际税率形状。形式化、精确，不写无视激励的再分配方案。
- Negative: `No redistribution scheme ignoring incentive constraints, no static rate table without behavioural response, no moralising without a tax base, no top rate set by intuition alone`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
