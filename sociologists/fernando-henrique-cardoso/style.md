# Fernando Henrique Cardoso — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fernando Henrique Cardoso, analyse how a small city depends on short-video platforms.` 
- ZH: 费尔南多·恩里克·卡多佐风格：务实、历史感强、政治经验与学术分析交织；与读者坦诚对话。

## (2) 研究方法组合

- 历史比较为主（约50%）、概念建构为辅（约30%）、统计材料为佐证（约20%）。`impression`（学界通说）
- 数据来源：拉美经济史、巴西社会史、发展统计、政治史文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：依附、关联性依附发展、不发达、发展、民主转型。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：历史情境开头（拉美依附的形成）—依附结构的类型区分—关联性发展的可能—结尾讨论民主与发展。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：务实、历史感强、政治经验与学术分析交织；与读者坦诚对话。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：依附、关联性依附发展、不发达、发展、民主转型；历史比较为主（约50%）、概念建构为辅（约30%）、统计材料为佐证（约20%）；历史情境开头（拉美依附的形成）—依附结构的类型区分—关联性发展的可能—结尾讨论民主与发展。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No dependency fatalism, no ahistorical economism, no nation-state isolation, no moralising conclusion, no statistics without history`

## (7) 测试提示词示例（现代题材：短视频平台对地方小城的依附）

- Prompt: `In the style of Fernando Henrique Cardoso, analyse how a small city depends on short-video platforms. Historicise dependency, distinguish types of dependent development, ask what associated development is possible, no dependency fatalism, no ahistorical economism.`
- 中文对照：费尔南多·恩里克·卡多佐风格：分析短视频平台对地方小城的依附。务实、历史感强、政治经验与学术分析交织；与读者坦诚对话。
- Negative: `No dependency fatalism, no ahistorical economism, no nation-state isolation, no moralising conclusion, no statistics without history`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
