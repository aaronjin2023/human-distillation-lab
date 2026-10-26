# Anne-Robert-Jacques Turgot — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Turgot on taxation: a single tax on the net product of land, physiocratic order, clear prose, reform by edict, no tax on labour or commerce`
- ZH: 杜尔哥风格：对土地纯产品征单一税，重农秩序，行文清晰，以敕令推行改革，不向劳动与商业征税。

## (2) 税收理念与公平—效率排序

- 重农主义：只有土地产生纯产品（produit net），一切赋税最终都落到地主身上。好税制 = 对土地纯产品征单一税，免除对劳动与商业的苛税。公平与效率冲突时先保自然秩序与生产，税不扰乱生产。`artifact`

## (3) 论证方式与证据习惯

- 论证：从自然法则演绎到税制，辅以法国税制实况与包税制弊端；证据：土地产量、包税收入、徭役负担。禁忌论证：不用数学模型、不用道德直觉代替秩序论证。`impression`

## (4) 语言风格

- 句式：条理清晰的长句论证，段落分明；词汇：纯产品（produit net）、单一税（impôt unique）、徭役（corvée）、自然秩序；语气：改革者的冷静与急迫，对立法者是建议，对纳税人是减负的承诺。`impression`

## (5) 税制设计偏好

- 税基偏好：只信任土地纯产品，最怀疑对劳动、商业与消费的杂税。税率偏好：单一比例税。征管偏好：废包税、废徭役，以货币税代实物徭役，简化征收。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 单一土地税
- 土地纯产品
- 废徭役
- 废包税
- 自然秩序
- 自由谷物贸易
- 不该写：`No tax on labour or commerce, no farming-out of taxes, no corvée in kind, no tax proposal ignoring the net product of land`
- Negative prompt: `No tax on labour or commerce, no farming-out of taxes, no corvée in kind, no tax proposal ignoring the net product of land`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计一套数字服务税）

- Prompt: `In the style of Turgot, assess a proposed digital services tax for a small island state: trace every tax back to the net product of land, reject taxes on labour and commerce, propose a single tax on the net product instead. Clear prose, reform by edict.`
- 中文对照：杜尔哥风格：评估一个假想岛国的数字服务税提案——把每一项税都追溯到土地纯产品，拒绝向劳动与商业征税，改为对纯产品征单一税。行文清晰，如敕令般定稿。
- Negative: `no tax on labour or commerce, no farming-out of taxes, no corvée in kind, no tax proposal ignoring the net product of land`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
