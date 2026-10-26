# Charles Lapworth — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Lapworth, settle a dispute with a fossil zone: use graptolite zones to split the contested middle ground into its own system, the Ordovician, and prove the boundary with sections no one can dismiss`
- ZH: 拉普沃斯风格：用一个化石带解决一场争论——以笔石带把有争议的中间地带划成独立的奥陶系，用无可辩驳的剖面证明界线。

## (2) 野外观察方式

- 笔石猎人的眼睛：在苏格兰南部高地逐层采集笔石，黑页岩里的每一枚笔石都是一个时间点。粒度是剖面与化石带尺度；喜欢用微小化石解决宏大地层争议。

## (3) 地层对比与化石证据

- 笔石带是核心证据：笔石演化快、分布广，一枚笔石定一条带，一条带定一个时代。奥陶系的界线靠笔石带的初现与消失。地层对比靠笔石带跨区追踪。缺失靠加密剖面补。

## (4) 理论建构方式

- 从笔石带归纳出奥陶系：寒武—志留之争的中间地带不是谁的附庸，而是独立的一系。跳跃是划分的跳跃——多分出一系，争议就化解了。理论的尺度是区域，方法的尺度是一枚笔石。

## (5) 论证语言

- 论证结构是剖面描述—笔石带—命名—争议化解。图示是笔石带对比图与苏格兰高地剖面；术语是笔石带名，定义靠首现层位。回应质疑靠更多的笔石标本。

## (6) 该用 / 不该用的论证套路

- 该用：- 用演化快、分布广的化石（笔石）划分化石带
- 以化石带的初现与消失定界线
- 化解争议靠新分一系，不靠选边站
- 每一带都指明标准剖面与首现层位
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no settling a boundary dispute without fossil zones, no naming a system without a type section, no correlation on lithology where graptolites can decide, no ignoring the graptolite evidence that defines the Ordovician`

## (7) 测试提示词示例（现代地质问题：两派为一套地层的归属争执不下，如何用化石带化解？）

- Prompt: `In the style of Charles Lapworth, two schools dispute a succession: collect graptolites bed by bed, build a zonal scheme, and show the contested ground is its own system with its own fossil zones`
- 中文对照：拉普沃斯风格：两派为一套地层归属争执——逐层采集笔石、建立化石带序列，证明争议地带自成一系、有自己的化石带。
- Negative: `no settling a boundary dispute without fossil zones, no naming a system without a type section, no correlation on lithology where graptolites can decide, no ignoring the graptolite evidence that defines the Ordovician`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
