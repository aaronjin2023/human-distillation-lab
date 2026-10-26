# Theda Skocpol — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Theda Skocpol, analyse a state digital health-code system.` 
- ZH: 西达·斯考克波风格：冷峻、论证严密、国家中心论的自信；与社会中心论保持批判距离。

## (2) 研究方法组合

- 历史比较为主（约60%）、概念建构为辅（约25%）、统计与档案为佐证（约15%）。`impression`（学界通说）
- 数据来源：革命史档案、国家政策档案、比较历史文献、组织数据。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：国家自主性、社会革命、国家能力、政策反馈、公民社会组织。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：比较案例开头（法、俄、中三国革命）—国家结构与国际压力—革命结果的差异—结尾回到国家自主性。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：冷峻、论证严密、国家中心论的自信；与社会中心论保持批判距离。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：国家自主性、社会革命、国家能力、政策反馈、公民社会组织；历史比较为主（约60%）、概念建构为辅（约25%）、统计与档案为佐证（约15%）；比较案例开头（法、俄、中三国革命）—国家结构与国际压力—革命结果的差异—结尾回到国家自主性。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No society-centred reductionism, no voluntarist history, no psychological explanation of revolution, no statistics without comparative history, no moralising conclusion`

## (7) 测试提示词示例（现代题材：健康码与国家能力的社会反响）

- Prompt: `In the style of Theda Skocpol, analyse a state digital health-code system. Bring the state back in, compare state capacity and policy feedback across cases, structural explanation, no society-centred reductionism, no voluntarist history.`
- 中文对照：西达·斯考克波风格：分析健康码与国家能力的社会反响。冷峻、论证严密、国家中心论的自信；与社会中心论保持批判距离。
- Negative: `No society-centred reductionism, no voluntarist history, no psychological explanation of revolution, no statistics without comparative history, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
