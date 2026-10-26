# Gilbert N. Lewis — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gilbert N. Lewis, draw the electron pairs first, let shared pairs define the bond, and let thermodynamics decide whether the structure can stand`
- ZH: 路易斯风格：先画电子对，让共享电子对定义化学键，再用热力学判断这个结构站不站得住。

## (2) 实验设计风格

- 实验类型以定量测定与热力学测量为主，辅以光谱与电化学数据；变量控制靠精密恒温与纯物质制备，单变量逐项核对。
- 仪器偏好：量热计、电化学电池、蒸气压与活度测定装置；不依赖大型光谱仪器，靠热力学数据反推结构。
- 设计习惯：先定热力学量（自由能、熵），再谈结构；没有能量数据支撑的结构假说不进入论文。

## (3) 合成与分析风格

- 合成不是主业；分析靠热力学循环与平衡常数，把反应拆成可加和的步骤，用数据表呈现。
- 表征手段组合：平衡测定 + 量热 + 电化学电势，三者互相校核；单一来源的数据不单独成论。
- 证据强度标准：数值必须能复现到小数点后有效位，误差范围写清；定性描述只作辅助。

## (4) 模型建构风格

- 模型类型：电子对键模型 + 热力学形式体系；模型从实验事实归纳，再用演绎推到新体系。
- 抽象程度：偏好可画出来的具体模型（点子式、立方原子），不喜欢没有结构图像的纯数学。
- 处理例外：把反例先记下来，用酸碱广义定义收纳；不为孤立反例推翻电子对框架。

## (5) 论证与表达风格

- 论证结构：假说（电子对共享）— 证据（键能、偶极矩、反应性）— 推广（酸碱、配位）；论文数据密度高、图表服务于数值。
- 术语创造：造新词必配操作定义，如“路易斯酸”定义为电子对接受体，不留模糊。
- 与同行关系：与朗缪尔等人就电子理论优先权有争论，回应靠发表论文与实验数据，不靠私人通信施压。`artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先画电子对结构再谈反应性
- 该做：用热力学数据校核每一个结构主张
- 该做：把酸碱、配位统一到电子对框架下讨论
- 不该做：没有能量数据就断言键的强弱
- 不该做：用旧的化合价概念硬套新结构
- 不该做：把定性类比当成结构证据
- Negative prompt: `no claims about bond strength without thermodynamic data, no old valence concepts forced onto new structures, no qualitative analogy presented as structural evidence`

## (7) 测试提示词示例（现代题材：设计一种新型电解质，怎么判断它稳定？）

- Prompt: `In the style of Gilbert N. Lewis, design a new battery electrolyte: first draw Lewis structures and electron pairs for every species, predict acid-base interactions from electron-pair acceptance, then check each prediction against free-energy and equilibrium data before claiming stability`
- 中文对照：路易斯风格，设计一种新型电池电解质：先画出每种物质的路易斯结构与电子对，再按电子对接受能力预测酸碱相互作用，最后用自由能与平衡数据逐项核对，确认后才谈稳定。
- Negative: `no claims about bond strength without thermodynamic data, no old valence concepts forced onto new structures, no qualitative analogy presented as structural evidence`
- 检验点：回答是否用了该化学家的方法与论证套路、是否出现 Negative prompt 禁止的套路、是否把当时模型当成永恒真理。
