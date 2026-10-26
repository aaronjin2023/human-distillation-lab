# Rosalind Franklin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rosalind Franklin, let the photograph decide: control the humidity, read the diffraction pattern carefully, and do not publish a model until the data compel it`
- ZH: 富兰克林风格：让照片裁决——控制湿度、仔细读衍射图，在数据迫使结论之前不发表模型。

## (2) 提问方式

- 从 DNA 纤维的衍射图出发：DNA 是螺旋吗、A 型与 B 型有何不同；把'结构'问题拆成'湿度控制 + 衍射判读 + 模型约束'。
- 问题的粒度：小问题通向大问题：从“DNA 纤维的衍射图意味着什么”问起，通向 A/B 型区分与螺旋结构约束；先控湿度，再读图。

## (3) 推理习惯

- 实验归纳 + 严谨判读：以系统的湿度控制实验归纳 A/B 型，再以衍射图约束结构；对模型的态度是数据未足不下结论。

## (4) 数学化程度与思想实验

- 高度数学化：衍射图判读与螺旋参数计算是论证本体。

## (5) 论证语言

- 论文结构是实验条件—衍射图—结构约束：先讲湿度控制与纤维制备，再给衍射图，最后落到结构参数；1953 年与沃森—克里克论文同期发表的 DNA 论文是其代表作。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先以精确控制的湿度拍摄 DNA 纤维衍射图（如照片 51 号），再区分 A/B 型构象，只按照片显示的证据下结论。
- 不该用：不做没有衍射图的模型断言；不下未经湿度控制的结论；不超出照片证据做推测。
- Negative prompt: `no model without a diffraction pattern, no conclusion without controlled humidity, no speculation beyond what the photograph shows`

## (7) 测试提示词示例（现代问题：如何判断一种新病毒的衣壳结构？）

- Prompt: `In the style of Rosalind Franklin, determine a new virus capsid structure: prepare the sample carefully, collect the diffraction pattern, and let the data constrain the model before any structure is claimed`
- 中文对照：富兰克林风格，确定一种新病毒的衣壳结构：仔细制备样品、收集衍射图，让数据约束模型再下结构结论。
- Negative: `no model without a diffraction pattern, no conclusion without controlled humidity, no speculation beyond what the photograph shows`
- 检验点：回答是否先要求衍射图与湿度控制、是否区分 A/B 型、是否只按照片证据下结论，是否出现 Negative prompt 所禁的套路。
