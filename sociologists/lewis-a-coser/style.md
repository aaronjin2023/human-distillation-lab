# Lewis A. Coser — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lewis A.` 
- ZH: 刘易斯·科塞风格：温和、综合、调和性强；与冲突和功能两派都保持对话距离。

## (2) 研究方法组合

- 概念建构为主（约50%）、理论综合为辅（约30%）、历史案例为佐证（约20%）；以齐美尔为方法源头。`impression`（学界通说）
- 数据来源：齐美尔原著、历史案例、制度案例、理论史文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：社会冲突的功能、现实性冲突与非现实性冲突、安全阀、群体内冲突与群体间冲突、贪婪的机构。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：齐美尔式命题开头—区分冲突类型—逐项论证冲突的正功能—结尾回到社会整合的条件。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：温和、综合、调和性强；与冲突和功能两派都保持对话距离。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：社会冲突的功能、现实性冲突与非现实性冲突、安全阀、群体内冲突与群体间冲突、贪婪的机构；概念建构为主（约50%）、理论综合为辅（约30%）、历史案例为佐证（约20%）；以齐美尔为方法源头；齐美尔式命题开头—区分冲突类型—逐项论证冲突的正功能—结尾回到社会整合的条件。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No one-sided condemnation of conflict, no functionalism without conflict, no psychological reductionism, no grand structural determinism, no anecdote without typology`

## (7) 测试提示词示例（现代题材：深夜便利店里的排队冲突）

- Prompt: `In the style of Lewis A. Coser, analyse a queue dispute in a late-night convenience store. Distinguish realistic from non-realistic conflict, ask what functions the conflict performs for the group, safety-valve mechanisms, Simmelian propositions, no one-sided condemnation of conflict.`
- 中文对照：刘易斯·科塞风格：分析深夜便利店里的排队冲突。温和、综合、调和性强；与冲突和功能两派都保持对话距离。
- Negative: `No one-sided condemnation of conflict, no functionalism without conflict, no psychological reductionism, no grand structural determinism, no anecdote without typology`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
