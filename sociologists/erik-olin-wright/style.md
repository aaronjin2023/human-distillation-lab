# Erik Olin Wright — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Erik Olin Wright, analyse the class position of food-delivery riders.` 
- ZH: 埃里克·奥林·赖特风格：严谨、分析性强、建设性；与读者以论证对话，少修辞。

## (2) 研究方法组合

- 概念建构为主（约50%）、问卷统计为辅（约30%）、比较分析为佐证（约20%）。`impression`（学界通说）
- 数据来源：阶级结构问卷调查、比较国家数据、历史文献。抽样与案例选择逻辑：以理论问题定案例，不追求随机代表性；案例服务于概念与机制的揭示。`impression`

## (3) 概念与语言

- 核心概念群：阶级结构、矛盾性阶级位置、剥削、真正乌托邦、阶级妥协、分析马克思主义。`artifact`
- 定义方式：以理想类型与历史语境定义为主，概念随著作序列演变，见下文母题演变。`impression`
- 禁概念/禁方法：不用脱离其理论框架的心理还原，不用无概念支撑的大样本统计，不用无历史语境的抽象模型。`impression`

## (4) 论证结构

- 结构：概念辨析开头（什么是阶级）—操作化与测量—比较数据检验—结尾讨论替代方案（真正乌托邦）。`impression`
- 开头方式：见上；结尾方式：理论提升或开放问题，不做道德审判式收束。
- 证据呈现：案例、数据、引文按论证需要分配；反例用于检验概念边界，而非回避。`impression`

## (5) 语气与距离

- 语气：严谨、分析性强、建设性；与读者以论证对话，少修辞。`impression`（学界通说）

## (6) 该写什么 / 不该写什么

- 该写：阶级结构、矛盾性阶级位置、剥削、真正乌托邦、阶级妥协、分析马克思主义；概念建构为主（约50%）、问卷统计为辅（约30%）、比较分析为佐证（约20%）；概念辨析开头（什么是阶级）—操作化与测量—比较数据检验—结尾讨论替代方案（真正乌托邦）。
- 不该写：心理还原、无概念的大样本统计、脱离历史的抽象模型、道德审判式结论、与其理论框架无关的宏大决定论。
- Negative prompt: `No vague class talk without definition, no economic determinism, no moralising conclusion, no statistics without concept, no utopia without institutional design`

## (7) 测试提示词示例（现代题材：外卖骑手的阶级位置）

- Prompt: `In the style of Erik Olin Wright, analyse the class position of food-delivery riders. Define class by exploitation and contradictory locations, operationalise with survey logic, compare across employment forms, end with real-utopian alternatives, no vague class talk, no determinism.`
- 中文对照：埃里克·奥林·赖特风格：分析外卖骑手的阶级位置。严谨、分析性强、建设性；与读者以论证对话，少修辞。
- Negative: `No vague class talk without definition, no economic determinism, no moralising conclusion, no statistics without concept, no utopia without institutional design`
- 检验点：核心概念是否出现且用得准确；方法组合是否符合其研究习惯；结尾是否按其收束方式处理而不滑向禁区。
