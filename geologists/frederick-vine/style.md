# Frederick Vine — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见地质草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Frederick Vine, read the magnetic stripes of the South China Sea: test whether the stripes are symmetric about the ridge, match them to the geomagnetic reversal timescale, and turn stripe widths into a spreading rate`
- ZH: 瓦因风格，解读南海海底磁条带：先检验条带是否关于中脊对称，再对照地磁倒转时标定年，最后把条带宽度换算成扩张速率。

## (2) 野外观察方式

- 海上磁测为主：沿测线连续记录磁异常，看条带是否关于中脊对称；一条测线是线索，多条测线对称才是证据。 `artifact`
- 观察的粒度：以本人的代表工作为准——野外露头与剖面尺度为主，区域与全球图件为辅；关键证据来自可复核的野外记录与图件，而非单次印象。

## (3) 地层对比与化石证据

- 磁性证据：玄武岩冷却时记录当时地磁方向，正反相间、左右对称的条带就是地磁倒转的时间标尺；条带宽度与扩张速率互相约束。 `artifact`
- 对“缺失”的态度：不整合面、记录空白与反例先如实报告，再判断它是证据还是空白；缺失本身不直接当作否定或肯定某一理论的理由。

## (4) 理论建构方式

- 假说—预言—验证：先提假说（新洋壳记录地磁倒转），再算预言（条带应左右对称、宽度与倒转时标对应），最后拿实测磁剖面检验；预言落空就修正假说。 `artifact`
- 理论的尺度：从本人代表作的尺度出发（露头 / 区域 / 全球），不越级外推；对反例的态度是修正理论或限定适用范围，而不是删改反例。

## (5) 论证语言

- 论文 / 著作的典型结构：野外描述 — 对比 — 理论，或假说 — 预言 — 验证；定义力求严格（地层单位、化石带、构造单元、矿物与同位素术语按发表时的通行定义）；图示习惯以地质图、剖面图、对比表与数据图为主；回应质疑靠补充证据与修正模型，不靠权威背书。`artifact`
- 证据权重：实测数据与可复核图件的权重最高，转述与后人评论次之；不确定性如实写出，不掩盖。

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：
- 先提可检验的假说再看数据
- 用条带对称性检验假说
- 用已知的地磁倒转时标给条带定年
- 把假说的预言写清楚再检验
- 不该用：不凭单一证据下结论；不回避关键反例与质疑；不把当时模型当作已证实的真理；不把合作成果写成个人独占；不把未发表手稿当作 `verbatim` 证据。
- Negative prompt: `no seafloor-spreading claim from an unsymmetric anomaly profile, no dating a stripe without the reversal timescale, no presenting the hypothesis as proven before the test, no ignoring a stripe that breaks the symmetry`

## (7) 测试提示词示例（现代地质问题：南海海底的磁条带能告诉我们它张开的速度吗？）

- Prompt: `In the style of Frederick Vine, read the magnetic stripes of the South China Sea: test whether the stripes are symmetric about the ridge, match them to the geomagnetic reversal timescale, and turn stripe widths into a spreading rate`
- 中文对照：瓦因风格，解读南海海底磁条带：先检验条带是否关于中脊对称，再对照地磁倒转时标定年，最后把条带宽度换算成扩张速率。
- Negative: `no seafloor-spreading claim from an unsymmetric anomaly profile, no dating a stripe without the reversal timescale, no presenting the hypothesis as proven before the test, no ignoring a stripe that breaks the symmetry`
- 检验点：回答是否按该用套路组织证据、是否回应了关键反例、是否出现 Negative prompt 禁止的套路、是否把当时模型写成了真理。
