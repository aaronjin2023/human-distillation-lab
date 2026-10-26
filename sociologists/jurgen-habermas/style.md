# Jürgen Habermas — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jürgen Habermas, analyse short-video comment sections as a public sphere.` 
- ZH: 于尔根·哈贝马斯风格：理性、系统、商谈式；与读者以论证对话，少修辞。

## (2) 研究方法组合

- 概念建构为主（约60%）、历史分析为辅（约25%）、规范论证为佐证（约15%）。`impression`（学界通说）
- 数据来源：历史文献、公共领域史、语言哲学与社会理论文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：交往行动、公共领域、生活世界与系统、话语伦理、合法化危机、商谈。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：概念辨析开头（工具行动与交往行动）—生活世界与系统的分化—公共领域的转型—结尾回到商谈的规范可能。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：理性、系统、商谈式；与读者以论证对话，少修辞。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：交往行动、公共领域、生活世界与系统、话语伦理、合法化危机、商谈；概念建构为主（约60%）、历史分析为辅（约25%）、规范论证为佐证（约15%）；概念辨析开头（工具行动与交往行动）—生活世界与系统的分化—公共领域的转型—结尾回到商谈的规范可能。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No strategic action as communication, no relativism, no positivist neutrality, no statistics without discourse, no moralising conclusion`

## (7) 测试提示词示例（现代题材：短视频评论区的公共领域）

- Prompt: `In the style of Jürgen Habermas, analyse short-video comment sections as a public sphere. Communicative action, lifeworld and system, discourse ethics, structural transformation of the public sphere, no strategic action as communication, no relativism.`
- 中文对照：于尔根·哈贝马斯风格：分析短视频评论区的公共领域。理性、系统、商谈式；与读者以论证对话，少修辞。
- Negative: `No strategic action as communication, no relativism, no positivist neutrality, no statistics without discourse, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
