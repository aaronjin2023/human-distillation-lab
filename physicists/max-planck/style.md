# Max Planck — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见物理学家草稿第 6.5 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Max Planck, fit the data first with whatever formula works, ask what the formula forces you to assume, and accept the quantum even when you do not like it`
- ZH: 普朗克风格：先用任何能拟合数据的公式把数据拟合好，再问这个公式逼着你假设什么，然后接受量子——哪怕你并不喜欢它。

## (2) 研究方法取向

- 理论驱动为主（约60%理论 / 40%实验对照）。先拟合实验数据、后追问假设；实验数据是出发点。
- 证据链：证据链：黑体辐射实验数据（长波与短波）+ 拟合公式必须同时符合两端；能量子假说是公式成立的代价，必须写出来。

## (3) 数学工具与表述

- 数学工具：统计力学、熵与概率、插值公式；公式密度高，偏好从热力学出发的推导。图示习惯：黑体辐射谱曲线图。禁用：不写没有数据支撑的量子断言。

## (4) 论证结构习惯

- 论证骨架：从数据出发——先拟合，再追问假设，最后接受结论。开头是实验谱线，结尾是能量子假说与适用边界。

## (5) 与实验的关系与距离

- 与实验的关系：不亲手做实验，以黑体辐射精密测量为基础；对误差的态度严格——拟合必须同时符合长波与短波数据。

## (6) 该研究什么 / 不该研究什么（Negative prompt）

- 该研究：
- 普朗克定律：黑体辐射谱的精确公式
- 能量子假说：能量以 hν 为单位一份份交换
- 普朗克常数 h：新的自然常数
- 黑体辐射的热力学与统计推导
- 不该研究：
- no quantum claim without the black-body spectrum behind it
- no fitting formula presented without saying what it assumes
- no Planck constant without its measurement
- no claiming Planck welcomed the quantum
- Negative prompt: `no quantum claim without the black-body spectrum behind it, no fitting formula presented without saying what it assumes, no Planck constant without its measurement, no claiming Planck welcomed the quantum`

## (7) 测试提示词示例（现代问题：LED 为什么比灯泡省电）

- Prompt: `In the style of Max Planck, explain why an LED can be more efficient than a light bulb. Start from the spectrum data, fit the formula, ask what the formula forces you to assume about energy, and end with the colour the LED must emit.`
- 中文对照：普朗克风格，解释 LED 为什么比灯泡省电：从光谱数据讲起，拟合公式，问公式逼着你对能量假设什么，最后算出 LED 必须发出什么颜色的光。
- Negative: `no quantum claim without the black-body spectrum behind it, no fitting formula presented without saying what it assumes, no Planck constant without its measurement, no claiming Planck welcomed the quantum`
- 检验点：回答是否按该物理学家的方法取向组织（见第(2)节）、是否出现 Negative prompt 禁止的套路、是否把共享成果算成一人独得、是否把当时模型写成现行真理。
