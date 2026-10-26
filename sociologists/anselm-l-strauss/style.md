# Anselm L. Strauss — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Anselm Strauss, analyse night-shift negotiations in a convenience store.` 
- ZH: 安瑟伦·施特劳斯风格：务实、程序清晰、方法论自觉；与读者如导师对话。

## (2) 研究方法组合

- 田野调查与访谈为主（约55%）、编码分析为辅（约30%）、概念建构为佐证（约15%）。`impression`（学界通说）
- 数据来源：医院田野、临终研究访谈、职业社会世界材料。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：扎根理论、社会世界、谈判、轨迹、持续比较、理论抽样。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：田野问题开头—开放编码—持续比较—理论抽样—结尾生成扎根理论。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：务实、程序清晰、方法论自觉；与读者如导师对话。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：扎根理论、社会世界、谈判、轨迹、持续比较、理论抽样；田野调查与访谈为主（约55%）、编码分析为辅（约30%）、概念建构为佐证（约15%）；田野问题开头—开放编码—持续比较—理论抽样—结尾生成扎根理论。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No forced categories, no statistics without coding, no grand theory without data, no psychological reductionism, no moralising conclusion`

## (7) 测试提示词示例（现代题材：深夜便利店店员的轮班谈判）

- Prompt: `In the style of Anselm Strauss, analyse night-shift negotiations in a convenience store. Grounded theory, open coding, constant comparison, social worlds, trajectories, no forced categories, no statistics without coding.`
- 中文对照：安瑟伦·施特劳斯风格：分析深夜便利店店员的轮班谈判。务实、程序清晰、方法论自觉；与读者如导师对话。
- Negative: `No forced categories, no statistics without coding, no grand theory without data, no psychological reductionism, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
