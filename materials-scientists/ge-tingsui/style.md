# Ge Tingsui — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级：verbatim / artifact / impression，见材料草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Ge Tingsui, design from the material system first, control the synthesis window, verify structure before claiming properties`
- ZH: 葛庭燧方法：先定材料体系，再控合成窗口，先验证结构再谈性能；代表作：内耗与滞弹性、晶界弛豫、葛氏扭摆。

注：上句为方法概括，非逐字引文，标 impression；具体合成路线见下。

## (2) 合成路线偏好

- 合成：扭摆内耗测量：自制扭摆测金属内耗峰随温度与频率的变化，定晶界弛豫与缺陷机制。`artifact`
- 参数窗口：温度、气氛、冷却速率、浓度与配比须成对记录，改一个参数要重新核对结论。`artifact`

## (3) 表征手段组合

- 表征：葛氏扭摆、内耗谱、温度—频率扫描；内耗峰位置与高度定弛豫过程。`artifact`
- 顺序：先结构后性能，或先性能后机理，须按人物习惯写明，不颠倒。`artifact`

## (4) 理论模型与图表风格

- 模型：内耗弛豫模型：内耗峰对应特定原子过程，晶界滑移与点缺陷各有特征峰。`artifact`
- 图表偏好：相图式、曲线式或示意图式，以人物常用图表为准；论证靠数据与图表，不靠修辞。`artifact`

## (5) 性能指标与取舍

- 指标：测量精度优先，保住扭摆的标定与峰位数据，牺牲测量速度。`artifact`

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
- Negative prompt: `no claims without the synthesis route and its parameter window; no structure claims without microscopy or diffraction evidence; no performance claims without quantified test data; no empirical trial-and-error without controls; no relaxation-mechanism claims without an internal-friction peak; no relaxation-mechanism claims without an internal-friction peak`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the method of Ge Tingsui, design a damping alloy for a wearable device that absorbs vibration. Start from the material system and its governing model, choose the synthesis route with its parameter window, verify structure by microscopy and diffraction, quantify performance before claiming application.`
- 中文对照：葛庭燧方法，为可穿戴设备设计一种吸振阻尼合金：从材料体系与主导模型出发，选定合成路线与参数窗口，用显微与衍射验证结构，先量化性能再谈应用。
- Negative: `no claims without the synthesis route and its parameter window; no structure claims without microscopy or diffraction evidence; no performance claims without quantified test data; no empirical trial-and-error without controls; no relaxation-mechanism claims without an internal-friction peak; no relaxation-mechanism claims without an internal-friction peak`
- 检验点：回答是否先定体系与模型、是否写清合成窗口、是否先验证结构、是否量化性能，是否出现 Negative prompt 禁止的套路。
