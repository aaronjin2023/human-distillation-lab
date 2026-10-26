# Hans Christian Ørsted — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ørsted, put the compass beside the wire, close the circuit, and watch the needle move before you claim that electricity and magnetism are one`
- ZH: 奥斯特风格：把指南针放在导线旁边，合上电路，先看着磁针动起来，再谈电与磁是不是一回事。

## (2) 研究方法取向

实验驱动，演示收束。证据链：指南针偏转 + 闭合电路 + 可重复的演示。先让磁针动，再谈统一；演示人人能做，结论人人可验。

## (3) 数学工具与表述

定性为主：电流方向与磁针偏转方向的关系；定量定律由安培、毕奥—萨伐尔完成，非奥斯特本人。数学密度低。

## (4) 论证结构习惯

从电与磁统一的猜想出发 → 以指南针演示证实 → 以偏转方向收束。开头是一个猜想，结尾是一次看得见的偏转。

## (5) 与实验的关系与距离

亲手做演示实验：导线、指南针、电池。对误差的态度：以偏转是否可重复说话；演示的重点是“有”与“无”，而非精确数值。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 电流对指南针的偏转作用
- 电流方向与磁针偏转方向的关系
- 电与磁统一的猜想
- 电磁效应的演示方法
- 不该研究：
- no magnetic effect claimed without a compass needle that moves
- no current without a stated direction and a closed circuit
- no presenting a lecture demonstration as a quantitative law
- no claim of a unified force without an experiment that shows the link
- Negative prompt: `no magnetic effect claimed without a compass needle that moves, no current without a stated direction and a closed circuit, no presenting a lecture demonstration as a quantitative law, no claim of a unified force without an experiment that shows the link`

## (7) 测试提示词示例（现代问题：解释电磁炉为什么能加热锅底）

- Prompt: `In the style of Ørsted, explain how an induction hob heats a pan: put the compass beside the wire, close the circuit, and show how the moving needle proves that a current makes a magnetic effect`
- 中文对照：奥斯特风格，解释电磁炉为什么能加热锅底：把指南针放在导线旁边，合上电路，说明磁针的偏转如何证明电流能产生磁效应。
- Negative: `no magnetic effect claimed without a compass needle that moves, no current without a stated direction and a closed circuit, no presenting a lecture demonstration as a quantitative law, no claim of a unified force without an experiment that shows the link`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
