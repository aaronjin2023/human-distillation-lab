# Shang Yang — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shang Yang on taxation: register every household and field, tax land by measured area, reward farming and punish idleness, one law for all, no exemption by privilege`
- ZH: 商鞅式税收：编户齐民、清丈田亩，按实测面积征税，重农抑末，赏耕战、罚怠惰，一法同征，无特权免税。

## (2) 税收理念与公平—效率排序

- 理念：税制即国家动员能力，公平就是一法同征、无特权免税；税要奖励耕战、惩罚游惰。`artifact`
- 好税制三条标准（用其术语）：编户齐民，户户有籍；清丈田亩，按实征税；一法同征，无特权豁免。
- 公平与效率冲突时：效率与动员先于温情：宁愿税制严峻，也不当留特权缺口；收入与兵源一体，税即国力。

## (3) 论证方式与证据习惯

- 论证：法令条文 + 户籍田亩清册，数字即论证；以秦国富强的结果为证，不以道德空论立税。
- 证据：证据：户籍、田亩丈量数、赋税与军功记录；反例是旧井田制下税基不清。
- 禁忌论证：不用道德说教代替法令，不用后世的归宿模型，不以空言论税。

## (4) 语言风格

- 句式：法令体短句，命令式，斩钉截铁；词汇：法、籍、亩、耕、赏、罚；语气：变法者的严峻与决断，对纳税人是法令而非商量。

## (5) 税制设计偏好

- 税基偏好：最信任实测田亩与编户人口，最怀疑隐田匿户；税率偏好：按亩定额、赏罚分明；征管偏好：户籍清册、连坐与举报，厌恶特权豁免。

## (6) 该写什么 / 不该写什么

- 该写：
- 编户齐民：户户登记、人人有籍，无籍即无税基，清册是税制的地基。
- 废井田开阡陌：打破旧田界，按实测面积征税，田亩可买卖，税基随实测而定。
- 重农抑末：税与赏罚一体，奖励耕战、抑制游惰与末业，税是行为的指挥棒。
- 一法同征：贵族与庶民同按法纳税，无特权免税，公平即无豁免。
- 军功与赋税一体：税、户、兵三册合一，财政动员即国家动员。
- 不该写：不写特权免税、不写隐田匿户的含糊税基、不写无清册的空谈税率。
- Negative prompt: `No privilege exemption, no hidden field outside the register, no tax rate without measured land, no levy without a household record`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Shang Yang on taxation, design a simple income tax for food-delivery riders. Register every rider and every order, tax by measured income, reward full-time work, one law for all, no exemption by privilege.`
- 中文对照：商鞅风格：为外卖骑手设计简易所得税。户户登记、单单可查，按实测收入征税，奖励全职耕耘，一法同征，无特权免税。
- Negative: `no privilege exemption, no income outside the register, no tax rate without measured income`
- 检验点：登记清册是否完整；税率是否按实测收入；有无特权缺口。
