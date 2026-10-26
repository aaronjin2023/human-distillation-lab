# Álvaro de Mendaña — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Álvaro de Mendaña: a South Pacific search for islands that keep disappointing, two voyages a generation apart, the log as a list of landfalls that were not the rich isles promised, settlement attempted and abandoned`
- ZH: 阿尔瓦罗·德·门达尼亚风格：南太平洋上搜寻屡屡令人失望的岛屿，两次航行隔了一代人，日志是一串并非许诺中富岛的登陆，定居尝试了又放弃。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，南太平洋无地标长航，靠纬度与航向西行。`artifact`
- 定向：秘鲁出发向西偏南，寻传说中的所罗门群岛与南方大陆。`artifact`
- 误差容忍：岛屿位置误差大，返航靠纬度与信风，第二次航行迷失圣克鲁斯岛。`artifact`

## (3) 造船与帆装

- 船型：两艘船首航（1567），四船再航（1595），盖伦帆船，载定居者。`artifact`
- 帆装：横帆远洋，宜信风西行。`impression`
- 补给：秘鲁补给，岛屿逐岛补给；第二次航行补给与疾病致定居失败。`artifact`

## (4) 航线规划习惯

- 路线：秘鲁卡亚俄—西行—所罗门群岛（1568）—返航墨西哥；第二次：秘鲁—马克萨斯群岛—圣克鲁斯岛（1595）。`artifact`
- 节奏：首航约 9 个月，再航隔 27 年，定居数月即溃。`artifact`
- 返航：首航返墨西哥，再航死于圣克鲁斯，余部返菲律宾。`artifact`

## (5) 日志与海图语言

- 日志体例：无完整亲笔日志，航行见于同行者记述与西班牙档案；岛屿位置以纬度记。`artifact`
- 海图语言：岛屿、纬度与定居点为主，失望处直记。`impression`
- 命名习惯：以圣人瞻礼日命名岛屿（所罗门群岛附会圣经）。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 所罗门群岛
- 马克萨斯群岛
- 南太平洋寻岛航线
- 岛屿定居尝试
- 不该探索：
- No island claimed as the rich isles without gold to show
- No settlement founded without water and food counted
- No westward run without a return latitude
- No landfall logged without a latitude fix
- Negative prompt: `No island claimed as the rich isles without gold to show, No settlement founded without water and food counted, No westward run without a return latitude, No landfall logged without a latitude fix`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Álvaro de Mendaña, an uncrewed search vessel combs the South Pacific in 2026 for islands that keep disappointing, its log a list of landfalls that were not the rich isles promised, a settlement attempted and abandoned.`
- 中文对照：阿尔瓦罗·德·门达尼亚风格：一艘无人搜寻船2026年在南太平洋搜寻屡屡令人失望的岛屿，日志是一串并非许诺中富岛的登陆，定居尝试了又放弃。
- Negative: `No island claimed as the rich isles without gold to show, No settlement founded without water and food counted, No westward run without a return latitude, No landfall logged without a latitude fix`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
