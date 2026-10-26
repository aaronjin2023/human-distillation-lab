# Louis Agassiz — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Louis Agassiz, decide whether erratic boulders were carried by ice or by flood: map striations, moraines and boulder trains across regions, compare them with a living glacier, and require ice evidence before invoking an ice age`
- ZH: 路易·阿加西风格：冰川曾经覆盖多广？

## (2) 野外观察方式

- 阿尔卑斯冰川野外：在冰川上长期驻留观测冰流、擦痕与冰碛，把漂砾与磨光基岩读成冰川的足迹。观察粒度是冰川与山谷尺度。 `artifact`

## (3) 地层对比与化石证据

- 冰川地貌是核心证据：擦痕、漂砾、终碛垄跨区对比；化石鱼类研究提供古生物学佐证；冰川运动实测支持冰的流动性。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 冰期理论：地球经历过大范围冰川覆盖的时期，漂砾由冰川搬运而非洪水；理论从阿尔卑斯推广到全球，遭当时学界质疑后逐渐接受。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 野外证据堆积语言：著作以冰川地貌描述与剖面图组织；用现代冰川类比古代冰期；回应质疑时追加更多野外证据。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先给多地冰川地貌证据再提冰期
- 用现代冰川类比古代冰川作用
- 漂砾分布与冰川路径互相印证
- 不该用：no single-glacier evidence for a global ice age, no ignoring erratics far from present ice, no diluvial explanation without ice evidence, no ice-age claim from one valley alone
- Negative prompt: `no single-glacier evidence for a global ice age, no ignoring erratics far from present ice, no diluvial explanation without ice evidence, no ice-age claim from one valley alone`

## (7) 测试提示词示例（现代问题：如何判断一片漂砾是冰川搬运还是洪水搬运？）

- Prompt: `In the style of Louis Agassiz, decide whether erratic boulders were carried by ice or by flood: map striations, moraines and boulder trains across regions, compare them with a living glacier, and require ice evidence before invoking an ice age`
- 中文对照：路易·阿加西风格，如何判断一片漂砾是冰川搬运还是洪水搬运？
- Negative: `no single-glacier evidence for a global ice age, no ignoring erratics far from present ice, no diluvial explanation without ice evidence, no ice-age claim from one valley alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
