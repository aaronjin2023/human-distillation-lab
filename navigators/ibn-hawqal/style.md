# Ibn Hawqal — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ibn Hawqal: a geographer's sailing survey, routes drawn as itineraries between ports, distances in days' sail, trade goods and winds noted at each harbour, revision upon revision of the map`
- ZH: 伊本·豪卡勒风格：地理学家的航海勘测，航线写成港口间的行程，距离以航行日计，每港记货物与风向，海图屡经修订。

## (2) 导航方法

- 定位：航路以港口接力定位，少用天文定位，多用“某港至某港航行若干日”的行程距离。`artifact`
- 定向：季风与信风为航路骨架，印度洋航路按季风换季分段。`impression`
- 误差容忍：距离用航行日数而非精确里程，同一航段多源互校，存疑处明言未亲历。`artifact`

## (3) 造船与帆装

- 船型：不自造船，记所乘商船——阿拉伯三角帆船（dhow），季风航行，沿岸与横渡兼用。`impression`
- 帆装：三角帆抢风性能好，宜季风海域；船小灵活，宜港口间短途接力。`impression`
- 补给：港口即补给站，航路志即补给清单——淡水、粮食、货物逐港记。`artifact`

## (4) 航线规划习惯

- 路线：印度洋—波斯湾—红海—地中海的贸易航路网，按港口串联，不追求单一直线。`artifact`
- 节奏：以贸易季与季风季定航期，港口停留长，记风物与物产。`impression`
- 返航：同一航路网往返，修订旧图——《大地景象》多次修订，以实地见闻改旧说。`artifact`

## (5) 日志与海图语言

- 日志体例：非逐日航海日志，而是航路志——分地区记航路、距离、港口、物产与风俗。`artifact`
- 海图语言：地图配文字，注记密度高，港口、航路、物产三层信息叠加。`artifact`
- 命名习惯：以港口与海域命名航段，距离以航行日计。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 印度洋贸易航路网与港口序列
- 波斯湾—红海—地中海航路
- 各港物产与季风窗口
- 旧图的修订与勘误
- 不该探索：
- No single straight route where a network of ports exists
- No precise mileage where only days' sail is known
- No unvisited coast described as surveyed
- No map left unrevised after new firsthand observation
- Negative prompt: `No single straight route where a network of ports exists, No precise mileage where only days' sail is known, No unvisited coast described as surveyed, No map left unrevised after new firsthand observation`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ibn Hawqal, an uncrewed survey ship logs a new route as an itinerary between ports in 2026, distances in days' sail, trade goods and winds noted at each harbour, the map revised on every return.`
- 中文对照：伊本·豪卡勒风格：一艘无人测量船2026年把新航线写成港口间的行程，距离以航行日计，每港记货物与风向，海图每次返航都修订。
- Negative: `No single straight route where a network of ports exists, No precise mileage where only days' sail is known, No unvisited coast described as surveyed, No map left unrevised after new firsthand observation`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
