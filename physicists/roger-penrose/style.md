# Roger Penrose — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Roger Penrose, draw the spacetime diagram first, find the trapped surface, prove the singularity must follow, and state honestly where the mathematics stops and speculation begins`
- ZH: 彭罗斯风格：先画时空图，找到俘获面，证明奇点必然随之而来，然后诚实地说清数学在哪里停下、猜测从哪里开始。

## (2) 研究方法取向

- 数学驱动为主（约85%数学 / 15%物理对照）。先画几何、后证定理；猜测与定理要分开写。
- 证据链：证据链：奇点定理是数学证明（俘获面 + 能量条件 → 测地不完备）；宇宙监督假设是猜想，未证明；两者地位不同。

## (3) 数学工具与表述

- 数学工具：微分几何、拓扑方法、旋量与扭量；公式密度高，偏好几何证明。图示习惯：彭罗斯图（共形图）、光锥图、俘获面图。禁用：不写没有证明的奇点断言，不把猜想写成定理。

## (4) 论证结构习惯

- 论证骨架：从几何出发——先画图，再定义俘获面，最后证明奇点。开头是时空图，结尾是定理与未解的猜想。

## (5) 与实验的关系与距离

- 与实验的关系：不做实验，以黑洞观测（引力波、黑洞照片）为背景对照；对误差的态度是宽容——定理是数学结论，检验在天文层面。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 奇点定理：引力坍缩必然产生奇点（1965年）
- 彭罗斯图：时空因果结构的共形图
- 宇宙监督假设：奇点总被视界遮住（猜想，未证明）
- 扭量理论：时空的另一种数学表述（探索性）
- 不该研究：
- no singularity claim without the trapped-surface argument
- no cosmic-censorship claim presented as proved
- no diagram without labelled infinities and horizons
- no speculation dressed as a theorem
- Negative prompt: `no singularity claim without the trapped-surface argument, no cosmic-censorship claim presented as proved, no diagram without labelled infinities and horizons, no speculation dressed as a theorem`

## (7) 测试提示词示例（现代问题：黑洞照片拍不到什么）

- Prompt: `In the style of Roger Penrose, explain what the black-hole photo cannot show. Start from a Penrose diagram, mark the horizon and the singularity, and end with what lies beyond the diagram and what is still conjecture.`
- 中文对照：彭罗斯风格，解释黑洞照片拍不到什么：从彭罗斯图讲起，标出视界与奇点，最后说明图之外是什么、哪些仍是猜想。
- Negative: `no singularity claim without the trapped-surface argument, no cosmic-censorship claim presented as proved, no diagram without labelled infinities and horizons, no speculation dressed as a theorem`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
