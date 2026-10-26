# Norio Taniguchi — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Norio Taniguchi: name the scale first, define nanotechnology as precision machining down to atomic dimensions, and let the加工精度 curve decide how far manufacturing can go`
- ZH: 谷口纪男方法：先给尺度命名，把纳米技术定义为向原子尺寸逼近的精密加工，让加工精度曲线来判定制造能走多远。

## (2) 合成路线偏好

- 超精密加工为主：离子束加工、金刚石切削、光刻；‘合成’即加工——把材料精度从微米推向纳米；加工精度与表面粗糙度是关键指标。

## (3) 表征手段组合

- 先测加工精度与表面粗糙度（纳米级测量），再谈器件；精度—时间曲线是核心表征：加工精度随年代指数提升，曲线本身就是证据。

## (4) 理论模型与图表风格

- 超精密加工模型：用精度—时间曲线讲加工技术演进，用‘纳米技术’定义讲原子尺度加工的目标；图表以精度演进曲线 + 加工方法对照表为主。

## (5) 性能指标与取舍

- 优先保住加工精度的可测量性与演进趋势，牺牲单项工艺的细节：定义先行、趋势先行；保住精度数据的真实性，牺牲对应用前景的夸大。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先定义尺度与目标再谈工艺；用精度—时间曲线讲技术演进；先测加工精度再谈器件；以可测量的纳米精度作判据；把超精密加工从机械推广到离子束与光刻。
- 不该做：不做无精度测量的纳米宣称；不跳过表面粗糙度直接谈纳米器件；不把微米结果冒充纳米结果；不以术语命名冒充技术实现；不脱离精度数据谈加工能力。
- Negative prompt: `no nanotechnology claims without precision measurement, no nanoscale devices without surface roughness data, no micrometer results presented as nanoscale results, no naming presented as technical realization, no machining claims without precision data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种纳米精度柔性传感材料）

- Prompt: `In the method of Norio Taniguchi, design a nanoscale-precision flexible sensing material for a wearable device. Define the scale and the precision target first, choose the machining method by measured precision, and let the precision curve decide how far manufacturing can go.`
- 中文对照：用谷口纪男的方法，为可穿戴设备设计一种纳米精度柔性传感材料：先定义尺度与精度目标，按实测精度选加工方法，让精度曲线来判定制造能走多远。
- Negative: `no nanotechnology claims without precision measurement, no nanoscale devices without surface roughness data, no micrometer results presented as nanoscale results, no naming presented as technical realization, no machining claims without precision data`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
