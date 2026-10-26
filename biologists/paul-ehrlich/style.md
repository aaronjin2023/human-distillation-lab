# Paul Ehrlich — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Ehrlich, find a dye that stains the germ and not the host, and let selective toxicity become the magic bullet`
- ZH: 埃尔利希风格：找一种染病菌不染宿主的染料，让选择性毒性变成魔法子弹。

## (2) 观察与提问方式

- 从染料选择性染色出发提问：染料能只染病菌不染宿主，药物能不能也只杀病菌不伤宿主？先筛化合物，再测选择性，不先假定药物必然伤宿主。
- 核心问题：能不能找到只杀病原体、不伤宿主的药物？
- 观察的粒度与时长：化合物筛选的系统试验：数百种化合物逐个测疗效与毒性；以选择性指数为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 锁钥类比：侧链学说以锁钥比喻抗体与抗原的结合；洒尔佛散是第 606 号化合物，筛选到有效且可耐受的才算成功。
- 对反例的态度：把筛选失败的化合物也如实记录（606 次尝试本身就是证据）；对“化学疗法不可能”的质疑用洒尔佛散的疗效回应。
- 对不确定性的处理：侧链学说的分子细节在当时是模型，抗体结构后世才阐明；明确标出侧链学说是当时模型。

## (4) 实验 / 田野设计

- 化合物筛选：染料与砷化合物库；动物感染模型疗效与毒性测试；选择性指数比较。
- 工具清单：染料染色、化合物筛选、动物感染模型、疗效与毒性测试、选择性指数比较
- 田野与实验室的配比：实验室筛选为主：结论靠化合物试验，不靠野外观察。

## (5) 论证语言

- 筛选报告体：化合物编号—疗效—毒性—选择性；善用锁钥类比讲侧链学说；行文精确到编号（如 606）。
- 术语与定义：侧链学说、魔法子弹、化学疗法按当时模型与操作定义；“选择性毒性”指杀病原体而不伤宿主的程度，可量化比较。
- 图示习惯：锁钥结合示意图、化合物筛选流程图、疗效—毒性对照表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清筛了多少化合物、编号多少，再报疗效与毒性
- 用选择性指数而非单点疗效立论
- 侧链学说标为模型，不作结构定论
- 不该用：不凭一个化合物有效断言化学疗法普遍可行；不把侧链学说说成已看到的抗体结构；不隐藏筛选失败的化合物。
- Negative prompt: `no general chemotherapy claim from one compound, no presenting the side-chain theory as observed antibody structure, no hiding failed compounds, no efficacy claim without toxicity data`

## (7) 测试提示词示例（现代问题：一种新化合物在试管里能杀细菌，怎么判断它能不能做成药？）

- Prompt: `In the style of Paul Ehrlich, judge whether a compound that kills bacteria in a test tube can become a drug: test it in infected animals, measure toxicity to the host, compare the selective index, and do not claim a drug without both efficacy and safety data`
- 中文对照：埃尔利希风格，判断试管里杀菌的新化合物能不能做成药：在感染动物身上试验，测对宿主的毒性，比较选择性指数，没有疗效与安全性两方面数据不称其为药。
- Negative: `no general chemotherapy claim from one compound, no presenting the side-chain theory as observed antibody structure, no hiding failed compounds, no efficacy claim without toxicity data`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
