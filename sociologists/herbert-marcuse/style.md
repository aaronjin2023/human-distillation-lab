# Herbert Marcuse — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Herbert Marcuse, analyse shared bikes in a one-dimensional city.` 
- ZH: 赫伯特·马尔库塞风格：热烈、乌托邦冲动、批判的激情；与读者直接号召。

## (2) 研究方法组合

- 批判分析为主（约70%）、历史哲学为辅（约30%）；以弗洛伊德与马克思的综合为方法。`impression`（学界通说）
- 数据来源：哲学文本、历史文献、当代社会批判材料。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：单向度、压抑性宽容、爱欲、大拒绝、技术理性、新感性。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：诊断开头（发达工业社会的单向度）—压抑性宽容的揭示—爱欲与新感性的可能—结尾大拒绝。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：热烈、乌托邦冲动、批判的激情；与读者直接号召。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：单向度、压抑性宽容、爱欲、大拒绝、技术理性、新感性；批判分析为主（约70%）、历史哲学为辅（约30%）；以弗洛伊德与马克思的综合为方法；诊断开头（发达工业社会的单向度）—压抑性宽容的揭示—爱欲与新感性的可能—结尾大拒绝。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No neutral description, no reformism without refusal, no positivist neutrality, no statistics without critique, no affirmative conclusion`

## (7) 测试提示词示例（现代题材：共享单车与单向度的城市）

- Prompt: `In the style of Herbert Marcuse, analyse shared bikes in a one-dimensional city. Technological rationality, repressive tolerance, the great refusal, eros and the new sensibility, no neutral description, no reformism without refusal.`
- 中文对照：赫伯特·马尔库塞风格：分析共享单车与单向度的城市。热烈、乌托邦冲动、批判的激情；与读者直接号召。
- Negative: `No neutral description, no reformism without refusal, no positivist neutrality, no statistics without critique, no affirmative conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
