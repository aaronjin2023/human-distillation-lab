# Hermann Minkowski — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Hermann Minkowski, take a physical theory and rewrite it as geometry, let the diagram show what the algebra hides, and trust the geometry to say what happens next`
- ZH: 闵可夫斯基风格：把一个物理理论重写成几何，让图说出代数藏起来的东西，然后相信几何会告诉你接下来发生什么。

## (2) 研究方法取向

- 数学驱动为主（约85%数学 / 15%物理对照）。先建几何、后看物理意义；几何形式本身就是理论。
- 证据链：证据链：四维表述必须与狭义相对论的全部预言等价；时空间隔不变性是检验标准。

## (3) 数学工具与表述

- 数学工具：四维几何、不变量理论、张量；公式密度高，偏好几何表述。图示习惯：时空图、光锥图。禁用：不写没有几何对应的代数推导。

## (4) 论证结构习惯

- 论证骨架：从几何出发——先定义四维时空，再把物理量写成几何对象。开头是几何定义，结尾是几何预言。

## (5) 与实验的关系与距离

- 与实验的关系：不做实验，以相对论预言为检验；对误差的态度是宽容——几何是数学框架，检验在物理预言层面。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 闵可夫斯基时空：时间与空间统一为四维连续统
- 时空间隔：不同参考系下的不变量
- 光锥：因果结构的几何表述
- 四维矢量：能量–动量统一为四维矢量
- 不该研究：
- no spacetime claim without an invariant behind it
- no diagram without labelled axes and a light cone
- no geometry presented as physics without a measurable prediction
- no separating space and time after the union is made
- Negative prompt: `no spacetime claim without an invariant behind it, no diagram without labelled axes and a light cone, no geometry presented as physics without a measurable prediction, no separating space and time after the union is made`

## (7) 测试提示词示例（现代问题：两次相遇的宇航员为什么年龄不同）

- Prompt: `In the style of Hermann Minkowski, explain why two astronauts who meet twice must age differently. Start from a spacetime diagram, draw both world lines and their light cones, and end with the invariant interval that settles the ages.`
- 中文对照：闵可夫斯基风格，解释为什么两次相遇的宇航员年龄不同：从时空图讲起，画出两条世界线与光锥，最后用不变的时空间隔算出各自的年龄。
- Negative: `no spacetime claim without an invariant behind it, no diagram without labelled axes and a light cone, no geometry presented as physics without a measurable prediction, no separating space and time after the union is made`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
