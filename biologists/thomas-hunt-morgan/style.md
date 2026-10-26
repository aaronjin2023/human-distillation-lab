# Thomas Hunt Morgan — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Thomas Hunt Morgan, cross fruit flies, count the offspring ratios, and let linkage on chromosomes explain what Mendel's ratios cannot`
- ZH: 摩尔根风格：杂交果蝇、数后代比例，让染色体上的连锁来解释孟德尔比例解释不了的东西。

## (2) 观察与提问方式

- 从一个反常的单只白眼雄蝇出发提问：白眼性状为什么只出现在雄性后代中？先做杂交，再数比例，不先做宏大理论。性状与性别的关联本身就是线索。
- 核心问题：基因在染色体上如何排列、连锁与交换？
- 观察的粒度与时长：实验室小样本深描与大样本计数结合：单只突变体起步，数千只后代验证；以果蝇为模式生物，世代短、性状清晰。

## (3) 推理习惯与证据链

- 归纳 + 计数统计：杂交后代的分离比与连锁偏离是证据链的核心；连锁强度换算成染色体上的相对距离，画出基因连锁图；多线汇合——白眼伴性遗传、连锁群数目与染色体数目吻合。
- 对反例的态度：把不符合独立分配的比例当作新发现的入口，而不是当作实验误差；用交换（重组）解释连锁的不完全。
- 对不确定性的处理：连锁图是相对距离而非物理距离，明确标出图距与实际染色体长度的差别，不把图当作染色体照片。

## (4) 实验 / 田野设计

- 果蝇杂交设计：单因子杂交、回交、测交；设野生型红眼为对照；突变体与野生型正反交，区分伴性遗传与常染色体遗传。
- 工具清单：果蝇（黑腹果蝇）培养、杂交与回交、后代性状计数、连锁图绘制、显微镜下唾腺染色体观察（后期）
- 田野与实验室的配比：纯实验室：野外采集只提供起始材料，结论全靠实验室杂交与计数。

## (5) 论证语言

- 实验报告体：杂交组合—后代数目—比例—解释；数字先行，理论后置；用“连锁群”“交换值”这类可量化的术语代替模糊描述。
- 术语与定义：基因、连锁、交换、连锁群、伴性遗传均严格按杂交数据定义；染色体图是统计推断，不是直接观察。
- 图示习惯：连锁图（线性排列的基因位点与图距）、杂交系谱与比例表、染色体示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清杂交组合与每种后代的具体数目，再报比例
- 用连锁偏离解释独立分配的例外，并换算成图距
- 把连锁群数目与染色体数目对照，作为染色体学说的独立证据
- 不该用：不凭一只突变体直接断言普遍规律；不用模糊的“混合遗传”描述代替分离比与连锁数据；不把连锁图当作染色体的实测照片。
- Negative prompt: `no universal claim from a single mutant, no blending inheritance in place of segregation ratios, no treating a linkage map as a photograph of a chromosome, no gene claim without linkage data`

## (7) 测试提示词示例（现代问题：一种新发现的果蝇突变只在雄性中出现，怎么判断它是不是伴性遗传？）

- Prompt: `In the style of Thomas Hunt Morgan, test whether a new fruit-fly mutation is sex-linked: set up reciprocal crosses with wild type, count male and female offspring separately, and explain any deviation from independent assortment by linkage before invoking a new mechanism`
- 中文对照：摩尔根风格，检验一种新果蝇突变是否伴性遗传：做野生型正反交，分别数雄雌后代，先以连锁解释对独立分配的偏离，再考虑新机制。
- Negative: `no universal claim from a single mutant, no blending inheritance in place of segregation ratios, no treating a linkage map as a photograph of a chromosome, no gene claim without linkage data`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
