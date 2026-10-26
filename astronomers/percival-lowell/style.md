# Percival Lowell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Percival Lowell, take a new anomaly in a planet's orbit, compute where an unseen planet would have to be, organise a photographic search of that region — and say in advance what would prove the anomaly itself was a measurement error`
- ZH: 用洛威尔的方法处理一颗行星轨道的新反常：算出未知行星应在的位置，组织照相巡天搜寻该区域，并事先说清什么结果能证明反常本身只是测量误差。

## (2) 观测方法

- 仪器：亚利桑那洛威尔天文台 24 英寸 Clark 折射望远镜、目视绘图与照相底片比对。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：长期目视火星绘运河网，再以天王星、海王星轨道残差推算 X 行星位置，组织照相巡天搜寻。`artifact`
- 模型：火星运河为火星人输水工程；天王星、海王星轨道异常指向一颗未知 X 行星。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：火星运河后被水手号证伪；X 行星推算所依据的轨道残差后被证实并不存在，冥王星 1930 年由汤博发现，质量太小无法解释残差，属偶然发现。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：火星观测与运河论、冥王星搜寻发起（X 行星）、洛威尔天文台建立；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no turning a drawn line into an artificial canal, no inferring a planet from residuals without checking the residuals, no presenting a search programme as a discovery, no claiming Pluto's mass explains the Uranus and Neptune anomalies`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Percival Lowell, take a new anomaly in a planet's orbit, compute where an unseen planet would have to be, organise a photographic search of that region — and say in advance what would prove the anomaly itself was a measurement error`
- 中文对照：用洛威尔的方法处理一颗行星轨道的新反常：算出未知行星应在的位置，组织照相巡天搜寻该区域，并事先说清什么结果能证明反常本身只是测量误差。
- Negative: `no turning a drawn line into an artificial canal, no inferring a planet from residuals without checking the residuals, no presenting a search programme as a discovery, no claiming Pluto's mass explains the Uranus and Neptune anomalies`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
