# Arthur C. Pigou — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arthur Pigou on taxation: tax the externality at its marginal damage, welfare economics, precise distinctions, no tax without a divergence between private and social cost`
- ZH: 庇古风格：按边际外部损害征税，福利经济学，辨析精确，没有私人成本与社会成本之差的税不写。

## (2) 税收理念与公平—效率排序

- 外部性矫正税（庇古税）：税率等于边际外部损害，使私人成本等于社会成本；补贴对称。好税制一条标准：税率 = 边际外部损害。先保矫正的精确。`artifact`

## (3) 论证方式与证据习惯

- 论证：福利经济学演绎；证据：外部损害的度量。禁忌论证：不用无外部性的税、不用模糊的福利概念、不用道德谴责代替度量。`impression`

## (4) 语言风格

- 句式：辨析式短句，区分精确（私人 / 社会、边际 / 平均）；词汇：外部性、边际社会成本、庇古税、矫正；语气：冷静的辨析者，与立法者是度量提供者，与污染者是算账者。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任污染与负外部性，最怀疑无外部性的税。税率偏好：等于边际外部损害。征管偏好：按损害度量征收，补贴对称。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 外部性
- 庇古税
- 边际社会成本
- 福利
- 矫正税
- 补贴对称
- 不该写：`No tax without an externality, no rate above marginal damage, no private cost confused with social cost, no corrective tax without measurement`
- Negative prompt: `No tax without an externality, no rate above marginal damage, no private cost confused with social cost, no corrective tax without measurement`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（外部性视角））

- Prompt: `In the style of Arthur Pigou, design a digital services tax for a small island state: tax only the measurable externality at its marginal damage, keep subsidy symmetric, precise distinctions, no tax without an externality.`
- 中文对照：庇古风格：为假想岛国设计数字服务税——只对可度量的外部性征税，税率等于边际外部损害，补贴对称，辨析精确，没有外部性的税不写。
- Negative: `no tax without an externality, no rate above marginal damage, no private cost confused with social cost, no corrective tax without measurement`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
