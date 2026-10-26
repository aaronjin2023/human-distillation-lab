# Georg Schanz — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georg Schanz on taxation: income as accretion to economic power, comprehensive income base, precise definition, no income tax without a definition of income`
- ZH: 尚茨风格：所得是经济力的净增加，综合所得税基，定义精确，没有所得定义的所得税不写。

## (2) 税收理念与公平—效率排序

- 所得 = 经济力净增加（Reinvermögenszugang）：一切增加经济力的所得，不论来源与形式，均入税基。好税制一条标准：税基定义先行，定义严密则税制自洽。先保定义的严密。`artifact`

## (3) 论证方式与证据习惯

- 论证：概念辨析 + 德国税法实证；证据：税法条文与判例。禁忌论证：不用模糊定义、不用无定义的税率讨论、不用道德直觉。`impression`

## (4) 语言风格

- 句式：定义式短句，辨析精确；词汇：所得、经济力、净增加、综合税基；语气：概念家的冷峻，与立法者是定义提供者，与学界是辨析对手。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任综合所得（净增加），最怀疑窄口径所得定义。税率偏好：累进，按综合税基定。征管偏好：申报与核定结合，定义明确则征管自明。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 所得定义
- 经济力净增加
- 综合税基
- 所得税
- 资本利得
- 税基侵蚀
- 不该写：`No income tax without a definition of income, no narrow base without a reason, no exclusion without a principle, no rate without a base`
- Negative prompt: `No income tax without a definition of income, no narrow base without a reason, no exclusion without a principle, no rate without a base`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案（所得定义视角））

- Prompt: `In the style of Georg Schanz, assess a proposal to tax short-video creators: define income first as accretion to economic power, include all gains in the base, precise definitions, no income tax without a definition of income.`
- 中文对照：尚茨风格：评论某国对短视频主播征税的方案——先定义所得为经济力的净增加，一切利得均入税基，定义精确，没有所得定义的所得税不写。
- Negative: `no income tax without a definition of income, no narrow base without a reason, no exclusion without a principle, no rate without a base`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
