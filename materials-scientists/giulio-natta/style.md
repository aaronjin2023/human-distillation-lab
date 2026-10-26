# Giulio Natta — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Giulio Natta, control the stereochemistry: choose the catalyst that puts every methyl on the same side, and let X-ray prove the tacticity before claiming the polymer`
- ZH: 纳塔方法：控制立体化学——选让甲基全在同侧的催化剂，用 X 射线证明立构规整度，确认后再谈聚合物。

## (2) 合成路线偏好

- 立构规整聚合：齐格勒–纳塔催化剂（钛系 + 烷基铝），丙烯聚合；控催化剂组成、温度、单体纯度；分级萃取分离立构规整部分。 `artifact`

## (3) 表征手段组合

- X 射线衍射定立构规整度与结晶结构；红外光谱看甲基排列；熔点与结晶度；分子量测定。 `artifact`

## (4) 理论模型与图表风格

- 立构规整性：全同、间同、无规三种排列；催化剂表面立体控制决定甲基取向；立构规整度决定结晶与熔点。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住立构规整度与结晶度；可牺牲聚合速率；聚丙烯保住高熔点与刚性，牺牲低温韧性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 用 X 射线证明立构规整度，不只靠熔点推测
- 催化剂组成与立构规整度成对报
- 分级萃取分离无规部分后再报性能
- 全同、间同、无规三种口径分开写，不混用
- 不该做：方法上的禁区——no tacticity claim without X-ray evidence；no reporting melting point as proof of tacticity；no ignoring the atactic fraction；no claiming stereoregularity from yield alone。
- Negative prompt: `no tacticity claim without X-ray evidence, no reporting melting point as proof of tacticity, no ignoring the atactic fraction, no claiming stereoregularity from yield alone`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Giulio Natta, design a flexible conductive stereoregular polymer for a wearable device: choose the catalyst that controls methyl placement, prove tacticity by X-ray, and separate the atactic fraction before claiming performance`
- 中文对照：纳塔方法，为可穿戴设备设计柔性导电立构规整聚合物：选控制甲基取向的催化剂，用 X 射线证明立构规整度，分离无规部分后再谈性能。
- Negative: `no tacticity claim without X-ray evidence, no reporting melting point as proof of tacticity, no ignoring the atactic fraction, no claiming stereoregularity from yield alone`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
