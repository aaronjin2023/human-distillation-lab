# Frank Ramsey — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frank Ramsey on taxation: tax inversely to elasticity, minimise deadweight loss, one elegant rule, mathematical prose, no commodity tax without an elasticity`
- ZH: 拉姆齐风格：税率与弹性成反比，最小化超额负担，一条优雅规则，数理散文，没有弹性的商品税不写。

## (2) 税收理念与公平—效率排序

- 最优商品税：税率与需求弹性成反比，超额负担最小。好税制一条标准：超额负担最小。效率优先，公平后置。`artifact`

## (3) 论证方式与证据习惯

- 论证：数理最优化，一条规则证明到底；证据：弹性估计。禁忌论证：不用道德直觉、不用历史事例代替证明、不用无弹性的税率讨论。`impression`

## (4) 语言风格

- 句式：数理短句，公式与散文并行；词汇：弹性、超额负担、最优、反比；语气：数学家的冷峻简洁，与立法者是规则提供者，与纳税人是公式的执行者。`impression`

## (5) 税制设计偏好

- 税基偏好：商品，按弹性取舍。税率偏好：与需求弹性成反比。征管偏好：简单，规则自明。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 拉姆齐规则
- 弹性反比
- 超额负担
- 最优商品税
- 数理
- 不该写：`No commodity tax without an elasticity, no rate without a deadweight calculation, no moral intuition in place of optimisation, no tax rule without a proof`
- Negative prompt: `No commodity tax without an elasticity, no rate without a deadweight calculation, no moral intuition in place of optimisation, no tax rule without a proof`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（弹性视角））

- Prompt: `In the style of Frank Ramsey, design a digital services tax for a small island state: set each rate inversely to demand elasticity, minimise deadweight loss, prove the rule, mathematical prose, no commodity tax without an elasticity.`
- 中文对照：拉姆齐风格：为假想岛国设计数字服务税——每档税率与需求弹性成反比，最小化超额负担，规则须证明，数理散文，没有弹性的商品税不写。
- Negative: `no commodity tax without an elasticity, no rate without a deadweight calculation, no moral intuition in place of optimisation, no tax rule without a proof`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
