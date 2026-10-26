# John B. Fenn — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #61。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Fenn, spray a solution into a fine mist, let the solvent evaporate and leave the ions bare, and weigh large molecules that were once thought too fragile for mass spectrometry`
- ZH: 芬恩风格：把溶液喷成细雾，让溶剂蒸发、离子裸露，称量一度被认为太脆弱而无法进质谱的大分子。

## (2) 实验设计风格

- 实验类型以质谱方法开发为主：电喷雾电离、分子束、质谱检测。变量控制是喷雾电压、溶剂组成与气流逐项固定；仪器偏好自制电喷雾质谱接口，离子化温和先于灵敏度。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以质荷比定分子量”：多电荷峰系列反推大分子分子量。数据呈现为质谱图与去卷积分子量，证据强度以峰系列的完整性与标准蛋白的符合度为准。

## (4) 模型建构风格

- 模型是归纳的：从电喷雾现象归纳出多电荷离子形成机制，再以此解释大分子谱图。抽象程度中等，模型必须对应可测的峰系列。遇例外先检查溶剂与喷雾条件，不轻易改电离机制。

## (5) 论证与表达风格

- 论证结构为“问题—电离方法—谱图—分子量”；论文以方法描述与应用实例为主，结论明确。术语创造（电喷雾电离）明确。与田中的方法互补：电喷雾用于溶液大分子，软激光解吸用于固体样品。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先做出稳定的电喷雾，再谈分子量
- 以多电荷峰系列反推分子量
- 用已知蛋白标准检验方法
- 先标明电离条件的适用范围
- 不该做：
- 不以单个峰定大分子分子量
- 不把碎片峰当分子离子峰
- 不忽略溶剂与 pH 对电离的影响
- 不把电喷雾结果外推到不挥发体系
- Negative prompt: `no determining a large-molecule mass from a single peak, no treating fragment peaks as molecular ion peaks, no ignoring solvent and pH effects on ionisation, no extrapolating electrospray results to non-volatile systems`

## (7) 测试提示词示例（现代题材：测定一种新型蛋白质药物的分子量与修饰）

- Prompt: `In the style of John Fenn, determine the molecular weight of a new protein drug: first make a stable electrospray from its solution, then record the multiply charged peak series, deconvolute it to a molecular weight, and check it against a known protein standard before claiming modifications`
- 中文对照：芬恩风格，测定一种新型蛋白质药物的分子量与修饰：先做出稳定电喷雾，再记录多电荷峰系列，去卷积得分子量，对已知蛋白标准检验后才谈修饰。
- Negative: `no determining a large-molecule mass from a single peak, no treating fragment peaks as molecular ion peaks, no ignoring solvent and pH effects on ionisation, no extrapolating electrospray results to non-volatile systems`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
