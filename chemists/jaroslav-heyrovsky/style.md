# Jaroslav Heyrovský — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #57。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jaroslav Heyrovský, let a mercury drop fall, record the current against voltage, and read concentration and identity from the shape of the polarographic wave`
- ZH: 海洛夫斯基风格：让汞滴落下，记录电流随电压的变化，从极谱波的形状读出浓度与物种。

## (2) 实验设计风格

- 实验类型以电化学测定为主：电流—电压曲线、半波电位、极限扩散电流。变量控制是汞滴周期、支持电解质与去氧逐项固定；仪器偏好自制极谱仪，电极表面更新先于结论。

## (3) 合成与分析风格

- 合成不是他的主线；分析风格是“以波形定量”：半波电位定物种，波高定浓度。数据呈现为极谱图与半波电位表，证据强度以波形的重现性与标准加入法的符合度为准。

## (4) 模型建构风格

- 模型是归纳与演绎结合：从扩散控制电流归纳出极谱方程，再以理论预言检验新体系。抽象程度中等，模型必须对应可测的波形参数。遇例外先检查氧干扰与电极过程，不轻易改方程。

## (5) 论证与表达风格

- 论证结构为“仪器—波形—定量—应用”；论文以方法描述与应用实例为主，结论谨慎，常给出检出限与干扰。术语创造（极谱法）明确。与同行的关系以方法推广为主。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先除氧、固定支持电解质，再记录波形
- 以半波电位定性、以波高定量
- 用标准加入法检验定量结果
- 先标明检出限与干扰
- 不该做：
- 不以未除氧的曲线定量
- 不把重叠波形硬拆成单组分
- 不忽略汞滴周期的影响
- 不把极谱波高直接当浓度，不做校准
- Negative prompt: `no quantifying from curves recorded without deoxygenation, no splitting overlapping waves into single components, no ignoring the mercury drop period, no reporting concentration from wave height without calibration`

## (7) 测试提示词示例（现代题材：测定一种新型工业废水中痕量重金属的浓度）

- Prompt: `In the style of Jaroslav Heyrovský, determine trace heavy metals in a new industrial wastewater: first remove oxygen and fix the supporting electrolyte, then record the polarographic waves, identify each metal from its half-wave potential, and quantify from wave height against standards`
- 中文对照：海洛夫斯基风格，测定一种新型工业废水中痕量重金属浓度：先除氧、固定支持电解质，再记录极谱波，以半波电位定性、以波高对标准定量。
- Negative: `no quantifying from curves recorded without deoxygenation, no splitting overlapping waves into single components, no ignoring the mercury drop period, no reporting concentration from wave height without calibration`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
