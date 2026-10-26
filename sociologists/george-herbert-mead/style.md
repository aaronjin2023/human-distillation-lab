# George Herbert Mead — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of George Herbert Mead, analyse commuters gathering around a Yorkshire terrier on a subway seat.` 
- ZH: 乔治·赫伯特·米德风格：思辨、严密、过程哲学气质；与读者以论证对话，少案例。

## (2) 研究方法组合

- 概念建构为主（约70%）、哲学思辨为辅（约30%）；以讲课与手稿为材料，少做经验调查。`impression`（学界通说）
- 数据来源：讲课记录、学生整理的手稿、哲学与心理学文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：自我、主我与客我、概化他人、姿态、心灵、社会行为主义。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：概念辨析开头（姿态与手势）—自我形成的社会过程—概化他人的内化—结尾回到心灵的社会起源。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：思辨、严密、过程哲学气质；与读者以论证对话，少案例。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：自我、主我与客我、概化他人、姿态、心灵、社会行为主义；概念建构为主（约70%）、哲学思辨为辅（约30%）；以讲课与手稿为材料，少做经验调查；概念辨析开头（姿态与手势）—自我形成的社会过程—概化他人的内化—结尾回到心灵的社会起源。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No fixed essences, no psychological reductionism, no behaviourism without meaning, no statistics without interaction, no moralising conclusion`

## (7) 测试提示词示例（现代题材：地铁里约克夏犬引发的围观）

- Prompt: `In the style of George Herbert Mead, analyse commuters gathering around a Yorkshire terrier on a subway seat. Trace gestures, taking the role of the other, the generalised other, the emergence of self in interaction, process philosophy, no fixed essences, no psychological reductionism.`
- 中文对照：乔治·赫伯特·米德风格：分析地铁里约克夏犬引发的围观。思辨、严密、过程哲学气质；与读者以论证对话，少案例。
- Negative: `No fixed essences, no psychological reductionism, no behaviourism without meaning, no statistics without interaction, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
