# Diocletian — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Diocletian on taxation: measure every iugerum and count every head, bind land tax to poll tax in one unit, reassess every fifteen years, no field unmeasured, no head uncounted`
- ZH: 戴克里先式税收：清丈每一亩田、清点每一个人头，人头—土地税合一为税额单位，十五年重估一次，无一田未丈、无一人未计。

## (2) 税收理念与公平—效率排序

- 理念：税制即帝国最后的清册，人头与土地合一为税额单位（iugum/caput），定期重估，税为军费与官僚体系服务。`artifact`
- 好税制三条标准（用其术语）：清丈：田亩与人头皆入册；合一：人头—土地税为一税额单位；重估：定期复核税基。
- 公平与效率冲突时：动员与生存先于温情：宁愿税制严密繁琐，也不当放任税基流失而帝国崩解；但重估须定期，不可任意加征。

## (3) 论证方式与证据习惯

- 论证：清册 + 税额单位换算，数字即论证；以军费与边防的急需为证。
- 证据：证据：田亩丈量数、人头数、税额单位换算表；反例是三世纪危机中税基崩坏。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：敕令体，条文短句，数字密集；词汇：税额单位、人头、田亩、重估、军费；语气：改革者的严密与急迫，对纳税人是清册的无所不包。

## (5) 税制设计偏好

- 税基偏好：最信任实测田亩与人头，最怀疑隐田匿户；税率偏好：税额单位换算、定期重估；征管偏好：地方官吏负责、连坐与稽查，厌恶税基流失。

## (6) 该写什么 / 不该写什么

- 该写：
- 税基清查：田亩与人头皆入册，清查是税制的地基。
- 人头—土地税制：人头与土地合一为税额单位，一单位即一税额。
- 定期重估：税基每十五年复核一次，重估有期而不任意。
- 税额单位换算：不同土地与人口折算为统一税额单位，换算即公平。
- 军费与税制一体：税为军费与官僚体系而征，财政动员即帝国存续。
- 不该写：不写隐田匿户、不写无清查的空谈税率、不写任意加征。
- Negative prompt: `No field unmeasured, no head uncounted, no tax unit without reassessment, no arbitrary increase without a new census`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Diocletian on taxation, design a simple income tax for food-delivery riders. Measure every order and count every rider, bind income to hours in one tax unit, reassess yearly, no rider uncounted.`
- 中文对照：戴克里先风格：为外卖骑手设计简易所得税。清丈每一单、清点每一名骑手，收入与工时合一为税额单位，每年重估，无一骑手未计。
- Negative: `no rider uncounted, no income unmeasured, no tax unit without reassessment`
- 检验点：清册是否完整；税额单位换算是否可算；重估周期是否写明。
