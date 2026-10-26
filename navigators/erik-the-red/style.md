# Erik the Red — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Erik the Red: an exile's navigation, a coast prospected for settlement, the land named green to draw settlers, the voyage as a search for a place to winter and stay`
- ZH: 红发埃里克风格：流放者的航行，海岸为定居而勘测，陆地取名“绿色”以招徕定居者，航行是为找一处能越冬、能留下来的地方。

## (2) 导航方法

- 定位：认岸与太阳方位，冰岛—格陵兰航线，靠海岸走向与浮冰定船位。`impression`
- 定向：冰岛西行，绕格陵兰南端，沿西海岸北上寻定居点。`artifact`
- 误差容忍：浮冰与雾中不硬航，沿岸认岸，定居点以越冬条件定。`impression`

## (3) 造船与帆装

- 船型：维京长船，载定居者、牲畜与木材，宜北大西洋与沿岸。`impression`
- 帆装：方帆顺风，近岸靠桨，浮冰区靠桨穿行。`impression`
- 补给：船载牲畜与粮食，定居后就地补给。`artifact`

## (4) 航线规划习惯

- 路线：冰岛—格陵兰南端—西海岸—布拉塔赫利德定居点。`artifact`
- 节奏：流放三年探查（约 982–985 年），返冰岛招徕定居者，985 年率 25 船再航。`artifact`
- 返航：定居后不再返航，格陵兰为终点。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志，事迹见《红发埃里克萨迦》与《格陵兰萨迦》；蒸馏以萨迦航路为准。`artifact`
- 海图语言：海岸与定居点为主，浮冰与雾为航行注记。`impression`
- 命名习惯：格陵兰（Greenland）以“绿色”命名招徕定居者，命名即宣传。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 格陵兰西海岸定居航线
- 流放探查法
- 越冬定居点选择
- 浮冰区沿岸航行
- 不该探索：
- No settlement founded where a ship cannot winter
- No coast named before prospecting it for settlement
- No ice sailed through without an open lead
- No settlers brought before the route is sailed twice
- Negative prompt: `No settlement founded where a ship cannot winter, No coast named before prospecting it for settlement, No ice sailed through without an open lead, No settlers brought before the route is sailed twice`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Erik the Red, an uncrewed prospecting ship surveys a new coast for settlement in 2026, the land named green to draw settlers, the voyage a search for a place to winter and stay.`
- 中文对照：红发埃里克风格：一艘无人勘测船2026年为定居勘测新海岸，陆地取名“绿色”以招徕定居者，航行是为找一处能越冬、能留下来的地方。
- Negative: `No settlement founded where a ship cannot winter, No coast named before prospecting it for settlement, No ice sailed through without an open lead, No settlers brought before the route is sailed twice`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
