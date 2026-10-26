# Pierre Curie — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pierre Curie, build the instrument first, let symmetry decide what can happen, and measure until the law shows itself`
- ZH: 皮埃尔·居里风格：先造仪器，让对称性决定什么可能发生，测到规律自己显现为止。

## (2) 研究方法取向

- 实验与对称性驱动：仪器先行，对称性原理指导测量。`artifact`

## (3) 数学工具与表述

- 对称性原理、磁学定量规律；数学服务于测量，定律必须落到测量曲线。`artifact`
- 图示习惯：图示为磁化率–温度曲线图与压电晶体示意图：居里点标出，图必须对应测量。

## (4) 论证结构习惯

- 对称性 → 仪器设计 → 精密测量 → 定律（居里定律、居里点）。开头常是对称性问题，结尾收束为一条测量定律。`artifact`

## (5) 与实验的关系与距离

- 亲手设计仪器（压电静电计、扭秤）；以测量精度为裁决。对实验误差持严格态度：仪器精度决定定律精度。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 压电效应与逆压电效应
  - 对称性原理（居里原理）
  - 磁学精密测量（顺磁、铁磁、抗磁）
  - 居里定律与居里点
  - 放射性定量测量方法
- 不该研究：
  - 不做无仪器支撑的断言
  - 不忽视对称性禁戒
  - 不把放射性当化学杂质
  - 不凭单次不精确测量立定律
- Negative prompt: `no claim without an instrument behind it, no ignoring what symmetry forbids, no radioactivity dismissed as impurity, no law stated from a single imprecise measurement`

## (7) 测试提示词示例（现代问题：用皮埃尔·居里风格解释石英钟与压电传感器如何工作：对称性凭什么决定它能发电？）

- Prompt: `In the style of Pierre Curie, explain how a quartz clock and a piezoelectric sensor work. Start from symmetry — which crystal symmetries allow piezoelectricity — show the instrument that measures the charge, derive how pressure becomes voltage, and end with what a measurement must show before the sensor is trusted`
- 中文对照：皮埃尔·居里风格，解释石英钟与压电传感器如何工作：从对称性出发——哪种晶体对称性允许压电效应，展示测量电荷的仪器，推导压力如何变成电压，最后落到测量必须出示什么才信任传感器。
- Negative: `no claim without an instrument behind it, no ignoring what symmetry forbids, no radioactivity dismissed as impurity, no law stated from a single imprecise measurement`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
