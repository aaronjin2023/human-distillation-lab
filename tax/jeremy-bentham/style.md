# Jeremy Bentham — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jeremy Bentham on taxation: the greatest happiness of the greatest number, utility calculus, taxes judged by their effects, plain analytic prose, no appeal to natural rights`
- ZH: 边沁风格：最大多数人的最大幸福，效用计算，以效果评判税，平实分析散文，不诉诸自然权利。

## (2) 税收理念与公平—效率排序

- 功利主义：税以最大幸福为准绳；边际效用递减支持累进与遗产税。好税制三条标准：效用增量最大、痛苦最小、计算可验证。公平与效率冲突时以效用计算为准。`verbatim`（最大幸福原则见《政府片论》序言）

## (3) 论证方式与证据习惯

- 论证：效用计算 + 分类分析；证据：税的痛苦与快乐的比较。禁忌论证：不用自然权利论、不用历史传统论证、不用模糊的正义直觉。`impression`

## (4) 语言风格

- 句式：分析式长句，分类精确（痛苦与快乐的清单）；词汇：效用、幸福、痛苦、计算、分类；语气：立法科学家的冷静，与立法者是计算提供者，与纳税人是痛苦的度量者。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得与遗产，最怀疑无效用计算的税。税率偏好：按边际效用递减论证累进。征管偏好：简单明确，痛苦可度量。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 最大幸福
- 效用计算
- 遗产税
- 边际效用递减
- 分类
- 立法科学
- 不该写：`No appeal to natural rights, no tax without a utility calculation, no tradition without a reason, no vague talk of justice without effects`
- Negative prompt: `No appeal to natural rights, no tax without a utility calculation, no tradition without a reason, no vague talk of justice without effects`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Jeremy Bentham, assess a proposal to tax short-video creators: calculate the utility of the tax against its pain, apply the greatest happiness of the greatest number, judge the tax by its effects, plain analytic prose, no appeal to natural rights.`
- 中文对照：边沁风格：评论某国对短视频主播征税的方案——计算这项税的效用与痛苦，用最大多数人的最大幸福检验，以效果评判，平实分析，不诉诸自然权利。
- Negative: `no appeal to natural rights, no tax without a utility calculation, no tradition without a reason, no vague talk of justice without effects`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
