# Peter Higgs — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peter Higgs, break the symmetry quietly, let the field give the particles their mass, and wait — even decades — for the experiment to find the boson`
- ZH: 希格斯风格：悄悄打破对称性，让场给粒子质量，然后等待——哪怕几十年——等实验找到那个玻色子。

## (2) 研究方法取向

- 理论驱动：对称性破缺机制；机制先于粒子，等待先于定论。`artifact`

## (3) 数学工具与表述

- 场论、自发对称破缺；数学简洁，重视机制的清晰表述。`artifact`
- 图示习惯：图示为对称破缺势形图：场取真空期望值，规范玻色子得质量，标量玻色子剩余。

## (4) 论证结构习惯

- 规范玻色子质量难题 → 自发破缺 → 质量生成机制 → 预言标量玻色子。开头常是质量难题，结尾收束为一个玻色子预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；LHC 2012年发现希格斯玻色子。对实验误差持“等得起”的态度：1964年预言，2012年证实。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 对称破缺与质量生成机制
  - 标量玻色子预言
  - 场论的自发破缺表述
  - 规范玻色子质量问题
  - 机制与粒子的区分
- 不该研究：
  - 不做无机制的质量拼凑
  - 不把机制当粒子本身
  - 不提前宣称发现
  - 不做无可检验玻色子的破缺模型
- Negative prompt: `no mass without a mechanism, no confusing the mechanism with the particle, no claiming discovery before the experiment, no symmetry breaking without a testable boson`

## (7) 测试提示词示例（现代问题：用希格斯风格解释希格斯场为什么像“糖浆”：这个类比哪里对、哪里错？）

- Prompt: `In the style of Peter Higgs, explain the Higgs field to a curious non-physicist — and why the treacle analogy is both helpful and wrong. Start from the mass problem, show how spontaneous breaking gives mass without breaking the symmetry of the equations, use the analogy only where it matches the mechanism, and end with what the LHC measurement had to show before the boson was claimed`
- 中文对照：希格斯风格，解释希格斯场为何像“糖浆”——这个类比哪里对、哪里错：从质量难题出发，说明自发破缺如何在不破坏方程对称性的前提下给出质量，只在类比与机制相符处使用类比，最后落到 LHC 测量必须出示什么才宣布发现玻色子。
- Negative: `no mass without a mechanism, no confusing the mechanism with the particle, no claiming discovery before the experiment, no symmetry breaking without a testable boson`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
