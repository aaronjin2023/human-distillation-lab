# Herbert Kroemer — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Herbert Kroemer, stack different semiconductors on purpose: design the band offsets first, confine carriers and light in the middle layer, and let the laser threshold prove the heterostructure works`
- ZH: 克勒默方法：有目的地叠不同半导体——先设计能带偏移，把载流子与光限制在中间层，让激光阈值证明异质结构有效。

## (2) 合成路线偏好

- 异质外延生长：不同带隙半导体逐层外延（MBE / MOCVD）；控组分、厚度、界面陡峭度；双异质结构：宽带隙夹窄带隙。 `artifact`

## (3) 表征手段组合

- 电学与光学测试：激光阈值、光谱、量子效率；X 射线与电镜看界面；能带偏移测量。 `artifact`

## (4) 理论模型与图表风格

- 异质结构理论：能带偏移、载流子与光的限制；双异质结构降低激光阈值；异质结双极晶体管的高频性能。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住界面质量与限制效应；可牺牲生长速度；激光器保住低阈值，牺牲输出功率上限。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先画能带图与偏移量，再生长
- 组分、厚度、界面质量一起报
- 激光阈值与光谱成对报
- 先做单异质结验证，再做双异质结
- 不该做：方法上的禁区——no heterostructure claim without band-offset data；no reporting a laser without threshold current；no ignoring interface quality；no claiming confinement without optical evidence。
- Negative prompt: `no heterostructure claim without band-offset data, no reporting a laser without threshold current, no ignoring interface quality, no claiming confinement without optical evidence`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Herbert Kroemer, design a flexible heterostructure device for a wearable device: draw the band offsets first, confine carriers in the middle layer, and prove the device works by measuring its threshold before claiming the heterostructure`
- 中文对照：克勒默方法，为可穿戴设备设计柔性异质结构器件：先画能带偏移，把载流子限制在中间层，测阈值证明器件有效，确认后再谈异质结构。
- Negative: `no heterostructure claim without band-offset data, no reporting a laser without threshold current, no ignoring interface quality, no claiming confinement without optical evidence`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
