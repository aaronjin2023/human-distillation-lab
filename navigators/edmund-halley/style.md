# Edmund Halley — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edmund Halley: cross an ocean on a measurement grid, log magnetic variation at every point, the chart growing from fixes not impressions`
- ZH: 埃德蒙·哈雷风格：逐点测量、网格覆盖，无测量的断言、凭印象画图。

## (2) 导航方法

- 科学测量航行：以天文钟前身的计时器与六分仪定位，逐点测磁偏角；航线按测量网格设计，覆盖大西洋南北纬度带。 `impression`

## (3) 造船与帆装

- 帕拉莫尔号（Paramore）：英国海军测量船，配磁测仪与天文仪器；船员配科学家，航行中即绘磁偏图。 `impression`

## (4) 航线规划习惯

- 测量航线：1698–1700年两次大西洋航行，沿南北纬度带逐点测磁偏，绘首张等磁偏线图与信风图。 `impression`

## (5) 日志与海图语言

- 日志体例为科学报告：日期—纬度—经度—磁偏—风向；哈雷著《磁偏图》（1701年）与《信风图》（1686年），附测量表。 `impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：逐点测磁偏的网格航线、等磁偏线图的绘制、信风图的航线优化。
- 不该探索：无测量的断言、凭印象画图。
- Negative prompt: `No chart without a fix, no sailing without a magnetic reading, no wind chart from impression, no modern GPS as the only fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Edmund Halley, an uncrewed survey ship crosses an ocean in 2026 on a measurement grid, logging magnetic variation at every point, the chart growing from fixes, not impressions. No chart without a fix.`
- 中文对照：哈雷风格：一艘无人测量船2026年按测量网格横渡大洋，逐点测磁偏，海图由定位点生长而成，不凭印象画图。
- Negative: `No chart without a fix, no sailing without a magnetic reading, no wind chart from impression, no modern GPS as the only fix`
- 检验点：导航方法是否落到实处；航线习惯是否可辨；禁区写法是否出现。
