# Ibn Khaldun — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Khaldun on taxation: at the beginning of a dynasty taxation yields a large revenue from small assessments, at the end a small revenue from large assessments, watch the cycle, no rate that kills the base it taxes`
- ZH: 伊本·赫勒敦式税收：王朝之初小额征税而收入丰，王朝之末重额征税而收入微，观周期而定税率，不征杀死税基之税。

## (2) 税收理念与公平—效率排序

- 理念：税率与收入呈周期关系，王朝初税轻而收入丰、王朝末税重而收入微；税的轻重随王朝周期而变，奢侈即税基之敌。`artifact`
- 好税制三条标准（用其术语）：周期：税随王朝兴衰而变；轻税丰收：初税轻而收入丰；重税微收：末税重而收入微。
- 公平与效率冲突时：周期洞察先于静态税率：宁愿税率随周期下调，也不当在王朝末期加税加速崩解；但下调须以周期判断为据。

## (3) 论证方式与证据习惯

- 论证：历史比较（各王朝财政周期）+ 周期推演，以《历史绪论》的史实为证；周期即论证的本体。
- 证据：证据：各王朝税率与收入记录、奢侈与税基的关系；反例是王朝末期重税致税基崩坏。
- 禁忌论证：不用静态均衡模型，不用后世的拉弗曲线数学化，不以空言论税。

## (4) 语言风格

- 句式：历史论述体，长句缜密；词汇：王朝、周期、税率、收入、奢侈、阿萨比亚；语气：历史哲学家的冷峻与洞察，对纳税人是“观周期”的警示。

## (5) 税制设计偏好

- 税基偏好：最信任随周期而动的税基，最怀疑静态定额；税率偏好：初轻末警、随周期调节；征管偏好：以周期判断定征管松紧，厌恶末期加税。

## (6) 该写什么 / 不该写什么

- 该写：
- 王朝财政周期：税随王朝兴衰而变，周期即税制的时钟。
- 税率与收入关系：初小额而收入丰、末大额而收入微，税率与收入非线性。
- 轻税丰收：王朝之初税轻、民富、税基广，收入反丰。
- 重税微收：王朝之末税重、民困、税基窄，收入反微。
- 奢侈即税基之敌：统治者奢侈则加税，加税则税基枯，循环即崩解。
- 不该写：不写静态税率、不写末期加税、不写脱离周期的空谈税率。
- Negative prompt: `No rate that kills the base it taxes, no static rate across the dynastic cycle, no heavier levy at the end of a dynasty, no tax without a reading of the cycle`

## (7) 测试提示词示例（现代题材：评论某国对短视频主播征税的方案）

- Prompt: `In the style of Ibn Khaldun on taxation, assess a tax on short-video creators. Read the cycle of the platform first, tax lightly while it grows, never heavier as it ages, no rate that kills the base it taxes.`
- 中文对照：伊本·赫勒敦风格：评论对短视频主播征税的方案。先读平台的周期，成长时轻税，衰老时不加税，不征杀死税基之税。
- Negative: `no rate that kills the base it taxes, no static rate across the cycle, no heavier levy as the platform ages`
- 检验点：周期判断是否先行；轻税丰收是否可算；末期加税是否被拒绝。
