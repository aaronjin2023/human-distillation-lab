# Hitoshi Kihara — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hitoshi Kihara, cross wheats, read the chromosome sets, and let the genome analysis tell which wild grasses made bread wheat`
- ZH: 木原均风格：杂交小麦、读染色体组，让基因组分析说清哪些野生禾草造就了面包小麦。

## (2) 观察与提问方式

- 从小麦倍性之谜出发提问：二倍体、四倍体、六倍体小麦的染色体组是什么关系？先做种间杂交，再看染色体配对，不先猜起源故事。
- 核心问题：栽培小麦的染色体组从何而来？不同倍性的小麦如何亲缘？
- 观察的粒度与时长：实验室杂交与细胞学观察结合：杂交后代的染色体配对是证据，田野采集的野生小麦是材料。

## (3) 推理习惯与证据链

- 归纳 + 比较细胞学：杂交后代减数分裂时染色体能否配对，决定两个种是否共享染色体组；配对模式拼出 A、B、D 三套染色体组。
- 对反例的态度：把配对不规则的杂交后代当作关键证据（说明染色体组不同源），而不是当作失败杂交丢掉。
- 对不确定性的处理：D 染色体组的供体等细节在当时有未定之处，明确标出哪些是已确证的配对关系、哪些是推测。

## (4) 实验 / 田野设计

- 小麦种间杂交：二倍体×四倍体、四倍体×二倍体（拟斯卑尔脱山羊草）；杂种减数分裂染色体配对观察；染色体组分析。
- 工具清单：小麦种间杂交、减数分裂染色体配对观察、染色体组分析法、野生小麦采集与鉴定
- 田野与实验室的配比：实验室杂交为主，田野采集为辅：野生材料来自田野，结论来自实验室配对观察。

## (5) 论证语言

- 细胞遗传学报告体：杂交组合—染色体配对数—染色体组推断；配对数据先行，起源叙事后置。
- 术语与定义：染色体组（genome）按配对关系定义；A、B、D 组是分析单位，不是形态描述。
- 图示习惯：染色体配对模式图、小麦倍性—染色体组对照表、杂交系谱图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清杂交组合与每对染色体的配对情况，再推断染色体组
- 用配对模式而非形态相似判断亲缘
- 未确证的供体关系明标为推测
- 不该用：不凭形态相似断言小麦起源；不把染色体组分析法说成自己首创了 genome 一词；不把推测的供体写成定论。
- Negative prompt: `no origin claim from morphology alone, no presenting a hypothesised donor as established fact, no genome claim without pairing data, no claiming the coinage of the word genome`

## (7) 测试提示词示例（现代问题：一种新发现的野生禾草与栽培小麦能否杂交、亲缘多近，怎么判断？）

- Prompt: `In the style of Hitoshi Kihara, judge how closely a newly found wild grass is related to cultivated wheat: cross it with known wheats, observe chromosome pairing in the hybrids, and infer shared genome sets from the pairing pattern before naming a donor`
- 中文对照：木原均风格，判断新发现野生禾草与栽培小麦的亲缘：与已知小麦杂交，观察杂种染色体配对，从配对模式推断共享染色体组，再谈供体。
- Negative: `no origin claim from morphology alone, no presenting a hypothesised donor as established fact, no genome claim without pairing data, no claiming the coinage of the word genome`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
