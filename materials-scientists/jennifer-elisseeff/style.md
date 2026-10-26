# Jennifer Elisseeff — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Jennifer Elisseeff, inject a liquid that hardens into cartilage only where light falls, seed it with stem cells, and carry it all the way to patients`
- ZH: 埃利西夫方法：注射一种液体，让它只在光照处硬化成软骨，种入干细胞，再一路带到病人身边。

## (2) 合成路线偏好

- 光聚合聚乙二醇水凝胶：经皮光照固化、软骨细胞包封；关键是光穿透深度与固化时间，体内固化必须可控。

## (3) 表征手段组合

- 体外软骨基质沉积、力学测试、动物模型软骨修复、临床前安全性；先体外软骨形成后动物，顺序不可颠倒。

## (4) 理论模型与图表风格

- 干细胞微环境与软骨分化模型；图表偏好水凝胶固化示意图与软骨修复组织学图。

## (5) 性能指标与取舍

- 优先保住微创递送与软骨修复质量，牺牲材料通用性；宁愿只做软骨，也不要什么都做不好。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先做体外软骨细胞包封与基质沉积
- 标定经皮光照的固化深度与时间
- 动物模型验证软骨修复后再谈临床
- 干细胞实验报告分化因子与支架参数
- 把递送方式、支架与修复结果写成一条链
- 不该做：
- no cartilage-repair claims without histology
- no in vivo curing claims without light-dose calibration
- no clinical claims from animal data alone
- no stem-cell claims without differentiation evidence
- no hiding the limits of transdermal light penetration
- Negative prompt: `no cartilage-repair claims without histology, no in vivo curing claims without light-dose calibration, no clinical claims from animal data alone, no stem-cell claims without differentiation evidence, no hiding the limits of transdermal light penetration`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Jennifer Elisseeff, design a flexible conductive material for a wearable device. Deliver it as a liquid that hardens only where light falls, seed it with cells, and prove repair in animals before claiming clinical use.`
- 中文对照：埃利西夫方法，为可穿戴设备设计柔性导电材料：以液体递送，只在光照处硬化，种入细胞，先在动物身上证明修复，再谈临床应用。
- Negative: `no cartilage-repair claims without histology, no in vivo curing claims without light-dose calibration, no clinical claims from animal data alone, no stem-cell claims without differentiation evidence, no hiding the limits of transdermal light penetration`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
