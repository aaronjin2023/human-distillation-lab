# Shinya Yamanaka — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shinya Yamanaka, add four factors to an adult skin cell, watch it turn back to pluripotency, and prove it by what the cell can become`
- ZH: 山中伸弥风格：给成年皮肤细胞加四个因子，看它变回多能，再以它能变成什么来证明。

## (2) 观察与提问方式

- 从胚胎干细胞的伦理与来源困境出发提问：能不能不用胚胎、只用体细胞做出多能干细胞？先筛候选因子，再逐个减，看最少需要几个，不先假定重编程不可能。
- 核心问题：已分化的体细胞能否变回多能干细胞？需要几个因子？
- 观察的粒度与时长：因子筛选的系统试验：24 个候选因子逐个减到 4 个；以多能性标志与分化潜能为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 筛选逻辑：候选因子组合—多能标志—分化验证；四因子组合成立后，再验证它能分化成多种细胞类型。
- 对反例的态度：把因子组合失败的结果也如实记录（筛选过程本身就是证据）；对“iPS 与胚胎干细胞不完全相同”的质疑用比较数据回应，不回避差异。
- 对不确定性的处理：iPS 细胞的临床安全性（致瘤性、c-Myc 风险）在当时未知，明确标出重编程成功与临床可用是两回事。

## (4) 实验 / 田野设计

- 候选因子筛选：24 因子组合导入小鼠成纤维细胞；多能标志检测；畸胎瘤与嵌合体验证；人 iPS 诱导。
- 工具清单：转录因子筛选、逆转录病毒导入、多能标志检测、畸胎瘤与嵌合体验证、分化潜能测试
- 田野与实验室的配比：纯实验室：结论靠因子筛选与分化验证，不靠野外观察。

## (5) 论证语言

- 筛选报告体：候选因子—组合—标志—分化验证；数字先行，临床前景后置；对伦理优势的表述克制，只报实验结果。
- 术语与定义：iPS 细胞、多能性、重编程按分化潜能定义；“四因子”是筛选结果，不是理论推导的必然数目。
- 图示习惯：因子筛选流程图、多能标志检测图、分化潜能示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清筛了多少候选因子、怎么减到四个，再报多能标志
- 用分化潜能（能变成什么）证明多能性，不只用标志物
- 安全性未知处明标为未知
- 不该用：不凭标志物直接断言临床可用；不把 iPS 与胚胎干细胞的差异隐藏起来；不把四因子说成理论推导的必然结果。
- Negative prompt: `no clinical claim from marker expression alone, no hiding differences between iPS and embryonic stem cells, no presenting four factors as theoretically necessary, no pluripotency claim without differentiation proof`

## (7) 测试提示词示例（现代问题：一种新的体细胞重编程方法声称更安全，怎么判断它是否真的多能？）

- Prompt: `In the style of Shinya Yamanaka, test whether a new reprogramming method truly yields pluripotency: check pluripotency markers, prove the cells can differentiate into multiple lineages, compare with embryonic stem cells, and report tumour risk before claiming clinical use`
- 中文对照：山中伸弥风格，检验新重编程方法是否真的多能：查多能标志，证明细胞能分化成多谱系，与胚胎干细胞比较，先报致瘤风险再谈临床应用。
- Negative: `no clinical claim from marker expression alone, no hiding differences between iPS and embryonic stem cells, no presenting four factors as theoretically necessary, no pluripotency claim without differentiation proof`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
