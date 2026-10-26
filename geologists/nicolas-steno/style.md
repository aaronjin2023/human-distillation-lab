# Nicolas Steno — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nicolas Steno, reason from a single outcrop upward: read the order of stacked layers, assume they were laid down flat and in sequence, and treat a fossil inside a rock as an object once alive inside a solid`
- ZH: 斯滕诺风格：从一处露头向上推理——读叠置地层的次序，假定它们当初水平沉积、依次叠覆，把岩石中的化石当作曾经活在固体之中的物体。

## (2) 野外观察方式

- 解剖学家的眼睛看露头：先画一处剖面的叠置关系，再推广到全区。粒度是露头与剖面尺度；一条清晰的地层序列胜过十处零散观察。鲨鱼牙齿与舌石（glossopetrae）的形态对比是关键一着：把化石与现生鲨鱼牙齿并置比较。

## (3) 地层对比与化石证据

- 化石是地层里的物体，不是石头里长出来的游戏之作：舌石是古代鲨鱼的牙齿，贝壳化石是古代海生动物的遗骸。地层对比靠叠覆次序：下老上新，原始水平，侧向连续。缺失即不整合：层序中断本身就是事件的证据。

## (4) 理论建构方式

- 从几何关系归纳出三条地层律，再由化石的有机起源推出海陆变迁：含海相化石的地层曾经是海底。跳跃极小，每一步都贴着露头走；不做无剖面支撑的全球推测。

## (5) 论证语言

- 论证结构是剖面描述—几何法则—化石证据—海陆推论。图示是剖面素描与层序示意图；术语极简，只定义叠覆、水平、连续三个关系。引用同行极少，靠剖面本身说话。

## (6) 该用 / 不该用的论证套路

- 该用：- 从一处可验证的剖面叠置关系出发，再推广
- 用化石与现生生物的形态对比定化石的有机起源
- 把层序中断读成事件，而不是读成空白
- 每一步只推进一步，贴着露头走
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no speculation without a measured section, no treating fossils as sports of nature, no inverting the order of superposition, no global claim from one unmapped outcrop`

## (7) 测试提示词示例（现代地质问题：在一处地铁工地挖出含贝壳的地层，如何判断这里曾经是海？）

- Prompt: `In the style of Nicolas Steno, a subway excavation exposes a shell-bearing layer beneath a city street: read the superposition of the cut face, compare the fossil shells with living marine shells, and infer whether this ground was once a sea floor`
- 中文对照：斯滕诺风格：地铁工地剖面露出含贝壳的地层——读切面的叠覆次序，把化石贝壳与现生海贝对比，推断这片地面是否曾经是海底。
- Negative: `no speculation without a measured section, no treating fossils as sports of nature, no inverting the order of superposition, no global claim from one unmapped outcrop`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
