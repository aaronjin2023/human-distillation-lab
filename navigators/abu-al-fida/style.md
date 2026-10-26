# Abu al-Fida — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abu al-Fida: a tabular geography of the sea, ports listed with latitude and longitude in tables, coastlines measured in degrees, trade routes summarised from earlier sailing manuals, concise and systematic`
- ZH: 阿布·菲达风格：表格化的海洋地理，港口以经纬度列表，海岸以度数丈量，航路取自前人航海手册，简洁系统。

## (2) 导航方法

- 定位：经纬度表格定位——《地名辞典》以表格列各地经纬度，是当时最系统的坐标汇编。`artifact`
- 定向：航路取自前人航海手册与商人讲述，按海域分卷，不自创新航线。`artifact`
- 误差容忍：坐标多源汇编，存疑处并列异说，不强行取一。`artifact`

## (3) 造船与帆装

- 船型：不自造船，记当时阿拉伯—印度洋商船的航路适用性。`impression`
- 帆装：不详述帆装，重点在航路与港口条件。`impression`
- 补给：港口表即补给表，逐港记淡水与物产。`artifact`

## (4) 航线规划习惯

- 路线：印度洋—波斯湾—红海—地中海航路网，以表格与文字双轨呈现。`artifact`
- 节奏：以编纂节奏代航行节奏——分海域逐卷写，系统重于速度。`impression`
- 返航：不适用；其航路是汇编而非亲历航行。`artifact`

## (5) 日志与海图语言

- 日志体例：非航海日志，而是地理辞典——表格 + 条目，港口按经纬度排序。`artifact`
- 海图语言：数字为主，注记为辅；坐标表密度高，叙事少。`artifact`
- 命名习惯：地名按阿拉伯地理传统，附异名对照。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 印度洋港口经纬度表
- 波斯湾与红海航路
- 地中海—印度洋贸易航线
- 前人航海手册的汇编与校勘
- 不该探索：
- No invented coordinates where sources disagree
- No firsthand claim for a coast never visited
- No narrative embellishment in a table
- No single source trusted without cross-check
- Negative prompt: `No invented coordinates where sources disagree, No firsthand claim for a coast never visited, No narrative embellishment in a table, No single source trusted without cross-check`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Abu al-Fida, an uncrewed survey ship maps a new coast in 2026, ports listed with latitude and longitude in tables, coastlines measured in degrees, trade routes summarised from earlier sailing manuals.`
- 中文对照：阿布·菲达风格：一艘无人测量船2026年测绘新海岸，港口以经纬度列表，海岸以度数丈量，航路取自前人航海手册。
- Negative: `No invented coordinates where sources disagree, No firsthand claim for a coast never visited, No narrative embellishment in a table, No single source trusted without cross-check`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
