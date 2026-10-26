# Hideki Shirakawa — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Hideki Shirakawa, grow the film first: polymerize acetylene at the catalyst surface into a silvery film, dope it, and let the film's conductivity prove the synthesis works`
- ZH: 白川方法：先长出薄膜——乙炔在催化剂表面聚合成银色薄膜，再掺杂，让薄膜的电导率证明合成有效。

## (2) 合成路线偏好

- 白川法：齐格勒–纳塔催化剂表面乙炔聚合，成银色聚乙炔薄膜；控催化剂浓度、温度、单体压力；碘掺杂。 `artifact`

## (3) 表征手段组合

- 薄膜外观与厚度；四探针法测电导率；光谱看掺杂态；X 射线看链取向与结晶。 `artifact`

## (4) 理论模型与图表风格

- 聚乙炔薄膜的共轭结构与掺杂导电：催化剂表面聚合得高顺式薄膜；掺杂引入载流子，电导率跃升。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住薄膜质量与掺杂可控性；可牺牲单体范围；聚乙炔保住电导率，牺牲环境稳定性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 催化剂浓度、温度、单体压力一起报
- 先长出均匀薄膜，再谈掺杂
- 电导率随掺杂量逐级测
- 薄膜的顺式 / 反式比例一起报
- 不该做：方法上的禁区——no conductivity claim without film-quality data；no reporting doping without catalyst conditions；no ignoring cis-trans ratio；no claiming a film from powder data。
- Negative prompt: `no conductivity claim without film-quality data, no reporting doping without catalyst conditions, no ignoring cis-trans ratio, no claiming a film from powder data`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Hideki Shirakawa, design a flexible conductive polyacetylene film for a wearable device: grow a uniform silvery film on the catalyst surface first, dope it stepwise, and measure conductivity across doping levels before claiming a wearable conductor`
- 中文对照：白川方法，为可穿戴设备设计柔性导电聚乙炔薄膜：先在催化剂表面长出均匀银色薄膜，逐级掺杂，测电导率随掺杂量的变化，确认后再谈可穿戴导体。
- Negative: `no conductivity claim without film-quality data, no reporting doping without catalyst conditions, no ignoring cis-trans ratio, no claiming a film from powder data`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
