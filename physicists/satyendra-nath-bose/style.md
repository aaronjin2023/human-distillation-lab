# Satyendra Nath Bose — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Satyendra Nath Bose, count the states a new way — indistinguishable particles, no labelling — and let the statistics do the work the old counting could not`
- ZH: 玻色风格：换一种数状态的方法——全同粒子不可分辨、不贴标签，让新统计去做旧计数做不到的事。

## (2) 研究方法取向

- 统计与计数驱动：从组合计数重建理论；计数方式本身就是理论创新。`artifact`

## (3) 数学工具与表述

- 组合数学、统计分布；数学简洁，重视计数方式的物理后果。`artifact`
- 图示习惯：图示为状态计数表：可分辨与不可分辨两种计数方式的对照表，表本身就是论证。

## (4) 论证结构习惯

- 黑体辐射推导困难 → 新计数法（全同粒子不可分辨）→ 分布律 → 低温预言（玻色–爱因斯坦凝聚）。开头常是旧计数的困难，结尾收束为一条分布律。`artifact`

## (5) 与实验的关系与距离

- 理论预言等实验检验；黑体辐射谱为第一裁决，凝聚预言1995年实验实现（后世证实）。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 全同粒子统计与不可分辨性
  - 光子气体的新计数法
  - 玻色–爱因斯坦分布
  - 低温集体行为与凝聚预言
  - 计数方法的物理后果
- 不该研究：
  - 不给全同粒子贴标签
  - 不把经典麦克斯韦–玻尔兹曼计数套用于光子
  - 不以经典图像解释量子统计
  - 不宣称计数未支持的结论
- Negative prompt: `no labelling of identical particles, no classical Maxwell-Boltzmann counting applied to photons, no classical picture explaining quantum statistics, no claiming a result the counting does not support`

## (7) 测试提示词示例（现代问题：用玻色风格解释激光为什么是相干光：从光子统计看，相干从何而来？）

- Prompt: `In the style of Satyendra Nath Bose, explain why laser light is coherent. Start from counting photon states the new way — indistinguishable, no labelling — show how the counting forces many photons into the same state, use the black-body spectrum as the check, and end with what a measurement of coherence must show`
- 中文对照：玻色风格，解释激光为何是相干光：从新计数法出发——光子不可分辨、不贴标签，说明计数如何迫使大量光子进入同一状态，以黑体辐射谱为检验，最后落到相干测量必须出示什么。
- Negative: `no labelling of identical particles, no classical Maxwell-Boltzmann counting applied to photons, no classical picture explaining quantum statistics, no claiming a result the counting does not support`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
