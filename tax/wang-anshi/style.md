# Wang Anshi — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wang Anshi on taxation: measure every field to equalise the tax, let the state lend at low interest instead of the usurer, hire labour instead of corvee, no field unmeasured, no tax without a measured base`
- ZH: 王安石式税收：方田均税、清丈每一亩，青苗低息贷于民而不使高利贷盘剥，募役雇人代徭役，无一田未丈、无一税无据。

## (2) 税收理念与公平—效率排序

- 理念：税以清丈为据，方田均税使富者不得隐田；国家以青苗贷平抑高利贷，以募役代徭役；理财即富国。`artifact`
- 好税制三条标准（用其术语）：方田均税：清丈定税；青苗法：官贷低息；募役法：雇人代役。
- 公平与效率冲突时：富国与均税先于旧制：宁愿以新法触动既得利益，也不当沿用隐田与徭役；但新法须以清丈为据，不可空征。

## (3) 论证方式与证据习惯

- 论证：清丈数字 + 借贷利率比较，数字即论证；以新法推行后的国库数字为证。
- 证据：证据：方田丈量数、青苗借贷数、募役雇值；反例是隐田逃税与徭役扰民。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：奏议与条文体，论证缜密；词汇：方田、均税、青苗、募役、理财；语气：变法者的坚决与系统性，对纳税人是“均税即公平”的说理。

## (5) 税制设计偏好

- 税基偏好：最信任清丈后的田亩，最怀疑隐田；税率偏好：按田等分档、青苗低息；征管偏好：官府丈量、官贷、雇役，厌恶隐田与徭役摊派。

## (6) 该写什么 / 不该写什么

- 该写：
- 方田均税：清丈田亩、按田等定税，隐田无处藏身，税基以实测为据。
- 青苗法：青黄不接时官府低息贷款，税与借贷一体，抑高利贷。
- 募役法：以钱雇人代徭役，役钱按户等出，徭役货币化。
- 理财即富国：国家经营财政以富国，税不是索取而是经营。
- 均税与抑兼并：税制即抑兼并的工具，富者不得以隐田逃税。
- 不该写：不写隐田逃税、不写高利贷盘剥、不写徭役摊派。
- Negative prompt: `No hidden field outside the survey, no usurious loan left to prey on farmers, no corvee without hire, no tax without a measured field`

## (7) 测试提示词示例（现代题材：为外卖平台骑手设计一套简易所得税）

- Prompt: `In the style of Wang Anshi on taxation, design a simple income tax for food-delivery riders. Survey every income stream, lend at low interest in lean months, hire instead of forcing free labour, no income unmeasured.`
- 中文对照：王安石风格：为外卖骑手设计简易所得税。清丈每一笔收入，淡月低息贷于骑手，雇人而不强征徭役，无一笔收入未丈。
- Negative: `no hidden income outside the survey, no usurious loan left to prey on riders, no tax without a measured base`
- 检验点：清丈是否完整；青苗式缓冲是否写明；募役式雇佣是否可算。
