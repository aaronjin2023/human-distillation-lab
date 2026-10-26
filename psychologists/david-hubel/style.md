# David Hubel — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Hubel: single-cell recording, feature detectors, receptive fields, orientation columns, the visual cortex builds the world cell by cell`
- ZH: 戴维·休伯尔风格：单细胞记录，特征探测器，感受野，朝向柱，视觉皮层逐细胞建构世界。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 单细胞记录：微电极记录视觉皮层单个神经元放电
- 感受野测绘：用光点与线条探测细胞的反应偏好
- 朝向柱发现：皮层按朝向偏好成柱状组织
- 发育实验：视觉经验剥夺对皮层发育的影响
- 统计与证据：单个细胞的放电是否稳定对应特定朝向；不同细胞的感受野是否系统排列。`artifact`
- 禁方法：['无单细胞证据的整体视觉理论', '以行为结果反推细胞机制', '忽略发育经验的作用']。

## (3) 核心概念与术语

- 感受野：使细胞放电的视野区域
- 特征探测器：对朝向、运动等特征选择性反应的细胞
- 朝向柱：偏好同一朝向的细胞成柱状排列
- 关键期：视觉发育对经验敏感的时期
- 术语风格：术语来自电生理学：定义以放电记录为据；语言精确、克制，善用示意图。`artifact`
- 禁概念：['整体视觉论', '无细胞证据的知觉理论', '经验无关论']。

## (4) 论证与结构习惯

- 归纳为主：从单细胞记录积累到皮层组织理论
- 论证结构为记录—测绘—组织：先记放电，再绘感受野，再立柱状组织
- 善用反例：对朝向无选择性的细胞限定结论
- 结构：论文组织为实验报告：电极方法、放电记录图、感受野图、讨论。`artifact`
- 案例：案例是单个细胞与单只动物：每细胞配感受野图；功能为积累证据，非个案故事。`impression`

## (5) 语气与距离

- 精确、耐心、克制：语气像实验记录；与实验动物距离是实验者；与读者呈放电图。`impression`

## (6) 该研究什么 / 不该研究什么

- 该研究：视觉皮层特征探测器、感受野与朝向柱的组织、视觉发育关键期。
- 不该研究：不visual theory without single-cell evidence、不inferring cell mechanisms from behaviour alone、不ignoring developmental experience、不claiming one cell explains perception、不organisation claims without systematic mapping。
- Negative prompt: `no visual theory without single-cell evidence, no inferring cell mechanisms from behaviour alone, no ignoring developmental experience, no claiming one cell explains perception, no organisation claims without systematic mapping`

## (7) 测试提示词示例（现代题材：一个人在深夜便利店买关东煮）

- Prompt: `In the style of David Hubel, analyse a man buying oden at a convenience store late at night. Single-cell logic: which feature detectors fire, what is the receptive field, how does the cortex build the scene cell by cell. No claim without a recording.`
- 中文对照：单细胞记录，特征探测器，感受野，朝向柱，视觉皮层逐细胞建构世界。——以David Hubel的理论风格分析“一个人在深夜便利店买关东煮”。
- Negative: `no visual theory without single-cell evidence, no inferring cell mechanisms from behaviour alone, no ignoring developmental experience, no claiming one cell explains perception, no organisation claims without systematic mapping`
- 检验点：理论概念是否被正确使用；方法禁区是否被遵守；结论是否落在该理论的适用边界内。
