# Pytheas — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pytheas: a lone astronomer-sailor measuring the north, latitudes by the sun, tides by the moon, Britain circumnavigated, Thule reported exactly as seen and doubted ever since`
- ZH: 皮西亚斯风格：孤身天文航海家以太阳测纬度、以月亮解潮汐，环不列颠，探图勒，所见如实写下，千古被疑。

## (2) 导航方法

- 天文导航：以日影测纬度（马赛纬度首测），观月相解潮汐，记极昼与凝固之海；出直布罗陀海峡后沿葡萄牙海岸北上。

## (3) 造船与帆装

- 马赛远洋商船：单船远航，载天文观测工具；无船队护航，靠沿岸停靠补给。

## (4) 航线规划习惯

- 出海峡北上，经伊比利亚西岸渡海峡至不列颠，环不列颠航行，北上至奥克尼，可能及图勒；返航原路。

## (5) 日志与海图语言

- 《论海洋》已佚，仅存斯特拉波、波利比乌斯、狄凯阿科斯引用的残篇，多为敌意转述；埃拉托色尼与喜帕恰斯则采信其天文数据。

## (6) 该探索什么 / 不该探索什么

- 该探索：环不列颠航行, 天文纬度测定, 图勒与极昼观测, 潮汐与月相记录。
- 不该探索：no fleet, no coastal-only sailing, no claims without measurement, no marvels without observation。
- Negative prompt: `no fleet, no coastal-only sailing, no claims without measurement, no marvels without observation`

## (7) 测试提示词示例（现代题材：一艘无人货轮横渡太平洋 / 一只坐在地铁里的约克夏犬）

- Prompt: `In the style of Pytheas, a lone uncrewed survey ship circles Britain in 2026 measuring latitude by the sun at noon, logging tides against the moon, and reporting a far northern island exactly as its sensors saw it, doubted or not.`
- 中文对照：皮西亚斯风格：一艘孤身无人勘测船环不列颠航行，正午以太阳测纬度，以月亮核对潮汐，如实报告最北岛屿的观测，任人怀疑。
- Negative: `No fleet, no coastal-only sailing, no claims without measurement, no marvels without observation`
- 检验点：导航方法是否按第 (2) 节走；航线规划是否按第 (4) 节走；禁区写法是否出现。
