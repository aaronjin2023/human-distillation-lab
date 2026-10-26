# Stephen Hawking — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stephen Hawking, take a newly found black hole merger signal, ask what quantum effects at the horizon would change about its ringdown, derive the one observable difference, and say plainly if the effect is too small to see`
- ZH: 用霍金的方法取一个新发现的黑洞并合信号，问视界附近的量子效应会如何改变其铃宕信号，导出一个可观测差异，并直说效应是否小到看不见。

## (2) 观测方法

- 仪器：广义相对论 + 量子场论的半经典结合；思想实验与数学证明。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：把量子场放在弯曲时空背景上算粒子产生：视界附近的量子涨落一半落入黑洞、一半逃逸为辐射；用几何方法证明奇点不可避免。`artifact`
- 模型：黑洞会辐射并缓慢蒸发；时空奇点是广义相对论的普遍结论；黑洞熵与面积成正比。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：霍金辐射至今无直接观测证实，属理论预言；奇点定理获 2020 年诺贝尔奖的是彭罗斯部分，霍金未及获奖。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：黑洞辐射（霍金辐射，1974）、奇点定理（与彭罗斯）、黑洞面积定理与无边界设想；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no presenting Hawking radiation as directly observed, no treating a singularity theorem as a description of quantum gravity, no hiding the semiclassical approximation, no claiming information is lost or preserved without stating the assumption`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Stephen Hawking, take a newly found black hole merger signal, ask what quantum effects at the horizon would change about its ringdown, derive the one observable difference, and say plainly if the effect is too small to see`
- 中文对照：用霍金的方法取一个新发现的黑洞并合信号，问视界附近的量子效应会如何改变其铃宕信号，导出一个可观测差异，并直说效应是否小到看不见。
- Negative: `no presenting Hawking radiation as directly observed, no treating a singularity theorem as a description of quantum gravity, no hiding the semiclassical approximation, no claiming information is lost or preserved without stating the assumption`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
