# Ejnar Hertzsprung — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见天文学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ejnar Hertzsprung, plot every star's brightness against its colour, let the giants separate from the dwarfs on the diagram, and read the life of a star off the pattern`
- ZH: 赫茨普龙风格：把每颗星的亮度对颜色作图，让巨星与矮星在图上自分， 从图样读出恒星的一生。

## (2) 观测方法

- 仪器：照相测光与光谱观测；以恒星视星等与光谱型为材料。
- 观测策略：系统收集恒星光度与光谱型数据，样本覆盖各类恒星。
- 样本：恒星光度与温度数据；造父变星样本（定标用）。

## (3) 推演与模型建构

- 推演：赫罗图——光度对温度作图，恒星分列为主序、巨星支等序列；由图样推断恒星演化路径。
- 模型：恒星演化模型——恒星在图上的位置随演化移动；模型边界是当时不知恒星能源（核聚变后世确立）。
- 链条：光度 + 温度 → 赫罗图 → 序列 → 演化推断。

## (4) 证据链

- 证据：赫罗图上的序列结构为直接证据；巨星与矮星的光度差异达数个星等。
- 关键证据：同一光谱型的恒星光度分属巨星与矮星两群，分类须用光度。
- 反证处理：图上偏离序列的恒星照实标出，不删除；演化推断保持为推断，不写成观测事实。

## (5) 理论语言与论证结构

- 语言：作图体——光度—温度图是论证本身；辅以分类表。
- 论证：归纳式——从大量恒星作图归纳序列，结尾给出赫罗图与演化推断。
- 图表：赫罗图是论证核心。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 恒星光度与温度的系统测量
- 赫罗图的绘制与序列分析
- 巨星与矮星的区分
- 造父变星周光关系的定标
- 不该研究：方法上的禁区，见 Negative prompt。
- Negative prompt: `no reading a star's age off one point on the diagram, no deleting a star that falls between the sequences, no claiming the diagram proves a theory of stellar energy, no using apparent brightness where luminosity belongs`

## (7) 测试提示词示例（现代题材：检验一个现代恒星群体的演化历史）

- Prompt: `In the style of Ejnar Hertzsprung, test a modern stellar population: plot every star's luminosity against its temperature, let the sequences separate themselves, and read the population's history off the diagram — keeping every star that falls between the sequences on the plot`
- 中文对照：以赫茨普龙的风格检验一个现代恒星群体：把每颗星的光度对温度作图，让各个序列自分，从图样读出群体的历史——把落在序列之间的每一颗星都留在图上。
- Negative: `no reading a star's age off one point on the diagram, no deleting a star that falls between the sequences, no claiming the diagram proves a theory of stellar energy, no using apparent brightness where luminosity belongs`
- 检验点：回答是否按该天文学家的方法组织（观测—推演—模型—验证），是否出现 Negative prompt 禁止的套路，是否把当时模型当作现代定论。
