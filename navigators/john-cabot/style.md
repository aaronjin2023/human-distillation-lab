# John Cabot — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of John Cabot: a short north Atlantic dash, one small ship, a coast sighted and claimed in weeks, the log mostly lost, the voyage known from a few letters and a pension record`
- ZH: 约翰·卡伯特风格：北大西洋上一次短促冲刺，一艘小船，数周内望见海岸并宣称，日志大半佚失，航行只见于几封信与一份年金记录。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，北大西洋高纬航行，靠纬度与航向西行。`impression`
- 定向：布里斯托尔出发向西北，乘风西行，纽芬兰登陆后沿海岸南下探查。`artifact`
- 误差容忍：船位误差大，登陆点具体位置（纽芬兰或拉布拉多）有争议，见 conflicts。`artifact`

## (3) 造船与帆装

- 船型：马修号单船，18 人，1497 年自布里斯托尔出发。`artifact`
- 帆装：卡拉维尔，宜北大西洋抢风与远洋。`impression`
- 补给：短程航行，布里斯托尔补给，纽芬兰登陆后返航。`impression`

## (4) 航线规划习惯

- 路线：布里斯托尔—北大西洋—纽芬兰（1497）—北美东海岸南下—返航布里斯托尔。`artifact`
- 节奏：去程约 35 日，登陆后沿岸探查约一月，返程 15 日。`artifact`
- 返航：1498 年第二次航行五船出发后失踪，无人生还记录。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，航行见于致国王信、商人信与编年史；蒸馏以信件航路为准。`artifact`
- 海图语言：海岸走向与登陆点为主，细节少。`impression`
- 命名习惯：以圣人名命名登陆日（圣约翰节前后），新地称“新发现地”。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 纽芬兰登陆点
- 北美东海岸航线
- 北大西洋高纬西行航法
- 单船短程远洋
- 不该探索：
- No coast claimed without a landing
- No westward run without a latitude to return on
- No second voyage without a supply ship
- No landfall described beyond what the letters record
- Negative prompt: `No coast claimed without a landing, No westward run without a latitude to return on, No second voyage without a supply ship, No landfall described beyond what the letters record`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of John Cabot, a single small uncrewed ship makes a short North Atlantic dash in 2026, a coast sighted and claimed in weeks, the voyage known from a few dispatches and a record.`
- 中文对照：约翰·卡伯特风格：一艘小型无人船2026年在北大西洋上短促冲刺，数周内望见海岸并宣称，航行只见于几份报告与一份记录。
- Negative: `No coast claimed without a landing, No westward run without a latitude to return on, No second voyage without a supply ship, No landfall described beyond what the letters record`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
