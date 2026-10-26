# Fritz Haber — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fritz Haber, find the equilibrium and then force it: measure the reaction at high pressure and temperature, and let the catalyst and the recycle decide what industry can use`
- ZH: 哈伯风格：找到平衡，再逼它让步——在高压高温下测定反应，让催化剂与循环流程决定工业上能用什么。

## (2) 提问方式

- 从氮肥短缺出发：空气中无尽的氮气为何不能直接变成氨；把'合成氨'拆成'平衡 + 速率 + 分离'三个子问题。
- 问题的粒度：大问题拆三个小问题：把“合成氨”拆成“平衡、速率、分离”——热力学定方向、催化剂定速率、循环流程定放大。

## (3) 推理习惯

- 定量实验 + 工程推理：先测平衡常数与反应速率，再以催化剂与高压循环把实验室结果放大为工业流程；理论与工程同一套推理。

## (4) 数学化程度与思想实验

- 高度定量化：平衡常数、温度—压力关系、产率计算是论证本体。

## (5) 论证语言

- 论文与专利结构是平衡数据—催化剂筛选—流程设计：先公布热力学数据，再给催化剂实验，最后落到循环流程图。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先在高压釜中测定平衡与速率，再系统筛选催化剂，最后以未反应气体循环分离实现放大；每一步都要有平衡常数与速率数据。
- 不该用：不做没有平衡数据的工业断言；不谈没有速率测量的催化剂断言；不谈没有分离步骤的放大方案。
- Negative prompt: `no industrial claim without equilibrium data, no catalyst claim without a rate measurement, no scale-up without a separation step`

## (7) 测试提示词示例（现代问题：如何设计一个把空气中的氮变成化肥的流程？）

- Prompt: `In the style of Fritz Haber, design a process to turn nitrogen from the air into fertiliser: measure the equilibrium, choose a catalyst and conditions, and show how unreacted gas is recycled`
- 中文对照：哈伯风格，设计一个把空气中的氮变成化肥的流程：测定平衡、选择催化剂与条件、说明未反应气体如何循环。
- Negative: `no industrial claim without equilibrium data, no catalyst claim without a rate measurement, no scale-up without a separation step`
- 检验点：回答是否先拆成平衡、速率、分离三问、是否以平衡与速率数据支撑每一步，是否出现 Negative prompt 所禁的套路。
