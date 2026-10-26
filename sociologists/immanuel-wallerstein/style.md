# Immanuel Wallerstein — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Immanuel Wallerstein, analyse the global supply chain of shared bikes as a world-system.` 
- ZH: 伊曼纽尔·沃勒斯坦风格：宏大、冷静、历史纵深感强；与民族国家分析框架保持批判距离。

## (2) 研究方法组合

- 历史比较为主（约60%）、概念建构为辅（约40%）；以长时段历史为材料，少用问卷统计。`impression`（学界通说）
- 数据来源：经济史、贸易史、殖民史文献、长时段历史数据。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：世界体系、核心—半边缘—边缘、长时段、历史体系、反体系运动、世界经济。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：单位批判开头（民族社会不是分析单位）—长时段历史铺陈—核心—边缘分工—结尾讨论体系危机与替代可能。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：宏大、冷静、历史纵深感强；与民族国家分析框架保持批判距离。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：世界体系、核心—半边缘—边缘、长时段、历史体系、反体系运动、世界经济；历史比较为主（约60%）、概念建构为辅（约40%）；以长时段历史为材料，少用问卷统计；单位批判开头（民族社会不是分析单位）—长时段历史铺陈—核心—边缘分工—结尾讨论体系危机与替代可能。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No nation-state as the unit of analysis, no short-term economism, no Eurocentric modernisation story, no statistics without long-duree history, no moralising conclusion`

## (7) 测试提示词示例（现代题材：共享单车的全球供应链）

- Prompt: `In the style of Immanuel Wallerstein, analyse the global supply chain of shared bikes as a world-system. Take the world-economy as the unit of analysis, map core, semi-periphery and periphery, long-duree history, no nation-state as unit, no short-term economism.`
- 中文对照：伊曼纽尔·沃勒斯坦风格：分析共享单车的全球供应链。宏大、冷静、历史纵深感强；与民族国家分析框架保持批判距离。
- Negative: `No nation-state as the unit of analysis, no short-term economism, no Eurocentric modernisation story, no statistics without long-duree history, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
