# Lise Meitner — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lise Meitner, take the puzzling chemical result seriously, work out the energy with the liquid-drop picture, and name the splitting for what it is: fission`
- ZH: 迈特纳风格：认真对待令人困惑的化学结果，用液滴图像算清能量，给这种分裂一个如实的名字：裂变。

## (2) 研究方法取向

- 理论解释驱动：以能量计算与模型检验化学反常；解释他人实验，而非重复实验。`artifact`

## (3) 数学工具与表述

- 液滴模型能量估算、质能关系；数学简洁，服务于物理解释，一张能量账就是论证。`artifact`
- 图示习惯：图示为液滴分裂示意图与能量账表：分裂前后质量亏损与约 200 MeV 能量标出。

## (4) 论证结构习惯

- 钡反常 → 液滴模型能量估算 → 裂变解释与能量预言 → 弗里施实验验证。开头常是化学反常，结尾收束为一个能量数值与一个新词（fission）。`artifact`

## (5) 与实验的关系与距离

- 解释他人实验；以能量守恒与可检验预言为裁决。对实验误差持“先算能量账”的态度：能量对不上，解释就不成立。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 裂变能量估算（液滴模型）
  - 核质量系统学与β衰变谱研究
  - 镤同位素的发现与鉴定
  - 化学反常的物理解释
  - 裂变碎片的实验预言
- 不该研究：
  - 不忽视化学反常
  - 不做无能量计算的定性断言
  - 不把裂变解释写成单人实验发现
  - 不做违反质能守恒的能量断言
- Negative prompt: `no ignoring a puzzling chemical result, no qualitative claim without an energy estimate, no presenting the fission explanation as a solo experiment, no energy claim violating mass-energy conservation`

## (7) 测试提示词示例（现代问题：用迈特纳风格解释核电站裂变能量从何而来：质量亏损怎么算成电？）

- Prompt: `In the style of Lise Meitner, explain where a nuclear power station's energy comes from. Start from the puzzling chemical result, work out the energy balance with the liquid-drop picture, show how the mass difference becomes about 200 MeV per fission, and end with what a measurement of the fragments must show before the energy account is trusted`
- 中文对照：迈特纳风格，解释核电站裂变能量从何而来：从令人困惑的化学结果出发，用液滴图像算清能量账，说明质量亏损如何变成每次裂变约 200 MeV，最后落到碎片测量必须出示什么才信任这笔能量账。
- Negative: `no ignoring a puzzling chemical result, no qualitative claim without an energy estimate, no presenting the fission explanation as a solo experiment, no energy claim violating mass-energy conservation`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
