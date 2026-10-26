# Paul Flory — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Paul Flory, count the configurations first: write the free energy of mixing, let entropy and interaction compete, and test the prediction against solution and swelling data`
- ZH: 弗洛里方法：先数构象——写出混合自由能，让熵与相互作用竞争，用溶液与溶胀数据检验预言。

## (2) 合成路线偏好

- 高分子合成与交联：聚合、交联网络制备；溶液配制（良溶剂 / 不良溶剂）；溶胀实验控交联度。 `artifact`

## (3) 表征手段组合

- 黏度与光散射测分子量与尺寸；溶胀度测交联密度；热分析与力学测试看橡胶弹性；X 射线看结晶。 `artifact`

## (4) 理论模型与图表风格

- Flory–Huggins 理论：混合自由能、相互作用参数 χ、临界点；交联网络的橡胶弹性（熵弹性）；高分子链的构象统计。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住理论预言与实验数据的定量吻合；可牺牲模型的简洁性；橡胶弹性保住熵的解释，牺牲能量项的细节。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先写自由能，再做预言，最后才看实验
- 用溶液、溶胀、力学三类数据交叉检验同一参数
- 相互作用参数 χ 的取值与温度依赖一起报
- 构象统计的假设写清，不藏假设
- 不该做：方法上的禁区——no theory claim without a free-energy expression；no fitting chi without reporting temperature dependence；no ignoring polydispersity when testing a prediction；no claiming network theory from swelling data alone。
- Negative prompt: `no theory claim without a free-energy expression, no fitting chi without reporting temperature dependence, no ignoring polydispersity when testing a prediction, no claiming network theory from swelling data alone`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Paul Flory, design a flexible conductive polymer gel for a wearable device: write the mixing free energy first, predict swelling and conductivity from the interaction parameter, and test the prediction against swelling and mechanical data`
- 中文对照：弗洛里方法，为可穿戴设备设计柔性导电聚合物凝胶：先写混合自由能，用相互作用参数预言溶胀与导电性，再用溶胀与力学数据检验预言。
- Negative: `no theory claim without a free-energy expression, no fitting chi without reporting temperature dependence, no ignoring polydispersity when testing a prediction, no claiming network theory from swelling data alone`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
