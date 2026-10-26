# Rustum Roy — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Rustum Roy, reach equilibrium the wet way: use high-pressure water and reactive sol-gel precursors to get phases that dry heat cannot reach, and map the phase diagram before claiming a new material`
- ZH: 罗伊方法：用水热之路达到平衡——用高压水与高活性溶胶-凝胶前驱体，得到干法到不了的相，先画相图再谈新材料。

## (2) 合成路线偏好

- 水热合成：高压釜、高温高压水介质，合成黏土、沸石与水合相；溶胶-凝胶法：高活性前驱体、低温成胶、烧结；微波与激光加工作补充。 `artifact`

## (3) 表征手段组合

- XRD 定相与相图；热分析看相变；电镜看微结构；水热釜内原位观察反应与晶体生长。 `artifact`

## (4) 理论模型与图表风格

- 相图与晶体化学：氧化物体系平衡相区；水热条件下高压水的高介电催化作用；溶胶-凝胶前驱体的高反应活性使无水体系也能达到平衡。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住相平衡的真实性与可重复性；可牺牲合成速度；新工艺保住普适性，牺牲单一体系的极致性能。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先画相图，再谈新相与新材料
- 用水热与溶胶-凝胶两条路线交叉验证同一相
- 高压水的温度、压力、介电条件一起报，不只报温度
- 跨学科合作时，各领域的证据标准都守住
- 不该做：方法上的禁区——no new-phase claim without a phase diagram；no reporting a hydrothermal product without pressure and water conditions；no calling a metastable product an equilibrium phase；no single-method proof for a new material。
- Negative prompt: `no new-phase claim without a phase diagram, no reporting a hydrothermal product without pressure and water conditions, no calling a metastable product an equilibrium phase, no single-method proof for a new material`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Rustum Roy, design a flexible conductive ceramic for a wearable device: map the phase diagram first, reach the target phase by hydrothermal or sol-gel routes that dry heat cannot reach, and verify equilibrium before claiming the material`
- 中文对照：罗伊方法，为可穿戴设备设计柔性导电陶瓷：先画相图，用水热或溶胶-凝胶路线得到干法到不了的目标相，验证平衡后再谈材料。
- Negative: `no new-phase claim without a phase diagram, no reporting a hydrothermal product without pressure and water conditions, no calling a metastable product an equilibrium phase, no single-method proof for a new material`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
