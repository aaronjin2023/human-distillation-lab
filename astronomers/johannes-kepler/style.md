# Johannes Kepler — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Johannes Kepler, fit the orbit to Tycho's positions and no other, sacrifice the circle when eight minutes of arc refuse it, and keep the ellipse only because the data demand it`
- ZH: 开普勒风格：只按第谷的位置拟合轨道，8 角分的残差不容圆轨道时就牺牲圆轨道，保留椭圆只因数据要求如此。

## (2) 观测方法

- 仪器：本人无大型观测仪器；以第谷二十年行星位置数据为材料，精度约 1 角分。
- 观测策略：以火星为突破口——火星轨道偏心率大，圆轨道模型的残差最明显。
- 样本：第谷火星位置序列（多年）、太阳与行星位置。

## (3) 推演与模型建构

- 推演：几何拟合——试遍圆轨道、本轮组合，残差最小仍有 8 角分，改试椭圆轨道，残差消失；由面积定律与调和定律完成三定律。
- 模型：椭圆轨道模型——太阳在椭圆一焦点；模型假设是行星受太阳的力驱动（当时为磁力类比，后世牛顿力学取代其机制解释）。
- 链条：第谷数据 → 圆轨道试拟合 → 8 角分残差 → 椭圆拟合 → 三定律。

## (4) 证据链

- 证据：8 角分残差是最关键的证据——小于第谷的观测误差即不可容忍，大于它即模型错误。
- 关键证据：火星位置的椭圆拟合残差降至观测误差之内。
- 反证处理：残差不删除、不平滑、不归因于观测误差；模型错了就改模型，数据永远优先。

## (5) 理论语言与论证结构

- 语言：数学拟合 + 几何证明；《新天文学》以长篇试错过程示人，失败尝试亦如实记录。
- 论证：归纳 + 演绎——从火星数据归纳椭圆，再演绎面积定律与调和定律；论证过程透明，试错全记录。
- 图表：轨道拟合图与残差表是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 火星轨道的椭圆拟合
- 行星运动三定律的推导
- 第谷数据的系统拟合与残差分析
- 《鲁道夫星表》的编制
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no ignoring an eight-minute residual to save the circle, no smoothing the data to fit the model, no claiming a law from one planet without testing the others, no presenting the magnetic-force guess as the law itself`

## (7) 测试提示词示例（现代题材：分析一份系外行星凌星数据）

- Prompt: `In the style of Johannes Kepler, analyse a modern exoplanet transit dataset: fit a circular orbit first, report the residuals honestly, try the ellipse only when the residuals exceed the measurement error, and keep the ellipse only if the residuals fall inside the error bars`
- 中文对照：以开普勒的风格分析一份现代系外行星凌星数据：先拟合圆轨道，如实报告残差，只在残差超过测量误差时才试椭圆，残差落回误差棒内才保留椭圆。
- Negative: `no ignoring an eight-minute residual to save the circle, no smoothing the data to fit the model, no claiming a law from one planet without testing the others, no presenting the magnetic-force guess as the law itself`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
