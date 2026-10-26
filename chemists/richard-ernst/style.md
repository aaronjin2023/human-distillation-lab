# Richard R. Ernst — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #62。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Ernst, replace slow frequency sweeps with a pulse and a Fourier transform, add a second dimension, and let the cross-peaks reveal the connections a one-dimensional spectrum hides`
- ZH: 恩斯特风格：以脉冲与傅里叶变换代替缓慢扫频，再加一个维度，让交叉峰揭示一维谱隐藏的连接。

## (2) 实验设计风格

- 实验类型以核磁共振方法开发为主：脉冲序列设计、傅里叶变换、二维谱采集。变量控制是脉冲宽度、延迟与采样点数逐项固定；仪器偏好自制与改装核磁共振谱仪，信噪比与分辨率先于结论。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以谱峰连接定结构”：化学位移定环境，耦合与交叉峰定连接。数据呈现为一维与二维谱图，证据强度以峰的分辨率与可重复性为准。

## (4) 模型建构风格

- 模型是演绎与归纳结合：从自旋物理演绎脉冲序列，再以谱图归纳结构。抽象程度中等，模型必须对应可测的谱峰。遇例外先检查脉冲校准与弛豫影响，不轻易改归属。

## (5) 论证与表达风格

- 论证结构为“脉冲—变换—谱图—归属—结构”；论文以方法描述与谱图为主，结论明确，常给出分辨率与灵敏度。术语创造（傅里叶变换核磁共振、二维核磁共振）明确。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先校准脉冲与变换参数，再采谱
- 以二维交叉峰定原子连接
- 用已知化合物检验新脉冲序列
- 先标明分辨率与灵敏度极限
- 不该做：
- 不以一维谱重叠峰定连接
- 不把伪峰当交叉峰
- 不忽略弛豫对定量的影响
- 不把方法灵敏度外推到不适用的核
- Negative prompt: `no assigning connections from overlapping one-dimensional peaks, no treating artefacts as cross-peaks, no ignoring relaxation effects on quantification, no extrapolating sensitivity to unsuitable nuclei`

## (7) 测试提示词示例（现代题材：解析一种新型天然产物的二维核磁共振结构）

- Prompt: `In the style of Richard Ernst, solve a new natural product by two-dimensional NMR: first calibrate the pulse sequence and Fourier transform, then collect the 2D spectrum, assign the cross-peaks to atomic connections, and only claim the structure when the assignments are consistent across spectra`
- 中文对照：恩斯特风格，解析一种新型天然产物的二维核磁共振结构：先校准脉冲序列与傅里叶变换，再采二维谱，把交叉峰归属到原子连接，多谱一致后才谈结构。
- Negative: `no assigning connections from overlapping one-dimensional peaks, no treating artefacts as cross-peaks, no ignoring relaxation effects on quantification, no extrapolating sensitivity to unsuitable nuclei`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
