# James Peebles — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Peebles, take a new measurement of the cosmic microwave background, compute what it implies for the baryon density and the growth of structure, and check the same numbers against primordial element abundances before claiming agreement`
- ZH: 用皮布尔斯的方法取一次新的宇宙微波背景测量，算出它对重子密度与结构增长的含义，再用原初元素丰度对照同一组数字，吻合后再谈一致。

## (2) 观测方法

- 仪器：解析计算 + 数值模拟；把微观物理（核合成、复合）与宇宙膨胀史结合。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：从膨胀宇宙出发算原初元素丰度与微波背景温度，再算密度扰动如何长成星系；每一步都给出可与观测对照的数值。`artifact`
- 模型：宇宙微波背景与轻元素丰度是大爆炸的可检验预言；大尺度结构由原初扰动引力放大而成。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1960 年代与迪克组预言微波背景；2019 年诺贝尔物理学奖（理论宇宙学一半份额）。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：宇宙微波背景理论、大尺度结构形成理论、原初核合成与宇宙学参数、2019 年诺贝尔物理学奖；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no claiming agreement from one dataset alone, no fitting cosmology without checking element abundances, no presenting a parameter value without its uncertainty, no ignoring a tension between independent measurements`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of James Peebles, take a new measurement of the cosmic microwave background, compute what it implies for the baryon density and the growth of structure, and check the same numbers against primordial element abundances before claiming agreement`
- 中文对照：用皮布尔斯的方法取一次新的宇宙微波背景测量，算出它对重子密度与结构增长的含义，再用原初元素丰度对照同一组数字，吻合后再谈一致。
- Negative: `no claiming agreement from one dataset alone, no fitting cosmology without checking element abundances, no presenting a parameter value without its uncertainty, no ignoring a tension between independent measurements`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
