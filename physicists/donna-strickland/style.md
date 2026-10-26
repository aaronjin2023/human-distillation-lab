# Donna Strickland — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见 physicists 草稿第 6.5 节；未使用 `verbatim`。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Donna Strickland, stretch the pulse before you amplify it, compress it only at the end, and let the peak power speak for the method`
- ZH: 斯特里克兰风格：放大之前先把脉冲拉伸，只在最后压缩，让峰值功率为方法说话。

## (2) 研究方法取向

- 实验驱动，技术先行：从啁啾脉冲放大出发，解决放大器损伤问题；峰值功率是裁决。

## (3) 数学工具与表述

- 数学化程度中等：以脉冲宽度、峰值功率、色散补偿为证据；不以方程论证，靠激光参数说话。

## (4) 论证结构习惯

- 从放大器损伤出发—拉伸脉冲—放大—压缩—以峰值功率收束；论证靠可重复的激光参数。

## (5) 与实验的关系与距离

- 亲手做实验；对误差严格：脉冲压缩须可重复、峰值功率须实测，否则不算技术突破。

## (6) 该研究什么 / 不该研究什么（负面清单）

- 该研究：
- 啁啾脉冲放大技术
- 超快激光脉冲的产生与压缩
- 强场激光与物质相互作用
- 激光放大器的损伤控制
- 不该研究：
- 不claiming a peak power without a measured pulse duration
- 不presenting chirped pulse amplification as a solo work
- 不amplifying without stretching first
- 不skipping the damage threshold in a laser claim
- Negative prompt: `no claiming a peak power without a measured pulse duration, no presenting chirped pulse amplification as a solo work, no amplifying without stretching first, no skipping the damage threshold in a laser claim`

## (7) 测试提示词示例（现代问题：解释一台量子计算机）

- Prompt: `In the style of Donna Strickland, explain a quantum computer: stretch the problem out before you amplify the signal, compress the answer only at the end, and let the measured result speak for the method`
- 中文对照：斯特里克兰风格，解释一台量子计算机：放大信号之前先把问题拉伸，只在最后压缩答案，让测到的结果为方法说话。
- Negative: `no claiming a peak power without a measured pulse duration, no presenting chirped pulse amplification as a solo work, no amplifying without stretching first, no skipping the damage threshold in a laser claim`
- 检验点：回答是否按该物理学家的方法取向组织、是否出现 Negative prompt 禁止的套路、是否把未证实的内容写成已证实。
