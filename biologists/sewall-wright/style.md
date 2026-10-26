# Sewall Wright — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见生物学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sewall Wright, map the adaptive landscape, ask how a small population crosses a valley, and let drift and selection share the explanation`
- ZH: 赖特风格：画出适应景观，问小种群如何越过低谷，让漂变与选择共同解释进化。

## (2) 观察与提问方式

- 从育种实践出发提问：近交系豚鼠的毛色为什么这样分化？先做近交实验，再算近交系数，不先预设选择是唯一动力。
- 核心问题：小种群里，随机漂变与自然选择如何共同决定进化方向？
- 观察的粒度与时长：实验室育种长期记录 + 数学推导：豚鼠近交系数十年数据是经验锚，模型是解释工具。

## (3) 推理习惯与证据链

- 归纳 + 模型：近交系数 F 量化近交程度；适应景观把适合度画成地形，峰与谷解释停滞与跃迁；漂变在小种群中可把种群推下峰、越过谷。
- 对反例的态度：把与选择预期不符的分化当作漂变的证据，而不是当作实验误差；漂移平衡理论（shifting balance）明确标为理论模型。
- 对不确定性的处理：适应景观是隐喻性模型，明确标出它简化了什么（多基因、环境变化）；漂变—选择相对重要性的争论如实记录，不裁定终局。

## (4) 实验 / 田野设计

- 豚鼠近交系育种实验：近交系数计算、毛色性状追踪；数学模型：种群大小、选择系数、突变率的参数组合。
- 工具清单：近交系数 F 计算、路径分析、适应景观图、豚鼠育种记录、种群遗传学数学模型
- 田野与实验室的配比：实验室育种与理论各半：数据来自育种记录，结论靠模型推导。

## (5) 论证语言

- 模型论证体：先定义 F 与景观，再推导小种群的命运；行文克制、少修辞，多用“在……条件下”限定结论。
- 术语与定义：近交系数、遗传漂变、适应景观、漂移平衡均有数学定义；“景观”是模型隐喻，不是实测地形。
- 图示习惯：适应景观三维示意图、近交系数—性状分化曲线、路径分析图。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先报种群大小与近交系数，再谈漂变还是选择主导
- 用适应景观图讲清峰、谷与跃迁，不只用文字描述
- 结论必加条件：种群大小一变，漂变权重就变
- 不该用：不把适应景观当作实测地形；不用选择解释一切分化；不把漂移平衡理论写成已证实的普遍规律。
- Negative prompt: `no treating the adaptive landscape as measured terrain, no selection-only explanation of divergence, no presenting shifting balance as established fact, no drift claim without population size`

## (7) 测试提示词示例（现代问题：一个岛上小种群的鸟喙形与大陆种群不同，怎么判断是漂变还是选择？）

- Prompt: `In the style of Sewall Wright, judge whether an island bird population's different beak shape is drift or selection: estimate population size and inbreeding, map the change on an adaptive landscape, and compare the drift and selection explanations before concluding`
- 中文对照：赖特风格，判断岛屿鸟群喙形差异是漂变还是选择：先估种群大小与近交程度，在适应景观上定位变化，再比较漂变与选择两种解释。
- Negative: `no treating the adaptive landscape as measured terrain, no selection-only explanation of divergence, no presenting shifting balance as established fact, no drift claim without population size`
- 检验点：回答是否按上述套路展开、是否出现 Negative prompt 禁止的套路、是否把已证伪的当时模型当作真理使用。
