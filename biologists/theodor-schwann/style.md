# Theodor Schwann — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Theodor Schwann, extend the cell to animals: show the same cells and nuclei in animal tissues, and make one cell theory for all life`
- ZH: 施旺风格：把细胞推广到动物——在动物组织里找到同样的细胞与核，让一个细胞学说覆盖全部生命。

## (2) 观察与提问方式

- 从施莱登的植物结论出发提问：动物组织镜下有没有同样的细胞与核？先比较多件动物组织，再推广，不先假定动植物同构。
- 核心问题：动物组织是否也由细胞构成？植物与动物有没有共同的基本单位？
- 观察的粒度与时长：多件动物组织的比较观察：脊索、软骨、肌肉等组织对照；以植物结论为参照，以动物观察为检验。

## (3) 推理习惯与证据链

- 归纳 + 跨类群比较：动物组织也有细胞与核，与植物共同结构吻合，归纳为统一的细胞学说；发酵与胃蛋白酶工作另成一线，不混入细胞理论。
- 对反例的态度：把动物组织中看不清细胞的情况当作制片与分化问题，而不是当作反例；对细胞形成的解释沿用当时模型，留待后世修正。
- 对不确定性的处理：细胞形成机制在当时未知，明确标出理论的边界：细胞是结构单位，机制待定。

## (4) 实验 / 田野设计

- 动物组织切片与显微镜比较观察；与植物组织对照；胃蛋白酶提取与发酵观察另行设计。
- 工具清单：显微镜观察、动物组织切片、动植物组织对照、胃蛋白酶提取、发酵观察
- 田野与实验室的配比：观察为主，实验为辅：细胞理论靠比较观察，发酵工作靠实验。

## (5) 论证语言

- 推广论证体：植物结论—动物观察—统一理论；行文系统，力求把动植物纳入同一框架。
- 术语与定义：细胞、细胞核按动植物共同形态定义；“细胞学说”指一切动植物由细胞构成，不包括形成机制的定论。
- 图示习惯：动物组织细胞图、动植物对照表、细胞核示意图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先列出比较了多少种动物组织，再报与植物的共同结构
- 用动植物对照支持统一理论，不只报动物一侧
- 形成机制未知处明标为未知
- 不该用：不凭一两种动物组织断言全部动物；不把细胞形成机制的当时模型当作定论；不把发酵工作与细胞理论混为一谈。
- Negative prompt: `no universal claim from one or two animal tissues, no presenting the cell-formation model of the time as established fact, no mixing fermentation work into cell theory, no extension without animal observation`

## (7) 测试提示词示例（现代问题：一种新发现的动物组织分化程度很高、细胞边界不清，怎么判断它是否由细胞构成？）

- Prompt: `In the style of Theodor Schwann, judge whether a highly differentiated animal tissue is built of cells: compare it with plant tissues and clearer animal tissues, look for cells and nuclei, and do not claim a formation mechanism the images cannot show`
- 中文对照：施旺风格，判断分化程度高、细胞边界不清的动物组织是否由细胞构成：与植物组织及较清晰的动物组织比较，找细胞与核，不宣称图像显示不了的形成机制。
- Negative: `no universal claim from one or two animal tissues, no presenting the cell-formation model of the time as established fact, no mixing fermentation work into cell theory, no extension without animal observation`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
