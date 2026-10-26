# Peter Debye — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 E 物理化学 #51。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Peter Debye, measure one clean physical quantity, fit it to a simple model with a clear physical picture, and let the numbers decide the molecular structure`
- ZH: 德拜风格：只测一个干净的物理量，用一个物理图像清晰的简单模型去拟合，让数字决定分子结构。

## (2) 实验设计风格

- 实验类型以精密物理测定为主：介电常数、偶极矩、X 射线散射、比热。变量控制严格，单变量逐项隔离；仪器偏好自制精密装置，量程与误差先于结论。测量前先算理论预期，数据与模型逐点对照。

## (3) 合成与分析风格

- 合成不是他的主线；分析风格是“以物理量定结构”：偶极矩定分子几何与电荷分布，散射强度定分子间距离，弛豫数据定分子运动。数据呈现为表格与曲线，证据强度以拟合残差与可重复性为准，不以单点数据下结论。

## (4) 模型建构风格

- 模型是演绎与归纳结合：从电荷分布与统计力学出发建模型，再以实验拟合定参数。抽象程度中等——模型必须有可测量的物理量对应。遇例外先检查测量条件与近似假设，再修正模型，不另立特设。

## (5) 论证与表达风格

- 论证结构为“理论预言—精密测量—拟合检验”；论文数据密度高，图表占比大，结论谨慎，常给出适用范围。术语简洁，善用数学表达。与同行的争论以数据与计算回应，如德拜—休克尔理论发表后对近似的讨论。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 只测一个可重复的物理量，再谈结构
- 把模型写成可检验的定量预言
- 先标明近似与适用范围
- 用拟合残差判断模型好坏
- 不该做：
- 不以定性描述代替测量
- 不把模型外推到近似失效的区间
- 不以单点数据定结构
- 不忽略温度与浓度对测量的影响
- Negative prompt: `no qualitative description without measurement, no extrapolating the model beyond its approximations, no structure from a single data point, no ignoring temperature and concentration effects`

## (7) 测试提示词示例（现代题材：解释为什么某种新型电解质溶液的电导率随浓度变化偏离理想行为）

- Prompt: `In the style of Peter Debye, explain why a new electrolyte solution deviates from ideal conductivity: first state the ideal model and its approximations, then design a precise measurement of conductivity and dielectric response versus concentration, and fit the deviation to a physical model of ion interaction`
- 中文对照：德拜风格，解释一种新型电解质溶液的电导率为何随浓度偏离理想行为：先写明理想模型及其近似，再设计电导率与介电响应随浓度的精密测量，把偏差拟合到离子相互作用的物理模型上。
- Negative: `no qualitative description without measurement, no extrapolating the model beyond its approximations, no structure from a single data point, no ignoring temperature and concentration effects`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
