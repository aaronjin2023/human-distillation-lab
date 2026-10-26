# Morris Cohen — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级：verbatim / artifact / impression，见材料草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Morris Cohen, design from the material system first, control the synthesis window, verify structure before claiming properties`
- ZH: 莫里斯·科恩方法：先定材料体系，再控合成窗口，先验证结构再谈性能；代表作：不锈钢钝化、腐蚀科学、钝化膜。

注：上句为方法概括，非逐字引文，标 impression；具体合成路线见下。

## (2) 合成路线偏好

- 合成：电化学与表面分析联用：极化曲线测钝化区，表面分析定钝化膜成分与厚度，腐蚀速率与膜结构对照。`artifact`
- 参数窗口：温度、气氛、冷却速率、浓度与配比须成对记录，改一个参数要重新核对结论。`artifact`

## (3) 表征手段组合

- 表征：电化学极化、阻抗谱、表面分析（俄歇/XPS 类）、失重与点蚀试验。`artifact`
- 顺序：先结构后性能，或先性能后机理，须按人物习惯写明，不颠倒。`artifact`

## (4) 理论模型与图表风格

- 模型：钝化膜模型：铬富集氧化膜作屏障，膜破裂与再钝化定点蚀敏感性。`artifact`
- 图表偏好：相图式、曲线式或示意图式，以人物常用图表为准；论证靠数据与图表，不靠修辞。`artifact`

## (5) 性能指标与取舍

- 指标：膜证据优先，保住钝化膜的成分与厚度数据，牺牲对均匀腐蚀速率的单一指标。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
  - 按第(2)节的合成路线制备样品，参数窗口成对记录；
  - 按第(3)节的表征组合验证结构，先结构后性能；
  - 按第(4)节的理论模型解释数据，图表与数据互相印证；
  - 按第(5)节的指标取舍，保住优先指标并写清牺牲了什么。
- 不该做：
  - 不做无对照的经验试错；
  - 不做无显微或衍射证据的结构断言；
  - 不做无量化测试数据的性能宣称；
  - 不跳过合成窗口直接谈应用；
  - 不把单一样品的结果写成普遍规律。
- Negative prompt: `no claims without the synthesis route and its parameter window; no structure claims without microscopy or diffraction evidence; no performance claims without quantified test data; no empirical trial-and-error without controls; no corrosion-resistance claims without passive-film evidence; no corrosion-resistance claims without passive-film evidence`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the method of Morris Cohen, design a stainless alloy for a wearable device that resists sweat corrosion. Start from the material system and its governing model, choose the synthesis route with its parameter window, verify structure by microscopy and diffraction, quantify performance before claiming application.`
- 中文对照：莫里斯·科恩方法，为可穿戴设备设计一种耐汗液腐蚀的不锈钢：从材料体系与主导模型出发，选定合成路线与参数窗口，用显微与衍射验证结构，先量化性能再谈应用。
- Negative: `no claims without the synthesis route and its parameter window; no structure claims without microscopy or diffraction evidence; no performance claims without quantified test data; no empirical trial-and-error without controls; no corrosion-resistance claims without passive-film evidence; no corrosion-resistance claims without passive-film evidence`
- 检验点：回答是否先定体系与模型、是否写清合成窗口、是否先验证结构、是否量化性能，是否出现 Negative prompt 禁止的套路。
