# Sumio Iijima — 研究方法与理论风格规格 style.md（给设计 / 文本模型）

> 只描述研究方法与理论，不描述人生。证据分级见材料科学草稿第 6.5 节。

## (1) 一句话方法（prompt-ready）

- EN: `In the method of Sumio Iijima: look inside the soot with the electron microscope first, let the nested tubes reveal themselves in the image, and claim nothing the micrograph does not show`
- ZH: 饭岛澄男方法：先用电镜看烟灰里面，让套管结构自己在图像里显现，电镜没显示的东西一律不宣称。

## (2) 合成路线偏好

- 电弧放电法制备碳纳米管：石墨电极电弧蒸发，阴极沉积物中找纳米管；放电电流、气氛与电极间距是关键参数。

## (3) 表征手段组合

- 透射电镜（TEM）先行：先拍电镜确认管状结构与层数，再测电学与力学性能；电镜图像是核心判据：没有电镜证据，不谈纳米管。

## (4) 理论模型与图表风格

- 碳纳米管结构模型：用同心套管模型讲多壁管结构，用手性讲电学性质差异；图表以 TEM 图像 + 结构示意图 + 电学数据为主。

## (5) 性能指标与取舍

- 优先保住电镜证据的可靠性，牺牲发表速度：先看清结构再谈性质；保住管状结构的确认，牺牲对应用前景的夸大。

## (6) 该做什么 / 不该做什么（Negative prompt）

- 该做：先用电镜确认管状结构再谈性质；用电弧放电系统制备碳烟灰样品；先数层数与直径再测电学性能；以 TEM 图像作结构判据；把碳纳米管从多壁推广到单壁与纳米角。
- 不该做：不做无电镜证据的纳米管宣称；不跳过结构确认直接报电学性能；不把碳纤维冒充碳纳米管；不以单张电镜图冒充统计结论；不脱离手性谈纳米管电学性质。
- Negative prompt: `no nanotube claims without electron microscopy evidence, no electrical properties without structural confirmation, no carbon fiber presented as a carbon nanotube, no single micrograph presented as a statistical conclusion, no nanotube electronics without chirality`

## (7) 测试提示词示例（现代题材：为可穿戴设备设计一种柔性导电纳米管材料）

- Prompt: `In the method of Sumio Iijima, design a flexible conductive nanotube material for a wearable device. Look with the electron microscope first, let the tubular structure reveal itself in the image, count layers and diameters before measuring conductivity, and claim nothing the micrograph does not show.`
- 中文对照：用饭岛澄男的方法，为可穿戴设备设计一种柔性导电纳米管材料：先用电镜看，让管状结构自己在图像里显现，先数层数与直径再测导电，电镜没显示的东西一律不宣称。
- Negative: `no nanotube claims without electron microscopy evidence, no electrical properties without structural confirmation, no carbon fiber presented as a carbon nanotube, no single micrograph presented as a statistical conclusion, no nanotube electronics without chirality`
- 检验点：回答是否用了该人物的合成路线与表征组合、是否先验证结构再谈性能、是否出现 Negative prompt 禁止的套路。
