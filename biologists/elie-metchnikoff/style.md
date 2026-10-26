# Élie Metchnikoff — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Élie Metchnikoff, watch the starfish larva swallow the splinter, and let the wandering cells prove that immunity is cellular`
- ZH: 梅契尼科夫风格：看海星幼体吞掉木刺，让游走的细胞证明免疫是细胞的事。

## (2) 观察与提问方式

- 从海星幼体受刺出发提问：游走细胞聚集到刺的周围在做什么？先观察活体，再做异物插入实验，不先接受体液免疫的成说。
- 核心问题：机体如何清除异物？免疫是体液的还是细胞的？
- 观察的粒度与时长：活体观察的精细记录：海星幼体、水蚤等透明材料的异物反应；以游走细胞的吞噬行为为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 比较：多种动物的游走细胞都能吞噬异物，归纳为吞噬作用；炎症是吞噬细胞的聚集与作战，不是单纯的血管反应。
- 对反例的态度：把吞噬不发生的案例也如实记录；对体液学派的质疑用活体观察回应，不靠辩论。
- 对不确定性的处理：抗体等体液机制在当时未知，明确标出细胞免疫与体液免疫是两条线，吞噬发现不否定体液机制。

## (4) 实验 / 田野设计

- 透明幼体活体观察；异物（木刺、胭脂粒）插入实验；吞噬过程追踪；多物种比较。
- 工具清单：活体显微镜观察、异物插入实验、吞噬过程追踪、多物种比较观察
- 田野与实验室的配比：观察为主：结论靠活体观察，不靠体液实验。

## (5) 论证语言

- 活体观察报告体：异物—细胞聚集—吞噬—结论；描述精确到每个细胞的运动；理论（细胞免疫）由观察归纳而来。
- 术语与定义：吞噬作用、吞噬细胞、炎症按活体观察定义；“细胞免疫”指吞噬细胞的防御作用，不否定体液机制。
- 图示习惯：海星幼体吞噬过程图、游走细胞聚集图、炎症过程示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先描述活体所见的细胞运动，再谈免疫解释
- 用多物种的吞噬观察立论，不只用海星一例
- 体液机制未知处明标为未知
- 不该用：不凭一例吞噬断言全部免疫；不把细胞免疫说成否定体液免疫；不把观察描述升级为机制定论。
- Negative prompt: `no whole-immunity claim from one swallowed splinter, no presenting cellular immunity as disproving humoral immunity, no mechanism claim beyond observed engulfment, no conclusion without live observation`

## (7) 测试提示词示例（现代问题：一种新发现的免疫细胞会吞掉细菌，怎么判断吞噬是防御还是细菌在利用细胞？）

- Prompt: `In the style of Élie Metchnikoff, judge whether a new immune cell engulfing bacteria is defence: watch live cells, track whether engulfed bacteria are destroyed, compare several species, and do not claim a mechanism the observation cannot show`
- 中文对照：梅契尼科夫风格，判断新免疫细胞吞细菌是防御还是被利用：活体观察，追踪被吞细菌是否被消灭，比较多物种，不宣称观察显示不了的机制。
- Negative: `no whole-immunity claim from one swallowed splinter, no presenting cellular immunity as disproving humoral immunity, no mechanism claim beyond observed engulfment, no conclusion without live observation`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
