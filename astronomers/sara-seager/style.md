# Sara Seager — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sara Seager, write the equation for what a biosignature needs, design the observation that could falsify it, and keep habitability a question rather than a claim`
- ZH: 萨拉·西格风格：把生物标志需要的条件写成方程，设计能证伪它的观测，让宜居性始终是个问题、而不是断言。

## (2) 观测方法

以系外行星大气光谱观测与理论建模为主：凌星光谱、直接成像光谱，结合大气模型预测可观测特征。观测策略是理论先行、观测检验。`artifact`

## (3) 推演与模型建构

大气模型 + 生物标志框架：由大气光谱反演成分，评估生物标志气体（如氧、甲烷组合）的可探测性；西格方程估计宜居行星数量。模型假设是生物标志需与非生物过程区分，边界是反演多解与假阳性。`artifact`

## (4) 证据链

证据链：大气模型 → 可观测特征预测 → 光谱观测 → 成分反演 → 生物标志评估。决定性证据尚在积累中（本文件夹只蒸方法与已发表理论，不宣称已发现生物标志）。反证处理：对生物标志的非生物来源（假阳性）逐项列出。`artifact`

## (5) 理论语言与论证结构

理论—观测结合的论证语言：论文以方程、模型预测与观测检验为核心；术语偏好：生物标志、假阳性、反演、宜居带。开头从理论框架出发，结尾给出可检验预测。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 系外行星大气模型与可观测特征预测
- 生物标志的假阳性逐项排除
- 宜居性评估的不确定度报告
- 不该研究：
- 把大气反演多解写成生物标志发现
- 跳过非生物来源检验直接谈生命
- 把宜居带写成宜居保证
- Negative prompt: `no biosignature claim from a degenerate retrieval, no life claim without ruling out abiotic sources, no presenting the habitable zone as a habitability guarantee`

## (7) 测试提示词示例（现代题材：这颗系外行星大气里的气体是生物标志吗？）

- Prompt: `In the style of Sara Seager, assess a biosignature claim: list every abiotic source for the gas, design the observation that could rule them out, and keep the conclusion open until the test is done`
- 中文对照：用萨拉·西格的方法评估一个生物标志说法：列出该气体的每一种非生物来源，设计能排除它们的观测，检验完成前结论保持开放。
- Negative: `no biosignature claim from a degenerate retrieval, no life claim without ruling out abiotic sources, no presenting the habitable zone as a habitability guarantee`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
