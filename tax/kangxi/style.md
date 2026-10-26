# Kangxi — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kangxi on taxation: freeze the poll tax forever, let the people multiply without new levies, remit grain in famine, no new tax on a newborn head`
- ZH: 康熙式税收：盛世滋生人丁永不加赋，人丁税额冻结，灾年蠲免钱粮，新生人丁不加新税。

## (2) 税收理念与公平—效率排序

- 理念：税以人丁旧额为限，滋生人丁永不加赋；税不可随人口增长而增长，蠲免即仁政。`artifact`
- 好税制三条标准（用其术语）：永不加赋：人丁税额冻结；滋生不加：人口增长不加税；蠲免：灾年免钱粮。
- 公平与效率冲突时：与民休息先于收入增长：宁愿冻结人丁税额少收，也不当随人口增长加税；但冻结须以田赋为后盾。

## (3) 论证方式与证据习惯

- 论证：诏令 + 人丁税额册，数字即论证；以人口滋生与社会安定的史实为证。
- 证据：证据：人丁税额册、蠲免记录、人口数字；反例是人头税随人口增长逼民逃亡。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：诏令体，庄重简洁；词汇：永不加赋、人丁、蠲免、滋生、钱粮；语气：帝王的仁厚与决断，对纳税人是“永不加赋”的承诺。

## (5) 税制设计偏好

- 税基偏好：最信任冻结的人丁旧额与田赋，最怀疑随人口加税；税率偏好：冻结、不随人口增长；征管偏好：诏令冻结、灾年蠲免，厌恶人头加派。

## (6) 该写什么 / 不该写什么

- 该写：
- 盛世滋生人丁永不加赋：人丁税额以康熙五十一年为限，永不加赋，诏令即税制。
- 人丁税额冻结：税额冻结于旧册，人口增长不加税，冻结即公平。
- 蠲免钱粮：灾年免除钱粮，蠲免有诏、有册、有期。
- 滋生不加：新生人丁不加新税，税与人口脱钩。
- 田赋为后盾：人丁冻结之后，田赋为国用之本，税基在田不在人。
- 不该写：不写随人口加税、不写灾年照旧征收、不写无诏令的任意加派。
- Negative prompt: `No new tax on a newborn head, no poll tax beyond the frozen quota, no levy in a famine year without remission, no increase without an edict`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Kangxi on taxation, design a simple income tax for food-delivery riders. Freeze the levy per rider, let new riders join without new taxes, remit in lean months, no new tax on a newborn rider.`
- 中文对照：康熙风格：为外卖骑手设计简易所得税。按骑手冻结税额，新骑手加入不加新税，淡月蠲免，新生骑手不加税。
- Negative: `no new tax on a new rider, no levy beyond the frozen quota, no tax in a lean month without remission`
- 检验点：冻结税额是否写明；新生不加是否可算；蠲免机制是否具体。
