# Maria Mitchell — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Maria Mitchell, sweep a new sky survey field night by night, compare every suspect object against the charts, and announce a comet only after its motion is recorded on successive nights`
- ZH: 用玛丽亚·米切尔的方法逐夜扫一片新巡天区，把每个可疑天体与星图比对，只在连续多夜记录到移动后才宣布发现彗星。

## (2) 观测方法

- 仪器：2 英寸折射望远镜（后为 3 英寸 Dollond）、星图比对、位置逐夜记录。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：每夜扫天、把可疑天体与星图逐一比对；发现后连续两夜记录位置再上报，不凭一夜印象定论。`artifact`
- 模型：新彗星须经多夜位置移动证实；太阳黑子是旋转的垂直空洞而非云。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1847 年 10 月 1 日发现，10 月 3 日上报；意大利德维科稍后独立报告，优先权归米切尔；1848 年丹麦金质奖章。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：彗星 C/1847 T1 发现（1847 年 10 月 1 日）、太阳黑子观测、瓦萨学院天文教学；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no announcing a comet from a single night, no reporting a position without a chart comparison, no confusing a faint comet with a star, no letting eagerness to announce replace two nights of verification`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Maria Mitchell, sweep a new sky survey field night by night, compare every suspect object against the charts, and announce a comet only after its motion is recorded on successive nights`
- 中文对照：用玛丽亚·米切尔的方法逐夜扫一片新巡天区，把每个可疑天体与星图比对，只在连续多夜记录到移动后才宣布发现彗星。
- Negative: `no announcing a comet from a single night, no reporting a position without a chart comparison, no confusing a faint comet with a star, no letting eagerness to announce replace two nights of verification`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
