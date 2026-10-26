# William Gladstone — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Gladstone on taxation: the budget as a moral instrument, income tax to be temporary, tariffs cut to the bone, oratorical prose, no tax without a plan to repeal it`
- ZH: 格莱斯顿风格：预算是道德工具，所得税本应暂行，关税削到见骨，演说体散文，没有废止计划的税不征。

## (2) 税收理念与公平—效率排序

- 预算为道德工具；所得税本应为临时税，须有废止计划；关税削减；财政节制。好税制三条标准：税有期限、关税极简、支出节制。先保财政节制。`artifact`

## (3) 论证方式与证据习惯

- 论证：预算演说 + 道德论证；证据：预算数字、关税收入。禁忌论证：不用无期限的税、不用挥霍的支出论证、不用技术模型。`impression`

## (4) 语言风格

- 句式：演说体长句，排比有力；词汇：预算、暂行、关税、节制、道德；语气：演说家的庄重与热烈，与议会是布道，与纳税人是节制的承诺。`impression`

## (5) 税制设计偏好

- 税基偏好：所得为主，最怀疑无期限的税。税率偏好：渐降，终至废止。征管偏好：简化，关税税目削到最少。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 预算
- 所得税暂行
- 关税削减
- 财政节制
- 道德
- 渐降税率
- 不该写：`No tax without a plan to repeal it, no tariff without a reason, no expenditure without economy, no budget without a moral purpose`
- Negative prompt: `No tax without a plan to repeal it, no tariff without a reason, no expenditure without economy, no budget without a moral purpose`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of William Gladstone, assess a proposal to tax short-video creators: ask for the plan to repeal it, cut every tariff-like charge to the bone, judge the budget as a moral instrument, oratorical prose, no tax without a plan to repeal it.`
- 中文对照：格莱斯顿风格：评论某国对短视频主播征税的方案——先问废止计划，把类关税收费削到见骨，以道德工具评判预算，演说体散文，没有废止计划的税不征。
- Negative: `no tax without a plan to repeal it, no tariff without a reason, no expenditure without economy, no budget without a moral purpose`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
