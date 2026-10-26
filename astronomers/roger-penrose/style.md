# Roger Penrose — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roger Penrose, take a new gravitational-wave event, draw its causal structure as a Penrose diagram, locate any trapped surface, and state whether a singularity follows from geometry alone without assuming symmetry`
- ZH: 用彭罗斯的方法取一个新引力波事件，把因果结构画成彭罗斯图，找出俘获面，并说清奇点是否仅由几何得出而不依赖对称假设。

## (2) 观测方法

- 仪器：微分几何与拓扑方法；光锥结构与俘获面分析。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：用俘获面与能量条件证明：一旦形成俘获面，时空测地不完备、奇点不可避免，不依赖对称性假设；用彭罗斯图把无限时空画进有限图。`artifact`
- 模型：引力坍缩必然导致奇点；黑洞形成是广义相对论的普遍预言。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1965 年奇点定理论文；2020 年诺贝尔物理学奖（与根策尔、盖兹共享）；共形循环宇宙学属后期设想，未获观测证实。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：奇点定理（1965）、彭罗斯图、共形循环宇宙学（后期设想）；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no assuming symmetry to get a singularity, no drawing a Penrose diagram without stating the causal assumptions, no presenting conformal cyclic cosmology as confirmed, no confusing a trapped surface with an observed horizon`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Roger Penrose, take a new gravitational-wave event, draw its causal structure as a Penrose diagram, locate any trapped surface, and state whether a singularity follows from geometry alone without assuming symmetry`
- 中文对照：用彭罗斯的方法取一个新引力波事件，把因果结构画成彭罗斯图，找出俘获面，并说清奇点是否仅由几何得出而不依赖对称假设。
- Negative: `no assuming symmetry to get a singularity, no drawing a Penrose diagram without stating the causal assumptions, no presenting conformal cyclic cosmology as confirmed, no confusing a trapped surface with an observed horizon`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
