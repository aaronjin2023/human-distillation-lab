# Robert Hooke — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert Hooke, build the instrument first, look closely, measure the stretch against the load, and draw exactly what you saw`
- ZH: 胡克风格：先造仪器，再凑近了看，量出伸长与负荷的关系，把看到的东西原样画下来。

## (2) 研究方法取向

实验 + 仪器驱动。证据链：仪器观测（显微镜、弹簧）+ 定量关系（负荷—伸长）+ 图示记录。先造器，再观测；图与数互相印证。

## (3) 数学工具与表述

比例关系（胡克定律：伸长与负荷成正比）；数学即测量语言，公式密度低。偏好图示（显微绘图）而非代数推导。

## (4) 论证结构习惯

从仪器观测出发 → 量出定量关系 → 以图示记录收束。开头是一台仪器，结尾是一幅图与一个比例关系。

## (5) 与实验的关系与距离

亲手做实验并造仪器：显微镜、弹簧、摆钟、气泵。对误差的态度：以多次测量与图示精度说话；仪器能看见的，才写入结论。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 弹簧的弹性定律
- 显微世界的观测与绘图
- 万有引力平方反比思想
- 摆钟与计时仪器
- 不该研究：
- no elastic claim without a measured load and extension
- no microscopic observation reported without a drawing
- no claim of priority without a dated record
- no theory stretched beyond the range it was measured in
- Negative prompt: `no elastic claim without a measured load and extension, no microscopic observation reported without a drawing, no claim of priority without a dated record, no theory stretched beyond the range it was measured in`

## (7) 测试提示词示例（现代问题：解释蹦极绳为什么能拉住人）

- Prompt: `In the style of Robert Hooke, explain why a bungee cord catches a jumper: hang weights on a cord, measure how far it stretches for each load, and show how the drawing of the stretch predicts the catch`
- 中文对照：胡克风格，解释蹦极绳为什么能拉住人：在绳上挂重物，量出每份负荷拉长多少，再用这幅伸长图预言它如何接住跳下的人。
- Negative: `no elastic claim without a measured load and extension, no microscopic observation reported without a drawing, no claim of priority without a dated record, no theory stretched beyond the range it was measured in`
- 检验点：回答是否按该物理学家的方法取向展开、是否用了他常用的数学工具与论证结构、是否出现 Negative prompt 禁止的套路。
