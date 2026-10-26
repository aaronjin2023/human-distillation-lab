# Abel Tasman — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abel Tasman: run down a latitude in two vessels, chart as you go, close the loop home when the coast is mapped, no single-ship venture into unknown water`
- ZH: 亚伯·塔斯曼风格：双船编队、航行中即绘图，单船深入未知水域。

## (2) 导航方法

- 大洋航行结合沿岸测绘：以纬度航行法（sailing by latitude）西行，抵近陆地后转沿岸测绘；用计程仪与罗盘推算船位，误差靠陆标修正。 `impression`

## (3) 造船与帆装

- 赫姆斯克尔克号与泽哈恩号双船编队：大船载补给与测绘员，小船前出探路；船员配有制图员，航行中即绘海图。 `impression`

## (4) 航线规划习惯

- 环形探索：从巴达维亚南下，绕澳大利亚南岸东行至塔斯马尼亚、新西兰，再北返经汤加、斐济回巴达维亚；去程与返程构成闭合环。 `impression`

## (5) 日志与海图语言

- 日志体例为公司远征报告：日期—纬度—风向—海况—事件；对新西兰毛利人的冲突有详细记录；海图以荷兰语命名（范迪门地、新西兰）。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：纬度航行法的大洋横渡、新地登陆与原住民冲突、环形返航的闭合航线。
- 不该探索：单船深入未知水域。
- Negative prompt: `No single-ship venture into unknown water, no landing without armed caution, no charting from memory, no modern GPS fix as the only position`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Abel Tasman, an uncrewed survey ship sails a great loop around an unknown southern land in 2026, running down a latitude, charting as it goes, two vessels in company, turning home when the coast is mapped. No single-ship venture into unknown water.`
- 中文对照：塔斯曼风格：一艘无人测量船2026年沿纬度环绕未知南方大陆航行，边航行边绘图，双船编队，海岸测绘完成即返航。不单船深入未知水域。
- Negative: `No single-ship venture into unknown water, no landing without armed caution, no charting from memory, no modern GPS fix as the only position`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
