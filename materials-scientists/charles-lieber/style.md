# Charles Lieber — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Charles Lieber, grow a nanowire with controlled diameter and doping, assemble it into a device, and let the device meet biology on the nanoscale`
- ZH: 利伯方法：先生长直径与掺杂可控的纳米线，再组装成器件，让器件在纳米尺度上与生物相遇。

## (2) 合成路线偏好

- 气—液—固（VLS）生长半导体纳米线：金催化剂、硅烷前驱体、掺杂气体；关键是直径由催化剂尺寸定，掺杂由气流比定。

## (3) 表征手段组合

- 电镜看直径与形貌，电学输运看迁移率与开关比，扫描探针看界面；先看单根纳米线的本征性能，再谈组装器件。

## (4) 理论模型与图表风格

- 一维输运与能带模型；图表偏好纳米线电镜图与晶体管转移特性曲线，器件示意图只作辅助。

## (5) 性能指标与取舍

- 优先保住纳米线的直径均匀性与掺杂可控性，牺牲生长通量；宁愿产量低，也不要直径失控。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 用催化剂尺寸定纳米线直径，用气流比定掺杂
- 单根纳米线先测输运再组装器件
- 用转移特性曲线报告开关比与迁移率
- 分层组装：合成—表征—组装—器件测试
- 生物接口先做体外验证再谈体内应用
- 不该做：
- no device claims from uncharacterized nanowires
- no averaging over uncontrolled diameters
- no biological-interface claims without in vitro validation
- no presenting ensemble data as single-wire properties
- no skipping doping calibration
- Negative prompt: `no device claims from uncharacterized nanowires, no averaging over uncontrolled diameters, no biological-interface claims without in vitro validation, no presenting ensemble data as single-wire properties, no skipping doping calibration`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Charles Lieber, design a flexible conductive material for a wearable device. Grow nanowires with controlled diameter and doping, verify single-wire transport first, then assemble them into a flexible device and measure it.`
- 中文对照：利伯方法，为可穿戴设备设计柔性导电材料：先生长直径与掺杂可控的纳米线，先测单根输运，再组装成柔性器件并实测。
- Negative: `no device claims from uncharacterized nanowires, no averaging over uncontrolled diameters, no biological-interface claims without in vitro validation, no presenting ensemble data as single-wire properties, no skipping doping calibration`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
