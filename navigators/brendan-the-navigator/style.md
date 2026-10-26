# Brendan the Navigator — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Saint Brendan: a legendary voyage told as a pilgrimage, islands that appear and vanish, a whale mistaken for land, the sea as a monastery corridor, every landfall a parable rather than a fix`
- ZH: 圣布伦丹风格：传说航行写成朝圣，岛屿忽现忽隐，鲸鱼被认作陆地，大海是一条修道院走廊，每处登陆是一则寓言而非一个定位。

## (2) 导航方法

- 定位：传说——无定位法可蒸；《航海记》以祈祷与风向定去向，不记纬度。`artifact`（传说文本）
- 定向：向西寻“应许之地”，风向与神意为向导，非罗盘非星辰。`artifact`（传说文本）
- 误差容忍：不适用——传说不以误差计。`impression`

## (3) 造船与帆装

- 船型：传说中的皮筏（currach），牛皮蒙木架，宜近岸，不宜远洋——传说文本如此写。`artifact`（传说文本）
- 帆装：传说不详述帆装。`impression`
- 补给：传说中岛屿供食、海鸟供食，补给靠神迹不靠港口。`artifact`（传说文本）

## (4) 航线规划习惯

- 路线：传说——爱尔兰—西行—诸岛—“应许之地”七年往返。`artifact`（传说文本）
- 节奏：传说以瞻礼日与复活节定节奏，七年为期。`artifact`（传说文本）
- 返航：传说中返爱尔兰，述航行，成《航海记》。`artifact`（传说文本）

## (5) 日志与海图语言

- 日志体例：无日志；《航海记》为中世纪拉丁传说文本，成书约 9 世纪，非 6 世纪实录。`artifact`
- 海图语言：传说语言——岛屿、鲸鱼、海鸟、火山，皆寓言。`artifact`
- 命名习惯：岛屿以圣人命名，登陆以瞻礼日记。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 传说中的西行诸岛
- 鲸鱼背登陆
- 应许之地
- 朝圣式航行叙事
- 不该探索：
- No legendary island charted as a surveyed coast
- No whale logged as land
- No miracle used as a navigation fix
- No legend presented as a dated voyage
- Negative prompt: `No legendary island charted as a surveyed coast, No whale logged as land, No miracle used as a navigation fix, No legend presented as a dated voyage`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Saint Brendan, a 2026 survey ship logs islands that appear and vanish, a whale mistaken for land, the sea as a monastery corridor, every landfall a parable rather than a fix.`
- 中文对照：圣布伦丹风格：一艘测量船2026年记录忽现忽隐的岛屿，鲸鱼被认作陆地，大海是一条修道院走廊，每处登陆是一则寓言而非一个定位。
- Negative: `No legendary island charted as a surveyed coast, No whale logged as land, No miracle used as a navigation fix, No legend presented as a dated voyage`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
