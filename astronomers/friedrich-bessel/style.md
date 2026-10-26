# Friedrich Bessel — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Friedrich Bessel, measure one star's tiny shift against the far background for a whole year, publish the parallax with its error bar, and predict the unseen companion from the wobble alone`
- ZH: 贝塞尔风格：整整一年测量一颗星相对遥远背景的微小位移，公布带误差棒的视差，只凭摆动就预言看不见的伴星。

## (2) 观测方法

- 仪器：柯尼斯堡天文台分仪（heliometer），精密测角；以暗弱近星为目标。
- 观测策略：选天鹅座 61——自行大、亮度暗，暗示距离近；整年跟踪其相对背景星的位移。
- 样本：天鹅座 61 的周年视差序列；天狼星的自行摆动记录。

## (3) 推演与模型建构

- 推演：由周年视差角算恒星距离（视差与距离成反比）；由天狼星自行摆动反推伴星质量与轨道。
- 模型：日心几何模型——地球绕太阳公转造成恒星周年视差；模型假设是背景星足够远、视差可忽略。
- 链条：选近星 → 整年测位移 → 视差角 → 距离 → 伴星预言。

## (4) 证据链

- 证据：周年视差的周期性位移为直接证据；视差角约 0.3 角秒，接近仪器极限，误差棒是论证的一部分。
- 关键证据：天鹅座 61 的位移周期恰为一年，与地球公转同步。
- 反证处理：视差信号微弱时以多年重复观测与误差分析支撑，不夸大精度。

## (5) 理论语言与论证结构

- 语言：精密测量体——视差角、误差棒、统计分析；论证靠误差估计。
- 论证：归纳 + 演绎——从整年位移归纳视差，再演绎距离，结尾给出带误差的距离值。
- 图表：位移—时间图与误差表是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星周年视差的精密测量
- 恒星距离的首次测定
- 天狼星伴星的预言
- 天体测量方法的建立
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no publishing a parallax without its error bar, no claiming a distance from a single season, no ignoring the background stars' own motion, no announcing a companion you have not seen without stating it is a prediction`

## (7) 测试提示词示例（现代题材：测量一颗系外行星宿主恒星的视差）

- Prompt: `In the style of Friedrich Bessel, measure a modern exoplanet host star's parallax: observe it for a full year against distant background stars, publish the parallax angle with its error bar, and predict any unseen companion from the residual wobble — clearly labelled as a prediction`
- 中文对照：以贝塞尔的风格测量一颗现代系外行星宿主恒星的视差：整年相对遥远背景星观测，公布带误差棒的视差角，从残余摆动预言任何看不见的伴星——并明确标注这是预言。
- Negative: `no publishing a parallax without its error bar, no claiming a distance from a single season, no ignoring the background stars' own motion, no announcing a companion you have not seen without stating it is a prediction`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
