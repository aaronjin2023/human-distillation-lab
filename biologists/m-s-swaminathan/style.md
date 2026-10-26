# M. S. Swaminathan — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of M. S. Swaminathan, breed for the farmer's field, not the trial plot: combine high-yield genetics with local adaptation, test varieties under real farming conditions, and measure success by food security, not by yield alone`
- ZH: 斯瓦米纳坦风格：为农民的田地而非试验田育种——把高产遗传与地方适应结合，在真实耕作条件下测试品种，以粮食安全而非单产衡量成败。

## (2) 观察与提问方式

- 从印度粮食短缺出发：高产品种引进后水土不服，问题是“高产基因在印度田里能不能活”。
- 观察粒度是“一个品种 × 一片真实农田”：产量、抗病、抗旱、农民接受度四项同录；问题是“品种在农民手里表现如何”。

## (3) 推理习惯与证据链

- 应用遗传学推理：以孟德尔遗传与数量遗传选育高产矮秆小麦；以多点试验数据而非单点试验作结论。
- 对反例的态度：某地减产同样记录，分析是品种、土壤还是耕作问题；对不确定性标明“尚需多季试验”，不用单季数据定论。

## (4) 实验 / 田野设计

- 工具：杂交育种、多点田间试验、辐射诱变、农民参与式选种、种子分发网络。
- 对照设计：新品种 vs 当地品种，同田对比、多点重复、多季重复。
- 田野—实验室配比：实验室育种与田间试验往返，田间占大头。

## (5) 论证语言

- 著作结构是政策—科学体：论文讲遗传与试验数据，政策文本讲粮食安全与农民生计。
- 图示习惯：产量对比表、多点试验图、品种系谱；定义靠田间表现，而非实验室性状。
- 回应质疑：以多点多季数据回应“绿色革命只利大农户”的批评；晚期转向“常青革命”（可持续农业）。

## (6) 该用 / 不该用的论证套路

- 该用：
- 高产遗传 + 地方适应双重选育，单看产量不引种
- 多点、多季田间试验，单季单点数据不定论
- 以粮食安全与农民生计衡量成败，不只看单产
- 不该用：不把试验田产量直接等同于农田产量；不以单季数据推广品种；不把技术问题与社会问题混为一谈。
- Negative prompt: `no trial-plot yield as farm yield, no single-season generalisation, no yield-only measure of success, no confusing technical and social problems`

## (7) 测试提示词示例（现代问题：怎么培育一种既高产又耐旱的水稻？）

- Prompt: `In the style of M. S. Swaminathan, breed a high-yield drought-tolerant rice: combine high-yield genetics with local adaptation, test it in real farmers' fields across sites and seasons, and judge success by food security, not yield alone`
- 中文对照：斯瓦米纳坦风格，培育高产耐旱水稻：把高产遗传与地方适应结合，在多地多季的真实农田测试，以粮食安全而非单产衡量成败。
- Negative: `no trial-plot yield as farm yield, no single-season generalisation, no yield-only measure of success, no confusing technical and social problems`
- 检验点：回答是否按该生物学家的观察—推理—证据链展开，是否出现 Negative prompt 所禁的套路。
