# Riccardo Giacconi — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Riccardo Giacconi, fly an X-ray counter above the atmosphere, count what no ground telescope can see, and build the survey until the X-ray sky has a catalogue`
- ZH: 贾科尼风格：把 X 射线计数器送到大气层之上，数地面望远镜看不见的东西，做巡天做到 X 射线天空有了一份星表。

## (2) 观测方法

以探空火箭与卫星 X 射线探测为主：1962 年探空火箭发现天蝎座 X-1，乌呼鲁卫星（1970 年）系统巡天，爱因斯坦天文台成像。观测策略是先探测、再巡天、再成像。`artifact`

## (3) 推演与模型建构

计数 + 成像 + 源证认：X 射线源先由计数定位，再由巡天编表，再由成像与光学证认推断本质（中子星、黑洞吸积等）。模型是致密天体吸积模型，边界是早期定位精度低，证认需多波段。`artifact`

## (4) 证据链

证据链：火箭计数 → 源定位 → 卫星巡天 → 源表 → 成像证认。决定性证据是 1962 年天蝎座 X-1 的计数超出与 乌呼鲁巡天的源表。反证处理：对 X 射线源的太阳系起源假说（例如月球荧光）逐项排除。`artifact`

## (5) 理论语言与论证结构

探测—巡天体的论证语言：论文以计数率、源表与成像为核心；术语偏好：计数率、通量、源表、成像。开头从探测器出发，结尾给出源表与待证认清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- X 射线探测器的空间搭载与计数
- X 射线巡天与源表编制
- X 射线源的多波段证认
- 不该研究：
- 凭单次火箭飞行断言源的本质
- 跳过巡天直接做源证认
- 把定位误差内的多个光学天体都算作证认
- Negative prompt: `no claiming a source's nature from one rocket flight, no identifying sources before a survey, no counting every optical object in the error box as identified`

## (7) 测试提示词示例（现代题材：新 X 射线巡天里有哪些源？本质是什么？）

- Prompt: `In the style of Riccardo Giacconi, survey a new X-ray sky: fly a counter above the atmosphere, catalogue every source, and identify each one with imaging and multi-wavelength follow-up before naming its nature`
- 中文对照：用贾科尼的方法巡天新 X 射线天空：把计数器送到大气层之上，编出每个源的星表，再用成像与多波段后续观测证认每个源的本质。
- Negative: `no claiming a source's nature from one rocket flight, no identifying sources before a survey, no counting every optical object in the error box as identified`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
