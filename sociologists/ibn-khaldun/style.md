# Ibn Khaldun — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Khaldun: asabiyyah, dynastic cycles, desert and city, the rise and decay of group solidarity, history as the science of civilization`
- ZH: 赫勒敦风格：阿萨比亚、王朝循环、沙漠与城市、团体精神的兴衰、历史即文明之学。

## (2) 研究方法组合

- 方法配比：历史比较为主（约 60%）、概念建构为辅（约 30%）、批判分析为辅（约 10%）；无田野调查与统计调查。。`impression`（学界通说）
- 数据来源：历史编年、王朝兴衰记录、游牧与定居社会的对照观察、本人为政经历中接触的史料（仅作史料，不蒸私生活）。。
- 抽样与案例选择：以王朝为案例单位，按兴—盛—衰三段取样；游牧与定居作对照组，北非与中东为核心比较范围。。

## (3) 概念与语言

- 核心概念群（5 个）：阿萨比亚（团体精神）、文明（umran）、王朝循环、游牧与定居、历史科学。`artifact`
- 定义方式：历史语境定义：概念从王朝与文明的实际演变中提炼，如阿萨比亚先指血缘团结，后扩展为一切团体凝聚力；定义随历史阶段而变。。
- 禁概念 / 禁方法：不用心理还原，不用单因解释，不用脱离历史的抽象模型，不用统计推断。。

## (4) 论证结构

- 结构：问题—历史编年—比较—循环模型—结论；先立一部文明通史的框架，再以王朝个案填充。。`impression`
- 开头方式：以王朝更替的历史悖论开篇；结尾方式：以循环模型的普遍性收束，指出衰落的必然机制而非道德谴责。
- 证据呈现：王朝个案、税收与城市规模的对照、游牧与定居的并置；反例（如长寿王朝）用阿萨比亚强弱差异解释，而非回避。；反例处理：反例不删除，用阿萨比亚的强弱与城市化程度的差异重新解释。。

## (5) 语气与距离

- 语气：冷峻、宏大、宿命而不悲情。`impression`
- 与研究对象的距离：疏离的史家距离，俯瞰王朝；与读者的距离：向读者讲授历史规律的导师距离。

## (6) 该写什么 / 不该写什么

- 该写：阿萨比亚、王朝循环、游牧与定居对照、文明兴衰、历史比较。
- 不该写：脱离历史的道德评判、单因解释、心理还原、无历史依据的统计。
- Negative prompt: `No ahistorical moralising, no single-cause explanation, no psychological reductionism, no statistics without historical grounding`

## (7) 测试提示词示例（现代题材：一个县城快递网点的兴衰）

- Prompt: `In the style of Ibn Khaldun, analyse the rise and fall of a county-level courier depot: asabiyyah among its couriers, the cycle from desert-like hardship to urban comfort, dynastic decay, history as the science of civilisation.`
- 中文对照：赫勒敦风格：分析一个县城快递网点的兴衰——快递员之间的阿萨比亚、从艰苦创业到城市安逸的循环、王朝式衰落、历史即文明之学。
- Negative: `No ahistorical moralising, no single-cause explanation, no psychological reductionism, no statistics without historical grounding`
- 检验点：是否出现阿萨比亚与王朝循环；是否以历史比较而非道德评判收束；是否拒绝单因解释。
