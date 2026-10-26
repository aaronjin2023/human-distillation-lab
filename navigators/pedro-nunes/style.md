# Pedro Nunes — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pedro Nunes: a mathematician's navigation, the loxodrome drawn as a spiral to the pole, latitudes measured by two suns, instruments invented on paper before they are built, theory that makes the chart honest`
- ZH: 佩德罗·努内斯风格：数学家的航行，斜航线画成旋向极点的螺旋，纬度以双太阳法测定，仪器先在纸上发明再造出来，理论让海图诚实。

## (2) 导航方法

- 定位：纬度测定法——太阳高度双测（正午与任意时刻），配星表。`artifact`
- 定向：斜航线理论——等角航线在墨卡托投影前以螺旋线逼近极点，纠正平面海图的航向误差。`artifact`
- 误差容忍：数学上承认平面海图的航向失真，以斜航线表修正。`artifact`

## (3) 造船与帆装

- 船型：不自造船、不领航，理论服务于葡萄牙印度航线船队。`artifact`
- 帆装：不详述帆装，重点在航向数学。`impression`
- 补给：不适用；其“补给”是航海表与仪器。`impression`

## (4) 航线规划习惯

- 路线：不适用——其航路是数学的：里斯本—印度航线的航向计算。`artifact`
- 节奏：以著述节奏代航行节奏——《航海论》与航海表逐版修订。`impression`
- 返航：不适用。`artifact`

## (5) 日志与海图语言

- 日志体例：非航海日志，而是航海论著——定理、表与仪器说明。`artifact`
- 海图语言：数学语言——斜航线、纬度表、仪器刻度。`artifact`
- 命名习惯：以数学术语命名航线（斜航线 loxodrome）。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 斜航线理论
- 纬度测定法
- 航海仪器（nonius 游标）
- 航海表编纂
- 不该探索：
- No course plotted as a straight line on a flat chart
- No latitude taken from a single solar observation
- No instrument trusted before its mathematics is proved
- No sailing rule taught that the chart contradicts
- Negative prompt: `No course plotted as a straight line on a flat chart, No latitude taken from a single solar observation, No instrument trusted before its mathematics is proved, No sailing rule taught that the chart contradicts`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Pedro Nunes, a 2026 routing model plots a course as a loxodrome spiralling to the pole, latitudes measured by two suns, instruments proved on paper before they are built.`
- 中文对照：佩德罗·努内斯风格：2026年一套航路模型把航线画成旋向极点的斜航线，纬度以双太阳法测定，仪器先在纸上证明再造出来。
- Negative: `No course plotted as a straight line on a flat chart, No latitude taken from a single solar observation, No instrument trusted before its mathematics is proved, No sailing rule taught that the chart contradicts`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
