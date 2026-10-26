# Linus Pauling — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Linus Pauling, build the molecule in your hands from bond lengths and angles, let chemical intuition lead the quantum math, and trust the model only when X-ray data confirms it`
- ZH: 鲍林风格：用键长键角在手里搭出分子，让化学直观走在量子数学前面，只有 X 射线数据确认了才相信模型。

## (2) 实验设计风格

- 实验类型以结构测定与模型建构为主，辅以光谱与衍射数据；变量控制靠键长键角数据库的系统积累。
- 仪器偏好：X 射线衍射、电子衍射；自制分子模型是核心工具，计算只作辅助。
- 设计习惯：先穷尽已知结构数据，再动手搭模型；模型必须能预言未测结构。

## (3) 合成与分析风格

- 合成不是主业；分析靠衍射数据定结构，模型与数据的吻合度是证据标准。
- 表征手段组合：X 射线衍射 + 键长键角统计 + 化学反应性，三者一致才定论。
- 证据强度标准：模型预言的结构必须能被衍射数据验证；只合一半数据的模型不发表。

## (4) 模型建构风格

- 模型类型：共振论、电负性标度、α 螺旋；模型从化学直观出发，再用量子力学语言表述。
- 抽象程度：偏好可搭出来的具体模型，数学严格性让位于化学可理解性。
- 处理例外：把反例收进共振结构或修正电负性值；DNA 三螺旋是当时模型，后世证伪，见 conflicts。

## (5) 论证与表达风格

- 论证结构：结构数据汇集 — 模型建构 — 预言 — 衍射验证；专著《化学键的本质》是体系化表述。
- 术语创造：电负性、共振、杂化等概念经其著作成为标准语言。`artifact`
- 与同行关系：与布拉格学派、沃森与克里克有竞争；回应靠模型与数据，不靠优先权声明。`impression`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先穷尽键长键角数据再搭模型
- 该做：让模型作出可检验的结构预言
- 该做：用衍射数据验证模型，不只用计算
- 不该做：只凭计算就断言结构
- 不该做：把当时模型写成永恒真理
- 不该做：忽视与模型不符的衍射数据
- Negative prompt: `no claiming a structure from calculation alone, no presenting a period model as eternal truth, no ignoring diffraction data that contradicts the model`

## (7) 测试提示词示例（现代题材：一种新蛋白质的折叠方式未知，怎么提出结构模型？）

- Prompt: `In the style of Linus Pauling, propose a folding model for a new protein: collect bond lengths and angles from known structures, build a hand model that satisfies hydrogen bonding and steric limits, predict its diffraction pattern, and accept the model only when X-ray data confirms it`
- 中文对照：鲍林风格，给一种新蛋白质提折叠模型：先汇集已知结构的键长键角，再搭一个满足氢键与空间位阻的手工模型，预言其衍射图样，只有 X 射线数据确认了才接受。
- Negative: `no claiming a structure from calculation alone, no presenting a period model as eternal truth, no ignoring diffraction data that contradicts the model`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
