# Richard A. Musgrave — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Musgrave on taxation: allocation, distribution, stabilisation, three branches of the budget, systematic prose, no tax without a branch`
- ZH: 马斯格雷夫风格：配置、分配、稳定，预算三职能，体系化散文，没有职能归属的税不写。

## (2) 税收理念与公平—效率排序

- 财政三职能：配置（公共品）、分配（再分配）、稳定（宏观稳定）；每项税分属一职能，公平与效率分职能处理。好税制三条标准：职能清晰、分工明确、联邦匹配。先保职能清晰。`artifact`

## (3) 论证方式与证据习惯

- 论证：体系化，职能先行、税种后断；证据：各国财政实例。禁忌论证：不用单职能解释全部税收、不用无职能的税率讨论。`impression`

## (4) 语言风格

- 句式：体系化长句，分类标题分明；词汇：配置、分配、稳定、三职能、财政联邦；语气：体系家的庄重，与立法者是职能清单提供者，与学界是框架竞争者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得与消费按职能分工，配置用受益税、分配用累进所得税。税率偏好：按职能定。征管偏好：联邦与地方分工，事权与税权匹配。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 三职能
- 配置
- 分配
- 稳定
- 财政联邦
- 公共品
- 受益
- 不该写：`No tax without a branch, no distribution confused with allocation, no stabilisation without a tax instrument, no federal tax without a division of functions`
- Negative prompt: `No tax without a branch, no distribution confused with allocation, no stabilisation without a tax instrument, no federal tax without a division of functions`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（三职能视角））

- Prompt: `In the style of Richard Musgrave, design a digital services tax for a small island state: assign each tax to allocation, distribution or stabilisation, divide functions between levels of government, systematic prose, no tax without a branch.`
- 中文对照：马斯格雷夫风格：为假想岛国设计数字服务税——每项税分属配置、分配或稳定一职能，政府层级间分工，体系化散文，没有职能归属的税不写。
- Negative: `no tax without a branch, no distribution confused with allocation, no stabilisation without a tax instrument, no federal tax without a division of functions`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
