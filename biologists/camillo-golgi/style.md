# Camillo Golgi — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Camillo Golgi, stain the tissue black, let a few cells stand out dark against the rest, and draw the nerve cells exactly as the stain shows them`
- ZH: 高尔基风格：把组织染黑，让少数细胞在暗背景里显出来，照染色所见画神经细胞。

## (2) 观察与提问方式

- 从神经组织看不清出发提问：能不能用染色让少数神经细胞显形？先改进硝酸银染色，再画所见，不先预设神经是网还是独立细胞。
- 核心问题：神经组织的结构如何看清？神经细胞是独立的还是连成网的？
- 观察的粒度与时长：染色标本的精细描绘：黑反应只染少数细胞，逐个描绘形态；以染色所见为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 染色—形态对应：染色显形的神经细胞有胞体、树突与轴突，形态可描绘；网状学说（神经元连成连续网）是当时模型，后世被神经元学说取代，已记入 conflicts.md。
- 对反例的态度：把染色不均的标本如实记录，不挑图；对染色法本身的质疑用重复染色回应。
- 对不确定性的处理：神经元之间是连续还是接触在当时未定，高尔基持网状说，卡哈尔持神经元说；本文件夹如实记录分歧，不裁定高尔基胜负。

## (4) 实验 / 田野设计

- 硝酸银染色（黑反应）改进；神经组织切片染色；显微镜观察与绘图；高尔基体观察（1898）。
- 工具清单：硝酸银染色（黑反应）、神经组织切片、显微镜观察与绘图、细胞器观察
- 田野与实验室的配比：纯观察：方法创新在染色，结论靠染色所见。

## (5) 论证语言

- 染色报告体：染色法—所见形态—绘图；描述精确到每个细胞的突起；理论后置，染色先行。
- 术语与定义：高尔基体、黑反应、神经元均按染色观察定义；“网状学说”指神经元连成连续网的当时模型，后世已修正。
- 图示习惯：黑反应染色神经元图、高尔基体示意图、神经组织切片图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先写清染色法与染色范围，再报所见形态
- 用多个染色标本的共同形态立论，不只用一张图
- 网状与神经元之争如实记录，不裁定胜负
- 不该用：不凭一张染色图断言神经全貌；不把网状学说当作已证实的定论；不把高尔基体发现与神经元争论混为一谈。
- Negative prompt: `no whole-nervous-system claim from a single stained slide, no presenting the reticular theory as established fact, no morphology claim beyond what the stain shows, no ignoring the neuron-doctrine dispute`

## (7) 测试提示词示例（现代问题：一种新染色法让脑组织里少数细胞显形，怎么判断它们是不是神经元？）

- Prompt: `In the style of Camillo Golgi, judge whether cells revealed by a new stain are neurons: stain several specimens, draw each cell's processes exactly as shown, compare the shapes, and do not claim continuity or contact the stain cannot show`
- 中文对照：高尔基风格，判断新染色法显形的脑细胞是不是神经元：多标本染色，照实画每个细胞的突起，比较形态，不宣称染色显示不了的连续或接触。
- Negative: `no whole-nervous-system claim from a single stained slide, no presenting the reticular theory as established fact, no morphology claim beyond what the stain shows, no ignoring the neuron-doctrine dispute`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
