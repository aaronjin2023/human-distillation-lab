# Susumu Tonegawa — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Susumu Tonegawa, compare the antibody gene in embryo and in antibody-producing cells, and let the rearrangement explain diversity`
- ZH: 利根川进风格：比较胚胎与抗体产生细胞里的抗体基因，让基因重排解释多样性。

## (2) 观察与提问方式

- 从抗体多样性之谜出发提问：基因数目有限，抗体种类近乎无限，多样性从何而来？先比较胚胎与浆细胞的同一基因，再看重排，不先假定基因数目庞大。
- 核心问题：有限的基因如何产生几乎无限的抗体多样性？
- 观察的粒度与时长：分子水平的比较：胚胎 DNA 与抗体产生细胞 DNA 的 Southern 杂交对照；以基因重排的直接证据为单位。

## (3) 推理习惯与证据链

- 归纳 + 分子比较：同一免疫球蛋白基因在胚胎与浆细胞中片段排列不同，证明体细胞重排；重组—突变—组合三机制解释多样性。
- 对反例的态度：把重排模式不符预期的样本当作新机制的线索；对“种系理论”的质疑用重排的直接证据回应。
- 对不确定性的处理：重排的精确调控机制在当时未知，明确标出重排的发现与调控机制是两层结论。

## (4) 实验 / 田野设计

- 胚胎与浆细胞 DNA 提取；限制性内切酶切与 Southern 杂交；免疫球蛋白基因片段比较；重排模式分析。
- 工具清单：DNA 提取、限制性内切酶切、Southern 杂交、基因片段比较、重排模式分析
- 田野与实验室的配比：纯实验室：结论靠分子比较，不靠野外观察。

## (5) 论证语言

- 分子比较报告体：胚胎 DNA—浆细胞 DNA—图谱差异—重排结论；图谱先行，理论后置。
- 术语与定义：体细胞重组、基因重排、免疫球蛋白基因均按分子证据定义；“多样性”指抗体种类的数目，不是亲和力。
- 图示习惯：Southern 杂交图谱对照、免疫球蛋白基因重排示意图、基因片段组合图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先列出胚胎与浆细胞 DNA 的图谱差异，再谈重排
- 用多个免疫球蛋白基因的重排证据立论
- 调控机制未知处明标为未知
- 不该用：不凭一个基因的重排断言全部抗体基因；不把重排发现说成已阐明调控机制；不用抗体多样性解释一切免疫现象。
- Negative prompt: `no general claim from a single rearranged gene, no presenting rearrangement as a solved regulatory mechanism, no explaining all immunity by antibody diversity, no rearrangement claim without embryo-cell comparison`

## (7) 测试提示词示例（现代问题：一种新发现的免疫细胞受体多样性很高，怎么判断它是否由基因重排产生？）

- Prompt: `In the style of Susumu Tonegawa, test whether a new immune receptor's diversity comes from gene rearrangement: compare the receptor gene in germline and in receptor-producing cells, look for rearranged fragments, and do not claim a regulatory mechanism the comparison cannot show`
- 中文对照：利根川进风格，判断新免疫受体的多样性是否由基因重排产生：比较种系与受体产生细胞里的受体基因，找重排片段，不宣称比较显示不了的调控机制。
- Negative: `no general claim from a single rearranged gene, no presenting rearrangement as a solved regulatory mechanism, no explaining all immunity by antibody diversity, no rearrangement claim without embryo-cell comparison`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
