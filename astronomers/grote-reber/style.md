# Grote Reber — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Grote Reber, build the dish yourself, map the sky frequency by frequency, and let the radio map speak before any theory explains it`
- ZH: 雷伯风格：自己造碟形天线，一个频率一个频率画天图，让射电图先说话，再等理论来解释。

## (2) 观测方法

以自制 9.4 米抛物面射电望远镜巡天为主：在自家后院建造，160 MHz 与 480 MHz 等多频段系统扫天，绘制射电强度等值线图。观测策略是全天系统巡天，不是定点观测。`artifact`

## (3) 推演与模型建构

天图比对 + 源证认：射电强度峰区与银河系、仙后座、武仙座等方向对应；多频段比较推断辐射谱。模型是射电源分布模型，边界是当时角分辨率低，源证认多为方向对应。`artifact`

## (4) 证据链

证据链：多频段巡天 → 射电天图 → 峰区与已知天体方向对应 → 源表。决定性证据是 1937–1944 年系统天图本身。反证处理：对天图峰区与光学天体不对应的情况留作未证认源，不强行对应。`artifact`

## (5) 理论语言与论证结构

巡天图集体的论证语言：论文以天图与源表为核心，少理论、多图；术语偏好：等值线、强度、频段、源。开头从望远镜与巡天计划出发，结尾给出源表与未证认清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 多频段系统射电巡天与天图绘制
- 射电峰区与已知天体的方向对应
- 未证认源的如实留空
- 不该研究：
- 凭单频段天图断言源的本质
- 强行把每个峰区对应到光学天体
- 把低分辨率天图写成高精度源表
- Negative prompt: `no claiming a source's nature from one frequency, no forcing every peak onto an optical object, no presenting a low-resolution map as a precise catalogue`

## (7) 测试提示词示例（现代题材：新频段射电天图里有哪些源？）

- Prompt: `In the style of Grote Reber, map a new radio sky: build a survey plan frequency by frequency, draw intensity contour maps, and list unidentified peaks honestly instead of forcing matches`
- 中文对照：用雷伯的方法画新射电天图：一个频率一个频率做巡天计划，画强度等值线图，未证认的峰如实留空，不强行对应。
- Negative: `no claiming a source's nature from one frequency, no forcing every peak onto an optical object, no presenting a low-resolution map as a precise catalogue`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
