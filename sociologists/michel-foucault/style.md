# Michel Foucault — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michel Foucault, analyse a digital health-code system as discipline.` 
- ZH: 米歇尔·福柯风格：冷峻、考古学式、反人道主义；与读者保持历史的距离。

## (2) 研究方法组合

- 历史—档案分析为主（约60%）、概念建构为辅（约40%）；以档案的考古学与谱系学为方法。`impression`（学界通说）
- 数据来源：监狱、医院、精神病院档案、历史文献、制度文本。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：权力、话语、规训、知识—权力、全景敞视、生命政治、主体化。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：档案细节开头（一次规训技术）—话语与权力的共生—谱系学的历史追溯—结尾回到主体化的可能。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：冷峻、考古学式、反人道主义；与读者保持历史的距离。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：权力、话语、规训、知识—权力、全景敞视、生命政治、主体化；历史—档案分析为主（约60%）、概念建构为辅（约40%）；以档案的考古学与谱系学为方法；档案细节开头（一次规训技术）—话语与权力的共生—谱系学的历史追溯—结尾回到主体化的可能。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No sovereign power only, no humanist subject, no moralising conclusion, no statistics without archives, no progress story without genealogy`

## (7) 测试提示词示例（现代题材：健康码与规训社会）

- Prompt: `In the style of Michel Foucault, analyse a digital health-code system as discipline. Archaeology and genealogy, power-knowledge, panopticism, biopolitics, no sovereign power only, no humanist subject, no moralising conclusion.`
- 中文对照：米歇尔·福柯风格：分析健康码与规训社会。冷峻、考古学式、反人道主义；与读者保持历史的距离。
- Negative: `No sovereign power only, no humanist subject, no moralising conclusion, no statistics without archives, no progress story without genealogy`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
