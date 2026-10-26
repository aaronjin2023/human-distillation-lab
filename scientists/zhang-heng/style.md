# Zhang Heng — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Heng, make the heavens into a working instrument: observe the sky, build a machine that turns with it, and let the instrument's reading settle the argument`
- ZH: 张衡风格：把天象做成能运转的仪器，观天、造器、让仪器的读数来裁决争论。

## (2) 提问方式

从“怎么测、怎么报”出发：地震从哪个方向来？浑天怎么转？问题的粒度是仪器级的——先问能不能做出来、报得准，再问宇宙论怎么说。`artifact`（《后汉书·张衡传》）

## (3) 推理习惯

观测 + 制器互证：仪器是理论的物化，仪器的读数反过来检验理论；演绎少、实证多；对反例的态度是“改仪器”——读数不准就改机械结构。`artifact`

## (4) 数学化程度与思想实验

数学化程度中等：浑象运转靠齿轮与漏水驱动的计算，历法推算用算术；思想实验少，更多是“造出来试试”；类比偏好：浑天类比鸡蛋（浑天说：天如鸡子）。`artifact`（《灵宪》浑天说）

## (5) 论证语言

论证语言是史传 + 赋体 + 仪器说明的混合：《灵宪》以散文立论，仪器以《后汉书》记载的构造说明传世；术语多取《周髀》《灵宪》传统；图示靠后人复原图，非原图。`artifact`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先观测、再制器、用仪器的读数检验理论；仪器构造写清到可复原；天文、地震、机械三线互相印证
- 不该用：不把仪器传说当成仪器实测；不把后人复原图当成原图；不以宇宙论的文采代替仪器的读数
- Negative prompt: `no legend presented as measurement, no later reconstruction presented as the original, no cosmology in place of an instrument reading`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Zhang Heng, design a dark-matter experiment: build an instrument that must turn and read by itself, state in advance which direction and magnitude it should report, and let the instrument's reading settle the question`
- 中文对照：张衡风格，设计一个验证暗物质的实验：造一台必须自己运转、自己读数的仪器，事先写清它应当报出哪个方向、多大读数，让仪器的读数来裁决问题。
- Negative: `no legend presented as measurement, no later reconstruction presented as the original, no cosmology in place of an instrument reading`
- 检验点：是否先定仪器的预报读数、再谈理论，而不是只谈理论模型。
