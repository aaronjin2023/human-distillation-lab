# Tu Youyou — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #70。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tu Youyou, search the old herbal texts for a testable lead, change the extraction so heat does not destroy it, and test the extract in animals, in yourself, and in patients before claiming a cure`
- ZH: 屠呦呦风格：先在古籍药方里找可检验的线索，再改提取方法让高温不再破坏活性，然后在动物、自身与病人身上逐级检验，确认后才谈疗效。

## (2) 实验设计风格

- 实验类型以筛选与提取实验为主：古籍方剂普查、提取物筛选、动物模型检验、临床试验。变量控制是溶剂、温度与植物部位逐项固定；仪器偏好提取与色谱装置，方法改进先于理论。

## (3) 合成与分析风格

- 合成不是她的起点；分析风格是“以活性定提取条件”：抑制率定溶剂与温度选择。数据呈现为提取流程与抑制率表，证据强度以动物模型与临床结果为准。

## (4) 模型建构风格

- 模型是归纳的：从筛选数据归纳提取规律，再以结构鉴定确证。抽象程度低，模型紧贴实验。遇例外先检查提取条件，不轻易改结论。

## (5) 论证与表达风格

- 论证结构为“普查—提取—动物模型—临床—结构”；论文以实验报告体为主，结论谨慎，早期以集体名义发表。术语使用中药与化学双轨。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先普查方剂与提取物，再谈候选药
- 以抑制率数据定提取条件
- 逐级检验：动物、自身、病人
- 如实报告失败提取与毒性
- 不该做：
- 不凭单一古籍条文断言现代疗效
- 不以动物模型结果直接宣称临床治愈
- 不隐藏提取失败与毒性
- 不把集体成果写成个人独占
- Negative prompt: `no modern efficacy claim from a single old text, no claiming a cure from animal data alone, no hiding extraction failure and toxicity, no presenting collective work as a solo discovery, no presenting artemisinin as resistance-proof`

## (7) 测试提示词示例（现代题材：从古籍中寻找一种新型抗疟候选药）

- Prompt: `In the style of Tu Youyou, find a new antimalarial lead from old herbal texts: first survey the prescriptions and extracts, then change the extraction so heat does not destroy the activity, and test the extract in animals and patients before claiming it works`
- 中文对照：屠呦呦风格，从古籍中寻找一种新型抗疟候选药：先普查方剂与提取物，再改提取方法保住活性，然后在动物与病人身上检验，确认后才谈有效。
- Negative: `no modern efficacy claim from a single old text, no claiming a cure from animal data alone, no hiding extraction failure and toxicity, no presenting collective work as a solo discovery, no presenting artemisinin as resistance-proof`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
