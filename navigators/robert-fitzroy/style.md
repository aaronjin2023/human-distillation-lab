# Robert FitzRoy — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert FitzRoy: hydrographic surveying from HMS Beagle, daily fixes and coastal charts, weather forecasting from barometer readings, plain factual logs, storm warnings before the storm`
- ZH: 菲茨罗伊风格：小猎犬号水文测绘，每日定位与海岸制图，凭气压读数做天气预报，平实的事实日志，风暴来临前先发预警。

## (2) 导航方法

定位：六分仪测纬度、天文钟定经度，每日正午定位，沿岸测绘逐点加密；巴塔哥尼亚与火地岛海岸线以三角测量与测深结合。`artifact` 气象导航：以气压计读数与风向变化预测风暴，首创系统性天气预报。`artifact`

## (3) 造船与帆装

船型：小猎犬号（HMS Beagle），双桅纵帆船，改装为测量船；帆装灵活，宜沿岸慢速测绘。补给：长期远航备足淡水与食物，重视船员健康与纪律。`artifact`

## (4) 航线规划习惯

路线：环球测绘航线，去程经大西洋、合恩角，返程经太平洋、印度洋；沿岸测绘步占大头，宁慢勿漏。节奏：测绘与航行时间约七三开，遇恶劣天气即停测绘保船。`artifact`

## (5) 日志与海图语言

日志体例：日期—纬度—经度—风向—气压—海况—测绘进度，逐日登记；语言简洁精确，结论只写测绘结果。海图注记密集，危险水域与锚地逐一标注。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：沿岸水文测绘、每日定位与海图加密、气压天气预报与风暴预警。
- 不该探索：不未经测绘的断言；不浪漫化冒险；不为求速度牺牲测绘精度。
- Negative prompt: `No uncharted claims without fixes, no romanticised adventure, no speed at the cost of surveying accuracy, no weather guess without barometer readings`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Robert FitzRoy, an uncrewed cargo ship crosses the Pacific in 2026. Daily log entries give latitude, longitude, wind and barometer readings. A storm warning is issued from falling pressure before any cloud is seen. Plain factual language, no embellishment.`
- 中文对照：菲茨罗伊风格：一艘无人货轮 2026 年横渡太平洋。每日日志记录纬度、经度、风向与气压读数。风暴预警在云未见时已由气压下降发出。语言平实无修饰。
- Negative: `No romanticised adventure, no uncharted claims without fixes, no weather guess without readings, no dramatic storms`
- 检验点：日志是否含气压与定位；预警是否先于天气现象；测绘精度是否优先于速度。
