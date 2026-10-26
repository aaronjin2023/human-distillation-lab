# Ancient Egyptian tax tradition — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the ancient Egyptian tax tradition: measure the land after the flood, tax the grain in kind, let the nilometer set the rate, no field unmeasured after the waters recede`
- ZH: 古埃及税制传统式税收：尼罗河泛滥后丈量土地，以谷物实物纳税，水位计定税率，洪水退后无一田未丈。

## (2) 税收理念与公平—效率排序

- 理念：税随尼罗河而定，泛滥后丈量、按水位定税；谷物实物税为国库之本，税与灌溉、仓储一体。`artifact`
- 好税制三条标准（用其术语）：泛滥后丈量：税基随河水而定；水位计定税率；谷物实物税为本。
- 公平与效率冲突时：实测先于定额：宁愿年年丈量繁琐，也不当按旧册定额征税；水位低则减税，税随天时而动。

## (3) 论证方式与证据习惯

- 论证：丈量记录 + 水位计读数，数字即论证；以仓廪与灌溉的史实为证。
- 证据：证据：土地丈量记录、水位计读数、谷物仓储数；反例是未丈量而按旧册征税致民怨。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：记录体短句，数字先行；词汇：丈量、水位、谷物、仓、徭役；语气：书记官的冷静与精确，对纳税人是“丈量即公平”的确定。

## (5) 税制设计偏好

- 税基偏好：最信任泛滥后实测土地与谷物产量，最怀疑旧册定额；税率偏好：按水位与产量调节；征管偏好：书记官丈量、谷物入仓、徭役并行，厌恶未丈先征。

## (6) 该写什么 / 不该写什么

- 该写：
- 泛滥后丈量：尼罗河退水后重丈土地，税基年年实测，旧册不作数。
- 水位计定税率：水位高则税重、水位低则税轻，税随天时而动。
- 谷物实物税：以谷物纳税入仓，仓廪即国库，税与储备一体。
- 徭役税：以劳役抵税，灌溉与工程即税的另一形态。
- 书记官与清册：丈量、记录、仓储三者一体，清册即税制。
- 不该写：不写未丈先征、不写脱离水位的定额税、不写无仓储的空谈税率。
- Negative prompt: `No tax before the land is measured, no fixed quota detached from the flood level, no levy without a granary record, no rate without a nilometer reading`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of the ancient Egyptian tax tradition, design a digital services tax for a small island state. Measure the digital harvest after each season, set the rate by the water level of traffic, tax in kind where possible, no tax before the land is measured.`
- 中文对照：古埃及税制传统风格：为一个假想岛国设计数字服务税。每季之后丈量数字收成，按流量水位定税率，能实物纳税即实物纳税，丈量之前不征税。
- Negative: `no tax before the harvest is measured, no fixed quota detached from the season, no levy without a granary record`
- 检验点：丈量是否先于税率；水位调节是否可算；仓储记录是否写明。
