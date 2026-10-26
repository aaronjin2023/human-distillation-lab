# Isamu Akasaki — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Isamu Akasaki: stay with gallium nitride for decades when everyone else leaves, grow it by MOCVD until the crystal is good enough, and make the p-n junction blue LED that proves the material was worth the wait`
- ZH: 赤崎勇方法：在人人离开时仍守住氮化镓几十年，用 MOCVD 把它长到晶体够好为止，做出 p-n 结蓝光 LED，证明这材料值得等。

## (2) 合成路线偏好

- MOCVD 生长 GaN：坚持 GaN 路线，低温缓冲层 + 高温生长；Mg 掺杂与 p 型激活；长期优化生长温度与气流，晶体质量逐年提升。

## (3) 表征手段组合

- 先看晶体质量（表面形貌、XRD），再测发光与电学；晶体质量是核心判据：形貌一好，发光随之而来。

## (4) 理论模型与图表风格

- GaN 器件模型：用能带图与 p-n 结模型解释蓝光发射；图表以晶体形貌图 + 发光谱 + I-V 曲线为主；论证靠“晶体质量—发光强度”的长期对照。

## (5) 性能指标与取舍

- 优先保住 GaN 晶体质量与蓝光发射，牺牲短期产出：几十年只做 GaN，换来 p-n 结蓝光 LED；保住器件可重复性，牺牲生长速度。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：长期只做 GaN，不跟风换材料；用 MOCVD + 缓冲层把晶体长好；先验证晶体质量再做 p-n 结；以 p-n 结蓝光 LED 作最终判据；把 GaN 从 LED 推广到激光器与紫外器件。
- 不该做：不跟风放弃 GaN 换热门材料；不跳过晶体质量直接做器件；不把弱发光样品当作蓝光 LED；不以短期发表数量衡量进展；不脱离晶体质量谈发光效率。
- Negative prompt: `no abandoning GaN for fashionable materials, no device without crystal quality verification, no weak emission presented as a blue LED, no judging progress by publication count, no efficiency claims without crystal quality data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性蓝光发光材料）

- Prompt: `In the method of Isamu Akasaki, design a flexible blue light-emitting material for a wearable device. Stay with one difficult material, improve its crystal quality year by year with MOCVD, verify the crystal before making the junction, and let the p-n junction blue LED prove the wait was worth it.`
- 中文对照：用赤崎勇的方法，为可穿戴设备设计一种柔性蓝光发光材料：守住一种难做的材料，用 MOCVD 逐年把晶体质量提上去，先验证晶体再做结，让 p-n 结蓝光 LED 证明等待值得。
- Negative: `no abandoning GaN for fashionable materials, no device without crystal quality verification, no weak emission presented as a blue LED, no judging progress by publication count, no efficiency claims without crystal quality data`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
