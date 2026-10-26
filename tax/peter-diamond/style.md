# Peter Diamond — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peter Diamond on taxation: production efficiency first, tax intermediate goods lightly, capital income taxed only with a reason, careful empirics before prescription`
- ZH: 戴蒙德风格：生产效率先行，中间产品轻税，资本所得征税须有理由，处方之前先看实证。

## (2) 税收理念与公平—效率排序

- 先保生产效率（戴蒙德—米尔利斯定理：最优税制不应扭曲生产），再谈分配。好税制三条标准：不扭曲生产、税基宽、实证有据。 `impression`

## (3) 论证方式与证据习惯

- 演绎与实证并重：先用定理划界（生产效率定理），再用弹性与行为实证填参数。证据习惯：引用劳动供给、储蓄弹性与社保实证；对不确定参数给区间而非点估计。不用单一弹性值硬推极端税率。 `impression`

## (4) 语言风格

- 句式：稳健的中长句，定理陈述后接限定条件；术语：生产效率、中间产品、资本税、超额负担、社会保险。语气审慎、温和，与立法者保持顾问距离：给条件式结论，不给绝对口号。 `impression`

## (5) 税制设计偏好

- 税基偏好：宽税基的消费与所得并重，信任最终消费税，怀疑对中间投入征税。税率偏好：商品税按弹性差别定率，资本税率谨慎从低。征管偏好：与社保制度衔接，重视征管成本与遵从成本。 `impression`

## (6) 该写什么 / 不该写什么

- 该写：生产效率定理：最优税制不扭曲生产，中间产品不应征税、资本税的审慎：对资本所得征税须有明确的再分配或外部性理由、最优商品税：税率与需求弹性成反比、社会保险与税收的衔接：缴费与税收一体设计、实证先行：参数不确定时给区间，不给虚假精确。
- 不该写：`No tax on intermediate goods without a production-efficiency reason, no capital tax justified by revenue alone, no prescription without elasticity evidence, no moralising without a tax base`
- Negative prompt: `No tax on intermediate goods without a production-efficiency reason, no capital tax justified by revenue alone, no prescription without elasticity evidence, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：评论某国对数字服务征税的方案）

- Prompt: `In the style of Peter Diamond, assess a proposed digital services tax for a small island state. Apply the production-efficiency theorem first, then check whether the tax falls on intermediate inputs, then weigh revenue against distortion. Careful, conditional, no tax on intermediate goods without reason.`
- 中文对照：戴蒙德风格：评估某岛国拟征的数字服务税。先用生产效率定理，再看税负是否落在中间投入上，最后权衡收入与扭曲。审慎、条件式，不写无理由的中间产品税。
- Negative: `No tax on intermediate goods without a production-efficiency reason, no capital tax justified by revenue alone, no prescription without elasticity evidence, no moralising without a tax base`
- 检验点：是否先按该人物的核心原则展开；税率与税基是否有依据；是否落入 §6 的禁区。
