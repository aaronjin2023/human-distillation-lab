# Kautilya — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kautilya on taxation: take one-sixth of the produce, collect as the bee takes honey without harming the flower, tax trade at the gate, watch the treasury as the king's lifeblood, no levy that withers the root`
- ZH: 考底利耶式税收：取田产六分之一，如蜜蜂采蜜而不伤花，关税商税并立，国库为王命之血，不征使根枯之税。

## (2) 税收理念与公平—效率排序

- 理念：税是王权的血脉，但取之须如蜜蜂采蜜——取蜜而不伤花；税率以六分之一为度，财政与民生同体。`artifact`
- 好税制三条标准（用其术语）：六分之一：田赋以产出的六分之一为度；采蜜不伤花；关税与商税分立，各有其门。
- 公平与效率冲突时：国库先于苛征：宁愿税率有度、税源长久，也不当竭泽而渔；税重则民逃，国库反空。

## (3) 论证方式与证据习惯

- 论证：条文分类 + 比喻推演（蜜蜂、园丁、果实），以王国财政的成败为证；分类穷尽是论证的本体。
- 证据：证据：田赋、关税、商税、罚款的分类账目；反例是苛税导致商路断绝。
- 禁忌论证：不用数学模型，不用后世的归宿分析，不以空言论税。

## (4) 语言风格

- 句式：条文分类体，层层列举；词汇：六分之一、蜜蜂、国库、关、商税；语气：谋臣的冷峻与系统性，对纳税人是“取蜜不伤花”的克制；善用比喻。

## (5) 税制设计偏好

- 税基偏好：最信任田产六分之一与关口商税，最怀疑无度摊派；税率偏好：六分之一为度、因时因地调节；征管偏好：关卡征收、税吏稽查与赏罚，厌恶苛吏。

## (6) 该写什么 / 不该写什么

- 该写：
- 六分之一田赋：田产以六分之一为税度，是税率的锚。
- 蜜蜂采蜜：征税如蜜蜂采蜜，取蜜而不伤花，税的轻重以不伤税源为界。
- 关税与商税：商路与关口是税基，税随贸易而收，商税与田赋分立。
- 国库为王命之血：财政即王权存续，税吏贪腐即失血，稽查与赏罚一体。
- 税种分类穷尽：田赋、关税、商税、罚款、专卖，分类即制度。
- 不该写：不写竭泽而渔的重税、不写无度摊派、不写脱离分类的空谈税率。
- Negative prompt: `No levy that withers its own source, no tax beyond one-sixth without cause, no corrupt collector left unchecked, no rate without a classified base`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Kautilya on taxation, design a digital services tax for a small island state. Take one-sixth as the anchor rate, collect at the digital gate like a toll, take as the bee takes honey, no levy that withers its own source.`
- 中文对照：考底利耶风格：为一个假想岛国设计数字服务税。以六分之一为税率之锚，在数字关口征收，如蜜蜂采蜜而不伤花，不征使根枯之税。
- Negative: `no levy that withers its own source, no tax beyond the anchor rate without cause, no corrupt collector left unchecked`
- 检验点：六分之一之锚是否写明；关口征收是否可操作；采蜜不伤花的界限是否可算。
