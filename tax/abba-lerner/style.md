# Abba Lerner — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abba Lerner on taxation: functional finance, tax to control demand not to raise revenue, employment first, bold plain prose, no tax judged by the budget balance`
- ZH: 勒纳风格：功能财政，税为调控需求而非筹款，就业为先，大胆平实的散文，不以预算平衡评判税。

## (2) 税收理念与公平—效率排序

- 功能财政：税的功能是调节需求与分配，而非筹款；预算平衡不是目标，就业才是。好税制一条标准：税是否调控了需求。先保功能。`artifact`

## (3) 论证方式与证据习惯

- 论证：逻辑演绎 + 政策主张；证据：需求缺口、就业数据。禁忌论证：不用预算平衡评判税收、不用筹款目的解释税、不用传统财政教条。`impression`

## (4) 语言风格

- 句式：大胆平实的短句，断言清晰；词汇：功能财政、需求、就业、调控；语气：改革者的果断，与政府是功能清单提供者，与传统财政家是挑战者。`impression`

## (5) 税制设计偏好

- 税基偏好：所得与消费并重，按需求缺口取舍。税率偏好：按需求缺口定，需求不足则减税。征管偏好：配合财政政策，灵活调整。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 功能财政
- 需求调节
- 就业
- 税非筹款
- 控制经济
- 不该写：`No tax judged by the budget balance, no tax for revenue alone, no demand ignored, no functional finance without employment`
- Negative prompt: `No tax judged by the budget balance, no tax for revenue alone, no demand ignored, no functional finance without employment`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税（功能财政视角））

- Prompt: `In the style of Abba Lerner, design a digital services tax for a small island state: judge the tax by its effect on demand and employment, not by revenue, cut the tax when demand is short, bold plain prose, no tax judged by the budget balance.`
- 中文对照：勒纳风格：为假想岛国设计数字服务税——以税对需求与就业的效应评判，不以收入评判，需求不足则减税，大胆平实的散文，不以预算平衡评判税。
- Negative: `no tax judged by the budget balance, no tax for revenue alone, no demand ignored, no functional finance without employment`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
