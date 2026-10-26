# Bjarni Herjólfsson — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bjarni Herjólfsson: a voyage that finds land by missing its destination, a coast sighted and deliberately not landed on, the sighting reported and left for others to finish`
- ZH: 比亚尼·赫约尔夫松风格：因错过目的地而发现陆地的航行，海岸望见了却刻意不登陆，目击报告留下，登陆留给别人完成。

## (2) 导航方法

- 定位：认岸与太阳方位，冰岛—格陵兰航线，雾与风吹偏航。`artifact`
- 定向：赴格陵兰寻父，偏航西南，望见北美海岸三段，转向东北返格陵兰。`artifact`
- 误差容忍：偏航不纠正，顺势望见新海岸；不登陆即返，目击为成果。`artifact`

## (3) 造船与帆装

- 船型：维京长船，载货物赴格陵兰，宜北大西洋。`impression`
- 帆装：方帆顺风，雾中靠风与洋流。`impression`
- 补给：船载货物与干粮，望见海岸后不登陆补给，直接返航。`artifact`

## (4) 航线规划习惯

- 路线：冰岛—雾中偏航—北美海岸三段（望见）—转向东北—格陵兰。`artifact`
- 节奏：一次偏航，望见三段海岸，不登陆，返航报信。`artifact`
- 返航：返格陵兰报目击，莱夫后买其船西行（见 #47）。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志，事迹见《格陵兰萨迦》；目击报告为其全部成果。`artifact`
- 海图语言：海岸三段望见记录——森林海岸为关键一笔。`impression`
- 命名习惯：不命名新地，只报目击。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 北美海岸首次目击
- 偏航发现法
- 望见不登陆
- 目击报告
- 不该探索：
- No landfall claimed without landing
- No coast named from a sighting alone
- No course corrected back into fog to chase a coast
- No sighting left unreported
- Negative prompt: `No landfall claimed without landing, No coast named from a sighting alone, No course corrected back into fog to chase a coast, No sighting left unreported`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bjarni Herjólfsson, an uncrewed ship misses its waypoint in 2026 and sights an uncharted coast, reports the sighting and sails on, leaving the landing for others to finish.`
- 中文对照：比亚尼·赫约尔夫松风格：一艘无人船2026年错过航点，望见一片未标海岸，报告目击后继续航行，登陆留给别人完成。
- Negative: `No landfall claimed without landing, No coast named from a sighting alone, No course corrected back into fog to chase a coast, No sighting left unreported`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
