# Yan Dongsheng — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Yan Dongsheng, design high-temperature ceramics from phase relations first: map the system, regulate microstructure at high temperature, and prove performance in service before claiming a material`
- ZH: 严东生方法：先从相关系设计高温陶瓷——画清体系相图，高温下调控微结构，在服役中考验性能，确认后才谈材料。

## (2) 合成路线偏好

- 高温固相烧结与热压烧结：氮化硅、SiAlON 体系，添加剂（稀土、碱土氧化物）调控液相烧结；碳纤维增强复合材料的浸渍与热压；闪烁晶体生长。 `artifact`

## (3) 表征手段组合

- XRD 定相、高温 XRD 看相变；SEM / TEM 看晶粒形貌与晶界相；热分析与高温力学测试；闪烁性能与光学测试。 `artifact`

## (4) 理论模型与图表风格

- 相图与相平衡：Si3N4–AlN–MxOy 体系相区；添加剂调控 α-SiAlON 晶粒生长与微结构；高温材料设计与微结构调控。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住高温强度与热稳定性；可牺牲室温加工便利性；功能陶瓷保住功能响应，牺牲部分机械性能。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先画清体系相图与相区，再定成分与添加剂
- 用高温表征验证相变与晶粒生长，不只看室温结构
- 微结构调控与性能测试成对报，不分开谈
- 服役条件下的性能优先于实验室常温数据
- 不该做：方法上的禁区——no composition claim without a phase diagram；no high-temperature claim from room-temperature data alone；no ignoring additives when reporting SiAlON microstructure；no performance claim without service-condition testing。
- Negative prompt: `no composition claim without a phase diagram, no high-temperature claim from room-temperature data alone, no ignoring additives when reporting SiAlON microstructure, no performance claim without service-condition testing`

## (7) 测试提示词示例（现代题材：为深海探测器设计一种耐压轻质结构材料）

- Prompt: `In the method of Yan Dongsheng, design a pressure-resistant lightweight ceramic for a deep-sea probe: map the phase diagram first, regulate grain growth with additives, and prove high-temperature and pressure performance in service conditions before claiming the material`
- 中文对照：严东生方法，为深海探测器设计耐压轻质陶瓷：先画清相图，用添加剂调控晶粒生长，在服役条件下验证耐压与高温性能，确认后才谈材料。
- Negative: `no composition claim without a phase diagram, no high-temperature claim from room-temperature data alone, no ignoring additives when reporting SiAlON microstructure, no performance claim without service-condition testing`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
