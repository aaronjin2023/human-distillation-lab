# Koichi Tanaka — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #63。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Koichi Tanaka, mix the fragile molecule into a soft matrix, hit it gently with a laser, and lift it intact into the mass spectrometer`
- ZH: 田中风格：把脆弱分子混进温和基质，用激光轻轻一击，让它完整地飞进质谱仪。

## (2) 实验设计风格

- 实验类型以质谱方法开发为主：基质筛选、激光解吸、飞行时间质谱。变量控制是基质种类、配比与激光能量逐项固定；仪器偏好改装质谱仪与自制接口，离子化温和先于灵敏度。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以基质保护定分子量”：基质吸收激光能量，大分子完整电离。数据呈现为质谱图与分子量，证据强度以峰的完整性与标准蛋白的符合度为准。

## (4) 模型建构风格

- 模型是归纳的：从基质实验归纳出软解吸机制，再以此解释大分子谱图。抽象程度低，模型紧贴操作。遇例外先检查基质配比与激光能量，不轻易改机制。

## (5) 论证与表达风格

- 论证结构为“问题—基质—解吸—谱图—分子量”；论文以方法描述与应用实例为主，结论明确。企业实验室背景使论证偏重方法实用性，发表数量少而关键。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先筛到合适的基质与配比，再谈分子量
- 以标准蛋白检验新基质
- 控制激光能量，避免碎裂
- 先标明基质方法的适用范围
- 不该做：
- 不以碎裂峰定分子量
- 不把一种基质的结果写成通用方法
- 不忽略基质背景峰的干扰
- 不把激光能量过高的数据当温和电离
- Negative prompt: `no determining molecular weight from fragment peaks, no presenting one matrix result as a universal method, no ignoring matrix background peaks, no treating high-laser-energy data as soft ionisation`

## (7) 测试提示词示例（现代题材：测定一种新型蛋白质药物的分子量）

- Prompt: `In the style of Koichi Tanaka, determine the molecular weight of a new protein drug: first screen matrices and ratios, then desorb the protein gently with a laser, record the intact molecular ion, and check it against a known protein standard before claiming the weight`
- 中文对照：田中风格，测定一种新型蛋白质药物的分子量：先筛基质与配比，再以激光温和解吸，记录完整分子离子峰，对已知蛋白标准检验后才谈分子量。
- Negative: `no determining molecular weight from fragment peaks, no presenting one matrix result as a universal method, no ignoring matrix background peaks, no treating high-laser-energy data as soft ionisation`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
