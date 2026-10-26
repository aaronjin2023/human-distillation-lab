# Pierre-Gilles de Gennes — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Pierre-Gilles de Gennes, find the scaling law first: name the motion reptation, reduce the entangled chain to a one-dimensional walk, and let the exponent prove the picture`
- ZH: 德热纳方法：先找标度律——把运动命名为爬行，把缠结链化为一维行走，让指数证明图像。

## (2) 合成路线偏好

- 理论工作为主：高分子溶液与熔体的标度分析；液晶相变；界面润湿与黏附；实验以文献数据与合作实验验证。 `artifact`

## (3) 表征手段组合

- 黏度与扩散数据检验标度指数；中子散射看链构象；流变测试看缠结；液晶光学观察看相变。 `artifact`

## (4) 理论模型与图表风格

- 爬行理论：缠结高分子链如蛇在管道中爬行，扩散与黏度服从标度律；标度概念统一液晶、聚合物与临界现象；朗道–德热纳理论。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住标度指数的普适性；可牺牲数值 prefactor 的精确性；理论保住图像的清晰，牺牲数学的繁复。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先写标度关系，再看数据
- 指数、适用范围、假设三者一起报
- 用多类体系（溶液、熔体、液晶）检验同一标度
- 把复杂问题化为简单图像，不藏复杂性
- 不该做：方法上的禁区——no scaling claim without an exponent and its range；no applying reptation outside entangled melts；no hiding the assumptions behind a scaling law；no claiming universality from a single system。
- Negative prompt: `no scaling claim without an exponent and its range, no applying reptation outside entangled melts, no hiding the assumptions behind a scaling law, no claiming universality from a single system`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Pierre-Gilles de Gennes, design a flexible conductive polymer for a wearable device: find the scaling law for chain motion first, name the regime, and test the predicted exponent against viscosity and diffusion data before claiming the design`
- 中文对照：德热纳方法，为可穿戴设备设计柔性导电聚合物：先找链运动的标度律，定出适用范围，用黏度与扩散数据检验预言指数，确认后再谈设计。
- Negative: `no scaling claim without an exponent and its range, no applying reptation outside entangled melts, no hiding the assumptions behind a scaling law, no claiming universality from a single system`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
