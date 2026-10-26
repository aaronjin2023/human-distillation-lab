# Frederick Soddy — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick Soddy, separate what chemistry cannot separate, measure the decay, and let identical chemistry with different mass force a new word: isotope`
- ZH: 索迪风格：把化学分不开的东西分开、测出衰变，让“化学性质相同、质量不同”逼出一个新词：同位素。

## (2) 实验设计风格

- 实验类型以放射性测量与化学分离为主；变量控制靠反复分离纯化与衰变曲线对照，单变量逐项核对。
- 仪器偏好：验电器/静电计测放射性、化学分离装置；不依赖光谱，靠衰变速率与化学行为双重证据。
- 设计习惯：同一份样品分多份平行分离，化学性质相同而衰变不同即为新证据。

## (3) 合成与分析风格

- 合成不是主业；分离是核心：用沉淀、萃取、结晶反复分离放射性元素，纯度以衰变曲线是否单一为准。
- 表征手段组合：衰变曲线 + 化学行为 + 原子量测定，三者一致才定论。
- 证据强度标准：衰变常数必须可复现；化学上不可分而物理上可区分，是同位素判据。

## (4) 模型建构风格

- 模型类型：衰变位移定律与同位素分类体系；模型从分离实验归纳，再用周期表位置演绎。
- 抽象程度：偏好具体实验事实，理论表述紧贴衰变数据；不先建宏大框架。
- 处理例外：把化学上不可分的元素先记为同一位置，再以原子量差异另立同位素，不为周期表整齐牺牲数据。

## (5) 论证与表达风格

- 论证结构：分离实验 — 衰变测量 — 分类命名；论文数据密度高，衰变曲线即论证。
- 术语创造：“同位素”（isotope）一词即其命名，定义为周期表中同一位置、原子量不同的原子。`artifact`
- 与同行关系：与卢瑟福合作衰变理论，与法扬斯各自独立提出位移定律，回应靠发表时序与实验记录。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：用衰变曲线与化学行为双重证据定论
- 该做：把化学不可分而质量不同的情况记为同位素
- 该做：先分离纯化再测衰变，顺序不颠倒
- 不该做：只凭化学性质相同就断言同一元素
- 不该做：用单一衰变测量代替平行分离
- 不该做：为周期表整齐牺牲原子量数据
- Negative prompt: `no claiming the same element from chemical identity alone, no single decay measurement without parallel separation, no sacrificing atomic-weight data to tidy the periodic table`

## (7) 测试提示词示例（现代题材：一批新发现的放射性核素，怎么判断它们是不是同位素？）

- Prompt: `In the style of Frederick Soddy, judge new radioactive nuclides: separate them chemically again and again, measure each decay curve, and call them isotopes only when chemistry cannot separate them but mass and decay differ`
- 中文对照：索迪风格，判断一批新放射性核素是不是同位素：反复化学分离、逐份测衰变曲线，只有化学分不开、质量与衰变又不同时，才叫同位素。
- Negative: `no claiming the same element from chemical identity alone, no single decay measurement without parallel separation, no sacrificing atomic-weight data to tidy the periodic table`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
