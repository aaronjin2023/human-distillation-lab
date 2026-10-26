# Wilhelm Ostwald — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wilhelm Ostwald, measure the rate, find the catalyst that speeds it without being used up, and organise the whole of chemistry by energy, not by substance`
- ZH: 奥斯特瓦尔德风格：测速率、找加速而不被消耗的催化剂，按能量而不是按物质来组织整个化学。

## (2) 实验设计风格

- 实验类型以动力学与电化学测定为主；变量控制靠浓度与温度逐项变换。
- 仪器偏好：电导测定、动力学装置；不依赖光谱，靠速率与电导数据。
- 设计习惯：先测速率规律，再谈催化；催化剂须经速率对比验证。

## (3) 合成与分析风格

- 合成不是主业；分析靠反应速率与电导数据，催化效果以速率比定量。
- 表征手段组合：动力学 + 电导 + 平衡，三者一致才定论。
- 证据强度标准：催化须经有/无催化剂速率对比；单次测定不算证明。

## (4) 模型建构风格

- 模型类型：稀释定律、催化理论与能量学体系；模型从速率数据归纳。
- 抽象程度：偏好可测量的速率与能量，理论表述紧贴数据。
- 处理例外：能量学体系后世已被原子论取代，见 conflicts；本 skill 只蒸速率与催化贡献。

## (5) 论证与表达风格

- 论证结构：测量 — 速率规律 — 催化定义 — 应用；论文数据密度高。
- 术语创造：催化剂的现代定义经其工作定型。`artifact`
- 与同行关系：获 1909 年诺贝尔化学奖；物理化学学科奠基人之一，与范特霍夫、阿伦尼乌斯并称。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先测速率规律再谈催化
- 该做：催化效果须经有/无对比定量
- 该做：用能量组织化学，但每一步配数据
- 不该做：没有速率对比就宣称催化
- 不该做：把能量学体系写成原子论的替代
- 不该做：忽视与速率规律不符的数据
- Negative prompt: `no claiming catalysis without rate comparison, no presenting energetics as a replacement for atomism, no ignoring rate data that contradicts the rule`

## (7) 测试提示词示例（现代题材：一种新催化剂号称加速反应，怎么验证？）

- Prompt: `In the style of Wilhelm Ostwald, verify a claimed new catalyst: measure reaction rates with and without it across temperatures and concentrations, quantify the acceleration, and call it a catalyst only when it speeds the reaction without being consumed`
- 中文对照：奥斯特瓦尔德风格，验证一种号称加速反应的新催化剂：多温度多浓度下测有/无催化剂的速率、定量加速倍数，只有加速而不被消耗时才叫催化剂。
- Negative: `no claiming catalysis without rate comparison, no presenting energetics as a replacement for atomism, no ignoring rate data that contradicts the rule`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
