# Martin Behaim — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Martin Behaim: a globe-maker's navigation, the earth made round and holdable, coasts transferred from charts onto a sphere, star tables and latitudes fitted to the curve of the world`
- ZH: 马丁·贝海姆风格：制球者的航行，大地做成浑圆可握的球，海岸从海图移到球面，星表与纬度贴合世界的弧度。

## (2) 导航方法

- 定位：纬度观测 + 星表，地球仪按纬度圈排布海岸。`artifact`
- 定向：西非海岸航行（随迪奥戈·康 1484–1485 年一说，见 conflicts），沿岸南下。`artifact`
- 误差容忍：1492 年地球仪无美洲，印度洋画错——以当时海图为准，不以后见之明改。`artifact`

## (3) 造船与帆装

- 船型：随迪奥戈·康船队的卡拉维尔（若成行），西非沿岸航行。`artifact`
- 帆装：拉丁帆，宜沿岸航行。`impression`
- 补给：沿岸补给，短程航行。`impression`

## (4) 航线规划习惯

- 路线：里斯本—西非沿岸（刚果一带），返航里斯本；后居纽伦堡制地球仪。`artifact`
- 节奏：一次西非航行，余生制图与制球。`impression`
- 返航：返航后以航行见闻制地球仪。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，地球仪即其航海记录——海岸、纬度与注记绘于球面。`artifact`
- 海图语言：球面语言——纬度圈、子午线、海岸线与图例。`artifact`
- 命名习惯：以圣人与港口命名海岸段，球面注记密集。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 西非海岸
- 地球仪制图法
- 纬度圈与海岸的球面排布
- 星表与导航
- 不该探索：
- No coast placed on the globe without a chart behind it
- No latitude drawn without an observation
- No ocean left blank where a coastline is known
- No globe made that cannot be read by a navigator
- Negative prompt: `No coast placed on the globe without a chart behind it, No latitude drawn without an observation, No ocean left blank where a coastline is known, No globe made that cannot be read by a navigator`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Martin Behaim, a 2026 digital globe is built from charts, coasts transferred onto a sphere, star tables and latitudes fitted to the curve of the world.`
- 中文对照：马丁·贝海姆风格：2026年一座数字地球仪由海图做成，海岸从海图移到球面，星表与纬度贴合世界的弧度。
- Negative: `No coast placed on the globe without a chart behind it, No latitude drawn without an observation, No ocean left blank where a coastline is known, No globe made that cannot be read by a navigator`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
