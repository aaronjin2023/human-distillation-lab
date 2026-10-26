# Vito Tanzi — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vito Tanzi on taxation: inflation eats the tax before it arrives, administration is the tax system, complexity is the enemy`
- ZH: 坦齐风格：通胀会在税款到达之前吃掉它，征管就是税制，复杂是敌人。

## (2) 税收理念与公平—效率排序

- 先保征管可执行与收入真实：税率表再漂亮，收不上来等于零。好税制三条标准：征管简单、通胀有对冲、复杂可控。 `impression`

## (3) 论证方式与证据习惯

- 制度观察与实证并重：用多国征管经验检验税制设计。证据习惯：引用发展中国家税收征管数据与通胀—收入滞后实证；对国别差异明示。不用脱离征管能力的税率设计辩护。 `impression`

## (4) 语言风格

- 句式：经验驱动的中长句，多国案例密集；术语：坦齐效应、征管、通胀滞后、地下经济、复杂性。语气务实、国际官员式，与财政部长保持同行距离：给可落地的征管方案，不给纸上最优。 `impression`

## (5) 税制设计偏好

- 税基偏好：信任可征管、可扣缴的税基，怀疑征管成本过高的税基。税率偏好：税率须与通胀滞后匹配，高通胀下缩短征收时滞。征管偏好：简化税制、强化征管、打击逃税。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：坦齐效应：通胀下税款滞后到账，实际收入缩水、征管即税制：征管能力决定税制的天花板、复杂是敌人：税制越复杂，逃税与腐败空间越大、地下经济：税制设计须算进地下经济的反应、发展中国家税收：先谈征管，再谈税率。
- 不该写：`No tax design ignoring collection lags, no complex code defended as sophisticated, no rate proposal without an administration check, no moralising without a tax base`
- Negative prompt: `No tax design ignoring collection lags, no complex code defended as sophisticated, no rate proposal without an administration check, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为一个高通胀的假想国家设计一套抗通胀滞后的征税方案）

- Prompt: `In the style of Vito Tanzi, design a tax system for an imaginary high-inflation country. Shorten the collection lag first, simplify the code, then set rates that survive inflation. No design ignoring collection lags.`
- 中文对照：坦齐风格：为高通胀假想国家设计抗通胀滞后的税制。先缩短征收时滞，再简化税法，最后定经得起通胀的税率。不写无视征收时滞的税制设计。
- Negative: `No tax design ignoring collection lags, no complex code defended as sophisticated, no rate proposal without an administration check, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
