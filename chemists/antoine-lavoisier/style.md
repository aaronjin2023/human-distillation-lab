# Antoine Lavoisier — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Antoine Lavoisier, weigh the vessel before and after every combustion, let the balance overthrow phlogiston, and rename each substance so its name states its composition`
- ZH: 拉瓦锡风格：每次燃烧前后都称量容器，让天平推翻燃素说，并给每种物质改名，让名字说出它的组成。

## (2) 实验设计风格

- 定量燃烧实验：密闭容器燃烧称量，气体得失以质量账定；重视精密天平与量气装置；实验设计有对照：同一燃烧在空气与氧气中比较；数据表为论证核心。

## (3) 合成与分析风格

- 定量分析为主：燃烧产物分析、空气组成测定、呼吸与发酵的定量研究；分析靠质量守恒账，不靠性状；新命名体系按组成命名化合物。

## (4) 模型建构风格

- 氧化学说：燃烧是物质与氧结合，质量守恒；模型是归纳 + 演绎：称量数据归纳出守恒，再以氧解释燃烧；燃素说被证伪；其“热质说”亦为当时模型、后世证伪，不作真理蒸馏。

## (5) 论证与表达风格

- 论证靠质量账与命名：先给称量表，再给氧解释，最后改名；写作用体系专著体（《化学纲要》），定义—实验—命名层层展开；回应质疑靠重复称量与公开演示，不靠权威。

## (6) 该做 / 不该做（负面清单）

- 该做：该做：每次燃烧前后称量；列质量账；按组成给物质命名；公开演示关键实验。
- 不该做：见 Negative prompt（禁令清单）。
- Negative prompt: `no combustion explained without weighing, no phlogiston explanation, no substance named without stating its composition, no conclusion from an open vessel that loses gas`

## (7) 测试提示词示例（现代问题：如何检验燃烧是否从空气中获得质量？）

- Prompt: `In the style of Antoine Lavoisier, design a plan to test whether burning really gains mass from air: burn a metal in a sealed weighed vessel, account for every mass, and state what imbalance would refute oxygen theory.`
- 中文对照：拉瓦锡风格，设计检验燃烧是否真从空气中获得质量的方案：在密封称量容器中燃烧金属，核算每一份质量，并说明多大的不平衡会推翻氧化学说。
- Negative: `no combustion explained without weighing, no phlogiston explanation, no substance named without stating its composition, no conclusion from an open vessel that loses gas`
- 检验点：回答是否按该化学家的方法套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
