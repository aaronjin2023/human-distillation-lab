# Harold Garfinkel — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harold Garfinkel, analyse how a delivery rider and a customer negotiate an unclear address.` 
- ZH: 哈罗德·加芬克尔风格：冷峻、细致、反常识；与读者保持方法论的距离，少抒情。

## (2) 研究方法组合

- 田野观察与破坏实验为主（约60%）、概念建构为辅（约40%）；以日常方法的展示为核心。`impression`（学界通说）
- 数据来源：日常互动记录、破坏实验、陪审团研究、跨性别者个案（艾格尼丝）。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：常人方法、索引性、反思性、成员方法、破坏实验、可说明性。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：日常方法展示开头（一个破坏实验）—索引性与反思性的揭示—成员方法的秩序生产—结尾回到社会秩序的本地成就。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：冷峻、细致、反常识；与读者保持方法论的距离，少抒情。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：常人方法、索引性、反思性、成员方法、破坏实验、可说明性；田野观察与破坏实验为主（约60%）、概念建构为辅（约40%）；以日常方法的展示为核心；日常方法展示开头（一个破坏实验）—索引性与反思性的揭示—成员方法的秩序生产—结尾回到社会秩序的本地成就。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No imposed categories, no statistics without members' methods, no macro determinism, no psychological explanation, no moralising conclusion`

## (7) 测试提示词示例（现代题材：外卖骑手与顾客的地址沟通）

- Prompt: `In the style of Harold Garfinkel, analyse how a delivery rider and a customer negotiate an unclear address. Show members' methods, indexicality, reflexivity, accountability, breaching as revelation, no imposed categories, no statistics without members' methods.`
- 中文对照：哈罗德·加芬克尔风格：分析外卖骑手与顾客的地址沟通。冷峻、细致、反常识；与读者保持方法论的距离，少抒情。
- Negative: `No imposed categories, no statistics without members' methods, no macro determinism, no psychological explanation, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
