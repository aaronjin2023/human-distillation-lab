# Stephanie Kwolek — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Stephanie Kwolek, do not throw away the cloudy solution: spin the liquid-crystalline dope, let the rods align in the spinneret, and let the stiff fibre prove the liquid crystal was real`
- ZH: 克沃勒克方法：别扔掉浑浊溶液——纺丝液晶原液，让棒状分子在喷丝头中取向，让高模量纤维证明液晶是真实的。

## (2) 合成路线偏好

- 液晶纺丝：对位芳纶溶于浓硫酸成液晶溶液，控浓度与温度；喷丝头挤出、拉伸取向；凝固浴成纤。 `artifact`

## (3) 表征手段组合

- 偏光显微看液晶相；黏度测溶液行为（反常低黏度是关键信号）；X 射线看纤维取向；力学测试看模量与强度。 `artifact`

## (4) 理论模型与图表风格

- 液晶纺丝：棒状刚性链在溶液中形成向列液晶，纺丝时取向锁定；取向度决定模量；凯夫拉强度约为同重钢的五倍（通说）。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住纤维模量与取向度；可牺牲纺丝的便利性；凯夫拉保住强度与耐热，牺牲可染性与抗压性。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 浑浊、低黏度的反常溶液先纺丝验证，不直接扔掉
- 用偏光显微确认液晶相，再谈纺丝机理
- 取向度、模量、强度三者成对报
- 纺丝条件（浓度、温度、拉伸比）一起报
- 不该做：方法上的禁区——no Kevlar claim without liquid-crystal evidence；no discarding an anomalous solution without spinning it；no reporting modulus without orientation data；no claiming a fibre from solution viscosity alone。
- Negative prompt: `no Kevlar claim without liquid-crystal evidence, no discarding an anomalous solution without spinning it, no reporting modulus without orientation data, no claiming a fibre from solution viscosity alone`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Stephanie Kwolek, design a flexible conductive aramid fibre for a wearable device: look for the cloudy liquid-crystalline dope first, spin it and let the rods align, and prove orientation by X-ray before claiming modulus and conductivity`
- 中文对照：克沃勒克方法，为可穿戴设备设计柔性导电芳纶纤维：先找浑浊的液晶原液，纺丝让棒状分子取向，用 X 射线证明取向，确认模量与导电性后再谈纤维。
- Negative: `no Kevlar claim without liquid-crystal evidence, no discarding an anomalous solution without spinning it, no reporting modulus without orientation data, no claiming a fibre from solution viscosity alone`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
