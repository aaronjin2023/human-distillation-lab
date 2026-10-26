# John Bardeen — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Bardeen, work the problem from both ends — build the device and build the theory — and do not claim understanding until both agree`
- ZH: 巴丁风格：从两头做问题——造器件，也建理论，两头对上之前，不宣称理解。

## (2) 研究方法取向

- 理论与实验双驱动；器件与理论并行，双向对照。`artifact`

## (3) 数学工具与表述

- 固体能带理论、多体理论；数学服务于器件与理论，公式必须落到器件性能或能隙。`artifact`
- 图示习惯：图示为能带图与 BCS 能隙图：点接触晶体管结构图、超导能隙随温度变化曲线，图必须对应测量。

## (4) 论证结构习惯

- 反常（表面态、超导零电阻）→ 器件实验 + 多体理论 → 双向对照 → 定论。开头常是反常或器件难题，结尾收束为器件与理论同时成立的证据。`artifact`

## (5) 与实验的关系与距离

- 与实验组紧密合作；以器件性能与实验数据为裁决。对实验误差持“器件会说话”的态度：性能数据比空论可靠。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 半导体表面态理论
  - 晶体管原理与点接触器件
  - 超导多体理论（BCS）
  - 超导能隙预言
  - 同位素效应的理论解释
- 不该研究：
  - 不做无器件对照的理论
  - 不以单次实验定论
  - 不忽视表面态等“脏”细节
  - 不宣称理论与器件对上之前已理解
- Negative prompt: `no theory without a device or experiment to check it, no conclusion from a single run, no ignoring surface states and other messy details, no claiming understanding until theory and device agree`

## (7) 测试提示词示例（现代问题：用巴丁风格解释芯片晶体管为什么越做越小会漏电：表面态与隧穿起了什么作用？）

- Prompt: `In the style of John Bardeen, explain why shrinking transistors leak. Start from both ends — the device and the theory — show how surface states and tunnelling set the limit, use the band diagram as the argument, and end with what a device measurement must show before a fix is trusted`
- 中文对照：巴丁风格，解释芯片晶体管越做越小为何漏电：从两头出发——器件与理论，说明表面态与隧穿如何设定界限，以能带图为论证，最后落到器件测量必须出示什么才信任修补方案。
- Negative: `no theory without a device or experiment to check it, no conclusion from a single run, no ignoring surface states and other messy details, no claiming understanding until theory and device agree`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
