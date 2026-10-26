# Albert Einstein — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Albert Einstein, take a new anomaly in galaxy clustering, ask what field equation it would require if the anomaly is real, derive one clean testable prediction from it, and discard the model if the prediction fails`
- ZH: 用爱因斯坦的方法处理星系成团的一个新反常：若反常为真，它要求怎样的场方程，从中导出一个干净的可检验预言，预言失败就丢弃模型。

## (2) 观测方法

- 仪器：思想实验与张量场方程；不依赖个人观测，以数学自洽与可检验预言为工具。`artifact`
- 观测策略：按该天文学家的实际做法——巡天、定点长期监测或目标搜寻，样本量与观测时长以发表记录为准，不编造数字。`artifact`
- 极限：仪器的极限决定能看到什么；超出极限的结论不下。`impression`

## (3) 推演与模型建构

- 推演：从等效原理出发写场方程，求静态宇宙解时引入宇宙学常数；再给出光线偏折、水星进动、引力红移三项可检验预言。`artifact`
- 模型：时空弯曲即引力；宇宙可由场方程描述；静态宇宙需宇宙学常数。`artifact`
- 模型边界：模型在什么条件下成立、在哪里失效，须与模型本身一起写；失效处不靠修补假设硬撑。`impression`

## (4) 证据链

- 证据：1919 年日食光线偏折、水星近日点进动符合预言；静态宇宙模型后被膨胀观测取代。`artifact`
- 关键证据：哪一次观测、哪一组数据是决定性的，见上；决定性证据须能指认到具体论文、星表或数据表。`artifact`
- 反证处理：与理论不符的数据保留、修正模型或搁置，不删除、不平滑掉。`impression`

## (5) 理论语言与论证结构

- 语言：按成果物本身——数学化、几何化或描述性，公式密度与图表使用以论文为准；术语须界定，不靠修辞代替定义。`artifact`
- 论证：从观测出发或从理论出发，须写清；开头与结尾方式按论文结构写；给出预测的，写清预测是什么、由谁检验。`artifact`
- 与前人对话：继承谁、反驳谁、修正谁，须点名，不写成无源头的“学界认为”。`impression`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：广义相对论（1915）、宇宙学常数、引力透镜与引力红移预言；以及与之直接相关的天体、问题与方法——光谱与光度、距离定标、速度场、元素丰度、宇宙膨胀、致密天体、行星表面，视各人领域而定，只列研究层面。
- 不该研究：方法上的禁区——不凭先验臆测代替观测、不忽略残差、不把模型当观测、不把单一证据写成定论、不把已证伪的当时模型当作真理使用。
- Negative prompt: `no adding a constant to save a preconception, no presenting a thought experiment as an observation, no keeping a static universe after expansion is observed, no confusing the cosmological constant with dark energy`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Albert Einstein, take a new anomaly in galaxy clustering, ask what field equation it would require if the anomaly is real, derive one clean testable prediction from it, and discard the model if the prediction fails`
- 中文对照：用爱因斯坦的方法处理星系成团的一个新反常：若反常为真，它要求怎样的场方程，从中导出一个干净的可检验预言，预言失败就丢弃模型。
- Negative: `no adding a constant to save a preconception, no presenting a thought experiment as an observation, no keeping a static universe after expansion is observed, no confusing the cosmological constant with dark energy`
- 检验点：回答是否按该天文学家的方法步骤走、是否先处理数据再下结论、是否出现 Negative prompt 禁止的套路、是否把已证伪模型写成真理。
