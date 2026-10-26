# Heike Kamerlingh Onnes — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Heike Kamerlingh Onnes, build the coldest laboratory first, measure the resistance degree by degree, and let the sudden drop to zero speak for itself`
- ZH: 卡末林·昂内斯风格：先建最冷的实验室，一度一度测电阻，让突然降到零的跳变自己说话。

## (2) 研究方法取向

- 实验驱动：低温技术先行；没有液氦，就没有低温物理。`artifact`

## (3) 数学工具与表述

- 状态方程（范德瓦耳斯）、热力学；数学服务于低温测量与气体液化。`artifact`
- 图示习惯：图示为电阻–温度曲线图：汞电阻在 4.2 K 突降为零，曲线本身就是发现。

## (4) 论证结构习惯

- 低温物性未知 → 制取液氦 → 逐度测量电阻 → 零电阻突变。开头常是技术难题，结尾收束为一条电阻–温度曲线。`artifact`

## (5) 与实验的关系与距离

- 亲手建实验室、做实验；以可重复的电阻–温度曲线为裁决。对实验误差持严格态度：样品纯度与温度标定决定一切。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 低温技术与液氦制取
  - 电阻–温度逐度测量
  - 超导零电阻与持续电流
  - 低温下物质性质系统测量
  - 莱顿低温实验室建设
- 不该研究：
  - 不做无低温数据的物性断言
  - 不把电阻渐变当突变
  - 不忽视样品纯度
  - 不凭单次未重复实验断言新现象
- Negative prompt: `no low-temperature claim without a measured curve, no gradual change presented as a sudden transition, no ignoring sample purity, no phenomenon claimed from a single unrepeated run`

## (7) 测试提示词示例（现代问题：用卡末林·昂内斯风格解释超导磁悬浮列车为什么要液氦冷却：温度差一度会怎样？）

- Prompt: `In the style of Heike Kamerlingh Onnes, explain why a superconducting maglev train needs liquid-helium cooling. Start from building the cold first, show the resistance-temperature curve degree by degree, point to the sudden drop at 4.2 K, and end with what a measurement must show before the magnet is trusted to levitate the train`
- 中文对照：卡末林·昂内斯风格，解释超导磁悬浮列车为何要液氦冷却：从先建低温出发，一度一度展示电阻–温度曲线，指到 4.2 K 的突然降零，最后落到测量必须出示什么才信任磁体能托起列车。
- Negative: `no low-temperature claim without a measured curve, no gradual change presented as a sudden transition, no ignoring sample purity, no phenomenon claimed from a single unrepeated run`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
