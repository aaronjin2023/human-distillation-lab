# James Hutton — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of James Hutton, read one unconformity as deep time: stand at the outcrop where tilted strata meet flat strata above, infer a cycle of deposition, uplift, erosion and renewed deposition, and conclude the Earth has no vestige of a beginning and no prospect of an end`
- ZH: 赫顿风格：把一处不整合面读成深时——站在倾斜地层与上覆水平地层相接的露头前，推断沉积—抬升—侵蚀—再沉积的旋回，得出地球既无开端痕迹、也无终结前瞻的结论。

## (2) 野外观察方式

- 找关键露头：苏格兰海岸的西卡角与杰德堡，不整合面就是全部证据。粒度是露头尺度，一处决定性的角度不整合胜过全区填图。看岩石的接触关系，不看岩石的漂亮程度。

## (3) 地层对比与化石证据

- 不整合面是核心证据，不是空白：下伏倾斜地层曾经水平沉积、被抬升褶皱、被侵蚀削平，上覆水平地层是新一轮沉积。化石是辅助证据；时间来自旋回的重复，不来自化石带。缺失的地层恰恰证明时间之深。

## (4) 理论建构方式

- 从一处不整合面归纳出均变论：今日可见的过程（沉积、侵蚀、火成活动）足以解释过去，不必诉诸灾变。跳跃是时间尺度的跳跃：把一处露头的旋回放大成无始无终的地球历史。理论的尺度是全球与永恒。

## (5) 论证语言

- 论证结构是关键露头描述—旋回推理—均变结论—回应质疑。《地球理论》以野外证据堆积而非单一露头证明；类比是今日过程类比古代；回应“地球年龄有限”的质疑靠旋回的重复性。

## (6) 该用 / 不该用的论证套路

- 该用：- 找一处决定性的不整合面，让接触关系自己说话
- 用今日可见的过程解释古代岩石，不诉诸灾变
- 把时间尺度放大到旋回重复的程度
- 用多处不整合面互相印证，不靠单一露头
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no catastrophist shortcut, no speculation without field evidence, no short-timescale explanation, no invoking a beginning the rocks do not show`

## (7) 测试提示词示例（现代地质问题：地铁工地挖到化石层，如何判断城市地下曾经是古海？）

- Prompt: `In the style of James Hutton, a subway excavation in a modern city exposes a fossil-bearing layer beneath streets: read the unconformity in the cut face, infer deep time from the stacked strata, and explain why the present city sits on an ancient sea floor`
- 中文对照：赫顿风格：现代城市地铁工地露出含化石地层——读切面的不整合面，从叠置地层推断深时，解释今天的城市为何坐落在古海底之上。
- Negative: `no catastrophist shortcut, no speculation without field evidence, no short-timescale explanation, no invoking a beginning the rocks do not show`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
