# Sossina M. Haile — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学家草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Sossina Haile, find the superprotonic transition first: map the phase change, measure the jump in proton conductivity, and build the fuel cell only after the electrolyte survives device conditions`
- ZH: 海尔方法：先找到超质子相变——画清相变，测质子电导率的跃升，电解质经得住器件条件后再做燃料电池。

## (2) 合成路线偏好

- 固相合成与溶液法制备固体酸：CsH2PO4 粉末合成、压片成型；薄膜电解质制备；电极复合与电池组装，控湿度与温度窗口。 `artifact`

## (3) 表征手段组合

- XRD 看相变与结构；阻抗谱测质子电导率随温度的跃升；DSC 测相变温度；电化学测试看电池极化与耐久性。 `artifact`

## (4) 理论模型与图表风格

- 超质子导电：高温无序相中氧阴离子重取向与氢键网络动态无序，质子电导率跃升 3–5 个数量级，活化能降至约 0.35 eV；CsH2PO4 兼具氧化还原稳定性。 `artifact`
- 图表偏好：相图 / 能带图 / 性能曲线 / 显微图像，按人物习惯选用；论证靠数据与模型，不靠修辞。`impression`

## (5) 性能指标与取舍

- 优先保住质子电导率与化学稳定性；可牺牲工作温度窗口的宽容度；器件保住耐久性，牺牲峰值功率。 `artifact`

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先测相变温度与电导率跃升，再谈燃料电池
- 用阻抗谱分开体电导与界面极化，不混为一谈
- 在器件相关气氛下测稳定性，不只测惰性气氛
- 化学掺杂微调相行为时，逐项报电导率变化
- 不该做：方法上的禁区——no fuel-cell claim without superprotonic conductivity data；no reporting conductivity without temperature and humidity；no ignoring chemical stability in device-relevant atmospheres；no claiming durability from a short test。
- Negative prompt: `no fuel-cell claim without superprotonic conductivity data, no reporting conductivity without temperature and humidity, no ignoring chemical stability in device-relevant atmospheres, no claiming durability from a short test`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Sossina Haile, design a flexible proton-conducting membrane for a wearable device: find the superprotonic transition first, measure the conductivity jump by impedance spectroscopy, and prove stability in humid device conditions before claiming a fuel cell`
- 中文对照：海尔方法，为可穿戴设备设计柔性质子导电膜：先找到超质子相变，用阻抗谱测电导率跃升，在潮湿器件条件下验证稳定性，确认后再谈燃料电池。
- Negative: `no fuel-cell claim without superprotonic conductivity data, no reporting conductivity without temperature and humidity, no ignoring chemical stability in device-relevant atmospheres, no claiming durability from a short test`
- 检验点：回答是否按该人物的方法路线走、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
