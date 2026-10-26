# Julia R. Greer — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Julia Greer, build the architecture first and the material second, let the nanoscale make ceramics ductile, and prove strength and lightness can coexist`
- ZH: 格里尔方法：先建结构、后选材料，让纳米尺度使陶瓷变韧，再证明强度与轻质可以共存。

## (2) 合成路线偏好

- 3D 纳米结构增材制造：双光子光刻写聚合物模板、镀膜、去模板得中空纳米晶格；关键是单胞尺寸与壁厚分开控制。

## (3) 表征手段组合

- 原位电镜压缩看变形与回复，纳米压痕定强度，结构表征定单胞几何；先结构后力学，顺序不可颠倒。

## (4) 理论模型与图表风格

- 尺寸效应与结构—性能耦合模型；图表偏好应力—应变曲线（回复段即韧性证据）与纳米晶格电镜图。

## (5) 性能指标与取舍

- 优先保住结构的可设计性与尺寸效应的可重复性，牺牲结构尺寸；宁愿结构小，也不要尺寸效应不清。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先设计单胞几何再选构成材料
- 壁厚与单胞尺寸分开控制
- 原位压缩观察变形与回复全过程
- 力学性能按密度归一化报告
- 把结构、尺寸效应与性能写成一条链
- 不该做：
- no strength claims without architecture data
- no presenting bulk ceramic behaviour as nanoscale behaviour
- no density-normalized claims without reporting density
- no hiding structural defects
- no skipping in situ observation of deformation
- Negative prompt: `no strength claims without architecture data, no presenting bulk ceramic behaviour as nanoscale behaviour, no density-normalized claims without reporting density, no hiding structural defects, no skipping in situ observation of deformation`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Julia Greer, design a flexible conductive material for a wearable device. Design the lattice architecture first, control wall thickness and unit-cell size separately, then prove strength and lightness coexist.`
- 中文对照：格里尔方法，为可穿戴设备设计柔性导电材料：先设计晶格结构，分别控制壁厚与单胞尺寸，再证明强度与轻质共存。
- Negative: `no strength claims without architecture data, no presenting bulk ceramic behaviour as nanoscale behaviour, no density-normalized claims without reporting density, no hiding structural defects, no skipping in situ observation of deformation`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
