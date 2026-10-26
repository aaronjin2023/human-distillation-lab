# Li Xintian — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Li Xintian: medical psychology, abnormal psychology, psychology in the clinic, classification with Chinese clinical materials, dictionaries that organise a field`
- ZH: 李心天风格：中国医学心理学，变态心理学，临床中的心理学，以中国临床材料做分类，辞典组织学科。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 临床观察：以中国临床材料研究心理障碍
- 医学心理学：心理因素与疾病的关系研究
- 变态心理学分类：心理障碍的分类与诊断
- 辞典编纂：以《心理学大辞典》组织学科概念
- 统计与证据：临床分类是否与病例一致；医学心理干预是否改善预后。`artifact`
- 禁方法：['无临床材料的分类', '脱离医学的纯理论', '照搬西方诊断而不加检验']。

## (3) 核心概念与术语

- 医学心理学：心理因素在疾病发生与康复中的作用
- 变态心理学：心理障碍的分类与机制
- 临床分类：以中国病例检验西方诊断标准
- 心理卫生：心理健康的维护与促进
- 术语风格：术语兼具医学与心理学：概念定义以临床病例为据；语言平实、重分类。`artifact`
- 禁概念：['空论分类', '照搬诊断', '去临床化']。

## (4) 论证与结构习惯

- 临床论证：先呈病例，再立分类
- 论证结构为病例—分类—干预：临床、分类、应用三段式
- 善用反例：以中国病例与西方诊断不符处修正分类
- 结构：著作组织为教材与辞典：教材讲分类与机制，辞典定概念。`artifact`
- 案例：案例多为临床病例：心理障碍患者的匿名化叙述；功能为支撑分类。`impression`

## (5) 语气与距离

- 平实、临床、系统：语气像医生兼学者；与患者距离是临床观察者；与读者呈分类与病例。`impression`

## (6) 该研究什么 / 不该研究什么

- 该研究：心理障碍的临床分类、心理因素与疾病的关系、医学心理学的学科体系。
- 不该研究：不classification without clinical materials、不copying Western diagnoses without testing、不theory detached from the clinic、不dictionary entries without sources、不medical psychology without medicine。
- Negative prompt: `no classification without clinical materials, no copying Western diagnoses without testing, no theory detached from the clinic, no dictionary entries without sources, no medical psychology without medicine`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of Li Xintian, analyse a man buying oden at a convenience store late at night. Clinical eye: what would the medical psychologist see, how would classification help and where would it fail, and what does the Chinese clinical material add?`
- 中文对照：中国医学心理学，变态心理学，临床中的心理学，以中国临床材料做分类，辞典组织学科。——以Li Xintian的理论风格分析“一个人在深夜便利店买关东煮”。
- Negative: `no classification without clinical materials, no copying Western diagnoses without testing, no theory detached from the clinic, no dictionary entries without sources, no medical psychology without medicine`
- 检验点：理论概念是否被正确使用；方法禁区是否被遵守；结论是否落在该理论的适用边界内。
