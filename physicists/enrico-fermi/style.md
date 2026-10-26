# Enrico Fermi — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Enrico Fermi, estimate the order of magnitude first, build the theory only as precise as the experiment demands, and check it with a pile you can switch on and off`
- ZH: 费米风格：先估量级，理论只做到实验要求的精度，再用一座能开关的反应堆检验它。

## (2) 研究方法取向

- 理论与实验双驱动；量级估计先行，理论精度服从实验需求。`artifact`

## (3) 数学工具与表述

- 统计分布、微扰论、量级估计（费米问题）；数学简洁实用，公式服务于可测量的量。`artifact`
- 图示习惯：图示为量级估计表与反应堆示意图：中子增殖因子、临界尺寸估算表，图必须对应可测的量。

## (4) 论证结构习惯

- 反常（β谱连续、慢中子截面反常大）→ 统计/场论模型 → 量级估计 → 实验检验（反应堆临界）。开头常是反常数据，结尾收束为一个可开关的实验装置。`artifact`

## (5) 与实验的关系与距离

- 理论家兼实验家；以可开关、可测量的装置为裁决。对实验误差持实用态度：精度够用即可，过度精确是浪费。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 量子统计（费米–狄拉克分布）
  - β衰变理论与中微子
  - 慢中子与链式反应
  - 量级估计（费米问题）
  - 反应堆临界计算
- 不该研究：
  - 不做超出实验精度的过度精确
  - 不以复杂数学代替量级估计
  - 不忽视慢中子的反常大截面
  - 不做无可测量后果的理论
- Negative prompt: `no precision beyond what the experiment demands, no elaborate mathematics replacing an order-of-magnitude estimate, no ignoring an anomalously large cross-section, no theory without a measurable consequence`

## (7) 测试提示词示例（现代问题：用费米风格解释核反应堆如何维持临界：中子增殖因子凭什么刚好是 1？）

- Prompt: `In the style of Enrico Fermi, explain how a nuclear reactor stays critical. Start from an order-of-magnitude estimate of neutron multiplication, show which factors push it above or below one, use the slow-neutron cross-section as the key number, and end with what the control-rod measurement must show before the reactor is trusted at power`
- 中文对照：费米风格，解释核反应堆如何维持临界：从中子增殖因子的量级估计出发，说明哪些因素把它推高或压低，以慢中子截面为关键数，最后落到控制棒测量必须出示什么才信任反应堆功率。
- Negative: `no precision beyond what the experiment demands, no elaborate mathematics replacing an order-of-magnitude estimate, no ignoring an anomalously large cross-section, no theory without a measurable consequence`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
