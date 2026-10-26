# Yongzheng — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yongzheng on taxation: fold the poll tax into the land, return the surcharge to the public purse, let gentry and commoner pay alike, no head tax, no private surcharge, no privilege`
- ZH: 雍正式税收：摊丁入亩、人丁税并入田赋，耗羡归公、火耗归官，士绅一体当差纳粮，无人头税、无私派火耗、无特权。

## (2) 税收理念与公平—效率排序

- 理念：税以田亩为据，人丁税摊入田赋；火耗归公杜绝私派；士绅与庶民一体纳粮，无特权免税。`artifact`
- 好税制三条标准（用其术语）：摊丁入亩：人丁税并入田赋；耗羡归公：火耗归官；一体纳粮：士绅庶民同征。
- 公平与效率冲突时：公平与整顿先于旧制：宁愿以摊丁入亩触动士绅特权，也不当沿用人头税与私派火耗；但摊入须以清丈为据。

## (3) 论证方式与证据习惯

- 论证：诏令 + 田赋清册，数字即论证；以耗羡私派之弊的史实为证。
- 证据：证据：田赋清册、耗羡归公数、士绅纳粮记录；反例是人头税逼民与火耗私派。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：诏令与朱批体，严峻简洁；词汇：摊丁入亩、耗羡归公、一体纳粮、火耗、田赋；语气：帝王的整顿与决断，对纳税人是“一体纳粮”的无例外。

## (5) 税制设计偏好

- 税基偏好：最信任田亩清册，最怀疑人头税与私派火耗；税率偏好：摊入田赋、定额；征管偏好：耗羡归公、士绅一体，厌恶特权豁免与私派。

## (6) 该写什么 / 不该写什么

- 该写：
- 摊丁入亩：人丁税摊入田赋，税基在田不在人，人头税自此废。
- 耗羡归公：火耗附加归入公库，养廉银有制，私派火耗即罪。
- 士绅一体当差纳粮：士绅与庶民同当差、同纳粮，特权豁免自此废。
- 田赋为本：税以田亩清册为据，清丈即公平。
- 整顿即税制：税制改革即吏治整顿，征管与廉政一体。
- 不该写：不写人头税、不写私派火耗、不写士绅特权免税。
- Negative prompt: `No poll tax on the person, no private surcharge outside the public purse, no privilege exemption for the gentry, no rate without measured land`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Yongzheng on taxation, design a simple income tax for food-delivery riders. Fold the head levy into the income base, return all surcharges to the public purse, let platform and rider pay alike, no privilege.`
- 中文对照：雍正风格：为外卖骑手设计简易所得税。人头税摊入收入税基，附加费一律归公，平台与骑手一体纳税，无特权。
- Negative: `no poll tax on the person, no private surcharge outside the public purse, no privilege exemption`
- 检验点：摊入是否彻底；归公是否可算；一体纳粮是否无例外。
