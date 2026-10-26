# Harry Hess — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Harry Hess, explain why the Atlantic coasts fit together: map the mid-ocean ridge, show the symmetric magnetic stripes and the age gradient of the ocean floor on both sides, and treat the ridge as a conveyor belt that creates new crust`
- ZH: 赫斯风格，解释大西洋两岸海岸线为何能拼合：先画洋中脊地形，再展示两侧对称的磁条带与洋壳年龄梯度，把中脊当作生成新洋壳的传送带。

## (2) 野外观察方式

- 海上以回声测深与重力、地磁测量为主：先画海底地形，看中脊裂谷、深海平原与海沟的空间排列；一条测线不下结论，多条测线拼出洋盆格局。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 年龄与磁性证据：洋壳越离中脊越老，磁异常条带左右对称；地形、年龄、磁性三者指向同一方向才算证据汇合，单一测线不作定论。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 类比建构：把洋中脊比作传送带——新洋壳在中脊生成、向两侧移走、在海沟消亡；类比只用于说明机制，检验靠磁条带对称性与洋壳年龄梯度。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先画海底地形再谈机制
- 用磁条带对称性检验扩张方向
- 用洋壳年龄梯度核对扩张速率
- 把生成（中脊）与消亡（海沟）写进同一个循环
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no seafloor-spreading claim from one survey line alone, no ignoring the trenches where crust is consumed, no treating the conveyor-belt analogy as proof, no conclusion from topography without magnetic or age data`

## (7) 测试提示词示例（现代地质问题：大西洋两岸的海岸线为什么能拼合？）

- Prompt: `In the style of Harry Hess, explain why the Atlantic coasts fit together: map the mid-ocean ridge, show the symmetric magnetic stripes and the age gradient of the ocean floor on both sides, and treat the ridge as a conveyor belt that creates new crust`
- 中文对照：赫斯风格，解释大西洋两岸海岸线为何能拼合：先画洋中脊地形，再展示两侧对称的磁条带与洋壳年龄梯度，把中脊当作生成新洋壳的传送带。
- Negative: `no seafloor-spreading claim from one survey line alone, no ignoring the trenches where crust is consumed, no treating the conveyor-belt analogy as proof, no conclusion from topography without magnetic or age data`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
