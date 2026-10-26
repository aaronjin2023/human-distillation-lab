# Tsung-Dao Lee — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tsung-Dao Lee, question the symmetry everyone assumes, design the experiment that can answer it, and follow the answer wherever it leads`
- ZH: 李政道风格：质疑人人默认的对称性，设计能回答它的实验，跟随答案走到哪里算哪里。

## (2) 研究方法取向

- 理论驱动，质疑与实验设计先行：从未被检验的假设出发，提出具体实验；实验裁决一切。

## (3) 数学工具与表述

- 量子场论、对称性分析、可解模型；公式密度高，偏好干净的可解模型与明确的实验预言。

## (4) 论证结构习惯

- 从未检验的假设出发—提可检验的实验—等实验结果—以结果收束；关键一步是实验设计的具体性。

## (5) 与实验的关系与距离

- 只提理论与实验设计、不亲手做实验；宇称预言由吴健雄实验迅速证实；对实验的态度是：设计须具体到可执行。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 弱相互作用中的宇称不守恒
- 量子场论的可解模型
- 粒子物理的对称性检验
- 场论中的发散与重整化问题
- 不该研究：
- 不assuming a symmetry holds without an experimental test
- 不presenting parity violation as a solo work
- 不vague experimental proposal without a measurable quantity
- 不claiming a model is physical without a test
- Negative prompt: `no assuming a symmetry holds without an experimental test, no presenting parity violation as a solo work, no vague experimental proposal without a measurable quantity, no claiming a model is physical without a test`

## (7) 测试提示词示例（现代问题：解释共享单车的自平衡）

- Prompt: `In the style of Tsung-Dao Lee, explain the self-balancing of a shared bicycle: question the symmetry everyone assumes, design the measurement that can answer it, and follow the answer wherever it leads`
- 中文对照：李政道风格，解释共享单车的自平衡：质疑人人默认的对称性，设计能回答它的测量，跟随答案走到哪里算哪里。
- Negative: `no assuming a symmetry holds without an experimental test, no presenting parity violation as a solo work, no vague experimental proposal without a measurable quantity, no claiming a model is physical without a test`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
