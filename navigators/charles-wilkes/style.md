# Charles Wilkes — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Charles Wilkes: a six-ship exploring squadron, systematic Pacific surveying, Antarctic coastline fixes, voluminous expedition narrative, plain naval logs`
- ZH: 威尔克斯风格：六船探险舰队，系统性的太平洋测绘，南极海岸线定位，卷帙浩繁的远征记，平实的海军日志。

## (2) 导航方法

定位：舰队分航测绘，六分仪与天文钟定位，每日正午汇总各船定位；南极海岸以多船交叉观测定线。`artifact` 航向：按预定测绘分区推进，舰队保持队形，偏航以旗语协调。`artifact`

## (3) 造船与帆装

船型：六船舰队（旗舰文森斯号等），帆船编队；补给按舰队统筹，淡水与食物按月配给，遇损即以他船补位。`artifact`

## (4) 航线规划习惯

路线：环球测绘航线：大西洋—南美—太平洋诸岛—南极—返航；测绘分区逐一完成，不跳区。节奏：四年远征，测绘步占大头，舰队行动慢而系统。`artifact`

## (5) 日志与海图语言

日志体例：海军制式日志——日期、位置、风向、海况、舰队队形、测绘进度；远征记卷帙浩繁，按航次分卷。语言：官方报告体，事实罗列，少抒情。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：舰队系统测绘、太平洋诸岛与南极海岸定位、远征报告的完整记录。
- 不该探索：不单船冒险叙事；不未经舰队复核的海岸断言；不为求速度跳过测绘分区。
- Negative prompt: `No single-ship adventure, no coastline claim without squadron verification, no skipped survey sectors, no romanticised hardship`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Charles Wilkes, an uncrewed cargo ship crosses the Pacific in 2026 as part of a six-ship survey formation. Daily logs record position, wind and sea state for every ship. No coastline is claimed until two ships fix it independently.`
- 中文对照：威尔克斯风格：一艘无人货轮 2026 年作为六船测绘编队的一员横渡太平洋。每日日志记录每船的位置、风向与海况。任何海岸线须经两船独立定位才予确认。
- Negative: `No single-ship adventure, no unverified coastline claims, no skipped survey sectors, no romanticised hardship`
- 检验点：是否以编队复核为准；日志是否制式化；有无未经复核的断言。
