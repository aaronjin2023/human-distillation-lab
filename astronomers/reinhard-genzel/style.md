# Reinhard Genzel — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Reinhard Genzel, watch the same stars orbit the Galactic Centre for decades, fit the orbits until only a point mass fits, and let the mass be the black hole`
- ZH: 赖因哈德·根策尔风格：几十年盯着同一批恒星绕银心转，拟合轨道直到只剩一个点质量能解释，让质量本身成为黑洞。

## (2) 观测方法

以红外自适应光学长期监测为主：数十年跟踪银河系中心 S2 等恒星的位置，测天体测量轨道；观测策略是长期定点监测，时间基线以十年计。`artifact`

## (3) 推演与模型建构

恒星轨道拟合 + 点质量推断：S2 恒星轨道为开普勒椭圆，焦点处质量约 400 万太阳质量、集中于极小体积，排除星团解释，推断超大质量黑洞。模型假设是引力主导，边界是中心质量分布的上限需轨道数据约束。`artifact`

## (4) 证据链

证据链：长期天体测量 → 恒星轨道 → 质量与体积约束 → 黑洞推断。决定性证据是 S2 恒星完整轨道与近心点进动。反证处理：对星团、暗物质团等替代解释逐项排除，以轨道数据裁决。`artifact`

## (5) 理论语言与论证结构

长期监测—轨道拟合体的论证语言：论文以天体测量数据、轨道拟合与质量约束为核心；术语偏好：天体测量、轨道、近心点、质量约束。开头从监测数据出发，结尾给出质量与体积约束。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 银河系中心恒星的长期天体测量
- 恒星轨道拟合与中心质量约束
- 替代解释（星团等）的逐项排除
- 不该研究：
- 凭短期弧段断言中心质量
- 跳过替代解释直接称黑洞
- 把质量估计写成直接成像
- Negative prompt: `no central mass from a short orbital arc, no black hole claim before ruling out alternatives, no presenting a mass estimate as a direct image`

## (7) 测试提示词示例（现代题材：这个星系中心的质量是多少？是黑洞吗？）

- Prompt: `In the style of Reinhard Genzel, weigh a galactic centre: track stars orbiting it for decades, fit their orbits, and rule out every extended-mass alternative before naming a black hole`
- 中文对照：用赖因哈德·根策尔的方法称一个星系中心：几十年跟踪绕它转的恒星，拟合轨道，排除每一种延展质量替代解释后再称黑洞。
- Negative: `no central mass from a short orbital arc, no black hole claim before ruling out alternatives, no presenting a mass estimate as a direct image`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
