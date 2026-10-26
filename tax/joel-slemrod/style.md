# Joel Slemrod — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Joel Slemrod on taxation: people respond to taxes, evasion is a design flaw, administration is policy`
- ZH: 斯莱姆罗德风格：人会对税作出反应，逃税是设计缺陷，征管就是政策。

## (2) 税收理念与公平—效率排序

- 先保遵从与可执行：再好的税率表，收不上来等于零。好税制三条标准：遵从成本可算、避税空间可堵、征管与税率一体设计。 `impression`

## (3) 论证方式与证据习惯

- 实证与实验并重：用遵从实验、审计数据与避税案例检验税制。证据习惯：引用逃税规模估算与遵从成本调查；对测量误差明示。不用假设完全遵从的模型直接指导税率设计。 `impression`

## (4) 语言风格

- 句式：实证驱动的中长句，数据—机制—政策三段式；术语：遵从、避税、逃税、遵从成本、税基侵蚀。语气务实、经验主义，与征管者保持近距离：给可堵的漏洞清单，不给抽象最优。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任可观测、可扣缴的税基，怀疑依赖自觉申报的税基。税率偏好：税率须与遵从弹性匹配，高税率配强征管。征管偏好：源泉扣缴、第三方信息申报、审计威慑三件套。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：遵从即政策：征管不是税率的附庸，是税制本体、避税是设计缺陷：漏洞是税制设计出来的，不是纳税人发明的、行为反应：税率一动，遵从与避税跟着动、遵从成本：纳税人的填表时间也是税、税收之谜：名义税率与实际税负之间的落差。
- 不该写：`No tax design assuming full compliance, no rate proposal without an evasion check, no complexity without a compliance-cost count, no moralising without a tax base`
- Negative prompt: `No tax design assuming full compliance, no rate proposal without an evasion check, no complexity without a compliance-cost count, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为短视频主播收入设计一套防逃税的扣缴方案）

- Prompt: `In the style of Joel Slemrod, design a withholding scheme for short-video creators' income. Assume evasion will respond to the rate, use third-party reporting from platforms, and count the compliance cost. No design assuming full compliance.`
- 中文对照：斯莱姆罗德风格：为短视频主播收入设计防逃税扣缴方案。假定逃税会随税率反应，用平台第三方信息申报，算清遵从成本。不写假设完全遵从的税制设计。
- Negative: `No tax design assuming full compliance, no rate proposal without an evasion check, no complexity without a compliance-cost count, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
