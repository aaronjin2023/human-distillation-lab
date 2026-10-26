# Arno Penzias — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Arno Penzias, take an unexplained uniform signal in a new radio survey, eliminate every instrumental source one by one — antenna, receiver, ground, sky — and only then compare what is left with a cosmological prediction`
- ZH: 用彭齐亚斯的方法处理新射电巡天中一个无法解释的均匀信号：逐一排除天线、接收机、地面、天空等一切仪器来源，再把剩下的与宇宙学预言对照。

## (2) 观测方法

- 仪器：贝尔实验室霍姆德尔角天线、微波辐射计、低噪声接收机。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：先排除一切仪器噪声：清鸽粪、测天线温度、换接收机，剩余的各向同性约 3 K 噪声无法消除；再与普林斯顿迪克组的理论预言对照。`artifact`
- 模型：天空存在约 3 K 的各向同性微波背景，是大爆炸的余辉。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1965 年与威尔逊的论文与迪克组解释论文同刊；1978 年诺贝尔奖与威尔逊共享一半（各 1/4 份额），另一半授予卡皮察。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：宇宙微波背景辐射发现（1965，与罗伯特·威尔逊）、霍姆德尔角天线射电测量、1978 年诺贝尔物理学奖；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no attributing a uniform signal to the sky before eliminating the instrument, no publishing a residual without listing what was removed, no confusing a 3 K excess with a calibrated temperature, no claiming a cosmological origin from one antenna alone`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Arno Penzias, take an unexplained uniform signal in a new radio survey, eliminate every instrumental source one by one — antenna, receiver, ground, sky — and only then compare what is left with a cosmological prediction`
- 中文对照：用彭齐亚斯的方法处理新射电巡天中一个无法解释的均匀信号：逐一排除天线、接收机、地面、天空等一切仪器来源，再把剩下的与宇宙学预言对照。
- Negative: `no attributing a uniform signal to the sky before eliminating the instrument, no publishing a residual without listing what was removed, no confusing a 3 K excess with a calibrated temperature, no claiming a cosmological origin from one antenna alone`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
