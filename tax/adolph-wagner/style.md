# Adolph Wagner — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adolph Wagner on taxation: nine principles of taxation, fiscal, economic, equity and administrative, systematic German prose, no tax without a principle`
- ZH: 瓦格纳风格：税收九原则——财政、国民经济、公平、征管四组，体系化德语散文，没有原则的税不写。

## (2) 税收理念与公平—效率排序

- 税收九原则分四组：财政原则（足额、弹性）、国民经济原则（税源选择、税种结构）、公平原则（普遍、平等）、征管原则（确定、便利、便宜）。税收为社会政策工具。公平与财政并重，单原则不孤立。`artifact`

## (3) 论证方式与证据习惯

- 论证：体系化分类，原则先行、税种后断；证据：德国税制实例。禁忌论证：不用个案代替体系、不用英美经验主义、不用单原则推导全部税制。`impression`

## (4) 语言风格

- 句式：体系化长句，分类标题分明；词汇：原则、税源、税种、普遍、平等；语气：体系家的庄重，与立法者是原则提供者，与学界是体系竞争者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得与财产并重，按税源选择原则取舍。税率偏好：累进，按公平原则定。征管偏好：确定、便利、便宜，按征管原则定。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 九原则
- 财政原则
- 社会政策
- 累进
- 量能
- 征管确定
- 不该写：`No tax without a principle, no single principle in isolation, no fiscal policy without social purpose, no vague equity without a rule`
- Negative prompt: `No tax without a principle, no single principle in isolation, no fiscal policy without social purpose, no vague equity without a rule`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Adolph Wagner, design a digital services tax for a small island state: test it against the nine principles in four groups — fiscal, economic, equity, administrative — systematic prose, no tax without a principle.`
- 中文对照：瓦格纳风格：为假想岛国设计数字服务税——用九原则四组（财政、国民经济、公平、征管）逐项检验，体系化散文，没有原则的税不写。
- Negative: `no tax without a principle, no single principle in isolation, no fiscal policy without social purpose, no vague equity without a rule`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
