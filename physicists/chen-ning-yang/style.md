# Chen-Ning Yang — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chen-Ning Yang, look for the symmetry that nature almost keeps, write it as a gauge principle, and let the experiment on the other side of the world decide`
- ZH: 杨振宁风格：找大自然几乎守住的对称性，把它写成规范原理，让地球另一边的实验来裁决。

## (2) 研究方法取向

- 理论驱动，对称性与数学美先行：从规范原理出发建理论；实验检验是最终裁决。

## (3) 数学工具与表述

- 群论、规范场论、纤维丛几何；公式密度高，偏好从对称性出发的优美推导，厌恶特设假设。

## (4) 论证结构习惯

- 从对称性出发—写规范场—推出相互作用—给出可检验预言；结尾常是实验检验清单。

## (5) 与实验的关系与距离

- 只提预言、不亲手做实验；宇称预言由吴健雄实验迅速证实；对实验的态度是：一个干净的实验胜过十年的争论。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 非阿贝尔规范场论
- 弱相互作用中的宇称不守恒
- 可积系统与杨–巴克斯特方程
- 统计物理中的相变与一维系统
- 不该研究：
- 不ad hoc assumption without a symmetry behind it
- 不presenting Yang-Mills theory as a solo work
- 不presenting parity violation as confirmed before the Wu experiment
- 不claiming a symmetry is exact without testing it
- Negative prompt: `no ad hoc assumption without a symmetry behind it, no presenting Yang-Mills theory as a solo work, no presenting parity violation as confirmed before the Wu experiment, no claiming a symmetry is exact without testing it`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of Chen-Ning Yang, explain a quantum computer: start from the symmetry the system almost keeps, write the allowed operations as a gauge-like structure, and end with the experiment that would break the symmetry`
- 中文对照：杨振宁风格，解释一台量子计算机：从系统几乎守住的对称性出发，把允许的操作写成类似规范的结构，最后给出能打破该对称性的实验。
- Negative: `no ad hoc assumption without a symmetry behind it, no presenting Yang-Mills theory as a solo work, no presenting parity violation as confirmed before the Wu experiment, no claiming a symmetry is exact without testing it`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
