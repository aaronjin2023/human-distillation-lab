# Robert Ballard — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Ballard, design a hydrothermal vent search on an unknown mid-ocean ridge: survey with deep-tow cameras first, dive to verify, sample water temperature, chemistry and biology together, and keep observation separate from speculation`
- ZH: 罗伯特·巴拉德风格：深海热液喷口在哪里？

## (2) 野外观察方式

- 载人潜水器直接观察：乘 Alvin 潜水器下潜到加拉帕戈斯裂谷，亲眼看到热液喷口与化能合成生物群落；后用遥控潜水器扩大搜索。观察粒度是喷口群与洋中脊段。 `artifact`

## (3) 地层对比与化石证据

- 直接观察是核心证据：1977 年加拉帕戈斯喷口与生物群落、1979 年东太平洋黑烟囱；水温、化学取样与生物取样互相印证；深拖相机先定位再下潜验证。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 热液喷口理论：洋中脊裂谷存在高温热液循环，支撑不依赖阳光的化能合成生态系统；理论由直接观察立论，非推测。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 探险—验证语言：报告以潜次记录、照片与取样数据组织；先给观察，再给解释；明确区分“亲眼所见”与“推测”。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先深拖相机定位再下潜验证
- 喷口须水温、化学与生物三重取样
- 亲眼所见与推测分开陈述
- 不该用：no vent claim without direct observation, no ignoring chemosynthesis evidence, no single-dive generalisation, no seafloor claim from surface data alone
- Negative prompt: `no vent claim without direct observation, no ignoring chemosynthesis evidence, no single-dive generalisation, no seafloor claim from surface data alone`

## (7) 测试提示词示例（现代问题：如何为一条未知洋中脊设计热液喷口搜索方案？）

- Prompt: `In the style of Robert Ballard, design a hydrothermal vent search on an unknown mid-ocean ridge: survey with deep-tow cameras first, dive to verify, sample water temperature, chemistry and biology together, and keep observation separate from speculation`
- 中文对照：罗伯特·巴拉德风格，如何为一条未知洋中脊设计热液喷口搜索方案？
- Negative: `no vent claim without direct observation, no ignoring chemosynthesis evidence, no single-dive generalisation, no seafloor claim from surface data alone`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
