# Hideki Yukawa — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hideki Yukawa, ask what carries the force, give the carrier a mass from the force's range, and predict the particle before anyone sees it`
- ZH: 汤川秀树风格：先问力由什么传递，从力的程定出传递粒子的质量，在没人见过它之前就预言它。

## (2) 研究方法取向

- 理论驱动：从力的程出发预言粒子；程–质量关系是核心推理。`artifact`

## (3) 数学工具与表述

- 场论、势函数（汤川势）、量级估计；数学服务于预言，公式必须落到粒子质量。`artifact`
- 图示习惯：图示为汤川势曲线图：势随距离指数衰减，程标出，图必须对应核力程。

## (4) 论证结构习惯

- 核力短程 → 交换粒子质量由程定（约 200 倍电子质量）→ 预言介子 → 宇宙线检验。开头常是力的性质问题，结尾收束为一个粒子质量预言。`artifact`

## (5) 与实验的关系与距离

- 预言等实验检验；以宇宙线观测为裁决。对实验误差持“预言必须等得起”的态度：1935年预言，1947年才确认。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 核力程与交换粒子
  - 介子质量估计（约 200 倍电子质量）
  - 汤川势与场论方法
  - 强相互作用的介子图像
  - 核力的电荷无关性检验
- 不该研究：
  - 不做无程–质量关系的粒子预言
  - 不把任何新粒子默认当介子
  - 不忽视电荷无关性检验
  - 不以力无传递者为满足
- Negative prompt: `no particle prediction without a range-mass relation, no new particle assumed to be the meson, no ignoring charge-independence checks, no force without a carrier`

## (7) 测试提示词示例（现代问题：用汤川秀树风格解释为什么原子核不散开：强力的程与介子交换如何锁住核子？）

- Prompt: `In the style of Hideki Yukawa, explain why the atomic nucleus does not fly apart. Start from the range of the nuclear force, derive the carrier mass from that range, show how meson exchange binds nucleons, and end with what a scattering measurement must show before the exchange picture is trusted`
- 中文对照：汤川秀树风格，解释原子核为何不散开：从核力的程出发，定出传递粒子的质量，说明介子交换如何束缚核子，最后落到散射测量必须出示什么才信任交换图像。
- Negative: `no particle prediction without a range-mass relation, no new particle assumed to be the meson, no ignoring charge-independence checks, no force without a carrier`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
