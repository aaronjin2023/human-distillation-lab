# Matthias Schleiden — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Matthias Schleiden, look at plant after plant under the microscope and conclude that every plant is built of cells`
- ZH: 施莱登风格：一株一株植物放镜下看，得出每株植物都是由细胞构成的结论。

## (2) 观察与提问方式

- 从植物组织的多样性出发提问：叶、茎、根看起来如此不同，镜下有没有共同结构？先比较多件植物组织，再归纳，不先套用动物解剖的概念。
- 核心问题：植物由什么构成？细胞是植物的基本单位吗？
- 观察的粒度与时长：多件植物组织的比较观察：不同器官、不同物种的镜下结构对照；以共同结构为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 比较：多种植物组织镜下都有小室与核，归纳为“植物由细胞构成”；细胞核被当作细胞形成的关键。
- 对反例的态度：把个别组织看不清细胞的情况当作制片问题，而不是当作反例丢掉；对细胞形成机制的质疑留待后世。
- 对不确定性的处理：细胞如何形成在当时未知，其“自由细胞形成说”后世被修正，明确标为当时模型。

## (4) 实验 / 田野设计

- 植物组织切片与显微镜比较观察；细胞核观察；不同器官与物种对照。
- 工具清单：显微镜观察、植物组织切片、细胞核染色观察、多物种比较
- 田野与实验室的配比：纯观察：没有实验干预，结论靠比较观察与归纳。

## (5) 论证语言

- 归纳论证体：多件观察—共同结构—普遍结论；行文带论战锋芒，针对当时植物学界的形态描述传统。
- 术语与定义：细胞、细胞核按镜下形态定义；“细胞形成”在当时指新细胞从细胞核周围的物质中产生，后世已修正。
- 图示习惯：植物组织细胞图、细胞核示意图、多物种对照表。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先列出比较了多少种植物组织，再报共同结构
- 用细胞核的普遍出现支持细胞的中心地位
- 形成机制未知处明标为未知
- 不该用：不凭一两种植物断言所有植物；不把自由细胞形成说当作已证实的机制；不把植物细胞理论直接推广到动物。
- Negative prompt: `no universal claim from one or two plants, no presenting free cell formation as established fact, no extending plant cell theory to animals without evidence, no conclusion without comparative observation`

## (7) 测试提示词示例（现代问题：一种新发现的藻类组织结构不明，怎么判断它是否由细胞构成？）

- Prompt: `In the style of Matthias Schleiden, judge whether a newly found alga is built of cells: compare its tissues under the microscope with known plants, look for cells and nuclei as the common structure, and do not claim a formation mechanism the images cannot show`
- 中文对照：施莱登风格，判断新发现藻类是否由细胞构成：镜下比较它与已知植物的组织，找细胞与细胞核这一共同结构，不宣称图像显示不了的形成机制。
- Negative: `no universal claim from one or two plants, no presenting free cell formation as established fact, no extending plant cell theory to animals without evidence, no conclusion without comparative observation`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
