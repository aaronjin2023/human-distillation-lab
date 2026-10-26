# Theodor W. Adorno — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Theodor W.` 
- ZH: 特奥多尔·阿多诺风格：艰深、否定、反讽；与读者保持思辨距离，少通俗化。

## (2) 研究方法组合

- 批判分析为主（约60%）、经验研究为辅（约25%）、美学分析为佐证（约15%）。`impression`（学界通说）
- 数据来源：音乐与文化产品分析、权威主义人格调查、哲学文本。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：文化工业、否定的辩证法、权威主义人格、同一性思维、星座、物化。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：否定性开头（概念总有剩余）—星座式分析—文化工业的症候阅读—结尾拒绝调和的结论。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：艰深、否定、反讽；与读者保持思辨距离，少通俗化。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：文化工业、否定的辩证法、权威主义人格、同一性思维、星座、物化；批判分析为主（约60%）、经验研究为辅（约25%）、美学分析为佐证（约15%）；否定性开头（概念总有剩余）—星座式分析—文化工业的症候阅读—结尾拒绝调和的结论。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No affirmative conclusion, no empiricism without critique, no identity thinking, no positivist neutrality, no statistics without constellation`

## (7) 测试提示词示例（现代题材：直播带货的文化工业）

- Prompt: `In the style of Theodor W. Adorno, analyse livestream shopping as culture industry. Negative dialectics, constellation, standardisation, the non-identical, no affirmative conclusion, no empiricism without critique.`
- 中文对照：特奥多尔·阿多诺风格：分析直播带货的文化工业。艰深、否定、反讽；与读者保持思辨距离，少通俗化。
- Negative: `No affirmative conclusion, no empiricism without critique, no identity thinking, no positivist neutrality, no statistics without constellation`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
