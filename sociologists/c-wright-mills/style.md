# C. Wright Mills — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of C.` 
- ZH: 查尔斯·赖特·米尔斯风格：热烈、批判、公共性强；与权力保持审判距离，与读者直接对话。

## (2) 研究方法组合

- 概念建构为主（约50%）、历史比较为辅（约30%）、公开统计为佐证（约20%）；少做田野访谈。`impression`（学界通说）
- 数据来源：公开统计、历史文献、职业结构数据、精英传记与组织材料。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：社会学的想象力、权力精英、白领、个人困扰与公共议题、科层制、权力结构。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：悖论式开头（个人困扰背后是公共议题）—历史结构分析—权力结构揭示—结尾号召公共理性。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：热烈、批判、公共性强；与权力保持审判距离，与读者直接对话。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：社会学的想象力、权力精英、白领、个人困扰与公共议题、科层制、权力结构；概念建构为主（约50%）、历史比较为辅（约30%）、公开统计为佐证（约20%）；少做田野访谈；悖论式开头（个人困扰背后是公共议题）—历史结构分析—权力结构揭示—结尾号召公共理性。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No abstracted empiricism, no grand theory without historical facts, no psychological reductionism, no neutral value-free pose, no anecdote without structure`

## (7) 测试提示词示例（现代题材：外卖骑手的劳动时间）

- Prompt: `In the style of C. Wright Mills, analyse food-delivery riders' working time in a modern city. Turn personal troubles of overwork into public issues of platform power, map the power elite of platforms, algorithms and regulators, historical-structural analysis, no abstracted empiricism, no grand theory without facts.`
- 中文对照：查尔斯·赖特·米尔斯风格：分析外卖骑手的劳动时间。热烈、批判、公共性强；与权力保持审判距离，与读者直接对话。
- Negative: `No abstracted empiricism, no grand theory without historical facts, no psychological reductionism, no neutral value-free pose, no anecdote without structure`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
