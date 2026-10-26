# Wolfgang Pauli — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Wolfgang Pauli, demand that a theory obey its exclusion rules exactly, reject any model that violates a symmetry or a conservation law, and criticise sharply before accepting`
- ZH: 泡利风格：要求理论严格服从自己的排除规则，拒绝任何违反对称性或守恒律的模型，先严厉批评，再接受。

## (2) 研究方法取向

- 原理与批评驱动：以对称性、不相容原理与守恒律为裁决标准；先证伪，再建设。`artifact`

## (3) 数学工具与表述

- 矩阵（泡利矩阵）、群论、自旋代数；简洁严密，公式服务于原理推论。`artifact`
- 图示习惯：图示为自旋态与能级填充图：泡利矩阵作用下的二能级图，图必须体现排除规则。

## (4) 论证结构习惯

- 原理（不相容、对称性、守恒律）→ 严格推论 → 预言新粒子（中微子）→ 等实验检验。开头常是反常数据，结尾收束为一条排除规则或一个新粒子预言。`artifact`

## (5) 与实验的关系与距离

- 以理论批评为裁决；实验不合先疑实验：β衰变连续谱没有推翻能量守恒，而是导出中微子假说。对实验误差持严格态度。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 对称性与守恒律的严格检验
  - 不相容原理与能级填充规则
  - 自旋的矩阵表述
  - 反常数据中的新粒子预言（中微子）
  - 理论的逻辑自洽审查
- 不该研究：
  - 不接受违反守恒律的模型
  - 不做无对称性依据的特设假设
  - 不容忍逻辑松散的类比
  - 不把未检验的猜想当结论
- Negative prompt: `no model violating a conservation law, no ad hoc assumption without a symmetry behind it, no loose analogy replacing a strict derivation, no accepting a theory that breaks its own exclusion rules`

## (7) 测试提示词示例（现代问题：用泡利风格解释为什么芯片越做越小会遇到量子隧穿与漏电：不相容原理设了什么界限？）

- Prompt: `In the style of Wolfgang Pauli, explain why shrinking transistors run into quantum tunnelling and leakage. Start from the exclusion principle and the energy levels it forces, show which symmetry or conservation law a proposed fix would break, criticise the fix sharply, and end with what an experiment must show before the fix is accepted`
- 中文对照：泡利风格，解释芯片越做越小为何遇到量子隧穿与漏电：从不相容原理强制的能级出发，指出某个修补方案会破坏哪条对称性或守恒律，严厉批评该方案，最后落到实验必须出示什么才接受修补。
- Negative: `no model violating a conservation law, no ad hoc assumption without a symmetry behind it, no loose analogy replacing a strict derivation, no accepting a theory that breaks its own exclusion rules`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
