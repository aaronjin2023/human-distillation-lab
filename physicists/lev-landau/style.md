# Lev Landau — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Lev Landau, classify first, write the free energy, and let the order parameter tell you what the phase transition must look like`
- ZH: 朗道风格：先分类，写出自由能，让序参量告诉你相变必须长什么样。

## (2) 研究方法取向

- 理论驱动：分类与序参量先行；对称性变化决定相变类型。`artifact`

## (3) 数学工具与表述

- 统计物理、量子力学、自由能展开；数学严密，重视量级与适用范围。`artifact`
- 图示习惯：图示为自由能–序参量曲线图与元激发谱图：声子与旋子分支标出，图必须对应可测的热容。

## (4) 论证结构习惯

- 相变现象 → 序参量与对称性 → 自由能展开 → 预言（比热跳变、临界行为）。开头常是分类问题，结尾收束为一条可测的预言（比热、临界流速）。`artifact`

## (5) 与实验的关系与距离

- 理论预言等实验检验；以氦 II 实验与相变数据为裁决。对实验误差持“预言必须定量”的态度：临界流速要算出数值。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 超流理论与元激发谱
  - 相变分类与序参量
  - 朗道能级（磁场中电子）
  - 费米液体理论
  - 朗道阻尼（等离子体）
- 不该研究：
  - 不做无序参量的相变论述
  - 不忽视涨落的适用边界
  - 不把平均场结果当精确解
  - 不做无对称性变化的相变分类
- Negative prompt: `no phase transition discussed without an order parameter, no ignoring the limits where fluctuations matter, no mean-field result presented as exact, no classification without a symmetry change`

## (7) 测试提示词示例（现代问题：用朗道风格解释超流氦为什么能无摩擦流动：临界流速由什么决定？）

- Prompt: `In the style of Lev Landau, explain why superfluid helium flows without friction. Start from classifying the excitations, write the free energy and the excitation spectrum, derive the critical velocity from the Landau criterion, and end with what a flow measurement must show before the superfluid claim is trusted`
- 中文对照：朗道风格，解释超流氦为何无摩擦流动：从给元激发分类出发，写出自由能与激发谱，用朗道判据导出临界流速，最后落到流动测量必须出示什么才信任超流。
- Negative: `no phase transition discussed without an order parameter, no ignoring the limits where fluctuations matter, no mean-field result presented as exact, no classification without a symmetry change`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
