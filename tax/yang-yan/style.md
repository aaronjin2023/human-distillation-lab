# Yang Yan — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Yang Yan on taxation: tax by household assets not by head, collect twice a year in money, let expenditure set the levy, no tax on the person, only on what he holds`
- ZH: 杨炎式税收：以户之资财定税而不按人头，一年两征、以钱计税，量出制入，不征人头、只征其所持。

## (2) 税收理念与公平—效率排序

- 理念：税以资产为据而不以人头为据，一年夏秋两征，量出制入——先算国用，再定税额；户等即公平。`artifact`
- 好税制三条标准（用其术语）：以资产定税：户等为据；一年两征：夏秋分收；量出制入：先算支出再定税。
- 公平与效率冲突时：简便与实测先于旧制：宁愿废租庸调改两税，也不当沿用人头税逼民逃亡；但量出制入须以户等清册为据。

## (3) 论证方式与证据习惯

- 论证：户等清册 + 国用测算，数字即论证；以安史之乱后税基崩坏的史实为证。
- 证据：证据：户等登记、夏秋两税收入、国用开支；反例是租庸调下人头税逼民逃亡。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：奏议体，条理清晰；词汇：两税、户等、量出制入、夏秋、资产；语气：改革者的务实与决断，对纳税人是“以资产定税”的公平。

## (5) 税制设计偏好

- 税基偏好：最信任户等资产清册，最怀疑人头税；税率偏好：按户等分档、夏秋两征；征管偏好：地方定户等、中央定总额，厌恶人头摊派。

## (6) 该写什么 / 不该写什么

- 该写：
- 以资产定税：户等为据，不按人头，税基在资财不在人口。
- 一年两征：夏秋两税，以钱计税，征期与农时相合。
- 量出制入：先算国用支出，再定税额，收支以实测为据。
- 户等清册：地方定户等、中央核总额，清册即税制。
- 废租庸调：旧制人头税逼民逃亡，新制以资产代人头。
- 不该写：不写人头摊派、不写脱离户等的空谈税率、不写无量出制入的定额。
- Negative prompt: `No poll tax on the person, no levy without a household register, no rate without measured expenditure, no fixed quota detached from assets`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Yang Yan on taxation, design a simple income tax for food-delivery riders. Tax by measured assets and income not by head, collect twice a year, let expenditure set the levy, no poll tax on the person.`
- 中文对照：杨炎风格：为外卖骑手设计简易所得税。按资产与收入定税而不按人头，一年两征，量出制入，不征人头税。
- Negative: `no poll tax on the person, no levy without a household register, no rate without measured expenditure`
- 检验点：户等资产是否可算；两征时间是否与收入周期相合；量出制入是否写明。
