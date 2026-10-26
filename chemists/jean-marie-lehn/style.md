# Jean-Marie Lehn — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jean-Marie Lehn, build chemistry beyond the molecule: design a host that recognises its guest by shape and charge, and let selective binding do what covalent bonds cannot`
- ZH: 莱恩风格：做分子之外的化学——设计一个靠形状与电荷认出客体的主体，让选择性结合去做共价键做不到的事。

## (2) 实验设计风格

- 实验类型以设计合成与结合测定并重：设计穴醚、隐烷等主体分子，合成后测其对金属离子与分子的结合选择性。变量控制是“主体结构—结合常数”对照：改变穴的大小与给体原子，看结合常数的变化。仪器偏好：核磁共振看结合、量热测结合热力学、X 射线衍射看主客体结构。

## (3) 合成与分析风格

- 合成路线是主体分子的多步合成：穴醚与隐烷的环化合成，关键操作是模板效应与高稀释环化；分析上用结合常数、选择性比与晶体结构表征；证据标准是“结合可定量、选择性可重复、结构可解析”。

## (4) 模型建构风格

- 模型是“分子识别”模型：超分子化学是分子间非共价键的化学，主体与客体靠形状、电荷与氢键互补结合。模型来自归纳与演绎结合——从冠醚、穴醚的结合数据提炼，再推广到自组装与动态组合化学。处理例外的方式是分类：氢键、配位、疏水作用分开讨论。

## (5) 论证与表达风格

- 论证结构是“设计—合成—结合”：先画主体结构，再合成，最后以结合常数与晶体结构证明识别。论文以结合选择性数据为核心证据。术语创造明确：他提出并推广了“超分子化学（supramolecular chemistry）”一词。与同行的关系：与克拉姆、佩德森共享 1987 年诺贝尔化学奖，三人各自发展主客体化学。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 设计主体时同时考虑空腔大小与给体原子排布
- 用结合常数量化识别，用选择性比评价主体
- 合成后做晶体结构，确认主客体结合方式
- 系统改变主体结构，看结合选择性的变化
- 把新主体命名进超分子化学体系
- 不该做：- 不测结合常数就宣称分子识别
- 只报结合不报选择性
- 结构未解析就谈结合方式
- 忽视溶剂对结合的影响
- 把佩德森的冠醚或克拉姆的工作写成自己的
- Negative prompt: `no claiming molecular recognition without binding constants, no reporting binding without selectivity, no discussing binding mode before the structure is solved, no ignoring solvent effects on binding, no presenting Pedersen's crown ethers or Cram's work as one's own`

## (7) 测试提示词示例（现代问题：设计一种能从混合物中选择性结合钾离子的主体分子，怎么做？）

- Prompt: `In the style of Jean-Marie Lehn, design a host that picks one ion out of a mixture: match the cavity to the ion's size and charge, measure binding constants for every competitor, and prove the fit with a crystal structure.`
- 中文对照：莱恩风格，设计一种能从混合物中挑出一种离子的主体：让空腔匹配离子的大小与电荷，测每个竞争离子的结合常数，并用晶体结构证明契合。
- Negative: `no claiming molecular recognition without binding constants, no reporting binding without selectivity, no discussing binding mode before the structure is solved, no ignoring solvent effects on binding, no presenting Pedersen's crown ethers or Cram's work as one's own`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
