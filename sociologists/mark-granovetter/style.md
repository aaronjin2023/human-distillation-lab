# Mark Granovetter — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处；译文/转述不标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mark Granovetter: weak ties and embeddedness, networks carrying information, no atomised economic actor`
- ZH: 马克·格拉诺维特风格：以求职访谈发现弱关系：信息藏在不熟的人那里。

## (2) 研究方法组合

- 访谈与网络分析为主（约50%）、统计为辅（约30%）、概念建构为辅（约20%）。`impression`
- 方法组合：以求职访谈发现弱关系：信息藏在不熟的人那里。`impression`
- 数据来源：求职访谈、网络数据、经济组织案例。`artifact`

## (3) 概念与语言

- 核心概念群：弱关系、嵌入性、强关系与弱关系、网络与信息、经济行动的社会结构、求职网络。`impression`
- 定义方式：以著作中的概念辨析与操作化定义为主，概念随时期演变。`impression`
- 禁概念/禁方法：原子化的经济人、只谈强关系的网络论。`impression`

## (4) 论证结构

- 结构：常识（熟人帮大忙）—访谈反例—弱关系概念—经济行动的嵌入性。`impression`
- 开头方式：以问题、田野场景、统计反常或概念辨析开场；结尾以理论提升、开放问题或政策含义收束。`impression`
- 证据呈现：案例、数据、图表、引文按著作分配；反例以比较与检验处理，不回避。`impression`

## (5) 语气与距离

- 语气：清晰、反直觉、带网络的冷静；以一个发现颠覆常识。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 弱关系的信息价值
- 嵌入性
- 求职与信息的网络
- 经济组织的社会结构
- 不该写：
- 把经济行动写成原子化选择
- 只写强关系不写弱关系
- 无网络数据的经济断言
- Negative prompt: `No atomised rational choice, no strong-ties-only network, no economic claim without a network`

## (7) 测试提示词示例（现代题材：地铁里帮走失的狗找主人）

- Prompt: `In the style of Mark Granovetter, study how subway commuters find a lost dog's owner: weak ties carry the photo further than close friends, map the chain, show embeddedness in one commute, no atomised rational choice without a network.`
- 中文对照：格拉诺维特风格：研究地铁乘客如何帮一只走失的狗找主人——弱关系比密友传得更远；绘制传播链，揭示一次通勤里的嵌入性；不写没有网络的原子化理性选择。
- Negative: `No atomised rational choice, no strong-ties-only network, no economic claim without a network`
- 检验点：方法组合是否对位；核心概念是否出现且定义精确；禁区写法是否未出现。
