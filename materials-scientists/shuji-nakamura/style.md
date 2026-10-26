# Shuji Nakamura — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Shuji Nakamura: take the material everyone abandoned, fix the crystal growth first with a buffer layer, solve p-type doping by annealing, and let a bright blue LED end the argument`
- ZH: 中村修二方法：接手人人放弃的材料，先用缓冲层解决晶体生长，再用退火解决 p 型掺杂，让一颗明亮的蓝光 LED 终结争论。

## (2) 合成路线偏好

- MOCVD 生长 GaN：低温 AlN 缓冲层先长、再高温生长 GaN；Mg 掺杂后热退火激活 p 型；生长温度、缓冲层厚度、退火条件是关键窗口。

## (3) 表征手段组合

- 先看晶体质量（XRD、TEM、表面形貌），再测电学（p 型确认）与发光；p 型激活与否是核心判据：退火前后电阻与发光对比。

## (4) 理论模型与图表风格

- 宽禁带半导体发光模型：用能带图与缺陷模型解释 GaN 难长、难掺杂；图表以 XRD 半峰宽 + 发光谱 + I-V 曲线为主；论证靠“缓冲层前后晶体质量对比”。

## (5) 性能指标与取舍

- 优先保住蓝光亮度与 p-n 结发光，牺牲生长简便性：两步生长法工艺繁琐但换来可用晶体；保住量产可行性，牺牲实验室小样品的完美性。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先解决晶体生长：缓冲层 + 两步生长法；用退火激活 Mg 掺杂的 p 型 GaN；生长后先测晶体质量再做器件；以高亮度蓝光 LED 作最终判据；把同一 GaN 工艺从 LED 推广到激光器。
- 不该做：不做无缓冲层的 GaN 直接生长；不跳过 p 型确认直接做 LED；不把弱发光样品当作蓝光 LED；不以小样品结果冒充量产可行；不脱离晶体质量谈发光效率。
- Negative prompt: `no direct GaN growth without a buffer layer, no LED without confirmed p-type doping, no weak emission presented as a blue LED, no small-sample results presented as mass production, no efficiency claims without crystal quality data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性蓝光发光材料）

- Prompt: `In the method of Shuji Nakamura, design a flexible blue light-emitting material for a wearable device. Fix crystal growth first with a buffer layer, activate p-type doping by annealing, verify crystal quality before making the device, and let a bright blue LED end the argument.`
- 中文对照：用中村修二的方法，为可穿戴设备设计一种柔性蓝光发光材料：先用缓冲层解决晶体生长，再用退火激活 p 型掺杂，先验证晶体质量再做器件，让明亮的蓝光 LED 终结争论。
- Negative: `no direct GaN growth without a buffer layer, no LED without confirmed p-type doping, no weak emission presented as a blue LED, no small-sample results presented as mass production, no efficiency claims without crystal quality data`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
