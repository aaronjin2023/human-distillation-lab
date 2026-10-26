# Vera Rubin — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vera Rubin, take the rotation curve of a newly mapped galaxy, measure speeds out to the faintest edge without smoothing the outer points away, and let a flat curve stand as evidence for unseen mass rather than trimming it to fit the visible mass`
- ZH: 用鲁宾的方法取一个新绘星系的旋转曲线，测到最暗边缘而不平滑掉外围点，让平坦曲线本身作为不可见质量的证据，而不是修掉它去迁就可见质量。

## (2) 观测方法

- 仪器：卡内基研究所图像增强摄谱仪（与肯特·福特合作）、光学光谱测速。`artifact`
- 观测策略：以卡内基 DTM 光谱仪沿星系主轴逐点测速，从仙女座（1970）扩展到 1978 年十个、1980 年二十一个旋涡星系；测到最暗边缘，不平滑掉外围点。`artifact`
- 极限：光谱仪的灵敏度决定能测到多暗的外围；超出极限的半径不下结论。`impression`

## (3) 推演与模型建构

- 推演：对多个旋涡星系逐半径测恒星与气体旋转速度，画旋转曲线；曲线在外围不下降即与可见质量预言冲突，差额即暗物质。`artifact`
- 模型：旋涡星系外围旋转速度基本不变（平坦旋转曲线）；星系嵌在远大于可见盘的暗物质晕中。`artifact`
- 模型边界：平坦旋转曲线只证未见质量的存在，不定其粒子性质；暗晕的形状与分布须另由引力透镜等方法定。`impression`

## (4) 证据链

- 证据：1970 年仙女座、1978 年十个星系的旋转曲线；暗物质概念首倡于兹威基 1933 年，鲁宾提供最有力证据；未获诺贝尔奖。`artifact`
- 关键证据：1970 年仙女座旋转曲线（Rubin & Ford, ApJ 159, 379）与 1978 年十个高光度旋涡星系的平坦旋转曲线；射电 21 厘米观测（罗伯茨等人）为并行证据。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：光谱数据表与旋转曲线图为主；结论写成“速度不随半径下降”的平直陈述，不做暗物质粒子层面的断言。`artifact`
- 论证：从逐半径测速出发，画旋转曲线，再与可见质量预言对照；结尾只称未见质量存在，不称已确认暗物质粒子。`artifact`
- 与前人对话：继承兹威基 1933 年的暗物质假说与巴布科克 1939 年的仙女座测速，把猜想变成系统的旋转曲线证据；与射电观测者并行，不独占。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：星系旋转曲线、暗物质证据、星系动力学巡天。
- 不该研究：方法上的禁区——不平滑掉外围旋转曲线点、不修数据去迁就可见质量、不把引力证据写成粒子确认、不把平坦曲线当作测量误差打发掉。
- Negative prompt: `no smoothing away the outer rotation-curve points, no trimming data to fit the visible mass, no claiming dark matter is identified when only its gravity is seen, no dismissing a flat curve as measurement error without testing it`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Vera Rubin, take the rotation curve of a newly mapped galaxy, measure speeds out to the faintest edge without smoothing the outer points away, and let a flat curve stand as evidence for unseen mass rather than trimming it to fit the visible mass`
- 中文对照：用鲁宾的方法取一个新绘星系的旋转曲线，测到最暗边缘而不平滑掉外围点，让平坦曲线本身作为不可见质量的证据，而不是修掉它去迁就可见质量。
- Negative: `no smoothing away the outer rotation-curve points, no trimming data to fit the visible mass, no claiming dark matter is identified when only its gravity is seen, no dismissing a flat curve as measurement error without testing it`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
