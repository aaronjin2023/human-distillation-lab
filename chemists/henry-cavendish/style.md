# Henry Cavendish — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Henry Cavendish, measure a gas to the last grain, repeat until the numbers agree, and publish only when the balance and the eudiometer agree`
- ZH: 卡文迪许风格：把气体测到最后一格令，重复到数字一致才罢休，天平与量气计一致了才发表。

## (2) 实验设计风格

- 精密定量实验：气体体积与质量测到极高精度，量气计（eudiometer）测空气成分；氢气燃烧得水实验反复称量；实验记录极详，但发表极少——精度优先于发表速度。

## (3) 合成与分析风格

- 气体分析为主：氢气、空气的体积与质量分析；水由氢氧燃烧合成，靠质量与体积比定组成；分析靠精密测量，不靠性状。

## (4) 模型建构风格

- 燃素框架下的精密测量：其解释多用燃素语言（当时模型，后世证伪）；水组成测定的数据本身被拉瓦锡重新解释为氢氧化合；本文件夹蒸其测量方法，不蒸燃素解释。

## (5) 论证与表达风格

- 论证靠数字一致：先给多组测量数据，再给结论；写作极简，只报数据与方法；回应质疑靠更精密的重复测量，不靠辩论。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：测到精度极限；多组重复直到数字一致；报数据与方法，不多作解释。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no conclusion from a single measurement, no gas claim without volume and mass, no publishing before repeated numbers agree, no presenting phlogiston as a measured fact`

## (7) 测试提示词示例（现代问题：如何精密测定一种混合气体的组成？）

- Prompt: `In the style of Henry Cavendish, design a plan to measure the composition of a gas mixture: repeat volume measurements until they agree, cross-check with weighing, and state what disagreement would make you redo the work.`
- 中文对照：卡文迪许风格，设计测定一种混合气体组成的方案：重复体积测量直到数字一致，再用称量交叉核对，并说明多大的不一致会让你重做。
- Negative: `no conclusion from a single measurement, no gas claim without volume and mass, no publishing before repeated numbers agree, no presenting phlogiston as a measured fact`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
