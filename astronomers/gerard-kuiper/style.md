# Gerard Kuiper — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gerard Kuiper, read a planet's spectrum and a moon's orbit together, infer the unseen population from the seen distribution, and state the prediction before the telescope can check it`
- ZH: 柯伊伯风格：把行星光谱与卫星轨道放在一起读，从已见的分布推断未见的群体，在望远镜能验证之前先把预言说清楚。

## (2) 观测方法

以大望远镜光谱与照相观测为主：行星与卫星光谱（土卫六甲烷吸收带）、卫星搜寻（长时间曝光照相底片）、行星亮度与颜色测量。观测策略是目标明确的定点观测，不是盲巡天。`artifact`

## (3) 推演与模型建构

从分布推断未见群体：由彗星轨道分布与太阳系形成理论推断海王星外应存在小天体带；由卫星轨道与行星光谱推断卫星成因与大气成分。模型假设是太阳系形成于旋转星云盘，残余物质应留在外围；边界是预言的带的具体密度与范围当时无法测定。`artifact`

## (4) 证据链

证据链：光谱吸收线 → 大气成分；卫星发现 → 轨道与成因；彗星轨道统计 → 外围带预言。决定性证据各不相同：土卫六甲烷靠光谱线证认，天卫二与海卫二靠底片上的新亮点，柯伊伯带靠后世巡天（1992 年 QB1）验证。反证处理：对预言与后世观测的出入（带的存在与密度）留待观测裁决。`artifact`

## (5) 理论语言与论证结构

理论—观测结合的论证语言：论文常从太阳系形成理论出发，再落到光谱与轨道数据；术语偏好：光谱带、轨道根数、星云盘、残余物质。开头常给理论框架，结尾给出可检验的预言或待观测清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 行星与卫星光谱的大气成分推断
- 卫星轨道与太阳系形成理论的结合
- 从已知分布外推未见天体群体的预言
- 不该研究：
- 把预言写成已观测到的事实
- 凭单条光谱线断言大气组成
- 忽略预言与后世观测的出入
- Negative prompt: `no presenting a prediction as an observation, no claiming an atmosphere from a single spectral line, no ignoring where later observations disagree with the prediction`

## (7) 测试提示词示例（现代题材：新巡天的遥远天体分布需要什么样的未见源群体？）

- Prompt: `In the style of Gerard Kuiper, infer an unseen population from a new survey: take the observed orbital distribution of distant objects, ask what source reservoir it requires, and state the prediction with its testable consequences`
- 中文对照：用柯伊伯的方法从新巡天推断未见群体：取已观测到的遥远天体轨道分布，问它需要什么样的源储库，再把预言连同可检验的后果一起说清楚。
- Negative: `no presenting a prediction as an observation, no claiming an atmosphere from a single spectral line, no ignoring where later observations disagree with the prediction`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
