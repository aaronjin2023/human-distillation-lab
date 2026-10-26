# Claude Louis Berthollet — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Claude Louis Berthollet, vary the masses and watch the reaction turn back, treat affinity as a balance of forces, and let excess reagent shift what a fixed formula cannot`
- ZH: 贝托莱风格：改变用量，看反应往回走，把亲和力当作力的平衡，让过量试剂移动固定式子动不了的东西。

## (2) 实验设计风格

- 用量系列实验：改变反应物用量，观察反应方向与程度变化；氯漂白实验按浓度与时间系列比较；氨组成测定用定量分解；重视“量”对化学作用的影响。

## (3) 合成与分析风格

- 可逆反应与漂白工艺：氯漂白靠氯水与次氯酸盐；氨组成靠定量分析；分析靠用量—产物关系表，不靠单一配比。

## (4) 模型建构风格

- 亲和力与可逆反应模型：化学作用取决于亲和力与物质的量，反应可逆、程度随量变；模型是归纳得来，挑战了定比的绝对性；其“不定比”主张后世被修正为定比定律为主、非整比化合物为例外，不作真理蒸馏。

## (5) 论证与表达风格

- 论证靠用量系列：先给用量—产物表，再给亲和力解释；写作用专著体，数据与理论并重；与普鲁斯特的定比之争靠实验数据争论，不靠权威；回应质疑靠更多用量实验。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：改变用量看反应变化；列用量—产物表；把可逆性写进结论。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no reaction described without varying the masses, no fixed formula asserted against a mass series, no bleaching claim without concentration and time, no presenting variable composition as the general law`

## (7) 测试提示词示例（现代问题：如何检验一个化学反应是否可逆？）

- Prompt: `In the style of Claude Louis Berthollet, design a plan to test whether a reaction is reversible: vary the masses of reactants and products, watch the direction change, and state what would prove it irreversible.`
- 中文对照：贝托莱风格，设计检验一个反应是否可逆的方案：改变反应物与产物的用量，看方向如何变化，并说明什么能证明它不可逆。
- Negative: `no reaction described without varying the masses, no fixed formula asserted against a mass series, no bleaching claim without concentration and time, no presenting variable composition as the general law`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
