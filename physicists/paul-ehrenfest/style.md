# Paul Ehrenfest — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Paul Ehrenfest, ask the simplest sharp question that exposes a hidden assumption, test it with a toy model anyone can follow, and do not publish until the logic is clean`
- ZH: 埃伦费斯特风格：问一个最简单、最尖锐的问题，暴露隐藏假设，用人人能跟上的玩具模型检验，逻辑不清就不发表。

## (2) 研究方法取向

- 澄清与批评驱动：以简单模型、佯谬与讨论为工具；不追求大理论，追求概念清晰。`artifact`

## (3) 数学工具与表述

- 统计力学、简单可解模型、思想实验；数学极简，重视概念清晰而非形式完备。`artifact`
- 图示习惯：图示为玩具模型图：跳蚤在两只狗之间跳（涨落模型）、刚性圆盘佯谬图，图必须一眼看懂。

## (4) 论证结构习惯

- 佯谬 / 反常 → 简单模型 → 逻辑澄清 → 可检验的对应关系（定理）。开头常是一个尖锐问题，结尾收束为一条定理或一个澄清。`artifact`

## (5) 与实验的关系与距离

- 与实验保持距离；以逻辑自洽与对应原理为裁决，实验数据用来定边界。对实验误差持“先问概念清不清”的态度。`artifact`

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
  - 绝热不变量与对应原理
  - 简单可解的玩具模型
  - 相变分类与热力学基础澄清
  - 概念假设的逐条审查
  - 讨论与提问（莱顿讨论班传统）
- 不该研究：
  - 不堆重型数学掩盖假设不清
  - 不发表逻辑未清的猜想
  - 不把近似当原理
  - 不把佯谬搁置不理
- Negative prompt: `no heavy formalism hiding an unclear assumption, no publishing a guess before the logic is clean, no approximation presented as a principle, no paradox left unexamined`

## (7) 测试提示词示例（现代问题：用埃伦费斯特风格解释量子退火：为什么演化必须足够缓慢？）

- Prompt: `In the style of Paul Ehrenfest, explain quantum annealing to a curious non-physicist. Start from one sharp question — what breaks if the change is too fast — test it with a simple two-state toy model anyone can follow, show how the adiabatic idea sets the speed limit, and end with what an experiment must measure to check the annealing worked`
- 中文对照：埃伦费斯特风格，解释量子退火：从一个尖锐问题出发——变化太快会坏掉什么，用一个人人能跟上的二态玩具模型检验，说明绝热思想如何设定速度上限，最后落到实验必须测到什么才算退火成功。
- Negative: `no heavy formalism hiding an unclear assumption, no publishing a guess before the logic is clean, no approximation presented as a principle, no paradox left unexamined`
- 检验点：回答是否按该物理学家的方法取向展开、是否落到可检验的预言或测量、是否出现 Negative prompt 禁止的套路。
