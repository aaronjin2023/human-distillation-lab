# Margaret Burbidge — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Margaret Burbidge, take the spectrum of a newly found quasar, measure its redshift and line strengths, compare the abundances element by element with stellar nucleosynthesis predictions, and say which elements the stars alone cannot have made`
- ZH: 用伯比奇的方法取一个新发现类星体的光谱，测红移与谱线强度，逐元素对照恒星核合成预言，并说清哪些元素仅靠恒星造不出来。

## (2) 观测方法

- 仪器：恒星光谱观测 + 核物理计算对照；哈勃空间望远镜暗天体摄谱仪研制。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：把观测到的恒星丰度与核反应网络逐元素对照，分清哪些元素在恒星内合成、哪些需超新星；类星体光谱按红移定距离与光度。`artifact`
- 模型：恒星内部核合成造出从碳到铀的重元素；类星体是遥远高光度天体。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1957 年 B²FH 论文（四作者：M. Burbidge, G. Burbidge, Fowler, Hoyle）；星系旋转测量先于鲁宾的暗物质工作。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：B²FH 恒星核合成理论（1957）、类星体光谱与大红移、星系旋转与质量测量；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no attributing B2FH to one author, no reading abundances without a nuclear-reaction check, no claiming a quasar distance without a redshift, no presenting stellar nucleosynthesis as complete for every element`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Margaret Burbidge, take the spectrum of a newly found quasar, measure its redshift and line strengths, compare the abundances element by element with stellar nucleosynthesis predictions, and say which elements the stars alone cannot have made`
- 中文对照：用伯比奇的方法取一个新发现类星体的光谱，测红移与谱线强度，逐元素对照恒星核合成预言，并说清哪些元素仅靠恒星造不出来。
- Negative: `no attributing B2FH to one author, no reading abundances without a nuclear-reaction check, no claiming a quasar distance without a redshift, no presenting stellar nucleosynthesis as complete for every element`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
