# Ptolemy — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。证据分级见草稿第 5.2 节。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ptolemy, save the phenomena with geometry: take long tables of observations, fit them with circles upon circles, and judge a model by whether it predicts positions, not by whether it is physically true`
- ZH: 托勒密风格：用几何拯救现象，拿长期观测表，用本轮均轮一层层拟合，以能否算出天体位置评判模型，而不问它物理上是否为真。

## (2) 提问方式

从“怎么算准”出发：行星为什么有时逆行？月亮位置怎么预报？问题的粒度是计算级的——先问模型能否复现观测表，再问模型是否简洁。`verbatim`（《天文学大成》体例）

## (3) 推理习惯

几何演绎 + 数据拟合：观测表是证据，几何模型是解释；以预测精度为评判标准；对反例的态度是“加一层轮”——模型靠增加本轮与偏心圆吸收反例，直到算准为止。`verbatim`

## (4) 数学化程度与思想实验

数学化程度极高：球面几何、弦表（三角学的先声）、本轮—均轮体系；思想实验即几何模型本身；类比偏好：天体运动类比匀速圆周运动的组合。`verbatim`

## (5) 论证语言

论证语言是手册体：《天文学大成》十三卷，先列观测与弦表，再逐卷建模型、给参数、附星表；术语严格（本轮、均轮、偏心圆）；图示是天球几何图；回应质疑的方式是“算给你看”——以星表精度作答。`verbatim`

## (6) 该用 / 不该用的论证套路（负面清单）

- 该用：先列观测表、再建几何模型；每个参数都给出数值与来源；以预测精度检验模型；星表与模型互相核对
- 不该用：不问模型物理上是否为真而只问算得准不准时，要明说这是“拯救现象”而非物理实在；不隐藏拟合的层数；不用哲学思辨代替数值检验
- Negative prompt: `no model presented without its prediction error, no hidden fitting layers, no philosophical argument in place of a numerical check`

## (7) 测试提示词示例（现代问题：如何设计一个验证暗物质的实验）

- Prompt: `In the style of Ptolemy, design a dark-matter experiment: start from the existing tables of galaxy rotation data, fit a geometric model that reproduces every observation, and state plainly the model's prediction error before claiming anything about what dark matter is`
- 中文对照：托勒密风格，设计一个验证暗物质的实验：从已有的星系旋转数据表出发，拟合一个能复现每一条观测的几何模型，并在断言暗物质是什么之前，先明说模型的预测误差。
- Negative: `no model presented without its prediction error, no hidden fitting layers, no philosophical argument in place of a numerical check`
- 检验点：是否先列数据表、再拟合模型、并明说预测误差，而不是直接断言暗物质的本质。
