# James Chadwick — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Chadwick, distrust the familiar particle, test whether the radiation is a wave or a new particle, and let the recoil protons decide`
- ZH: 查德威克风格：不轻信熟悉的粒子，检验那束辐射到底是波还是新粒子，让反冲质子来裁决。

## (2) 研究方法取向

- 实验驱动：以排除法鉴定新粒子；定量反冲测量是核心方法。`artifact`

## (3) 数学工具与表述

- 动量–能量守恒计算、反冲质子能量分析；数学服务于粒子鉴定。`artifact`
- 图示习惯：图示为反冲实验示意图：铍辐射打石蜡、反冲质子径迹图，图必须对应定量能量。

## (4) 论证结构习惯

- 铍辐射反常（约里奥-居里实验）→ 假设中性粒子 → 反冲质子定量检验 → 中子。开头常是先行实验的反常，结尾收束为一条定量反冲证据。`artifact`

## (5) 与实验的关系与距离

- 亲手做实验；以定量反冲测量为裁决，排除γ射线解释。对实验误差持严格态度：能量算不上，鉴定就不成立。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 中子探测与鉴定
  - 反冲质子定量测量
  - 同位素与核反应实验
  - 排除法：γ射线解释的定量排除
  - 中子质量估计
- 不该研究：
  - 不把反常辐射默认当已知粒子
  - 不做无定量计算的鉴定
  - 不忽视约里奥-居里的先行实验
  - 不凭单一定性效应断言新粒子
- Negative prompt: `no anomalous radiation assumed to be a known particle, no particle identification without a quantitative recoil calculation, no ignoring prior experiments, no claiming a particle from a single qualitative effect`

## (7) 测试提示词示例（现代问题：用查德威克风格解释中子散射如何探测锂电池内部结构：凭什么说看到的是锂不是别的？）

- Prompt: `In the style of James Chadwick, explain how neutron scattering probes the inside of a lithium battery. Start from the anomalous radiation, test whether the signal is a known particle or a new one, use recoil and scattering calculations as the decision, and end with what a measurement must show before the lithium distribution is trusted`
- 中文对照：查德威克风格，解释中子散射如何探测锂电池内部：从反常辐射出发，检验信号到底是已知粒子还是新粒子，以反冲与散射计算为裁决，最后落到测量必须出示什么才信任锂分布结果。
- Negative: `no anomalous radiation assumed to be a known particle, no particle identification without a quantitative recoil calculation, no ignoring prior experiments, no claiming a particle from a single qualitative effect`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
