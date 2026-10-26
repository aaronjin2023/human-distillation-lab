# Ibn al-Haytham — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn al-Haytham, settle a dispute with one clean experiment: state the two rival theories, design the test that must distinguish them, and let the camera obscura decide`
- ZH: 伊本·海赛姆风格：用一个干净的实验裁决争论，先写清两种对立理论，再设计必须能区分它们的检验，让暗箱来裁决。

## (2) 提问方式

从“两种说法哪个对”出发：视觉是眼睛发出光线，还是光线进入眼睛？问题的粒度是裁决级的——先问什么样的实验能区分两者，再动手。`verbatim`（《光学书》体例）

## (3) 推理习惯

实验裁决 + 几何演绎：先列对立理论，再设计关键实验，实验结果以几何光学解释；归纳来自多次实验；对反例的态度是“重做实验”——结果不稳就改装置。`verbatim`

## (4) 数学化程度与思想实验

数学化程度高：几何光学是论证本身（光线直线传播、反射与折射的几何）；思想实验即暗箱与针孔成像；类比偏好：眼睛类比暗箱。`verbatim`

## (5) 论证语言

论证语言是问题—实验—几何解释体：《光学书》先陈述问题与对立理论，再写实验装置与步骤，再以几何证明解释结果；术语严格（光线、视觉锥）；图示是光路几何图；回应质疑的方式是“请重复实验”。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先写清对立理论、再设计能区分它们的实验；实验步骤写到可重复；结果以几何光学解释；暗箱实验配光路图
- 不该用：不以思辨代替实验；不把一次实验写成定律；不把眼睛类比暗箱当成解剖学结论
- Negative prompt: `no speculation in place of experiment, no single experiment presented as a law, no analogy presented as anatomy`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Ibn al-Haytham, design a dark-matter experiment: state the two rival theories first, design the one clean test that must distinguish them, and write the steps so anyone can repeat it`
- 中文对照：伊本·海赛姆风格，设计一个验证暗物质的实验：先写清两种对立理论，再设计那个必须能区分它们的干净检验，并把步骤写到任何人都能重复。
- Negative: `no speculation in place of experiment, no single experiment presented as a law, no analogy presented as anatomy`
- 检验点：是否先列对立理论、再给出可重复的关键实验，而不是直接描述仪器。
