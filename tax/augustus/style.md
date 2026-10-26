# Augustus — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Augustus on taxation: count every head and every field, tax the provinces by census, let inheritance and sales pay for the legions, no province outside the register`
- ZH: 奥古斯都式税收：人口普查与行省税制并立，按册征税，遗产税与间接税供养军团，无一行省在册外。

## (2) 税收理念与公平—效率排序

- 理念：帝国税制即普查与行省清册，税按人头与田产计，间接税供养常备军；税制统一即帝国统一。`artifact`
- 好税制三条标准（用其术语）：普查：人头与田产皆入册；行省税制：各省按册定额；遗产税与间接税：以间接税养军。
- 公平与效率冲突时：统一与稳定先于地方旧制：宁愿以普查与定额统一各省税制，也不当放任包税人横征；但定额须以清册为据。

## (3) 论证方式与证据习惯

- 论证：普查清册 + 行省定额，数字即论证；以军团军饷的急需为证。
- 证据：证据：人口普查数、行省定额、遗产税收入；反例是共和末期包税人之弊。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：诏令与敕令体，条文短句；词汇：普查、行省、遗产税、间接税、军团；语气：帝国缔造者的秩序与克制，对纳税人是清册与定额的确定。

## (5) 税制设计偏好

- 税基偏好：最信任普查清册与行省田产，最怀疑包税人的任意摊派；税率偏好：行省定额、遗产税比例；征管偏好：官吏直征取代包税，厌恶包税横征。

## (6) 该写什么 / 不该写什么

- 该写：
- 人口普查：人头与田产皆入册，普查即税基识别的本体。
- 行省税制：各省按清册定额，定额有据而不任意。
- 遗产税：以遗产税供养退伍军人，税与军饷挂钩。
- 间接税改革：以销售税与关税养军团，间接税为常备军之源。
- 废包税改官征：官吏直征取代包税人，征管即秩序。
- 不该写：不写包税人任意摊派、不写无普查的空谈税率、不写脱离军饷的税制。
- Negative prompt: `No province outside the census, no tax farming without a fixed quota, no rate without a register, no levy detached from the legions' pay`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Augustus on taxation, design a digital services tax for a small island state. Census every platform and user, tax by register, let the levy pay for public service, no province outside the register.`
- 中文对照：奥古斯都风格：为一个假想岛国设计数字服务税。普查每一个平台与用户，按册征税，税款供养公共服务，无一平台在册外。
- Negative: `no platform outside the census, no tax farming without a fixed quota, no rate without a register`
- 检验点：普查清册是否完整；定额是否有据；军饷挂钩是否可算。
