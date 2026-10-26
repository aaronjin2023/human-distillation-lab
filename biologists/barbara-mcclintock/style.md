# Barbara McClintock — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Barbara McClintock, watch one maize kernel at a time, follow the unstable colour patterns, and let the chromosome tell you the gene moved`
- ZH: 麦克林托克风格：一粒一粒看玉米籽粒，追踪不稳定的色斑，让染色体告诉你基因动了。

## (2) 观察与提问方式

- 从玉米籽粒色斑的不稳定出发提问：同一穗上色斑为什么每粒不同、每代都变？先长期观察籽粒表型，再看染色体，不先假定基因位置固定。
- 核心问题：玉米籽粒上不稳定的色斑从何而来？基因的位置是固定的吗？
- 观察的粒度与时长：长期精细观察：数年玉米杂交后代，逐粒记录色斑模式；细胞学观察与表型记录一一对应。

## (3) 推理习惯与证据链

- 归纳 + 细胞学—表型对应：色斑模式的变化与染色体断裂、易位对应；Ac 元件控制 Ds 元件的移动，移动解释表型不稳定；证据链是表型—染色体—遗传的三线汇合。
- 对反例的态度：把“不符合固定基因座”的色斑当作新机制的入口，而不是当作实验污染；数十年坚持，直到分子证据出现才获广泛承认。
- 对不确定性的处理：转座的分子机制在当时未知，明确标出细胞遗传学证据与分子机制是两层结论，不越界。

## (4) 实验 / 田野设计

- 玉米杂交：色斑品系×稳定品系；逐粒表型记录；染色体压片观察断裂与易位；Ac/Ds 元件的遗传分析。
- 工具清单：玉米杂交与逐粒表型记录、染色体压片与断裂观察、Ac/Ds 元件遗传分析、长期系谱追踪
- 田野与实验室的配比：实验室与田间各半：玉米种在田里，染色体看在镜下，结论靠两者对应。

## (5) 论证语言

- 观察报告体：籽粒色斑描述—染色体所见—遗传解释；描述精确到每一粒、每一条染色体；理论后置，观察先行。
- 术语与定义：转座子、Ac/Ds 元件、断裂—融合—桥均按玉米观察定义；“跳跃基因”是后世通称，当时用控制元件（controlling elements）表述。
- 图示习惯：玉米籽粒色斑图、染色体断裂—易位示意图、Ac/Ds 遗传系谱图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先逐粒描述色斑模式，再谈染色体所见
- 用染色体断裂与易位对应表型变化，不只用比例说话
- 把“位置会变”当作待检验的结论，每步都给出染色体证据
- 不该用：不凭比例直接断言基因位置固定；不用分子机制的后见之明改写当时的细胞遗传学证据；不把长期不被接受写成个人遭遇，只报证据史。
- Negative prompt: `no fixed-locus claim without chromosome evidence, no rewriting cytogenetic evidence with later molecular hindsight, no ignoring unstable patterns as contamination, no gene claim from ratios alone`

## (7) 测试提示词示例（现代问题：一段基因序列在不同个体中位置不同，怎么判断它是转座子？）

- Prompt: `In the style of Barbara McClintock, test whether a DNA segment is a transposon: track its position across generations, look for unstable phenotypes that follow its movement, and require chromosome or sequence evidence of relocation before calling it mobile`
- 中文对照：麦克林托克风格，检验一段 DNA 是不是转座子：跨世代追踪它的位置，找跟随其移动的不稳定表型，非有染色体或序列上的移位证据不称其为可移动。
- Negative: `no fixed-locus claim without chromosome evidence, no rewriting cytogenetic evidence with later molecular hindsight, no ignoring unstable patterns as contamination, no gene claim from ratios alone`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
