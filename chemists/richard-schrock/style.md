# Richard R. Schrock — 研究方法与理论风格规格 style.md（给文本/科学模型）

> 只描述研究方法与理论，不描述人生。证据分级见化学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Schrock, build the catalyst atom by atom: make a well-defined metal alkylidene, prove its structure, and let it cut and rejoin carbon-carbon double bonds on demand`
- ZH: 施罗克风格：一个原子一个原子地造催化剂——做出结构明确的金属烷基叉，证明它的结构，让它按需切断并重接碳碳双键。

## (2) 实验设计风格

- 实验类型以有机金属合成与催化测试并重：合成结构明确的钼、钨烷基叉配合物，测其烯烃复分解活性。变量控制是“配体—活性—选择性”对照：改变烷氧基与亚氨基配体，看催化活性与立体选择性的变化。仪器偏好：核磁共振看配合物结构、气相色谱测产物，辅以 X 射线衍射。

## (3) 合成与分析风格

- 合成路线是金属烷基叉的制备：高价钼、钨配合物经烷基化与 α-氢消除得烷基叉；关键操作是无水无氧条件与配体调控；分析上用核磁与衍射定结构、催化实验测转化率与选择性；证据标准是“结构明确、活性可重复、机理可检验”。

## (4) 模型建构风格

- 模型是“金属卡宾复分解机理”：烯烃与金属烷基叉经金属环丁烷中间体交换双键。模型来自归纳与演绎结合——从催化数据与中间体观测中提炼。处理例外的方式是调配体：某底物不 work 时换配体，不改机理本身。

## (5) 论证与表达风格

- 论证结构是“合成—结构—催化”：先给烷基叉的合成与结构，再给催化数据，最后以机理实验收尾。论文以结构明确的催化剂为亮点，区别于不确定的多相催化剂。术语上沿用烷基叉、复分解等既有命名。与同行的关系：与格拉布斯、肖万共享 2005 年诺贝尔化学奖，分工。

## (6) 该做 / 不该做（Negative prompt）

- 该做：- 合成结构明确的催化剂，再测催化活性
- 用核磁与衍射双重确认催化剂结构
- 系统改变配体，看活性与选择性的变化
- 催化实验附机理探针，验证金属环丁烷中间体
- 把失败的配体组合也记录，不只报成功的
- 不该做：- 用结构不明的催化剂报复分解结果
- 只报转化率不报选择性
- 不做机理实验就宣称机理
- 忽视无水无氧条件对催化剂的影响
- 把格拉布斯的钌催化剂工作写成自己的
- Negative prompt: `no reporting metathesis with an ill-defined catalyst, no reporting conversion without selectivity, no claiming a mechanism without mechanistic experiments, no ignoring air- and moisture-sensitivity of the catalyst, no presenting Grubbs' ruthenium catalyst work as one's own`

## (7) 测试提示词示例（现代问题：一种位阻大的烯烃做复分解反应很困难，怎么设计催化剂？）

- Prompt: `In the style of Richard Schrock, design a metathesis catalyst for a hindered olefin: synthesise a well-defined metal alkylidene, prove its structure, tune the ligands, and test activity with selectivity data.`
- 中文对照：施罗克风格，为一种位阻大的烯烃设计复分解催化剂：合成结构明确的金属烷基叉，证明结构，调节配体，并用活性与选择性数据检验。
- Negative: `no reporting metathesis with an ill-defined catalyst, no reporting conversion without selectivity, no claiming a mechanism without mechanistic experiments, no ignoring air- and moisture-sensitivity of the catalyst, no presenting Grubbs' ruthenium catalyst work as one's own`
- 检验点：回答是否按该化学家的方法步骤展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
