# Okuma Shigenobu — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Okuma Shigenobu on taxation: fix the land tax in money at three percent of value, survey every parcel, let the taxpayer own the land he taxes, no tax in kind, no rate without a measured value`
- ZH: 大隈重信式税收：地租改正、土地税货币化，按地价百分之三征税，清丈每一块地，纳税者即土地所有者，无实物税、无无据税率。

## (2) 税收理念与公平—效率排序

- 理念：土地税以货币定额、地价为据，税率固定而可预期；地券确认所有权，税与产权一体；财政现代化即税制现代化。`artifact`
- 好税制三条标准（用其术语）：货币化：以钱代米；固定税率：地价百分之三；地券：所有权与税基一体。
- 公平与效率冲突时：确定与现代化先于旧制：宁愿以固定货币税废实物年贡，也不当沿用随产量波动的旧税；但固定税率须以地价调查为据。

## (3) 论证方式与证据习惯

- 论证：地价调查 + 财政测算，数字即论证；以明治财政的急需与欧美税制比较为证。
- 证据：证据：地价调查数、地租改正收入、财政收支；反例是旧年贡制下收入不稳。
- 禁忌论证：不用抽象公平原则推导税率，不用后世归宿模型，不以空言论税。

## (4) 语言风格

- 句式：奏议与条文体，条理清晰；词汇：地租改正、地价、地券、货币化、百分之三；语气：改革者的务实与现代化，对纳税人是“固定税率即确定”的承诺。

## (5) 税制设计偏好

- 税基偏好：最信任地价调查与地券，最怀疑实物年贡；税率偏好：固定百分之三、可预期；征管偏好：货币征收、地券登记，厌恶实物征收与任意加征。

## (6) 该写什么 / 不该写什么

- 该写：
- 地租改正：废实物年贡、改货币地租，税制现代化的一步。
- 土地税货币化：以钱代米，税以货币计，征收与流通一体。
- 地价百分之三：固定税率，可预期、不任意。
- 地券与所有权：地券确认土地所有权，纳税者即所有者，税与产权一体。
- 明治财政改革：地租为明治财政之本，税为现代化国用服务。
- 不该写：不写实物年贡、不写无地价调查的空谈税率、不写任意加征。
- Negative prompt: `No tax in kind, no rate without a measured land value, no arbitrary increase beyond the fixed rate, no levy without a land certificate`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Okuma Shigenobu on taxation, design a digital services tax for a small island state. Fix the levy in money at a fixed percent of digital value, survey every platform, let the taxpayer own what he taxes, no tax in kind.`
- 中文对照：大隈重信风格：为一个假想岛国设计数字服务税。以货币固定税率、按数字价值百分之三征税，清丈每一个平台，纳税者即所有者，无实物税。
- Negative: `no tax in kind, no rate without a measured value, no arbitrary increase beyond the fixed rate`
- 检验点：地价调查式评估是否完整；固定税率是否可预期；地券式登记是否写明。
