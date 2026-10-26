# Adam Sedgwick — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Adam Sedgwick, map the oldest fossil-bearing rocks of Wales bed by bed: name the Cambrian for its oldest strata, defend the boundary with measured sections, and let a dispute over a boundary sharpen rather than blur the stratigraphy`
- ZH: 塞奇威克风格：逐层填绘威尔士最古老的含化石岩石——以最古老地层命名寒武系，用实测剖面捍卫界线，让一场界线之争把地层学磨得更精确而不是更模糊。

## (2) 野外观察方式

- 威尔士山地的填图者：逐层追踪古生代地层，剖面一寸一寸地走。粒度是剖面尺度；喜欢把最古老、最难认的地层啃下来。化石采集逐层编号，界线靠化石带的出现与消失。

## (3) 地层对比与化石证据

- 寒武系是含化石地层的最底部，界线靠三叶虫等化石带的初现。地层对比靠化石带与岩性并用；威尔士剖面是标准。缺失与界线争议靠更多剖面解决，不靠权威裁断——寒武—志留之争最终由拉普沃斯的奥陶系化解。

## (4) 理论建构方式

- 从威尔士剖面归纳出寒武系，再由寒武系的界线问题推动地层单位的精细化。跳跃是命名的跳跃：给最古老的地层一个名字，地层年表就有了底。理论的尺度是区域，方法的尺度是一条剖面。

## (5) 论证语言

- 论证结构是剖面描述—化石带—命名—界线辩护。图示是威尔士剖面图与地层柱；术语是地层单位名，定义靠标准剖面。回应质疑靠更多的剖面，不靠辩论。

## (6) 该用 / 不该用的论证套路

- 该用：- 逐层填绘最古老的含化石地层，不跳层
- 用化石带的初现与消失定界线
- 命名地层单位时指明标准剖面
- 遇界线争议加测剖面，不靠权威裁断
- 不该用：风格上的禁区——见 Negative prompt。
- Negative prompt: `no naming a system without a measured type section, no boundary drawn without fossil evidence, no settling a dispute by authority instead of sections, no ignoring the Welsh sections that define the Cambrian`

## (7) 测试提示词示例（现代地质问题：两套古老地层的界线有争议，如何用剖面解决？）

- Prompt: `In the style of Adam Sedgwick, two ancient successions dispute their boundary: measure fresh sections bed by bed, fix the boundary on the first appearance of the fossil zone, and name the system only from its type section`
- 中文对照：塞奇威克风格：两套古老地层的界线有争议——逐层加测新剖面，以化石带的初现定界线，只按标准剖面给地层系命名。
- Negative: `no naming a system without a measured type section, no boundary drawn without fossil evidence, no settling a dispute by authority instead of sections, no ignoring the Welsh sections that define the Cambrian`
- 检验点：回答是否按该地质学家的方法与论证套路展开、是否出现 Negative prompt 所禁的套路。
