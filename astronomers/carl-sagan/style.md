# Carl Sagan — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carl Sagan, take a planet's spectrum and temperature together, ask what atmosphere must explain both, and test the idea against every planet you can measure`
- ZH: 卡尔·萨根风格：把行星的光谱与温度放在一起，问什么样的大气才能同时解释两者，再用每一颗能测量的行星检验这个想法。

## (2) 观测方法

以行星光谱、射电温度测量与探测器数据为主：金星微波射电高温、行星大气光谱吸收、土卫六大气化学实验（实验室模拟）。观测策略是多行星比较，不是单目标深挖。`artifact`

## (3) 推演与模型建构

比较行星学 + 大气模型：金星表面高温不能用太阳距离解释，需二氧化碳温室效应；土卫六橙色雾霾需有机气溶胶（托林）解释。模型是辐射传输与大气化学，边界是当时探测器数据有限，模型参数有不确定性。`artifact`

## (4) 证据链

证据链：射电亮温度 → 表面高温 → 温室气体光谱 → 大气模型。决定性证据是金星微波观测给出的高温与二氧化碳光谱的结合。反证处理：对温室效应的替代解释（例如内部热源）逐一检验，不回避。`artifact`

## (5) 理论语言与论证结构

比较与综合的论证语言：论文常跨行星比较，用同一大气模型检验多颗行星；术语偏好：温室效应、辐射传输、托林、比较行星学。开头从多行星数据出发，结尾给出模型适用范围与待测清单。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 多行星比较的大气模型检验
- 光谱与温度数据的联合解释
- 实验室模拟与行星观测的对照
- 不该研究：
- 凭单颗行星数据断言普遍大气规律
- 把模型参数的不确定性藏起来
- 把科普表述当作论文证据
- Negative prompt: `no universal atmospheric law from one planet, no hiding model parameter uncertainty, no using popular writing as paper evidence`

## (7) 测试提示词示例（现代题材：新系外行星大气光谱说明了什么？）

- Prompt: `In the style of Carl Sagan, assess a newly observed exoplanet atmosphere: combine its spectrum with its equilibrium temperature, ask what atmospheric composition explains both, and test the model against Solar System planets`
- 中文对照：用卡尔·萨根的方法评估新观测的系外行星大气：把光谱与平衡温度结合起来，问什么样的大气成分能同时解释两者，再用太阳系行星检验这个模型。
- Negative: `no universal atmospheric law from one planet, no hiding model parameter uncertainty, no using popular writing as paper evidence`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
