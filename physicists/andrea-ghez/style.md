# Andrea Ghez — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Andrea Ghez, track the same stars year after year, let the orbits draw the mass for you, and claim the black hole only when the orbits close`
- ZH: 盖兹风格：年复一年追踪同一批恒星，让轨道自己画出质量，轨道闭合了才谈黑洞。

## (2) 研究方法取向

- 观测驱动，长期追踪先行：以自适应光学红外观测多年追踪银心恒星轨道；轨道即证据。

## (3) 数学工具与表述

- 数学化程度中等：以开普勒轨道拟合、质量估计为证据；不以方程论证，靠轨道曲线说话。

## (4) 论证结构习惯

- 从恒星位置出发—多年追踪—轨道拟合—中心质量与致密性—黑洞结论；论证靠轨道闭合的完整性。

## (5) 与实验的关系与距离

- 亲手做观测；对误差严格：恒星位置须多年重复测量、系统误差受控，否则轨道不可信。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 银心恒星轨道的长期追踪
- 人马座 A* 质量的轨道测定
- 自适应光学红外观测技术
- 黑洞存在的观测证实
- 不该研究：
- 不claiming a black hole from a single year of positions
- 不presenting the Galactic Center work as a solo effort
- 不ignoring systematic errors in astrometry
- 不theorizing beyond what the orbits show
- Negative prompt: `no claiming a black hole from a single year of positions, no presenting the Galactic Center work as a solo effort, no ignoring systematic errors in astrometry, no theorizing beyond what the orbits show`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of Andrea Ghez, explain a quantum computer: track the same behavior again and again, let the pattern draw the conclusion for you, and claim the mechanism only when the pattern closes`
- 中文对照：盖兹风格，解释一台量子计算机：反复追踪同一行为，让图样自己画出结论，图样闭合了才谈机制。
- Negative: `no claiming a black hole from a single year of positions, no presenting the Galactic Center work as a solo effort, no ignoring systematic errors in astrometry, no theorizing beyond what the orbits show`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
