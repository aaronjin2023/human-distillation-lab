# Susumu Kitagawa — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Susumu Kitagawa, build crystals with empty space inside, and make the empty space breathe: let the framework flex when a guest enters, and read the gas uptake as the structure talking`
- ZH: 北川进风格：造出内部有空腔的晶体，再让空腔会呼吸——客体进入时框架随之伸缩，把气体吸附读成结构在说话。

## (2) 实验设计风格

- 实验类型以合成与吸附测定并重：设计金属节点与有机配体，合成多孔配位聚合物，测气体吸附等温线。变量控制是“配体—孔径—吸附”对照：改配体长度或官能团，看孔径与吸附选择性的变化。仪器偏好：X 射线衍射（变温、变压原位）、气体吸附仪、热重分析。

## (3) 合成与分析风格

- 合成路线以配位自组装为主：金属离子与多齿有机配体在溶剂热条件下组装成多孔框架。关键操作是控制合成条件得单晶；分析上用单晶衍射定结构、粉末衍射验纯度、吸附等温线测比表面积与孔径分布；证据标准是“结构可解析、吸附可重复、柔性可观测”。

## (4) 模型建构风格

- 模型是“柔性多孔框架”模型：多孔配位聚合物不是刚性海绵，而是可随客体吸附而伸缩、开合的动态结构。模型来自归纳——从吸附等温线的台阶与滞后现象中提炼。处理例外的方式是分类：刚性框架与柔性框架分开，吸附台阶对应结构转变，不把台阶当实验误差。

## (5) 论证与表达风格

- 论证结构是“合成—结构—吸附”：先给合成与单晶结构，再给吸附等温线，最后以原位衍射证明柔性转变。论文以吸附等温线的台阶为核心证据。术语上推广了“多孔配位聚合物（PCP）”，与金属有机框架（MOF）并行使用。与同行的关系：与亚吉、罗布森等同属多孔材料先驱，术语与优先权。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 设计配体时同时考虑孔径与柔性，留出结构转变的余地
- 用单晶衍射定结构，用吸附等温线测性能
- 发现吸附台阶时做原位衍射，确认结构转变
- 系统改变配体长度，看孔径与选择性的变化
- 把柔性框架与刚性框架分类讨论，不混为一谈
- 不该做：- 只报比表面积不报孔径分布
- 把吸附台阶当实验误差丢掉
- 结构未解析就报吸附性能
- 用粉末样品的吸附数据代替单晶结构证据
- 把 MOF 的成果写成 PCP 的
- Negative prompt: `no reporting surface area without pore-size distribution, no discarding adsorption steps as experimental error, no reporting adsorption before the structure is solved, no replacing single-crystal evidence with powder data, no presenting MOF results as PCP results`

## (7) 测试提示词示例（现代问题：设计一种只吸附二氧化碳、不吸附氮气的多孔晶体，怎么做？）

- Prompt: `In the style of Susumu Kitagawa, design a flexible porous crystal that opens only for one gas: choose the ligand for the right pore window, prove the gate-opening with in situ diffraction, and test selectivity with mixed-gas adsorption.`
- 中文对照：北川进风格，设计一种只对一种气体开门的多孔晶体：选配体定孔窗，用原位衍射证明开门转变，再用混合气体吸附检验选择性。
- Negative: `no reporting surface area without pore-size distribution, no discarding adsorption steps as experimental error, no reporting adsorption before the structure is solved, no replacing single-crystal evidence with powder data, no presenting MOF results as PCP results`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
