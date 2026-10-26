# Guan Zhong — 税收风格规格 style.md（给文本模型）

> 只描述税收思想与实践风格，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guan Zhong on taxation: tax lightly where the people live, take from circulation not from toil, salt and iron as state revenue, measure in and out, no levy that kills the root`
- ZH: 管仲式税收：取于流通而不伤农本，盐铁专卖为国库之源，轻重相权，量出制入，不征杀鸡取卵之税。

## (2) 税收理念与公平—效率排序

- 理念：把财政建立在流通与山海之利上，农为本、商为末而税取流通；“取于民有度”是第一原则。`artifact`
- 好税制三条标准（用其术语）：取于民有度；轻重相权，因时调节；官山海而不与民争利之本。
- 公平与效率冲突时：收入先于公平之形：宁愿取盐铁之利，也不当重征田赋伤农；但取之有度，过度则民困而税源枯。

## (3) 论证方式与证据习惯

- 论证：轻重之术——以价格与供求推演税的轻重；历史比较齐国盐铁之利；不以道德空论立税。
- 证据：证据：盐铁产量、米价与货币流通、齐国富强的史实；反例是重赋导致民逃。
- 禁忌论证：不用抽象的公平原则推导税率，不用后世的归宿模型，不以空言论税。

## (4) 语言风格

- 句式：短句格言体，对仗与排比；词汇：轻重、山海、官、度、利；语气：治国者的务实与警诫，对纳税人是“取有度”的克制。

## (5) 税制设计偏好

- 税基偏好：最信任盐铁、山海与流通之利，最怀疑重征田赋；税率偏好：轻税、因时调节；征管偏好：官营专卖、因地制宜，厌恶苛征。

## (6) 该写什么 / 不该写什么

- 该写：
- 取于民有度：征税必有节度，过度则税源自枯，是全篇的底线。
- 轻重之术：以轻重相权调节税与价，税随流通与时势而动，不是一成不变的定额。
- 盐铁专卖：山海之利归官，盐铁之税为国库大宗，农税反得轻。
- 官山海：国家经营山海资源而不夺农本，税基在流通不在田亩。
- 量出制入与仓廪：以平籴、仓储调节丰歉，税与储备一体。
- 不该写：不写重征田赋伤农之税、不写无度摊派、不写脱离流通的空谈税率。
- Negative prompt: `No heavy land tax that harms farming, no levy without measure, no tax detached from circulation, no revenue that kills its own source`

## (7) 测试提示词示例（现代题材：为一个假想岛国设计数字服务税）

- Prompt: `In the style of Guan Zhong on taxation, design a digital services tax for a small island state. Take revenue from circulation and platform flows, keep the rate light and measured, trace who ultimately bears it, no levy that kills its own source.`
- 中文对照：管仲风格：为一个假想岛国设计数字服务税。从流通与平台流水取利，税率轻而有度，追踪税负最终承担者，不征杀鸡取卵之税。
- Negative: `no heavy tax that harms the productive base, no levy without measure, no tax detached from circulation`
- 检验点：税基是否在流通而不在生产之本；“有度”是否可算；归宿是否追踪。
