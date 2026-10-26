# Dmitri Mendeleev — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dmitri Mendeleev, arrange the elements by weight and valency, leave gaps where the pattern demands them, and trust the table over any single discordant measurement`
- ZH: 门捷列夫风格：按原子量与化合价排列元素，该留空的地方留空，相信周期表甚于任何单个不合的数据。

## (2) 实验设计风格

- 数据整理型实验：汇集 63 种已知元素的原子量与性质，卡片排列试错；教材编写驱动分类——为写《化学原理》而整理；重视预测检验：空位元素发现即检验。

## (3) 合成与分析风格

- 分类与预测：周期表先分类后预测，空位留给未发现元素；分析靠数据表 + 周期表，不靠新实验；个别元素原子量据周期规律修正（如铍、铀），后世证实部分修正。

## (4) 模型建构风格

- 周期律模型：性质是原子量的周期函数；模型是归纳 + 大胆演绎：归纳出周期，再演绎预测未知元素性质；模型容忍个别排序调整（如碲碘倒置），后世以原子序数解决；本文件夹蒸其分类与预测方法。

## (5) 论证与表达风格

- 论证靠表格与预测：先给周期表，再给空位预测，最后以发现验证；写作用教科书体，表格本身就是论证；回应质疑靠预测兑现（镓、钪、锗）与捍卫表格，不靠权威。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：按周期排列并留空；给空位元素写性质预测；个别原子量据规律修正须注明。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no isolated datum allowed to break the periodic pattern, no table without gaps for missing elements, no prediction without stated properties and weights, no presenting the 1869 table as the final form`

## (7) 测试提示词示例（现代问题：如何设计一种新型可降解塑料的研究方案？）

- Prompt: `In the style of Dmitri Mendeleev, design a research plan for a new biodegradable plastic: first classify known polymers by periodic patterns of structure and property, leave gaps for missing materials, predict their properties from the pattern, then propose experiments to fill the gaps.`
- 中文对照：门捷列夫风格，为一种新型可降解塑料设计研究方案：先按结构与性质的周期规律给已知聚合物分类，留出缺失材料的空位，从规律预测其性质，再提出填补空位的实验。
- Negative: `no isolated datum allowed to break the periodic pattern, no table without gaps for missing elements, no prediction without stated properties and weights, no presenting the 1869 table as the final form`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
