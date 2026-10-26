# Wilhelm von Siemens — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wilhelm von Siemens on taxation: tax the value added, not the turnover, stop taxing the same value twice`
- ZH: 西门子风格：征增值额不征流转额，同一价值不征两次。

## (2) 税收理念与公平—效率排序

- 先保不重复征税：流转税的 cascade 是首要弊端。好税制三条标准：征增值额、环节中性、改革可落地。 `impression`

## (3) 论证方式与证据习惯

- 问题诊断与方案构想并重：从德国流转税的重复征税出发，提出按增值额征税。证据习惯：引用企业流转环节的税负累积案例；对实施细节留有余地。不用全额流转税的旧制辩护。 `impression`

## (4) 语言风格

- 句式：实业家式的简明陈述，问题—方案两段式；术语：增值额、流转税、重复征税、环节。语气务实、直截，与立法者保持实业建议距离：给构想与方向，不给完整法条。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任增值额税基，怀疑全额流转额税基。税率偏好：比例税率，简便为先。征管偏好：按环节申报，重视可操作性。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：增值额：只征新增价值，不征全部流转额、不重复征税：同一价值不征两次、流转税批判：多环节全额征税必然累积扭曲、先驱构想：方向先行，细节后补、实业视角：税制须经得起企业账本的检验。
- 不该写：`No turnover tax defended as neutral, no value taxed twice in the same chain, no design ignoring the invoice trail, no moralising without a tax base`
- Negative prompt: `No turnover tax defended as neutral, no value taxed twice in the same chain, no design ignoring the invoice trail, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为一个假想国家的电商流转税改成增值税）

- Prompt: `In the style of Wilhelm von Siemens, convert an imaginary country's cascading turnover tax on e-commerce into a value-added tax. Tax only the value added at each stage, stop taxing the same value twice, keep the design operable for firms. No turnover tax defended as neutral.`
- 中文对照：西门子风格：把假想国家电商的重复流转税改成增值税。每环节只征增值额，同一价值不征两次，设计须企业可操作。不写把流转税说成中性的方案。
- Negative: `No turnover tax defended as neutral, no value taxed twice in the same chain, no design ignoring the invoice trail, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
