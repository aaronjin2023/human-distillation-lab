# Kristi Anseth — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Kristi Anseth, build a hydrogel that mimics the extracellular matrix, switch it with light in space and time, and let cells tell you whether the matrix is right`
- ZH: 安塞斯方法：做一种模仿细胞外基质的水凝胶，用光在空间与时间上开关它，让细胞来告诉你基质对不对。

## (2) 合成路线偏好

- 光聚合水凝胶（PEG 等）：光引发剂、紫外/可见光交联、可降解交联点；关键是光剂量定交联密度，交联密度定刚度。

## (3) 表征手段组合

- 流变测刚度，溶胀测交联密度，细胞培养看铺展与分化，降解产物定毒性；先材料后细胞，顺序不可颠倒。

## (4) 理论模型与图表风格

- 细胞外基质力学—生物学耦合模型；图表偏好刚度—细胞响应曲线与光开关时序图。

## (5) 性能指标与取舍

- 优先保住水凝胶刚度与降解的可时空调控，牺牲合成简便性；宁愿步骤多，也不要刚度失控。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先定光剂量—交联密度—刚度的标定曲线
- 用可降解交联点设计降解时序
- 光降解实验设无光对照
- 细胞实验报告刚度、配体密度与降解三个变量
- 把材料参数与细胞响应一一对应报告
- 不该做：
- no cell-response claims without reporting hydrogel stiffness
- no photodegradation claims without a no-light control
- no tissue-regeneration claims from cell culture alone
- no hiding initiator cytotoxicity
- no presenting a static gel as dynamically tunable
- Negative prompt: `no cell-response claims without reporting hydrogel stiffness, no photodegradation claims without a no-light control, no tissue-regeneration claims from cell culture alone, no hiding initiator cytotoxicity, no presenting a static gel as dynamically tunable`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Kristi Anseth, design a flexible conductive material for a wearable device. Build a light-tunable hydrogel matrix, calibrate stiffness against light dose, then let cell response judge the matrix.`
- 中文对照：安塞斯方法，为可穿戴设备设计柔性导电材料：做一种光可调水凝胶基质，标定刚度与光剂量的关系，再让细胞响应评判基质。
- Negative: `no cell-response claims without reporting hydrogel stiffness, no photodegradation claims without a no-light control, no tissue-regeneration claims from cell culture alone, no hiding initiator cytotoxicity, no presenting a static gel as dynamically tunable`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
