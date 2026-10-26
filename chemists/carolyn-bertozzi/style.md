# Carolyn Bertozzi — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Carolyn Bertozzi, design a reaction that ignores everything in a living cell except its one chosen target, and prove it works inside the organism, not just in a flask`
- ZH: 贝尔托齐风格：设计一个在活细胞里只认一个目标、对其余一切都视而不见的反应，并在活体中证明它有效，而不只在烧瓶里有效。

## (2) 实验设计风格

- 实验类型以反应设计与活体验证为主：先在体外筛选生物正交反应对（叠氮—炔环加成、斯陶丁格连接），再在细胞、斑马鱼、小鼠中逐级验证。变量控制是“正交性优先”：反应必须对水、氧、硫醇、胺等生物官能团全部惰性，只对预设的化学手柄起作用。仪器偏好：质谱与荧光成像追踪标记，核磁共振确认结构，活体成像验证定位。

## (3) 合成与分析风格

- 合成路线以模块化为核心：先合成带叠氮或炔基的代谢前体（如叠氮糖），让细胞自身的代谢机器把它装进聚糖，再用环辛炔探针做无铜环加成。关键反应是张力促进的叠氮—炔环加成（SPAAC），不用铜催化，避免铜的细胞毒性。分析上用荧光标记强度定量标记效率，用质谱确认聚糖结构；证据标准是“活体中可检出、可定量、可对照”。

## (4) 模型建构风格

- 模型是“正交性”模型：把化学反应按其与生物体系的相容性分类，生物正交反应是其中与生命过程互不干扰的一类。模型来自归纳——从斯陶丁格连接、SPAAC 等具体反应中提炼出正交性的判据（快速、选择性、无毒、水相兼容）。处理例外的方式是换反应对而不是放宽标准：若一个反应在活体中太慢或有副反应，就设计新的张力炔或四嗪连接，而不是接受“差不多正交”。

## (5) 论证与表达风格

- 论证结构是“体外—细胞—活体”三级递进：先给速率常数与选择性数据，再给细胞标记图像，最后给活体成像。论文数据密度高，图示以反应机理图与荧光成像并列。术语创造明确：她提出并推广了“生物正交化学（bioorthogonal chemistry）”一词。与同行的关系以合作为主，方法开源共享，优先权争议少；与夏普莱斯的点击化学是互补而非对立——铜催化点击用于体外，无铜点击用于活体。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 先定义化学手柄（叠氮、炔、四嗪），再设计与之配对的反应
- 在水相、37°C、有硫醇与胺存在的条件下测试反应
- 用速率常数量化反应快慢，用对照实验（无手柄组）证明选择性
- 先细胞标记，再活体成像，逐级验证
- 把新反应命名为可推广的通用方法，而不只写成一个个案
- 不该做：- 在活体体系中使用有细胞毒性的铜催化
- 只报体外产率就宣称活体可用
- 用需要苛刻条件（高温、强酸、有机溶剂）的反应标记活细胞
- 把荧光信号当作结构证据而不做质谱确认
- 为凑反应速度牺牲选择性
- Negative prompt: `no copper catalysis in living systems, no claiming in vivo utility from test-tube yield alone, no harsh conditions for live-cell labelling, no fluorescence signal without mass-spectrometry confirmation, no sacrificing selectivity for speed`

## (7) 测试提示词示例（现代问题：为活体小鼠中一种新的细胞表面聚糖设计标记方案，怎么保证反应只认目标、不干扰生命过程？）

- Prompt: `In the style of Carolyn Bertozzi, design a bioorthogonal labelling plan for a new cell-surface glycan in live mice: choose a metabolic precursor the cells will install, pair it with a fast copper-free reaction, and prove labelling with imaging plus mass spectrometry controls.`
- 中文对照：贝尔托齐风格，为活体小鼠中一种新的细胞表面聚糖设计生物正交标记方案：选一种细胞代谢能装入的前体，配一个快速无铜反应，并用成像加质谱对照证明标记成功。
- Negative: `no copper catalysis in living systems, no claiming in vivo utility from test-tube yield alone, no harsh conditions for live-cell labelling, no fluorescence signal without mass-spectrometry confirmation, no sacrificing selectivity for speed`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
