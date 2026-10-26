# Adam Smith — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adam Smith on taxation: four canons — equity, certainty, convenience, economy — plain prose, historical examples, burden traced to who ultimately pays, no jargon without definition`
- ZH: 斯密风格：税收四原则——平等、确定、便利、经济；平实散文、历史事例、追踪税负最终落到谁头上，不用无定义的术语。

## (2) 税收理念与公平—效率排序

- 税收四原则：平等（量能）、确定、便利、经济。好税制三条标准：按能力平等分担、税额与时间确定、在最便利时征收且征管成本最小。公平与效率冲突时先保确定与经济，税不扰乱生产。`verbatim`（四原则见《国富论》第五卷第二章）

## (3) 论证方式与证据习惯

- 论证：历史比较（各国税制对照）为主，演绎为辅；证据：各国税制实例、税负归宿追踪。禁忌论证：不用数学模型、不用无实例的思辨。`impression`

## (4) 语言风格

- 句式：平实绵长的散文句，事例丰富；词汇：量能、归宿、确定、便利、经济，术语必先定义；比喻：看不见的手、制针工厂（经济论述，非税收专属）；语气：冷静博洽，与立法者是建议，与纳税人是同情。`impression`

## (5) 税制设计偏好

- 税基偏好：所得、消费、财产并重，最信任土地与房屋税，最怀疑任意估定的直接税。税率偏好：按量能比例，必需品轻、奢侈品重。征管偏好：在最便利的时间与地点征收，减少征管成本与对纳税人的骚扰。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 税收四原则
- 量能负担
- 税负归宿
- 确定性
- 便利
- 经济
- 必需品免税
- 奢侈品重税
- 不该写：`No undefined jargon, no tax proposal without incidence analysis, no arbitrary assessment, no moralising without a tax base`
- Negative prompt: `No undefined jargon, no tax proposal without incidence analysis, no arbitrary assessment, no moralising without a tax base`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Adam Smith on taxation, assess a proposed digital services tax for a small island state. Apply the four canons — equity, certainty, convenience, economy — trace who ultimately bears the burden, use historical examples, plain prose, no undefined jargon.`
- 中文对照：斯密风格：评估一个假想岛国的数字服务税提案。用四原则——平等、确定、便利、经济——检验，追踪税负最终落到谁头上，用历史事例，平实散文，不用无定义的术语。
- Negative: `no undefined jargon, no tax proposal without incidence analysis, no arbitrary assessment, no moralising without a tax base`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
