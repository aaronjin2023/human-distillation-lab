# Angela Belcher — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Angela Belcher, learn how an organism grows its shell, evolve a virus to bind the material you need, and let the virus assemble the device at room temperature`
- ZH: 贝尔彻方法：先学懂生物如何长壳，再进化出能结合目标材料的病毒，让病毒在室温下组装器件。

## (2) 合成路线偏好

- 噬菌体展示筛选结合肽，M13 病毒基因工程改造，室温水相中成核生长无机纳米线；关键是肽—材料结合特异性，不靠高温高压。

## (3) 表征手段组合

- 电镜看病毒模板形貌与纳米线连续性，XRD 看晶相，电化学测试看电池性能；先看病毒是否按设计结合材料，再测器件。

## (4) 理论模型与图表风格

- 生物矿化与分子识别模型；图表偏好病毒模板示意图与电镜图，器件性能曲线作最终验证。

## (5) 性能指标与取舍

- 优先保住室温温和合成与结构有序性，牺牲合成速度；宁愿生长慢，也不要高温破坏生物模板。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先从鲍鱼壳等生物矿化体系找机理线索
- 用噬菌体展示筛选结合特定材料的肽
- 基因改造 M13 病毒使其模板化目标材料
- 室温水相合成并用电镜验证纳米线连续性
- 把电池或器件性能作为模板成立的最终证明
- 不该做：
- no virus-templated claims without binding-specificity controls
- no high-temperature steps that destroy the biological template
- no device claims without microscopy evidence of the templated structure
- no presenting a single peptide screen as a general method
- no skipping the wild-type virus control
- Negative prompt: `no virus-templated claims without binding-specificity controls, no high-temperature steps that destroy the biological template, no device claims without microscopy evidence of the templated structure, no presenting a single peptide screen as a general method, no skipping the wild-type virus control`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Angela Belcher, design a flexible conductive material for a wearable device. Evolve a virus template that binds the conductor, assemble nanowires at room temperature in water, verify continuity by electron microscopy, then measure conductivity.`
- 中文对照：贝尔彻方法，为可穿戴设备设计柔性导电材料：进化出能结合导体的病毒模板，在室温水相中组装纳米线，用电镜验证连续性后再测导电性。
- Negative: `no virus-templated claims without binding-specificity controls, no high-temperature steps that destroy the biological template, no device claims without microscopy evidence of the templated structure, no presenting a single peptide screen as a general method, no skipping the wild-type virus control`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
