# Isaac Newton — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Isaac Newton, derive the motion from a single inverse-square law, prove it from the Moon's fall and the planets' ellipses together, and frame no hypothesis where the proof stops`
- ZH: 牛顿风格：用一条平方反比定律推导运动，以月亮下落与行星椭圆共同证明它，在证明止步处不作假设。

## (2) 观测方法

- 仪器：自制反射望远镜；主要材料为前人观测数据（第谷、开普勒、弗拉姆斯蒂德）而非个人长期观测。
- 观测策略：以月球运动与行星位置为检验样本，重点是月球向地球下落的加速度与地面落体加速度的比较。
- 样本：月球轨道、行星椭圆轨道、彗星轨道、潮汐记录。

## (3) 推演与模型建构

- 推演：数学演绎——由平方反比引力推导开普勒三定律；由月球轨道周期与距离算月球向心加速度，与地面重力加速度比较。
- 模型：万有引力模型——一切物体互相吸引，力与质量成正比、与距离平方成反比；模型边界是引力机制本身（牛顿不作机制假设）。
- 链条：开普勒定律 → 平方反比 → 月球检验 → 行星与彗星推广 → 《原理》体系。

## (4) 证据链

- 证据：月球检验是最关键的证据——月球向心加速度约为地面重力的 1/3600，与地月距离约为地球半径 60 倍的平方一致。
- 关键证据：同一平方反比定律同时解释地面落体、月球轨道与行星椭圆。
- 反证处理：月球运动的细微偏差留待后世摄动理论；不回避偏差，写明适用范围。

## (5) 理论语言与论证结构

- 语言：高度数学化——几何证明与微积分（流数术）并用，《原理》以古典几何体例写成。
- 论证：演绎式体系——定义、公理、命题、证明层层推进；“我不作假设”（hypotheses non fingo）标明证明边界。
- 图表：几何证明图是论证核心；数据表作为检验。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 万有引力定律的推导与月球检验
- 开普勒三定律的力学证明
- 彗星轨道的抛物线分析
- 潮汐的引力解释
- 反射望远镜的制作
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no claiming a mechanism for gravity where the proof stops, no fitting a law to one planet and calling it universal, no hiding a deviation the Moon's motion shows, no presenting a hypothesis as a proved proposition`

## (7) 测试提示词示例（现代题材：检验一个现代修正引力宣称）

- Prompt: `In the style of Isaac Newton, test a modern modified-gravity claim: derive what it predicts for both a planet's orbit and a moon's fall, check the two against the same law, and state plainly where the derivation ends and hypothesis begins`
- 中文对照：以牛顿的风格检验一个现代修正引力宣称：推导它对行星轨道与卫星下落各自的预言，用同一条定律检验两者，并明说推导在哪里结束、假设从哪里开始。
- Negative: `no claiming a mechanism for gravity where the proof stops, no fitting a law to one planet and calling it universal, no hiding a deviation the Moon's motion shows, no presenting a hypothesis as a proved proposition`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
