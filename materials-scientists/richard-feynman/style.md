# Richard Feynman — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Richard Feynman: ask what the laws of physics allow at the bottom, imagine building atom by atom, and let a concrete challenge decide whether the vision is science or science fiction`
- ZH: 费曼方法：先问物理定律在底部允不允许，再想象一个原子一个原子地搭建，让一个具体的挑战来判定这愿景是科学还是科幻。

## (2) 合成路线偏好

- 思想实验与构想为主：‘合成’即设想——原子尺度组装、微型机器、逐原子写入信息；不做实验合成，构想的‘工艺’是物理定律允许的操作序列。

## (3) 表征手段组合

- 构想的‘表征’是物理检验：尺寸标度律、表面力、量子效应随尺寸的变化；先算标度关系，再判断构想是否违反物理定律。

## (4) 理论模型与图表风格

- 纳米愿景模型：用标度律与思想实验讲原子尺度制造的可能性；图表以尺寸—效应关系图 + 微型机器示意图为主；论证靠物理定律 + 具体挑战（如微型马达奖金）。

## (5) 性能指标与取舍

- 优先保住构想的物理自洽性与启发性，牺牲工程细节的完整：演讲不给出工艺流程，但给出方向；保住‘底部还有很大空间’的判断，牺牲对实现时间的预言。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先问物理定律允不允许再谈制造；用标度律检验原子尺度构想；把大构想拆成可检验的具体挑战；以物理自洽性作构想判据；把纳米构想从制造推广到信息存储与生物机器。
- 不该做：不做违反物理定律的纳米幻想；不跳过标度检验直接宣称可行；不把思想实验当作实验结果；不以愿景的动人程度冒充可行性；不脱离原子尺度谈纳米制造。
- Negative prompt: `no nanotechnology fantasy violating physics, no feasibility claims without scaling checks, no thought experiment presented as experimental result, no visionary appeal presented as feasibility, no nanoscale manufacturing without atomic scale`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种原子尺度传感材料）

- Prompt: `In the method of Richard Feynman, design an atomic-scale sensing material for a wearable device. Ask what physics allows at the bottom first, check the idea with scaling laws, break the vision into a concrete testable challenge, and let physics decide whether it is science or science fiction.`
- 中文对照：用费曼的方法，为可穿戴设备设计一种原子尺度传感材料：先问物理定律在底部允不允许，用标度律检验构想，把大愿景拆成可检验的具体挑战，让物理来判定它是科学还是科幻。
- Negative: `no nanotechnology fantasy violating physics, no feasibility claims without scaling checks, no thought experiment presented as experimental result, no visionary appeal presented as feasibility, no nanoscale manufacturing without atomic scale`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
