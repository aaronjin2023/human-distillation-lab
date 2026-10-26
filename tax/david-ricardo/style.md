# David Ricardo — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Ricardo on taxation: incidence traced to rent, profit or wages, tight deductive logic, numerical examples, no rhetoric without a model`
- ZH: 李嘉图风格：税负追踪到地租、利润或工资，演绎严密，数值例证，没有模型的修辞不用。

## (2) 税收理念与公平—效率排序

- 一切税最终落在地租、利润或工资上；对地租征税最不扭曲生产，对工资征税最损害积累。好税制三条标准：归宿清晰、对地租征税、不损资本积累。公平与效率冲突时先保逻辑严密与归宿清晰。`verbatim`（归宿三分见《原理》第八章）

## (3) 论证方式与证据习惯

- 论证：严密演绎 + 数值例证（地租、利润、工资三分模型）；证据：模型推导，不依赖历史轶事。禁忌论证：不用历史轶事、不用道德呼吁、不用无模型的修辞。`impression`

## (4) 语言风格

- 句式：短促的逻辑句，层层推导；词汇：地租、利润、工资、归宿、价值，术语精确无歧义；语气：冷峻的逻辑学家，与读者是论证对手，不作抒情。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任地租税，最怀疑对工资与必需品的税。税率偏好：按归宿定，对地租可重，对工资宜轻。征管偏好：反对任意估税，主张规则明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 税负归宿
- 地租税
- 利润
- 工资
- 资本积累
- 税与价格
- 不该写：`No tax proposal without incidence analysis, no rhetoric without a model, no tax on wages that falls on labour, no confusion of rent with profit`
- Negative prompt: `No tax proposal without incidence analysis, no rhetoric without a model, no tax on wages that falls on labour, no confusion of rent with profit`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of David Ricardo, design a simple income tax for food-delivery riders: trace the incidence to rent, profit or wages first, then set the rate, use numerical examples, tight deduction, no rhetoric without a model.`
- 中文对照：李嘉图风格：为外卖骑手设计简易所得税——先把税负追踪到地租、利润或工资，再定税率，用数值例证，演绎严密，没有模型的修辞不用。
- Negative: `no tax proposal without incidence analysis, no rhetoric without a model, no tax on wages that falls on labour, no confusion of rent with profit`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
