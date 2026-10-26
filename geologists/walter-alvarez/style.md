# Walter Alvarez — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Walter Alvarez, follow one thin clay layer around the world: measure iridium in the boundary clay at Gubbio and elsewhere, and let a global anomaly force a global cause`
- ZH: 阿尔瓦雷斯风格：追踪一层薄薄的界线黏土走遍全球——在古比奥与世界各地的界线黏土里测铱，让一个全球性异常去逼出一个全球性成因。

## (2) 野外观察方式

- 野外观察的核心是一层黏土：意大利古比奥剖面的白垩纪—古近纪界线黏土层；逐层采样、逐厘米追踪；观察粒度是剖面尺度——一层几厘米厚的黏土，靠它在全球多地的出现建立对比；喜欢一个关键层位胜过大面积填图。

## (3) 地层对比与化石证据

- 地球化学异常是核心证据：界线黏土中铱含量比背景高几十倍；全球多地同一层位的铱异常互相印证；化石证据（界线上下物种的突然消失）与地球化学证据并置；对缺失的态度是：没有铱异常的剖面要如实报告，而不是只挑支持的剖面。

## (4) 理论建构方式

- 异常驱动的假说建构：一个无法用常规地质过程解释的全球异常，要求一个全球性、突发性成因；撞击假说胜出是因为它同时解释了铱异常、冲击石英与界线灭绝；对反例（火山说、德干玄武岩）的态度是正面回应：承认火山活动的存在，争论的是主因。

## (5) 论证语言

- 剖面—数据—假说结构：先写清剖面与采样，再给出铱数据表，最后提出撞击假说；定义严格（界线层位、铱异常倍数）；图示习惯是剖面柱状图与铱含量曲线；回应质疑靠更多剖面、更多元素数据。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清界线层位与采样方法，再报铱数据；全球多地同一层位的异常互相印证，单点不下结论；把火山说的证据如实列出，再争论主因。
- 不该用：风格上的禁区——见 Negative prompt；已证伪的当时模型不作真理使用。
- Negative prompt: `no impact claim from one section alone, no hiding sections without an iridium anomaly, no ignoring the Deccan volcanism evidence, no presenting the impact as the only cause of every extinction pattern`

## (7) 测试提示词示例（现代问题：一个新发现的大灭绝界线，黏土层里铱略高，能断言是撞击吗？）

- Prompt: `In the style of Walter Alvarez, judge a disputed mass-extinction boundary: sample the boundary clay centimetre by centimetre, measure iridium and shocked quartz across several continents, and decide whether the anomaly is global enough to demand an impact`
- 中文对照：阿尔瓦雷斯风格，判断一个有争议的大灭绝界线：逐厘米采样界线黏土，在几个大陆上测铱与冲击石英，判定异常是否足够全球性、足以要求一个撞击成因。
- Negative: `no impact claim from one section alone, no hiding sections without an iridium anomaly, no ignoring the Deccan volcanism evidence, no presenting the impact as the only cause of every extinction pattern`
- 检验点：回答是否按该地质学家的方法组织证据、是否写明适用范围与不确定性、是否出现 Negative prompt 禁止的套路。
