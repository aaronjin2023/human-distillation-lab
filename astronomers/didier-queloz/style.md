# Didier Queloz — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Didier Queloz, take the same velocity curve your supervisor found, test it against every stellar excuse, and then spend the next decades reading the planets' atmospheres`
- ZH: 迪迪埃·奎洛兹风格：把导师发现的那条速度曲线拿来，用每一种恒星借口检验它，然后花接下来几十年读行星的大气。

## (2) 观测方法

以视向速度测量与系外行星大气观测为主：飞马座 51b 发现时为马约尔的博士生，负责数据分析；后期转向凌星光谱与大气表征。观测策略是视向速度 + 凌星光谱结合。`artifact`

## (3) 推演与模型建构

视向速度 + 大气光谱：速度曲线定行星轨道与质量下限，凌星光谱测大气成分（水、钠等）；两类数据联合推断行星本质。模型是行星大气模型，边界是大气反演多解。`artifact`

## (4) 证据链

证据链：速度曲线 → 轨道 → 凌星光谱 → 大气成分。决定性证据是飞马座 51 速度曲线的周期性（与马约尔条目同源）与后期大气光谱。反证处理：恒星活动假信号逐项排除，大气反演多解如实报告。`artifact`

## (5) 理论语言与论证结构

数据分析—大气表征体的论证语言：论文以速度曲线拟合与光谱反演为核心；术语偏好：视向速度、大气光谱、反演、成分。开头从数据出发，结尾给出大气成分与不确定度。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 视向速度曲线的细致分析
- 恒星活动假信号的逐项排除
- 凌星光谱的大气成分反演
- 不该研究：
- 凭短期速度摆动断言行星
- 把大气反演多解写成唯一成分
- 把质量下限写成真实质量
- Negative prompt: `no planet from a short velocity wobble, no single atmospheric composition from a degenerate retrieval, no presenting a minimum mass as the true mass`

## (7) 测试提示词示例（现代题材：这颗系外行星大气里有什么？）

- Prompt: `In the style of Didier Queloz, characterise a new exoplanet atmosphere: take its transit spectrum, retrieve the composition, and report the degeneracies honestly before naming any molecule`
- 中文对照：用迪迪埃·奎洛兹的方法表征一颗新系外行星大气：取凌星光谱，反演成分，如实报告多解性后再谈分子。
- Negative: `no planet from a short velocity wobble, no single atmospheric composition from a degenerate retrieval, no presenting a minimum mass as the true mass`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
