# Christopher Columbus — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Christopher Columbus: a westward gamble on dead reckoning, latitudes fudged in the log, two sets of distances kept, islands named for saints by the day, the log as both navigation record and legal claim`
- ZH: 克里斯托弗·哥伦布风格：向西一搏的推测航法，日志里纬度含糊，两套距离并记，岛屿按圣人瞻礼日命名，日志既是航行记录也是法律凭证。

## (2) 导航方法

- 定位：推测航法为主，纬度观测不准且日志所记纬度多有涂改；去程记两套距离（一真一假以安抚船员）。`artifact`
- 定向：乘东北信风西行，返程北上借西风——信风环流的利用为其核心航法。`artifact`
- 误差容忍：船位误差大，屡以“印度”误认加勒比；返程靠纬度与西风重聚。`impression`

## (3) 造船与帆装

- 船型：三船（圣玛利亚号、平塔号、尼尼雅号），卡拉维尔与卡拉克并用，小船队远洋。`artifact`
- 帆装：拉丁帆与横帆并用，信风顺风航行。`impression`
- 补给：加那利群岛补给，加勒比岛屿逐岛补给；四次航行补给屡屡告罄。`artifact`

## (4) 航线规划习惯

- 路线：帕洛斯—加那利—信风西渡—巴哈马—古巴—海地，四次航行逐次向南向西扩展。`artifact`
- 节奏：首航去程 36 日，返程借西风北上；后三次航行屡陷风暴与补给困境。`artifact`
- 返航：返程必北上至西风带再东行，此为其航线结构的核心。`artifact`

## (5) 日志与海图语言

- 日志体例：《航海日志》（Diario）仅存拉斯卡萨斯节略本，原稿已佚；引文以节略本为准，不冒充原文。`artifact`
- 海图语言：岛屿按圣人瞻礼日命名，海岸走向随航行逐段绘入。`artifact`
- 命名习惯：新地以圣人、王室与宗教命名，命名即宣称。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 信风西渡大西洋航线
- 加勒比岛屿序列
- 返程西风带航线
- 岛屿命名与宣称程式
- 不该探索：
- No westward run without the trade winds behind
- No return without climbing north to the westerlies
- No island claimed without a landing and a name
- No log distance trusted without a second reckoning
- Negative prompt: `No westward run without the trade winds behind, No return without climbing north to the westerlies, No island claimed without a landing and a name, No log distance trusted without a second reckoning`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Christopher Columbus, an uncrewed cargo ship gambles westward on dead reckoning in 2026, latitudes fudged in the log, two sets of distances kept, islands named for saints by the day.`
- 中文对照：克里斯托弗·哥伦布风格：一艘无人货轮2026年凭推测航法向西一搏，日志里纬度含糊，两套距离并记，岛屿按圣人瞻礼日命名。
- Negative: `No westward run without the trade winds behind, No return without climbing north to the westerlies, No island claimed without a landing and a name, No log distance trusted without a second reckoning`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
