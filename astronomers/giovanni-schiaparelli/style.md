# Giovanni Schiaparelli — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giovanni Schiaparelli, map a new planetary surface by patient visual drawing at opposition, record every linear marking exactly as seen, and separate what was drawn from what it means — never let a translated word add an interpretation the drawing does not contain`
- ZH: 用斯基亚帕雷利的方法在大冲期间耐心目视绘制一颗新行星表面，如实记录每条线状痕迹，并把“画到了什么”与“它意味着什么”分开，绝不让一个译词给图加上图本身没有的解释。

## (2) 观测方法

- 仪器：米兰布雷拉天文台 8.6 英寸 Merz 折射望远镜、目视绘图。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：大冲期间长时间目视火星，逐线绘图、反复核对；流星雨则把辐射点轨道与已知彗星轨道比对。`artifact`
- 模型：火星表面有线状 canali 网络；英仙座流星雨碎片来自斯威夫特—塔特尔彗星轨道。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：canali 意为“水道”而非人工“运河”，英译误导；线状特征后被证实多为视错觉；流星雨—彗星关联成立。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：火星 canali 观测与制图（1877）、英仙座流星雨与斯威夫特—塔特尔彗星关联、双星观测；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no translating canali as canals, no turning a drawn line into an artificial structure, no ignoring observers who saw no lines, no presenting a visual impression as a photographed fact`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Giovanni Schiaparelli, map a new planetary surface by patient visual drawing at opposition, record every linear marking exactly as seen, and separate what was drawn from what it means — never let a translated word add an interpretation the drawing does not contain`
- 中文对照：用斯基亚帕雷利的方法在大冲期间耐心目视绘制一颗新行星表面，如实记录每条线状痕迹，并把“画到了什么”与“它意味着什么”分开，绝不让一个译词给图加上图本身没有的解释。
- Negative: `no translating canali as canals, no turning a drawn line into an artificial structure, no ignoring observers who saw no lines, no presenting a visual impression as a photographed fact`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
