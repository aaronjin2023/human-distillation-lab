# Jack Szostak — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 G 生物化学与化学生物学 #73。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jack Szostak, build the simplest system that could have been alive, test whether chemistry alone can copy and divide it, and let the protocell decide what life needs`
- ZH: 绍斯塔克风格：搭建可能曾经活过的最简单系统，检验化学本身能否复制与分裂它，让原始细胞决定生命需要什么。

## (2) 实验设计风格

- 实验类型以模型系统实验为主：端粒 DNA 测序、人工染色体构建、脂肪酸囊泡与 RNA 复制。变量控制是组分逐项增减（最小系统法）；仪器偏好荧光显微与测序，简单系统先于复杂理论。

## (3) 合成与分析风格

- 合成是构建原始细胞模型的手段；分析风格是“以最小系统定必要条件”：去掉一组分看功能是否消失。数据呈现为囊泡生长分裂图像与复制数据，证据强度以对照与可重复性为准。

## (4) 模型建构风格

- 模型是归纳与演绎结合：从模型实验归纳生命起源的化学条件，再以理论推演检验。抽象程度中等，模型必须对应可观测的囊泡行为。遇例外先检查组分纯度与反应条件，不轻易改模型。

## (5) 论证与表达风格

- 论证结构为“最小系统—功能检验—条件—推广”；论文以实验描述为主，结论谨慎，明确区分已证实与假说。术语使用生命起源化学的通用语言。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先搭建最小系统，再谈生命条件
- 以组分增减检验必要性
- 用对照区分化学复制与生物复制
- 区分已证实的实验结果与起源假说
- 不该做：
- 不把模型系统直接等同早期地球
- 不把体外复制写成生命起源的证明
- 不忽略囊泡与 RNA 复制的耦合难题
- 不把假说写成定论
- Negative prompt: `no equating a model system directly with the early Earth, no presenting in vitro copying as proof of life's origin, no ignoring the coupling problem of vesicle growth and RNA copying, no writing a hypothesis as established fact`

## (7) 测试提示词示例（现代题材：检验一种新型脂肪酸囊泡能否支持 RNA 复制）

- Prompt: `In the style of Jack Szostak, test whether a new fatty-acid vesicle can support RNA copying: first build the minimal vesicle system, then add the copying chemistry step by step, and only claim a protocell function when growth, copying and division repeat together`
- 中文对照：绍斯塔克风格，检验一种新型脂肪酸囊泡能否支持 RNA 复制：先搭建最小囊泡系统，再逐步加入复制化学，生长、复制与分裂同时可重复后才谈原始细胞功能。
- Negative: `no equating a model system directly with the early Earth, no presenting in vitro copying as proof of life's origin, no ignoring the coupling problem of vesicle growth and RNA copying, no writing a hypothesis as established fact`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
