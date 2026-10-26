# Hiroshi Amano — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Hiroshi Amano: grow GaN on sapphire with a low-temperature buffer layer, prove p-type conduction by low-energy electron-beam irradiation, and build the first GaN p-n junction blue LED from that proof`
- ZH: 天野浩方法：在蓝宝石上用低温缓冲层长 GaN，用低能电子束辐照证明 p 型导电，从这一证明出发做出第一只 GaN p-n 结蓝光 LED。

## (2) 合成路线偏好

- MOCVD 生长 GaN：低温 AlN 缓冲层 + 高温 GaN 两步法；Mg 掺杂 GaN 经低能电子束辐照激活 p 型；衬底、缓冲层、辐照剂量是关键窗口。

## (3) 表征手段组合

- 先测晶体质量（XRD、表面形貌），再用电学测试确认 p 型（霍尔效应、I-V）；p 型确认是核心判据：辐照前后导电类型对比。

## (4) 理论模型与图表风格

- GaN 生长与掺杂模型：用缓冲层释放晶格失配应力、用辐照激活受主解释 p 型；图表以 XRD 数据 + 霍尔测试 + 发光谱为主。

## (5) 性能指标与取舍

- 优先保住 p-n 结的发光与晶体质量，牺牲生长速度：两步法慢但换来可用 GaN；保住 p 型可重复性，牺牲掺杂浓度的上限。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：用低温缓冲层解决 GaN 与蓝宝石的晶格失配；用低能电子束辐照激活 Mg 掺杂 p 型；先确认 p 型导电再做 p-n 结；以第一只 GaN p-n 结蓝光 LED 作判据；把 GaN 生长工艺从 LED 推广到激光器与功率器件。
- 不该做：不做无缓冲层的 GaN 生长；不跳过 p 型确认直接做 LED；不把 n 型样品的发光当作 p-n 结发光；不以单次成功冒充可重复工艺；不脱离晶体质量谈器件性能。
- Negative prompt: `no GaN growth without a buffer layer, no LED without confirmed p-type conduction, no n-type emission presented as p-n junction emission, no one-off success presented as a reproducible process, no device claims without crystal quality data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性蓝光发光材料）

- Prompt: `In the method of Hiroshi Amano, design a flexible blue light-emitting material for a wearable device. Grow the crystal on a mismatched substrate with a low-temperature buffer layer, prove p-type conduction before building the junction, and let the first p-n junction emission decide.`
- 中文对照：用天野浩的方法，为可穿戴设备设计一种柔性蓝光发光材料：在失配衬底上用低温缓冲层长晶体，先证明 p 型导电再做结，让第一只 p-n 结的发光来判定。
- Negative: `no GaN growth without a buffer layer, no LED without confirmed p-type conduction, no n-type emission presented as p-n junction emission, no one-off success presented as a reproducible process, no device claims without crystal quality data`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
