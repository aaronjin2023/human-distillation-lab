# Kiyotsugu Hirayama — 发现方法与理论风格规格 style.md（给文本 / 科学模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Kiyotsugu Hirayama, remove planetary perturbations to find proper orbital elements, group asteroids by shared elements, and infer a common origin from the grouping`
- ZH: 平山清次风格：先扣除行星摄动算出固有轨道根数，再按共有轨道根数把小行星分组，从分组推断共同起源。

## (2) 观测方法

以已发表的小行星轨道观测数据为材料，不靠新望远镜观测：汇集大量小行星的瞬时轨道根数（半长轴、偏心率、轨道倾角），样本量以百计。关键在数据处理而非仪器——用摄动理论把行星引力造成的长期摆动扣除，得到近似不变的固有根数。`artifact`

## (3) 推演与模型建构

统计分组 + 成因推断：固有根数相近的小行星聚成族（最初认出 Koronis、Eos、Themis 族，后补 Flora、Maria 族）；从“轨道根数相近到不可能是巧合”推断同族成员源自同一母体分裂。模型假设是固有根数在千万年尺度上近似守恒；边界是瞬时根数会摆动，不能直接分组。`artifact`

## (4) 证据链

证据链：轨道数据 → 固有根数计算 → 族群聚类 → 共同起源推断。决定性证据是 1918 年论文中三个族的聚类本身。反证处理：对族群边界模糊的成员不强行归属；对母体分裂机制（爆炸说 vs 碰撞说）留作开放问题，不以分组证据直接断言分裂机制。`artifact`

## (5) 理论语言与论证结构

数学化、统计式的论证语言：论文以轨道根数表与分布图为核心，少修辞、多数值；先摆数据分布，再给分组判据，最后才谈成因。术语偏好：固有根数（proper elements）、平均运动、族（family）。开头从轨道数据分布出发，结尾给出族群表并留下成因问题。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 小行星轨道根数的统计分组与族群识别
- 固有根数计算与摄动扣除方法
- 从轨道聚类推断小天体共同起源
- 不该研究：
- 只看瞬时轨道根数就分组
- 把轨道相近直接说成同一次分裂事件
- 凭单一小行星推断整个族群的成因
- Negative prompt: `no grouping from osculating elements alone, no claiming a single breakup event from orbital similarity, no inferring a whole family's origin from one asteroid`

## (7) 测试提示词示例（现代题材：新巡天小行星样本里有没有新的小行星族？）

- Prompt: `In the style of Kiyotsugu Hirayama, analyse a new survey sample of 500 asteroids: compute proper orbital elements, look for clusters in semi-major axis, eccentricity and inclination, and name any family you find only if the clustering survives perturbation removal`
- 中文对照：用平山清次的方法分析新巡天得到的 500 颗小行星样本：算出固有轨道根数，在半长轴、偏心率、倾角上找聚类，只有聚类在扣除摄动后仍然成立时才命名为一个族。
- Negative: `no grouping from osculating elements alone, no claiming a single breakup event from orbital similarity, no inferring a whole family's origin from one asteroid`
- 检验点：回答是否按该天文学家的方法走完观测—数据—模型—验证的链条，是否出现 Negative prompt 禁止的套路，是否把当时模型当作已证伪的真理使用。
