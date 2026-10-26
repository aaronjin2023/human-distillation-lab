# Susan Kieffer — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Susan Kieffer, predict the blast range of a volcanic lateral explosion: translate the eruption into a compressible multiphase flow problem, test it with shock-tube experiments and numerical models, and state the uncertainty before giving any hazard advice`
- ZH: 苏珊·基弗风格：极端地质事件里的流体到底如何运动？

## (2) 野外观察方式

- 实验室与野外两头看：在实验室做冲击波与可压缩流体实验，在圣海伦斯火山口与黄石老忠实泉做野外观测，还把探头与微型摄像机伸进间歇泉导管。观察粒度从矿物晶格振动到行星尺度喷发。 `artifact`

## (3) 地层对比与化石证据

- 三线汇合：可压缩流体力学实验、数值模拟、野外观测互相校核；同位素与矿物热力学模型给出物质性质；一次事件（如圣海伦斯侧向爆轰）同时用实验、模拟与野外三套证据检验。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反常数据先当作证据线索处理，而非直接略过；缺失本身须在论证中注明位置与影响。`impression`（学界共识）

## (4) 理论建构方式

- 以流体力学统一灾害：火山喷发、陨石撞击、洪水与滑坡都是多相流体的快速状态变化；先算清流体行为，再谈灾害后果。 `artifact`
- 理论的尺度：从野外与记录尺度出发，逐步推广到区域乃至全球模型；推广一步，证据须跟一步；对反例的态度是限定适用范围或修正模型，而非回避。`impression`（学界共识）

## (5) 论证语言

- 物理语言论证：用冲击波、膨胀、相变等流体力学概念组织论文；类比日常现象（爆胎、水槽涟漪）解释极端过程；科普著作《The Dynamics of Disaster》（2013）把同一框架讲给公众。 `artifact`

## (6) 该用 / 不该用的论证套路

- 该用：
- 先把地质过程翻译成流体力学问题再求解
- 用实验室冲击波实验校核野外观测
- 把行星上的同类过程与地球过程并列比较
- 不该用：no qualitative-only description without fluid mechanics, no ignoring compressibility in high-pressure flow, no single-mechanism explanation for multiphase flow, no hazard advice without quantified uncertainty
- Negative prompt: `no qualitative-only description without fluid mechanics, no ignoring compressibility in high-pressure flow, no single-mechanism explanation for multiphase flow, no hazard advice without quantified uncertainty`

## (7) 测试提示词示例（现代问题：如何预测一次火山侧向爆发的冲击范围？）

- Prompt: `In the style of Susan Kieffer, predict the blast range of a volcanic lateral explosion: translate the eruption into a compressible multiphase flow problem, test it with shock-tube experiments and numerical models, and state the uncertainty before giving any hazard advice`
- 中文对照：苏珊·基弗风格，如何预测一次火山侧向爆发的冲击范围？
- Negative: `no qualitative-only description without fluid mechanics, no ignoring compressibility in high-pressure flow, no single-mechanism explanation for multiphase flow, no hazard advice without quantified uncertainty`
- 检验点：回答是否按该用套路展开、是否出现 Negative prompt 所禁的套路、结论是否注明证据边界。
