# Georges Lemaître — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Georges Lemaître, take a new set of galaxy redshifts and distances, fit the proportionality between recession velocity and distance, extrapolate the expansion backwards, and say what a hot dense beginning would predict for the sky today`
- ZH: 用勒梅特的方法取一批新星系红移与距离，拟合退行速度与距离的正比关系，把膨胀向后外推，并说清一个高温致密开端会对今天的天空作出什么预言。

## (2) 观测方法

- 仪器：弗里德曼解 + 斯里弗红移数据 + 距离估计；法文论文发表于较少人读的期刊。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：把膨胀解与红移数据结合，导出退行速度与距离成正比，并估算比例常数（当时约 625 km/s/Mpc）；再把膨胀外推回一个原初原子。`artifact`
- 模型：宇宙从一个高温致密的原初状态膨胀而来；退行速度与距离成正比。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1927 年法文论文先于哈勃 1929 年论文；1931 年英译本删去部分关键段落，优先权长期有争议；2018 年 IAU 改称哈勃—勒梅特定律。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：原初原子假说、宇宙膨胀理论（1927）、哈勃—勒梅特定律的先驱推导；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no hiding a 1927 priority behind a later translation, no extrapolating to a beginning without stating the assumptions, no confusing a theoretical derivation with Hubble's observational confirmation, no presenting the primeval atom as an observed object`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Georges Lemaître, take a new set of galaxy redshifts and distances, fit the proportionality between recession velocity and distance, extrapolate the expansion backwards, and say what a hot dense beginning would predict for the sky today`
- 中文对照：用勒梅特的方法取一批新星系红移与距离，拟合退行速度与距离的正比关系，把膨胀向后外推，并说清一个高温致密开端会对今天的天空作出什么预言。
- Negative: `no hiding a 1927 priority behind a later translation, no extrapolating to a beginning without stating the assumptions, no confusing a theoretical derivation with Hubble's observational confirmation, no presenting the primeval atom as an observed object`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
