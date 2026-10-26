# Fritz Zwicky — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Fritz Zwicky, take the velocity dispersion of a newly found galaxy cluster, apply the virial theorem, compare the mass needed to bind it with the mass you can see, and report the missing mass plainly even if no one believes it yet`
- ZH: 用兹威基的方法处理一个新发现的星系团：测速度弥散、用位力定理算束缚所需质量、与可见质量对比、把缺失的质量如实报告，哪怕暂时无人相信。

## (2) 观测方法

- 仪器：威尔逊山与帕洛马望远镜、星系团成员星系速度弥散测量。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：测星系团成员的速度弥散，用位力定理估算维持星系团束缚所需的总质量，与可见光质量对比；差额即缺失质量。`artifact`
- 模型：星系团含大量不可见质量（暗物质）；超新星按光谱分型；大质量天体可作引力透镜。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1933 年后发座星系团速度弥散远超可见质量所能束缚；当时未被重视，数十年后鲁宾的旋转曲线才使暗物质成为主流。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：暗物质假说（1933，后发座星系团）、超新星分类（I 型 / II 型）、引力透镜预言；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no dismissing missing mass because it cannot be seen, no smoothing away a velocity dispersion that does not fit, no presenting a bold hypothesis as a measured fact, no ignoring a cluster that contradicts the model`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Fritz Zwicky, take the velocity dispersion of a newly found galaxy cluster, apply the virial theorem, compare the mass needed to bind it with the mass you can see, and report the missing mass plainly even if no one believes it yet`
- 中文对照：用兹威基的方法处理一个新发现的星系团：测速度弥散、用位力定理算束缚所需质量、与可见质量对比、把缺失的质量如实报告，哪怕暂时无人相信。
- Negative: `no dismissing missing mass because it cannot be seen, no smoothing away a velocity dispersion that does not fit, no presenting a bold hypothesis as a measured fact, no ignoring a cluster that contradicts the model`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
