# Jean-Baptiste Colbert — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Baptiste Colbert on taxation: tax trade at the gate and consumption in the town, spare the peasant's plough, let indirect taxes fill the treasury, no direct tax where an indirect tax will serve`
- ZH: 柯尔贝尔式税收：税贸易于关口、税消费于市镇，免农人之犁，间接税充国库，无间接税可用不征直接税。

## (2) 税收理念与公平—效率排序

- 理念：间接税优先，关税与消费税为国库之本；直接税伤农，间接税伤轻；税为重商主义与王权财政服务。`artifact`
- 好税制三条标准（用其术语）：间接税优先：关税与消费税为本；免农犁：直接税伤农；国库：税为王权财政服务。
- 公平与效率冲突时：间接税先于直接税：宁愿以关税与消费税充国库，也不当以直接税伤农；但间接税须以贸易与消费为据。

## (3) 论证方式与证据习惯

- 论证：贸易与消费统计 + 关税测算，数字即论证；以法国财政的急需为证。
- 证据：证据：关税收入、消费税记录、贸易统计；反例是直接税致农民逃亡。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：大臣奏议体，条理清晰、数字先行；词汇：柯尔贝尔主义、间接税、关税、专卖、贸易；语气：理财大臣的务实与决断，对纳税人是“间接税伤轻”的分际。

## (5) 税制设计偏好

- 税基偏好：最信任关税与消费税，最怀疑直接税与人头税；税率偏好：间接税为主、关税保护本国产业；征管偏好：关卡征收、专卖税，厌恶直接税摊派。

## (6) 该写什么 / 不该写什么

- 该写：
- 间接税优先：关税与消费税为国库之本，直接税为最后手段。
- 关税与专卖税：税贸易于关口，专卖税为国库大宗。
- 免农人之犁：直接税伤农，税基在贸易与消费不在田亩。
- 柯尔贝尔主义：税为重商主义服务，关税保护本国产业。
- 王权财政：税为王权与国用服务，财政即王权。
- 不该写：不写直接税伤农、不写无贸易依据的空谈税率、不写脱离王权财政的税制。
- Negative prompt: `No direct tax where an indirect tax will serve, no levy on the peasant's plough, no rate without trade and consumption figures, no tax detached from the treasury's need`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Jean-Baptiste Colbert on taxation, design a digital services tax for a small island state. Tax trade at the digital gate and consumption in the town, spare the small creator, no direct tax where an indirect tax will serve.`
- 中文对照：柯尔贝尔风格：为一个假想岛国设计数字服务税。税贸易于数字关口、税消费于市镇，免小主播之犁，无间接税可用不征直接税。
- Negative: `no direct tax where an indirect tax will serve, no levy on the small creator, no rate without trade figures`
- 检验点：间接税是否优先；关口征收是否可算；免农犁式保护是否具体。
