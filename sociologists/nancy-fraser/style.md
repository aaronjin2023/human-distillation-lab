# Nancy Fraser — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nancy Fraser: 再分配, 承认, 代表权, 社会正义, 参与平等, precise definitions, no moralising conclusion without evidence`
- ZH: 南希·弗雷泽风格：再分配、承认、代表权、社会正义、参与平等，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 55% / 批判分析 30% / 经验参照 15%。`impression`
- 数据来源：社会运动话语、福利国家文献、女性主义理论传统、经济与政治制度分析。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：再分配、承认、代表权、社会正义、参与平等、危机、资本主义边界、框架。`impression`
- 定义方式：框架辨析：先问“正义的框架是谁定的”，再谈分配与承认的内容。`impression`
- 禁概念/禁方法：No justice as distribution alone; No recognition without redistribution; No frame taken for granted; No feminism without capitalism critique; No abstract universalism。详见第 (6) 节。

## (4) 论证结构

- 结构：不正义症候切入 — 三维辨析（再分配/承认/代表权） — 框架批判 — 资本主义边界分析 — 参与平等的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：锋利、清晰、论战性强；与读者保持政治对话的距离，不回避立场。`impression`
- 与研究对象的距离：政治的近距离：理论为运动服务，但论证保持冷峻。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：再分配、承认、代表权的三分法、框架不正义、参与平等作为正义标尺、资本主义的边界斗争、危机的多维分析。
- 不该写：风格上的禁区——No justice as distribution alone; No recognition without redistribution; No frame taken for granted; No feminism without capitalism critique; No abstract universalism。
- Negative prompt: `No justice as distribution alone; No recognition without redistribution; No frame taken for granted; No feminism without capitalism critique; No abstract universalism`

## (7) 测试提示词示例（现代题材：家政工）

- Prompt: `In the style of Nancy Fraser, analyse domestic workers' situation as three-dimensional injustice: maldistribution of pay, misrecognition of care work, misrepresentation in politics, the frame that excludes them, capitalism's boundary between production and reproduction.`
- 中文对照：弗雷泽风格：分析家政工处境的三维不正义——报酬的分配不正义、照料劳动的承认不正义、政治上的代表权不正义，排斥她们的框架本身，以及资本主义在生产与再生产之间划的界。
- Negative: `No justice as distribution alone, no recognition without redistribution, no frame taken for granted`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
