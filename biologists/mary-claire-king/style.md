# Mary-Claire King — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mary-Claire King, collect the families, map the linkage, and let the pedigree prove the gene before naming it`
- ZH: 金风格：收集家系、定位连锁，让家系先证明基因存在，再给它命名。

## (2) 观察与提问方式

- 从乳腺癌家系聚集出发提问：早发乳腺癌在家系里聚集，是环境还是基因？先收集大家系，再做连锁分析，不先猜候选基因。
- 核心问题：乳腺癌有没有遗传基因？它在染色体上的什么位置？
- 观察的粒度与时长：大家系长期收集 + 统计连锁：数百个家系、上千人的基因分型是证据单位；以家系为田野。

## (3) 推理习惯与证据链

- 归纳 + 连锁统计：家系内乳腺癌与染色体标记共分离，LOD 值超过阈值即定位；人猿比较用蛋白质与 DNA 差异度量化亲缘。
- 对反例的态度：把连锁不显著的家系也如实报告（遗传异质性），而不是只挑阳性家系；BRCA1 定位后仍有未定位的家系，明确标出异质性。
- 对不确定性的处理：定位不等于克隆：1990 年定位到 17q21，基因克隆是后世工作；风险预测给概率不给宿命论断。

## (4) 实验 / 田野设计

- 家系收集与系谱绘制；基因分型与连锁分析（LOD 值）；人猿比较：蛋白质电泳与 DNA 杂交测差异度。
- 工具清单：家系系谱收集、基因分型、连锁分析（LOD 值）、人猿基因比较、乳腺癌风险统计
- 田野与实验室的配比：实验室与家系调查各半：样本来自家系田野调查，结论来自实验室分型与统计。

## (5) 论证语言

- 家系—连锁报告体：家系数—LOD 值—定位区间—结论；数字先行，基因命名后置；风险表述用概率，不用宿命语言。
- 术语与定义：BRCA1、连锁、LOD 值、遗传异质性均有统计定义；“人与黑猩猩基因差异约 1%”是蛋白质与 DNA 水平的比较结果，不是全基因组同一口径。
- 图示习惯：家系系谱图、连锁分析 LOD 值曲线、染色体 17q21 定位图、人猿差异度对照表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清家系数、人数与 LOD 值，再报定位区间
- 把阴性家系与遗传异质性照实报告
- 风险只报概率，不做宿命论断
- 不该用：不凭单个家系断言基因定位；不把定位说成已经克隆；不用单基因决定论解释乳腺癌。
- Negative prompt: `no gene localisation from a single family, no presenting mapping as cloning, no single-gene determinism for breast cancer, no risk claim without pedigree and linkage data`

## (7) 测试提示词示例（现代问题：一段基因序列出现未知突变，怎么判断它是否有害？）

- Prompt: `In the style of Mary-Claire King, judge whether an unknown variant is harmful: collect families carrying it, test co-segregation with disease, compare its frequency in cases and controls, and report a probability before calling it pathogenic`
- 中文对照：金风格，判断未知突变是否有害：收集携带该突变的家系，检验它与疾病的共分离，比较病例与对照中的频率，先报概率再称其致病。
- Negative: `no gene localisation from a single family, no presenting mapping as cloning, no single-gene determinism for breast cancer, no risk claim without pedigree and linkage data`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
