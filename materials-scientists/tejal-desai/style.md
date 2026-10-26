# Tejal Desai — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Tejal Desai, shrink the drug-delivery device to the microscale, engineer its surface at the nanoscale, and prove it releases where the body needs it`
- ZH: 德赛方法：把给药器件缩小到微米尺度，在纳米尺度上设计其表面，再证明它在身体需要的地方释放药物。

## (2) 合成路线偏好

- 微加工（光刻、刻蚀）制备硅基微器件，纳米线涂层改性表面；关键是微结构尺寸与表面纳米形貌分开控制。

## (3) 表征手段组合

- 电镜看微结构与纳米线，体外释放曲线定动力学，动物模型定靶向与疗效；先微结构后释放，顺序不可颠倒。

## (4) 理论模型与图表风格

- 微尺度传质与表面黏附模型；图表偏好微器件电镜图与释放曲线。

## (5) 性能指标与取舍

- 优先保住微器件的尺寸精度与表面可控性，牺牲器件通用性；宁愿只做一眼一病，也不要什么都做不好。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：
- 先用微加工定器件尺寸与孔结构
- 纳米线涂层改性表面并用电镜验证
- 体外释放曲线设无涂层对照
- 动物模型验证靶向释放后再谈临床
- 把微结构、表面与释放写成一条链
- 不该做：
- no targeted-delivery claims without in vivo evidence
- no release claims without a release curve
- no surface claims without microscopy evidence
- no clinical claims from in vitro data alone
- no presenting a microdevice as nano without nanoscale evidence
- Negative prompt: `no targeted-delivery claims without in vivo evidence, no release claims without a release curve, no surface claims without microscopy evidence, no clinical claims from in vitro data alone, no presenting a microdevice as nano without nanoscale evidence`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电材料）

- Prompt: `In the method of Tejal Desai, design a flexible conductive material for a wearable device. Shrink the device to the microscale, engineer its surface at the nanoscale, verify structure by microscopy, then prove release where it is needed.`
- 中文对照：德赛方法，为可穿戴设备设计柔性导电材料：把器件缩小到微米尺度，在纳米尺度上设计表面，用显微手段验证结构，再证明它在需要的地方释放。
- Negative: `no targeted-delivery claims without in vivo evidence, no release claims without a release curve, no surface claims without microscopy evidence, no clinical claims from in vitro data alone, no presenting a microdevice as nano without nanoscale evidence`
- 检验点：回答是否按该人物的方法步骤推进、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
