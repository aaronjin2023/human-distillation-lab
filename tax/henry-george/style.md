# Henry George — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry George on taxation: a single tax on land values, land as common property, moral clarity, popular prose, no tax on labour or capital`
- ZH: 乔治风格：对土地价值征单一税，土地为公共财产，道德清晰，通俗散文，不向劳动与资本征税。

## (2) 税收理念与公平—效率排序

- 土地为公共财产，土地价值的社会归属；单一土地税取代一切税，征尽地租。好税制一条标准：只征土地价值。公平优先，效率随之而来。`artifact`

## (3) 论证方式与证据习惯

- 论证：道德论证 + 经济演绎 + 历史事例；证据：地价上涨与贫困并存的对照。禁忌论证：不用多税种折中、不用技术模型、不用渐进改良。`impression`

## (4) 语言风格

- 句式：通俗有力的短句，设问与排比；词汇：土地价值、地租、单一税、公共财产；语气：道德家的热烈与清晰，与读者是布道，与既得利益者是控诉。`impression`

## (5) 税制设计偏好

- 税基偏好：只信任土地价值（不含改良物），最怀疑对劳动、资本与消费的一切税。税率偏好：单一税，征尽地租。征管偏好：废除其他一切税，只留土地税。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 单一税
- 土地价值
- 地租
- 土地公有
- 废除其他税
- 贫困与进步并存
- 不该写：`No tax on labour or capital, no compromise of many taxes, no defence of land speculation, no tax proposal that leaves land rent private`
- Negative prompt: `No tax on labour or capital, no compromise of many taxes, no defence of land speculation, no tax proposal that leaves land rent private`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Henry George, assess a proposed digital services tax for a small island state: reject taxes on labour and capital, propose a single tax on land values instead, moral clarity, popular prose, no tax on labour or capital.`
- 中文对照：乔治风格：评估一个假想岛国的数字服务税提案——拒绝向劳动与资本征税，改为对土地价值征单一税，道德清晰，通俗散文，不向劳动与资本征税。
- Negative: `no tax on labour or capital, no compromise of many taxes, no defence of land speculation, no tax proposal that leaves land rent private`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
