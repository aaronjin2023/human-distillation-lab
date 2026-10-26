# Gardar Svavarsson — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gardar Svavarsson: a North Atlantic circuit sailed by landmarks, an island found by being blown off course, the coast followed all the way round until it closes, settlement chosen where the ship can winter`
- ZH: 加尔达·斯瓦瓦松风格：北大西洋上凭地标环航的航行，因偏航发现一座岛，沿海岸一路跟到底直到闭合，定居点选在船能越冬处。

## (2) 导航方法

- 定位：认岸与太阳方位，无罗盘，靠海岸走向与日影定船位。`impression`
- 定向：挪威—冰岛航线，偏航发现冰岛，环岛航行确认其为岛。`artifact`
- 误差容忍：偏航即发现，误差转为成果；环岛闭合为确认。`artifact`

## (3) 造船与帆装

- 船型：维京长船，单桅方帆，宜北大西洋与沿岸。`impression`
- 帆装：方帆顺风，划桨辅助，近岸靠桨。`impression`
- 补给：船载干粮，冰岛登陆后就地补给，胡萨维克越冬。`artifact`

## (4) 航线规划习惯

- 路线：挪威—偏航—冰岛东岸—环岛—胡萨维克越冬—返航挪威。`artifact`
- 节奏：环岛一圈，越冬一季，返航报信。`artifact`
- 返航：返挪威报冰岛为岛，留一人在胡萨维克定居。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志，事迹见《定居记》（Landnámabók）与萨迦；蒸馏以萨迦航路为准。`artifact`
- 海图语言：海岸走向与定居点为主，地标密集。`impression`
- 命名习惯：以定居点与地貌命名（胡萨维克）。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 冰岛环岛航线
- 偏航发现法
- 北大西洋认岸航行
- 越冬定居点选择
- 不该探索：
- No island claimed before sailing all the way round it
- No settlement chosen where a ship cannot winter
- No course held without a landmark ahead
- No return without a report of the coast
- Negative prompt: `No island claimed before sailing all the way round it, No settlement chosen where a ship cannot winter, No course held without a landmark ahead, No return without a report of the coast`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gardar Svavarsson, an uncrewed ship blown off course finds an island in 2026 and follows its coast all the way round until it closes, choosing settlement where the ship can winter.`
- 中文对照：加尔达·斯瓦瓦松风格：一艘无人船2026年因偏航发现一座岛，沿海岸一路跟到底直到闭合，定居点选在船能越冬处。
- Negative: `No island claimed before sailing all the way round it, No settlement chosen where a ship cannot winter, No course held without a landmark ahead, No return without a report of the coast`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
