# Gao Xiaoxia — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gao Xiaoxia, measure what others cannot see: push polarography down to trace levels, and let a clean polarographic wave decide whether the rare earth is really there`
- ZH: 高小霞风格：测别人测不出来的东西——把极谱分析推到痕量水平，让一条干净的极谱波决定稀土元素到底在不在。

## (2) 实验设计风格

- 实验类型以方法开发与应用并重：发展极谱微量分析技术，解决稀土元素分离生产中的分析难题。变量控制是“电解质—电极—波形”对照：改变支持电解质与电极条件，看极谱波的灵敏度与选择性。仪器偏好：极谱仪、微量分析装置，辅以光谱对照。

## (3) 合成与分析风格

- 合成层面不适用；其“合成”是分析方法的构建：极谱法测定痕量稀土元素，半波电位定性、扩散电流定量。关键操作是消除干扰、提高灵敏度；分析上用极谱波形、标准加入法与回收率验证；证据标准是“检出限可量化、回收率达标、与独立方法一致”。

## (4) 模型建构风格

- 模型是“极谱定量”模型：扩散电流与被测物浓度成正比，半波电位是定性指纹。模型来自演绎——从极谱理论出发，再经痕量体系验证。处理例外的方式是消除干扰：共存离子干扰时改进支持电解质与分离步骤，不改极谱定量原理。

## (5) 论证与表达风格

- 论证结构是“方法—验证—应用”：先建立极谱微量分析方法，再以标准样品与回收率验证，最后用于稀土生产分析。论文数据以检出限与回收率为主。术语上沿用极谱、半波电位等既有命名。与同行的关系：与徐光宪的稀土分离工作配合，分析服务于分离生产；1980 年当选中科院学部委员。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先做标准样品验证，再测实际样品
- 用标准加入法与回收率检验准确度
- 系统改变支持电解质，看干扰消除效果
- 把检出限与精密度写清，不只报检出结果
- 分析方法与独立方法对照验证
- 不该做：- 不做标准验证就报痕量结果
- 只报检出不报检出限
- 忽视共存离子干扰
- 用单一极谱波下定性结论而不看半波电位
- 把稀土分离工艺的成果写成分析工作的
- Negative prompt: `no reporting trace results without standard validation, no reporting detection without a detection limit, no ignoring interference from coexisting ions, no identifying an element from a single polarographic wave without its half-wave potential, no presenting rare-earth separation results as analytical work`

## (7) 测试提示词示例（现代问题：复杂混合物里痕量稀土怎么测准？）

- Prompt: `In the style of Gao Xiaoxia, measure a trace rare earth in a complex mixture: build a polarographic method, remove the interferences one by one, and prove accuracy with standard additions and recovery.`
- 中文对照：高小霞风格，测定复杂混合物中的痕量稀土：建立极谱方法，逐一消除干扰，并用标准加入与回收率证明准确度。
- Negative: `no reporting trace results without standard validation, no reporting detection without a detection limit, no ignoring interference from coexisting ions, no identifying an element from a single polarographic wave without its half-wave potential, no presenting rare-earth separation results as analytical work`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
