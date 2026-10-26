# Michel Mayor — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Michel Mayor, measure a star's wobble metre by metre, fold years of velocities into one period, and claim a planet only when the orbit closes`
- ZH: 米歇尔·马约尔风格：把恒星的摆动一米一米量出来，把多年的速度折叠成一个周期，只有轨道闭合时才谈行星。

## (2) 观测方法

以高精度视向速度测量为主：ELODIE 光谱仪长期监测类太阳恒星，视向速度精度达米每秒级；飞马座 51 的速度曲线呈现约 4.2 天周期摆动。观测策略是长期定点监测，不是单次快照。`artifact`

## (3) 推演与模型建构

视向速度曲线 + 开普勒轨道拟合：周期性速度摆动拟合为行星轨道，定行星质量下限与轨道周期；飞马座 51b 为热木星，轨道周期短、质量约木星一半。模型假设是摆动由行星引力引起，边界是视向速度只给质量下限（轨道倾角未知）。`artifact`

## (4) 证据链

证据链：长期速度监测 → 周期信号 → 轨道拟合 → 行星解释。决定性证据是飞马座 51 速度曲线的周期性与相位稳定性。反证处理：对恒星活动（星斑、脉动）造成的假信号逐项排除，以多周期复现检验。`artifact`

## (5) 理论语言与论证结构

精密测量体的论证语言：论文以速度曲线、周期图与轨道拟合为核心；术语偏好：视向速度、周期、质量下限、轨道拟合。开头从仪器精度出发，结尾给出轨道参数与待测清单。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 高精度视向速度长期监测
- 周期信号的轨道拟合
- 恒星活动假信号的逐项排除
- 不该研究：
- 凭短期速度摆动断言行星
- 跳过恒星活动检验直接拟合轨道
- 把质量下限写成真实质量
- Negative prompt: `no planet from a short velocity wobble, no orbit fit before ruling out stellar activity, no presenting a minimum mass as the true mass`

## (7) 测试提示词示例（现代题材：这颗恒星的速度摆动是行星吗？）

- Prompt: `In the style of Michel Mayor, confirm a new exoplanet: monitor the star's radial velocity for years, fold the data into a period, rule out stellar activity, and fit the orbit before naming the planet`
- 中文对照：用米歇尔·马约尔的方法确认一颗新系外行星：多年监测恒星视向速度，把数据折叠成周期，排除恒星活动，拟合轨道后再命名行星。
- Negative: `no planet from a short velocity wobble, no orbit fit before ruling out stellar activity, no presenting a minimum mass as the true mass`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
