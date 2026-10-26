# Claudius Ptolemy — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claudius Ptolemy, build one geometric machine that saves every phenomenon: deferent, epicycle, eccentric and equant, each tuned until the predicted place matches the observed place`
- ZH: 托勒密风格：造一台能解释一切现象的几何机器：均轮、本轮、偏心圆、均衡点，逐一调校，直到预报位置与观测位置相符。

## (2) 观测方法

仪器为肉眼加测角器（浑仪、象限仪）；观测策略是汇集前人观测（喜帕恰斯等）加自己的长期记录，重点观测行星位置、月食与恒星位置。观测的极限是人眼与测角精度，但数据量大、时间跨度长。`artifact`

## (3) 推演与模型建构

推演是几何模型建构：地球居中，行星在本轮上绕均轮运行，偏心圆解释速度不均，均衡点进一步调校速度。模型假设：天体运动为匀速圆周运动的组合。链条：观测位置 → 几何模型 → 参数调校 → 预报检验。模型能预报行星位置，精度在当时极高。`artifact`

## (4) 证据链

证据链：行星位置的长期记录 → 本轮模型解释逆行 → 均衡点解释速度变化 → 预报与观测对照。关键证据强度在当时很高：模型可预报、可复核。但模型是“当时模型，后世证伪”：地心说与匀速圆周假设已被日心说与椭圆轨道取代，蒸馏的是建模方法，不是地心结论。`artifact`

## (5) 理论语言与论证结构

语言为几何化论证：《天文学大成》为命题—证明—数表的结构，公式即几何作图与数表。论证开头从观测现象出发，结尾给出可查表的预报。术语：本轮、均轮、偏心圆、均衡点。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星位置的长期记录与模型拟合
- 本轮—均轮—偏心圆—均衡点的几何建构
- 以预报与观测的对照检验模型
- 不该研究：
- 不把地心说写成真理（当时模型，后世证伪）
- 不凭模型优美就忽视观测残差
- 不把承袭喜帕恰斯的星表写成全然原创
- Negative prompt: `no geocentrism as truth, no ignoring residuals for an elegant model, no presenting inherited catalogue as wholly original`

## (7) 测试提示词示例（现代题材：用托勒密的方法，为一颗现代系外行星的视运动建一个几何模型并检验残差）

- Prompt: `In the style of Claudius Ptolemy, build a geometric model for a modern exoplanet's apparent motion: deferent plus epicycle, tune the parameters until predictions match observations, list the residuals, and state where the model is a calculating device rather than a physical truth`
- 中文对照：托勒密风格，为一颗现代系外行星的视运动建几何模型：均轮加本轮，调校参数直到预报与观测相符，列出残差，并明说模型在何处只是计算工具而不是物理真理。
- Negative: `no geocentrism as truth, no ignoring residuals for an elegant model, no presenting inherited catalogue as wholly original`
- 检验点：回答是否按该天文学家的方法走（观测 → 几何假设 → 模型建构 → 预测检验 → 成书）、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
