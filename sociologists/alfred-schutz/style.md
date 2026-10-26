# Alfred Schutz — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Alfred Schutz, analyse how a delivery rider and a customer share a taken-for-granted address.` 
- ZH: 阿尔弗雷德·舒茨风格：严密、思辨、现象学式的耐心；与读者以论证对话。

## (2) 研究方法组合

- 概念建构与现象学分析为主（约80%）、日常经验描述为辅（约20%）；少做经验调查。`impression`（学界通说）
- 数据来源：胡塞尔现象学文献、日常经验描述、韦伯方法论文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：生活世界、意义建构、意向性、类型化、互为主体性、自然态度。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：日常经验描述开头—自然态度的悬置—意义结构的类型化—结尾回到互为主体性的生活世界。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：严密、思辨、现象学式的耐心；与读者以论证对话。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：生活世界、意义建构、意向性、类型化、互为主体性、自然态度；概念建构与现象学分析为主（约80%）、日常经验描述为辅（约20%）；少做经验调查；日常经验描述开头—自然态度的悬置—意义结构的类型化—结尾回到互为主体性的生活世界。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No behaviourism, no statistics without meaning, no objectivism without subjectivity, no psychological reductionism, no moralising conclusion`

## (7) 测试提示词示例（现代题材：外卖骑手与顾客的地址沟通）

- Prompt: `In the style of Alfred Schutz, analyse how a delivery rider and a customer share a taken-for-granted address. Phenomenology of the life-world, typification, intersubjectivity, natural attitude, no statistics without meaning, no behaviourism.`
- 中文对照：阿尔弗雷德·舒茨风格：分析外卖骑手与顾客的地址沟通。严密、思辨、现象学式的耐心；与读者以论证对话。
- Negative: `No behaviourism, no statistics without meaning, no objectivism without subjectivity, no psychological reductionism, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
