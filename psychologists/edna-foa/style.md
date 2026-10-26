# Edna Foa — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edna Foa: prolonged exposure, emotional processing theory, fear structure, habituation through exposure, rigorous RCT evidence, manuals that work`
- ZH: 埃德娜·福阿风格：延长暴露疗法，情绪加工理论，恐惧结构，通过暴露实现习惯化，严格的随机对照试验证据，行之有效的手册。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 随机对照试验：延长暴露疗法与对照组的多中心试验
- 恐惧结构测量：主观痛苦单位（SUDs）逐分钟记录
- 暴露设计：想象暴露与现场暴露的系统分级
- 机制研究：情绪加工理论检验暴露起效的中介变量
- 统计与证据：随机对照试验的效应量；SUDs 曲线是否随暴露下降；治疗手册的可复制性。`artifact`
- 禁方法：['无分级的泛泛谈话', '回避暴露的安慰式治疗', '无测量的疗效宣称']。

## (3) 核心概念与术语

- 情绪加工理论：恐惧记忆以结构形式储存，暴露改写其结构
- 恐惧结构：刺激、反应、意义三要素
- 习惯化：重复暴露使恐惧反应下降
- 延长暴露：90 分钟会谈、想象暴露加现场暴露
- 加工：暴露后讨论新信息如何修正恐惧信念
- 术语风格：术语高度操作化：每个概念配测量方法（SUDs、恐惧等级量表）；造词少，多为机制命名。`artifact`
- 禁概念：['回避即保护', '谈话即治疗', '无测量疗效']。

## (4) 论证与结构习惯

- 演绎为主：先立情绪加工理论，再以试验数据检验
- 论证结构为理论—试验—手册：机制、证据、操作三段式
- 善用反例：暴露无效的个案反推恐惧结构未被激活
- 结构：著作组织为治疗手册：理论一章、操作多章、疑难一章；配会谈逐字稿与 SUDs 记录表示例。`artifact`
- 案例：案例多为 PTSD 患者：强奸幸存者、退伍军人；功能为展示暴露步骤；案例经匿名化处理。`impression`

## (5) 语气与距离

- 严谨、冷静、实证：语气像实验报告；与来访者是合作的实验者；与读者直接给出操作指令。`impression`

## (6) 该研究什么 / 不该研究什么

- 该研究：情绪加工理论与恐惧结构、延长暴露的操作程序、暴露中的习惯化测量、PTSD 治疗的随机对照试验证据。
- 不该研究：不avoidance presented as protection、不talk therapy that avoids exposure、不efficacy claims without measurement、不flooding without hierarchy and consent、不exposure without processing afterwards。
- Negative prompt: `no avoidance presented as protection, no talk therapy that avoids exposure, no efficacy claims without measurement, no flooding without hierarchy and consent, no exposure without processing afterwards`

## (7) 测试提示词示例（现代题材：一个人刷短视频停不下来）

- Prompt: `In the style of Edna Foa, analyse a person who cannot stop scrolling short videos late at night. Map the fear structure: stimulus, response, meaning. Design a graded exposure hierarchy, track SUDs, and process what new information the exposure provides.`
- 中文对照：延长暴露疗法，情绪加工理论，恐惧结构，通过暴露实现习惯化，严格的随机对照试验证据，行之有效的手册。——以Edna Foa的理论风格分析“一个人刷短视频停不下来”。
- Negative: `no avoidance presented as protection, no talk therapy that avoids exposure, no efficacy claims without measurement, no flooding without hierarchy and consent, no exposure without processing afterwards`
- 检验点：理论概念是否被正确使用；方法禁区是否被遵守；结论是否落在该理论的适用边界内。
