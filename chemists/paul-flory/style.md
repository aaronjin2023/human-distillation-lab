# Paul Flory — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Flory, turn polymer chemistry into statistical physics: write the free energy, count the configurations, and let the equation predict what the beaker will do`
- ZH: 弗洛里风格：把高分子化学变成统计物理——写出自由能，数清构象，让方程预测烧杯里会发生什么。

## (2) 实验设计风格

- 实验类型以理论建模与实验验证并重：先建立高分子溶液与缩聚反应的统计模型，再用渗透压、光散射与黏度数据验证。变量控制是“模型参数—实验量”对照：改变分子量、浓度、溶剂，看理论预测是否成立。仪器偏好：渗透压计、光散射仪、黏度计，数据用于检验理论而非单纯记录。

## (3) 合成与分析风格

- 合成层面是缩聚动力学的定量描述：官能团等活性假设下，分子量分布由反应程度决定（Flory 分布）。关键操作是精确测定反应程度与分子量分布；分析上用渗透压测数均分子量、光散射测重均分子量、黏度测特性黏度，三者互相印证；证据标准是“理论曲线与实验点重合”。

## (4) 模型建构风格

- 模型是统计热力学模型：Flory–Huggins 溶液理论用相互作用参数描述聚合物—溶剂混合自由能；高分子链构象用无规线团统计描述。模型来自演绎——从统计力学第一性原理出发，再经实验修正。处理例外的方式是加修正项：良溶剂与不良溶剂、排除体积效应分开处理，不为一个反例推翻统计框架。

## (5) 论证与表达风格

- 论证结构是“方程—预测—验证”：先推导自由能与分布函数，再给出可检验的预测（θ 温度、凝胶点），最后用实验数据验证。论文数学密度高，图表以理论曲线与实验点对照为主。术语上“Flory–Huggins 理论”“θ 溶剂”沿用至今。与同行的关系：与哈金斯各自独立发展溶液理论，共享命名。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先写自由能或分布函数，再做实验验证
- 用渗透压、光散射、黏度三种方法测分子量，互相印证
- 给出可证伪的定量预测（如 θ 温度、凝胶点）
- 把理论曲线与实验点画在同一张图上对照
- 例外出现时加修正项，不推翻统计框架
- 不该做：- 只报实验数据而不建模型
- 用单一方法测分子量就下结论
- 做不可检验的定性论断
- 为凑理论曲线挑选数据点
- 把模型适用边界之外的结果写成模型失效
- Negative prompt: `no reporting data without a model, no molecular-weight claim from a single method, no untestable qualitative claims, no cherry-picking data points to fit the curve, no presenting out-of-range results as a failure of the model`

## (7) 测试提示词示例（现代问题：一种新聚合物能不能溶解，怎么从理论上预测并用实验检验？）

- Prompt: `In the style of Paul Flory, predict whether a new polymer will dissolve: write the Flory-Huggins free energy, estimate the interaction parameter, and test the prediction with osmotic pressure and light scattering.`
- 中文对照：弗洛里风格，预测一种新聚合物能否溶解：写出 Flory–Huggins 自由能，估计相互作用参数，再用渗透压与光散射检验预测。
- Negative: `no reporting data without a model, no molecular-weight claim from a single method, no untestable qualitative claims, no cherry-picking data points to fit the curve, no presenting out-of-range results as a failure of the model`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
