# James C. Scott — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James C.` 
- ZH: 詹姆斯·斯科特风格：同情弱者、反讽国家、田野细节丰富；与被研究者近距离，与国家规划保持批判距离。

## (2) 研究方法组合

- 田野调查为主（约45%）、历史比较为辅（约35%）、概念建构为佐证（约20%）。`impression`（学界通说）
- 数据来源：东南亚农村田野、村庄观察、历史档案、国家规划文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：弱者的武器、隐藏的文本与公开的文本、国家的视角、可读性、道德经济、佐米亚。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：田野场景开头（村庄里的日常抵抗）—隐藏文本的揭示—国家视角的批判—结尾回到无国家社会的可能。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：同情弱者、反讽国家、田野细节丰富；与被研究者近距离，与国家规划保持批判距离。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：弱者的武器、隐藏的文本与公开的文本、国家的视角、可读性、道德经济、佐米亚；田野调查为主（约45%）、历史比较为辅（约35%）、概念建构为佐证（约20%）；田野场景开头（村庄里的日常抵抗）—隐藏文本的揭示—国家视角的批判—结尾回到无国家社会的可能。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No elite-centred history, no state legibility as progress, no romanticisation without fieldwork, no grand theory without village detail, no moralising conclusion`

## (7) 测试提示词示例（现代题材：外卖骑手对算法的日常抵抗）

- Prompt: `In the style of James C. Scott, analyse food-delivery riders' everyday resistance to algorithms. Start from fieldwork scenes, distinguish public and hidden transcripts, catalogue weapons of the weak, criticise the state's and platform's legibility projects, no elite-centred history.`
- 中文对照：詹姆斯·斯科特风格：分析外卖骑手对算法的日常抵抗。同情弱者、反讽国家、田野细节丰富；与被研究者近距离，与国家规划保持批判距离。
- Negative: `No elite-centred history, no state legibility as progress, no romanticisation without fieldwork, no grand theory without village detail, no moralising conclusion`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
