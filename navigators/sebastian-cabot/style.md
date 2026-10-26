# Sebastian Cabot — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Sebastian Cabot: a pilot-major's navigation, charts and theory first, the river explored as a waterway to be measured, the map as the voyage's real product, claims larger than the sailing behind them`
- ZH: 塞巴斯蒂安·卡伯特风格：领航长的航行，海图与理论先行，河流当作待测量的水道，地图才是航行的真正产品，宣称大于背后的航行。

## (2) 导航方法

- 定位：纬度观测 + 海图测绘，拉普拉塔河溯河而上，以纬度与河道定船位。`artifact`
- 定向：1526 年拉普拉塔河探查，沿河道上溯，寻通往太平洋的水道。`artifact`
- 误差容忍：1508–1509 年西北航道航行是否成行有争议（见 conflicts），蒸馏不采其为实测。`artifact`

## (3) 造船与帆装

- 船型：1526 年四船船队赴拉普拉塔，河船与海船并用。`artifact`
- 帆装：河口用小帆船上溯，宜浅水河道。`impression`
- 补给：拉普拉塔河筑堡补给，土著袭击致补给中断而返。`artifact`

## (4) 航线规划习惯

- 路线：塞维利亚—巴西—拉普拉塔河—巴拉那河—巴拉圭河上溯—返航西班牙。`artifact`
- 节奏：溯河慢，筑堡停留长，1529 年决定返航。`artifact`
- 返航：返航后受审，判流放未执行，后获赦。`artifact`

## (5) 日志与海图语言

- 日志体例：无完整亲笔日志传世，航行见于西班牙档案与 1544 年世界地图；地图为主要成果物。`artifact`
- 海图语言：1544 年世界地图为代表作，海岸、河道与注记密集。`artifact`
- 命名习惯：以圣人与王室命名河段。`impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 拉普拉塔河与巴拉那河
- 西北航道尝试
- 1544 年世界地图
- 领航长制图法
- 不该探索：
- No river claimed as a passage without sailing its full length
- No voyage claimed on the strength of a map alone
- No latitude trusted from a single observation
- No northern passage promised without wintering through it
- Negative prompt: `No river claimed as a passage without sailing its full length, No voyage claimed on the strength of a map alone, No latitude trusted from a single observation, No northern passage promised without wintering through it`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Sebastian Cabot, a chart-first expedition explores a new river as a waterway to be measured in 2026, the map the voyage's real product, claims larger than the sailing behind them.`
- 中文对照：塞巴斯蒂安·卡伯特风格：2026年一次海图先行的考察把新河流当作待测量的水道，地图才是航行的真正产品，宣称大于背后的航行。
- Negative: `No river claimed as a passage without sailing its full length, No voyage claimed on the strength of a map alone, No latitude trusted from a single observation, No northern passage promised without wintering through it`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
