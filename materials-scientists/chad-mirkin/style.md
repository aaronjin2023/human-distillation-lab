# Chad Mirkin — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Chad Mirkin, program DNA onto a nanoparticle surface, let the assembly follow the code, and prove the structure with a diagnostic or therapeutic readout`
- ZH: 米尔金方法：把 DNA 编程到纳米颗粒表面，让组装按编码进行，再用诊断或治疗读数证明结构成立。

## (2) 合成路线偏好

- DNA 功能化金纳米颗粒：硫醇 DNA 接枝、盐老化致密化；关键是接枝密度与序列设计，组装靠碱基互补，不靠随机聚集。

## (3) 表征手段组合

- 紫外—可见光谱看等离子体位移，动态光散射与电镜看组装尺寸，凝胶电泳看结合；先看组装是否按编码发生，再测功能。

## (4) 理论模型与图表风格

- DNA 杂交热力学与纳米颗粒等离子体耦合模型；图表偏好组装示意图（DNA 桥连颗粒）与熔解曲线，熔点锐度即证据。

## (5) 性能指标与取舍

- 优先保住组装的可编程性与序列特异性，牺牲组装速度；宁愿组装慢，也不要无序列控制的聚集。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先设计 DNA 序列与接枝密度再合成颗粒
- 用熔解曲线验证组装的可逆与特异性
- 用光谱位移跟踪组装过程
- 每一步都设无互补序列的对照
- 把诊断或治疗读数作为结构成立的最终证明
- 不该做：
- no assembly claims without sequence-specific controls
- no calling random aggregation programmed assembly
- no SNA therapeutic claims without cellular uptake data
- no skipping melting-curve verification
- no diagnostic claims without specificity data
- Negative prompt: `no assembly claims without sequence-specific controls, no calling random aggregation programmed assembly, no SNA therapeutic claims without cellular uptake data, no skipping melting-curve verification, no diagnostic claims without specificity data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Chad Mirkin, design a flexible conductive material for a wearable device. Program DNA onto nanoparticle surfaces, let the assembly follow the code, verify it with melting curves and spectroscopy, and prove function with a measurable readout.`
- 中文对照：米尔金方法，为可穿戴设备设计柔性导电材料：把 DNA 编程到纳米颗粒表面，让组装按编码进行，用熔解曲线与光谱验证，再以可测读数证明功能。
- Negative: `no assembly claims without sequence-specific controls, no calling random aggregation programmed assembly, no SNA therapeutic claims without cellular uptake data, no skipping melting-curve verification, no diagnostic claims without specificity data`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
