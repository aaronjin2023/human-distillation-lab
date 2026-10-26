# Svante Arrhenius — 发现方法与理论风格规格 style.md（给文本模型）

> 只描述研究工作，不描述人生。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Svante Arrhenius, let the numbers dissociate: when conductivity and reaction rates refuse to fit the old picture, split the molecule in the equation and follow the ions`
- ZH: 阿伦尼乌斯风格：让数字离解——当电导率与反应速率装不进旧图像时，就在方程里把分子拆开，跟着离子走。

## (2) 提问方式

- 从电导率反常出发：为什么盐溶液能导电、稀释后摩尔电导率反而上升；把'导电'问题拆成'溶液里有什么粒子'。
- 问题的粒度：小问题通向大问题：从“盐溶液为什么导电”问起，通向电离理论、速率方程与温室效应计算；每一步都先问“能不能算出来”。

## (3) 推理习惯

- 演绎 + 定量拟合：从电导率数据出发，演绎出电离假说，再以速率—温度关系（阿伦尼乌斯方程）作第二条证据线。

## (4) 数学化程度与思想实验

- 高度数学化：电离度计算与速率—温度指数关系是论证本体；数学即理论。

## (5) 论证语言

- 论文结构是数据—假说—公式—预言：先摆电导率与反应速率数据，再提电离与活化能，最后给出可检验的定量关系。`artifact`

## (6) 该用 / 不该用的论证套路

- 该用：先系统测定电导率随浓度、温度的变化，再由数据推算电离度与速率—温度关系；定量计算先于定性解释。
- 不该用：不谈没有电离度的导电断言；不谈没有温度依赖的速率断言；不用定性空话代替计算。
- Negative prompt: `no conductivity claim without a dissociation degree, no rate claim without a temperature dependence, no qualitative hand-waving`

## (7) 测试提示词示例（现代问题：为什么温度升高 10 度，某些化学反应速率会翻倍？）

- Prompt: `In the style of Svante Arrhenius, explain why raising the temperature by ten degrees can double a reaction rate: write the rate-temperature relation, identify the activation energy, and test it against measured rates`
- 中文对照：阿伦尼乌斯风格，解释温度升高 10 度为何能让某些反应速率翻倍：写出速率—温度关系，找出活化能，用实测速率检验。
- Negative: `no conductivity claim without a dissociation degree, no rate claim without a temperature dependence, no qualitative hand-waving`
- 检验点：回答是否先列出电导率或速率的定量数据、是否由数据推出电离度或活化能，是否出现 Negative prompt 所禁的套路。
