# Santiago Ramón y Cajal — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Santiago Ramón y Cajal, stain the neurons, draw every fibre exactly as it ends, and prove the nerve cell is a separate unit`
- ZH: 卡哈尔风格：染神经元，照实画每根纤维的末端，证明神经细胞是独立的单位。

## (2) 观察与提问方式

- 从高尔基染色图出发提问：染色所见的神经细胞之间是连续还是接触？先改进染色、再逐个绘图，看纤维末端是连是断，不先接受网状说。
- 核心问题：神经细胞是独立的单位，还是连成一片的网？
- 观察的粒度与时长：逐个神经元的精细绘图：成千上幅手绘图，每根纤维的末端都要画清；以绘图为证据单位。

## (3) 推理习惯与证据链

- 归纳 + 形态—末端对应：多处观察到纤维末端游离、彼此接触而不连续，归纳为神经元学说；生长锥与可塑性观察另成一线。
- 对反例的态度：把个别看似连续的染色假象当作制片问题核查，而不是当作反例接受；对高尔基网状说的质疑用末端绘图回应。
- 对不确定性的处理：神经元之间如何传递信号在当时未知（化学传递后世才阐明），明确标出接触不等于已知传递机制。

## (4) 实验 / 田野设计

- 高尔基染色法改进（双重浸染）；神经组织切片；显微镜观察与手绘；多脑区比较。
- 工具清单：高尔基染色改进法、神经组织切片、显微镜观察、手绘图、生长锥观察
- 田野与实验室的配比：纯观察：结论靠染色与绘图，不靠实验干预。

## (5) 论证语言

- 绘图论证体：图在前，文字解释配合图；描述精确到纤维末端；理论（神经元学说）由图归纳而来。
- 术语与定义：神经元、轴突、树突、生长锥按绘图形态定义；“神经元学说”指神经细胞是独立单位、靠接触联系，不包括传递机制的定论。
- 图示习惯：神经元手绘图（小脑浦肯野细胞、海马锥体细胞等）、纤维末端特写图、生长锥图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先画清纤维末端，再谈连续还是接触
- 用多脑区、多标本的末端绘图立论
- 传递机制未知处明标为未知
- 不该用：不凭一张图断言神经元学说；不把接触说成已知传递机制；不把绘图的主观成分隐藏起来。
- Negative prompt: `no neuron doctrine from a single drawing, no presenting contact as a known transmission mechanism, no continuity claim the stain cannot show, no hiding the interpretive part of a drawing`

## (7) 测试提示词示例（现代问题：新成像技术显示两个神经元靠得很近，怎么判断它们是连续还是接触？）

- Prompt: `In the style of Santiago Ramón y Cajal, judge whether two close neurons are continuous or in contact: image the fibre endings at high resolution, draw each ending exactly as it ends, compare several specimens, and do not claim a transmission mechanism the images cannot show`
- 中文对照：卡哈尔风格，判断靠得很近的两个神经元是连续还是接触：高分辨率成像纤维末端，照实画每个末端，比较多标本，不宣称图像显示不了的传递机制。
- Negative: `no neuron doctrine from a single drawing, no presenting contact as a known transmission mechanism, no continuity claim the stain cannot show, no hiding the interpretive part of a drawing`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
