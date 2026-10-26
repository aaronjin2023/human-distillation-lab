# Ralf Dahrendorf — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ralf Dahrendorf, analyse conflicts between ride-hailing platforms and drivers.` 
- ZH: 拉尔夫·达伦多夫风格：冷峻、思辨、自由主义克制；与研究对象保持疏离，与读者理性对话。

## (2) 研究方法组合

- 概念建构为主（约60%）、历史比较为辅（约40%）；以韦伯的权威概念为分析工具，少用统计。`impression`（学界通说）
- 数据来源：历史文献、制度文本、阶级结构的历史材料。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：权威、命令等级、准群体与利益群体、潜在利益与显在利益、冲突的制度化、社会冲突。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：概念辨析开头（权威先于财产）—准群体到利益群体的转化—冲突制度化的条件—结尾讨论自由社会的冲突管理。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：冷峻、思辨、自由主义克制；与研究对象保持疏离，与读者理性对话。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：权威、命令等级、准群体与利益群体、潜在利益与显在利益、冲突的制度化、社会冲突；概念建构为主（约60%）、历史比较为辅（约40%）；以韦伯的权威概念为分析工具，少用统计；概念辨析开头（权威先于财产）—准群体到利益群体的转化—冲突制度化的条件—结尾讨论自由社会的冲突管理。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No economic reductionism, no class determinism, no psychological explanation of conflict, no statistics without authority analysis, no moralising conclusion`

## (7) 测试提示词示例（现代题材：网约车平台的规则冲突）

- Prompt: `In the style of Ralf Dahrendorf, analyse conflicts between ride-hailing platforms and drivers. Start from authority relations and command hierarchies, trace latent interests turning into manifest conflict groups, ask when conflict is institutionalised, precise definitions, no economic reductionism.`
- 中文对照：拉尔夫·达伦多夫风格：分析网约车平台的规则冲突。冷峻、思辨、自由主义克制；与研究对象保持疏离，与读者理性对话。
- Negative: `No economic reductionism, no class determinism, no psychological explanation of conflict, no statistics without authority analysis, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
