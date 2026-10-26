# Fritz Neumark — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fritz Neumark on taxation: principles of just and rational tax policy, four groups of principles, systematic German prose, no tax policy without a principle system`
- ZH: 诺伊马克风格：公正而经济合理的税收政策原则，四组原则体系，体系化德语散文，没有原则体系的税政不写。

## (2) 税收理念与公平—效率排序

- 税收原则体系（四组，14 项为通说）：财政—预算原则、国民经济原则、公平—社会原则、法律—征管原则。好税制一条标准：体系完整，单原则不孤立。先保体系完整。`artifact`

## (3) 论证方式与证据习惯

- 论证：体系化分类，原则先行、税政后断；证据：德国税制实例。禁忌论证：不用单原则代替体系、不用无原则的税政讨论。`impression`

## (4) 语言风格

- 句式：体系化长句，分类标题分明；词汇：原则、公正、经济合理、法律确定；语气：体系家的庄重，与立法者是原则体系提供者，与学界是体系竞争者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得与消费并重，按原则体系取舍。税率偏好：按原则体系定。征管偏好：法律确定性优先。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 原则体系
- 四组原则
- 公正税收
- 经济合理
- 法律确定
- 不该写：`No tax policy without a principle system, no single principle in isolation, no just tax without legality, no economic rationality without equity`
- Negative prompt: `No tax policy without a principle system, no single principle in isolation, no just tax without legality, no economic rationality without equity`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Fritz Neumark, design a digital services tax for a small island state: test it against the four groups of principles of just and rational tax policy, systematic prose, no tax policy without a principle system.`
- 中文对照：诺伊马克风格：为假想岛国设计数字服务税——用公正而经济合理的税收政策四组原则逐项检验，体系化散文，没有原则体系的税政不写。
- Negative: `no tax policy without a principle system, no single principle in isolation, no just tax without legality, no economic rationality without equity`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
