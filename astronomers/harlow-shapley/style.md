# Harlow Shapley — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harlow Shapley, map the three-dimensional distribution of a new sample of globular clusters, find where their centre lies, and infer the size and centre of the Galaxy from that distribution — then say which part of the inference would collapse if the distance scale were wrong`
- ZH: 用沙普利的方法画一批新球状星团的三维分布，找出分布中心，由此推断银河系的大小与中心，并说清若距离定标错了，推论的哪一部分会垮掉。

## (2) 观测方法

- 仪器：威尔逊山望远镜照相底片、球状星团中造父变星与 RR 天琴座变星。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：用变星周光关系逐个定球状星团距离，再把星团的三维分布当作银河系形状的示踪物；分布中心即银心。`artifact`
- 模型：大银河系模型：银河系直径远大于此前估计，太阳远离银心；旋涡星云属于银河系内（此点后被证伪）。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：球状星团分布不对称、集中于人马座方向；1920 年与柯蒂斯的大辩论；1924 年后哈勃的造父变星证明旋涡星云在银河系外。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：银河系大小与太阳偏离中心位置、球状星团距离测定、造父变星定标银河系尺度；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no claiming spiral nebulae are inside the Galaxy, no using one distance indicator without cross-checking, no letting a debate win replace a measurement, no ignoring dust extinction in distance estimates`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Harlow Shapley, map the three-dimensional distribution of a new sample of globular clusters, find where their centre lies, and infer the size and centre of the Galaxy from that distribution — then say which part of the inference would collapse if the distance scale were wrong`
- 中文对照：用沙普利的方法画一批新球状星团的三维分布，找出分布中心，由此推断银河系的大小与中心，并说清若距离定标错了，推论的哪一部分会垮掉。
- Negative: `no claiming spiral nebulae are inside the Galaxy, no using one distance indicator without cross-checking, no letting a debate win replace a measurement, no ignoring dust extinction in distance estimates`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
