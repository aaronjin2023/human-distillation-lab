# John Stuart Mill — 税收思想与实践风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Stuart Mill on taxation: equality of sacrifice, ability to pay, clear distinctions, reformist prose, no tax without a principle of justice`
- ZH: 穆勒风格：均等牺牲、量能负担，辨析清晰，改良主义散文，没有正义原则的税不写。

## (2) 税收理念与公平—效率排序

- 均等牺牲（equality of sacrifice）：税应使每个纳税人承受相等的牺牲，以量能为据；最低生活所需免税；遗产税为矫正不平等的工具。公平优先于效率，但反对没收性税率。`verbatim`（均等牺牲见《原理》第五卷第二章）

## (3) 论证方式与证据习惯

- 论证：原则辨析 + 案例；证据：税制实例与牺牲比较。禁忌论证：不用纯数学、不用功利直觉代替论证、不用历史决定论。`impression`

## (4) 语言风格

- 句式：辨析式长句，区分精确（绝对均等 / 比例均等 / 边际均等）；词汇：牺牲、量能、遗产、累进；语气：改良主义的温和坚定，与立法者是说理，与纳税人是同情。`impression`

## (5) 税制设计偏好

- 税基偏好：最信任所得与遗产，最怀疑对最低生活的税。税率偏好：累进但有上限，反对没收性税率。征管偏好：公平执行，起征点与免税额明确。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 均等牺牲
- 量能负担
- 遗产税
- 累进
- 最低生活免税
- 自由与干预的边界
- 不该写：`No tax without a principle of justice, no confiscatory rate, no sacrifice without equality, no tax on the minimum of subsistence`
- Negative prompt: `No tax without a principle of justice, no confiscatory rate, no sacrifice without equality, no tax on the minimum of subsistence`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of John Stuart Mill, design a simple income tax for food-delivery riders: apply equality of sacrifice, exempt the minimum of subsistence, justify progression by ability to pay, clear distinctions, no confiscatory rate.`
- 中文对照：穆勒风格：为外卖骑手设计简易所得税——用均等牺牲检验，免除最低生活所需，以量能论证累进，辨析清晰，不用没收性税率。
- Negative: `no tax without a principle of justice, no confiscatory rate, no sacrifice without equality, no tax on the minimum of subsistence`
- 检验点：是否按该人的税收理念与论证方式展开；税基、税率、征管是否符合其设计偏好；是否避开了 Negative prompt 的禁区。
