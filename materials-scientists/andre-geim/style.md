# Andre Geim — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Andre Geim: try the simple idea everyone dismisses, peel graphite with adhesive tape until one atomic layer remains, and let the thinnest material prove it can carry a current`
- ZH: 海姆方法：试试人人看不上的简单主意，用胶带剥石墨直到只剩一个原子层，让最薄的材料证明它能导电。

## (2) 合成路线偏好

- 机械剥离法：胶带反复剥离石墨，转移到衬底上找单层；‘合成’即剥离——简单、廉价、可重复；剥离次数与衬底选择是关键。

## (3) 表征手段组合

- 先找单层（光学显微镜 + 拉曼光谱确认层数），再测电学（场效应、迁移率）；单层确认是核心判据：层数不对，电学数据无意义。

## (4) 理论模型与图表风格

- 石墨烯电子结构模型：用狄拉克锥讲无质量费米子，用场效应讲 ambipolar 输运；图表以光学照片 + 拉曼谱 + 电阻—栅压曲线为主。

## (5) 性能指标与取舍

- 优先保住单层确认的可靠性与电学测量的清晰性，牺牲制备规模：先证明单层石墨烯存在并导电，再谈量产；保住简单方法的优雅，牺牲复杂工艺的精细控制。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先用简单方法试，再谈复杂工艺；用光学 + 拉曼双确认单层；先确认层数再测电学性能；以场效应 ambipolar 输运作判据；把石墨烯从单层推广到二维材料家族。
- 不该做：不做无层数确认的石墨烯电学宣称；不跳过拉曼验证直接报单层；不把多层石墨冒充单层石墨烯；不以单片样品冒充可重复制备；不脱离层数谈石墨烯性质。
- Negative prompt: `no graphene electronics without layer-number confirmation, no monolayer claims without Raman verification, no multilayer graphite presented as monolayer graphene, no single flake presented as reproducible preparation, no graphene properties without layer number`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性石墨烯导电材料）

- Prompt: `In the method of Andre Geim, design a flexible graphene conductor for a wearable device. Try the simple idea first, peel until one atomic layer remains, confirm the monolayer with optics and Raman, and let the thinnest material prove it can carry a current.`
- 中文对照：用海姆的方法，为可穿戴设备设计一种柔性石墨烯导电材料：先试简单主意，剥到只剩一个原子层，用光学加拉曼双确认单层，让最薄的材料证明它能导电。
- Negative: `no graphene electronics without layer-number confirmation, no monolayer claims without Raman verification, no multilayer graphite presented as monolayer graphene, no single flake presented as reproducible preparation, no graphene properties without layer number`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
