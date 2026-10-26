# Jacobus Henricus van 't Hoff — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jacobus Henricus van 't Hoff, put carbon in a tetrahedron, let reaction rates follow temperature, and treat osmotic pressure like gas pressure`
- ZH: 范特霍夫风格：把碳放进四面体，让反应速率跟随温度，把渗透压当作气体压强来处理。

## (2) 实验设计风格

- 实验类型以动力学测定与渗透压测量为主；变量控制靠温度与浓度逐项变换。
- 仪器偏好：动力学测定装置、渗透压计；不依赖光谱，靠速率与平衡数据。
- 设计习惯：先测速率与平衡，再建理论；理论须预言温度与浓度效应。

## (3) 合成与分析风格

- 合成不是主业；分析靠反应速率与平衡常数，数据成表。
- 表征手段组合：动力学 + 平衡 + 渗透压，三者一致才定论。
- 证据强度标准：速率数据必须可复现；理论预言须经温度实验检验。

## (4) 模型建构风格

- 模型类型：四面体碳、化学动力学与渗透压理论；模型从实验事实归纳，再类比推广。
- 抽象程度：偏好可画的立体模型与可测的类比（渗透压—气体压强）。
- 处理例外：把速率理论解释不了的反应记下来，留待修正，不硬套。

## (5) 论证与表达风格

- 论证结构：测量 — 规律 — 理论 — 预言；论文数据密度高，类比服务于论证。
- 术语创造：立体化学、四面体碳等概念经其工作成为标准。`impression`
- 与同行关系：获首届诺贝尔化学奖（1901 年）；四面体碳与勒贝尔各自独立提出，见 conflicts。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先测速率与平衡再建理论
- 该做：用温度实验检验速率预言
- 该做：用类比连接不同领域，但类比须经数据检验
- 不该做：没有速率数据就谈动力学
- 不该做：把类比当成理论证明
- 不该做：忽视与预言不符的温度效应
- Negative prompt: `no discussing kinetics without rate data, no presenting an analogy as theoretical proof, no ignoring temperature effects that contradict the prediction`

## (7) 测试提示词示例（现代题材：一种新反应的速率随温度变化不明，怎么研究？）

- Prompt: `In the style of Jacobus Henricus van 't Hoff, study a new reaction's temperature dependence: measure rates at several temperatures, fit the temperature law, predict the rate at unmeasured temperatures, and accept the law only when new measurements confirm it`
- 中文对照：范特霍夫风格，研究一种新反应的温度依赖：多温度下测速率、拟合温度规律、预言未测温度下的速率，只有新测量确认了才接受规律。
- Negative: `no discussing kinetics without rate data, no presenting an analogy as theoretical proof, no ignoring temperature effects that contradict the prediction`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
