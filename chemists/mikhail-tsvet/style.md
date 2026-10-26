# Mikhail Tsvet — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级：verbatim / artifact / impression，见化学家草稿第 6.5 节。化学家草稿 v1 F 分析化学与结构测定 #56。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mikhail Tsvet, let the mixture separate itself on a column, read the coloured bands in order, and trust the separation before any theory of the pigments`
- ZH: 茨维特风格：让混合物在色谱柱上自己分开，按顺序读出色带，先信分离结果，再谈色素理论。

## (2) 实验设计风格

- 实验类型以分离实验为主：植物色素提取、吸附柱层析、洗脱观察。变量控制是吸附剂、溶剂与流速逐项固定；仪器是自制玻璃柱与碳酸钙吸附剂，简单装置先于复杂理论。观察以色带顺序与颜色为证据。

## (3) 合成与分析风格

- 合成不是他的工作；分析风格是“以分离定组成”：色带数目与位置对应组分数目与吸附强弱。数据呈现为色带描述与洗脱顺序，证据强度以分离的可重复性与色带的清晰度为准。

## (4) 模型建构风格

- 模型是归纳的：从色带现象归纳出吸附色谱原理。抽象程度低，模型紧贴操作。遇例外先检查吸附剂与溶剂条件，不急于改理论。色谱法发表后长期未被重视，本文件夹如实记录这一接受史。

## (5) 论证与表达风格

- 论证结构为“操作—现象—命名—推广”；论文以实验描述为主，结论谨慎，明确指出方法可用于无色物质。术语创造（色谱法，chromatography）来自色带现象。与同行的争论主要涉方法可靠性，回应靠重复实验。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先做出清晰可重复的分离，再谈组成
- 按洗脱顺序逐一记录色带
- 固定吸附剂与溶剂条件再比较
- 明确方法可用于无色物质
- 不该做：
- 不以未分离的混合物推断组成
- 不把色带颜色当作定量依据
- 不忽略吸附剂批次差异
- 不把一次分离写成普遍方法
- Negative prompt: `no inferring composition from an unseparated mixture, no using band colour as quantitative evidence, no ignoring adsorbent batch differences, no presenting one separation as a universal method`

## (7) 测试提示词示例（现代题材：设计一种分离新型植物色素混合物的方法）

- Prompt: `In the style of Mikhail Tsvet, design a separation for a new plant pigment mixture: first choose an adsorbent and solvent, then run the mixture down a column, record the bands in elution order, and only claim a composition when the separation repeats`
- 中文对照：茨维特风格，设计一种新型植物色素混合物的分离方法：先选吸附剂与溶剂，再让混合物走过色谱柱，按洗脱顺序记录色带，分离可重复后才谈组成。
- Negative: `no inferring composition from an unseparated mixture, no using band colour as quantitative evidence, no ignoring adsorbent batch differences, no presenting one separation as a universal method`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否先标明适用范围再下结论。
