# Amerigo Vespucci — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Amerigo Vespucci: a letter-writer's navigation, coasts described as prose, latitudes and star positions quoted to prove a new continent, the voyage argued into print rather than only sailed`
- ZH: 亚美利哥·韦斯普奇风格：书信家的航行，海岸写成散文，纬度与星位用来证明一块新大陆，航行不只航出来，还要写进信里论证出来。

## (2) 导航方法

- 定位：纬度观测 + 南天星位，南美东海岸航行以南十字星定南纬。`artifact`
- 定向：沿南美东海岸南下，信风与巴西洋流为路标，转向处以纬度定。`impression`
- 误差容忍：书信所记纬度与航程有夸大之嫌，以航路事实为准，不采书信数字为实测。`artifact`

## (3) 造船与帆装

- 船型：西班牙与葡萄牙船队中的卡拉维尔，1497–1504 年间多次大西洋航行。`artifact`
- 帆装：拉丁帆，宜沿岸南下与抢风。`impression`
- 补给：沿南美海岸逐港补给，淡水与食物靠登陆补充。`impression`

## (4) 航线规划习惯

- 路线：加的斯—大西洋—委内瑞拉—巴西—南美东海岸南下至拉普拉塔一带。`artifact`
- 节奏：多次短航拼成南美东海岸序列，无一次完整环航。`artifact`
- 返航：沿东海岸北返，乘信风与洋流回欧洲。`impression`

## (5) 日志与海图语言

- 日志体例：无亲笔航海日志传世，代表作是书信（《新大陆》Mundus Novus 等），书信即航行记录。`artifact`
- 海图语言：书信中海岸走向、纬度与星位并重，论证性强于记录性。`artifact`
- 命名习惯：以圣人与王室命名海岸段；“新大陆”之名出自其书信的传播。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 南美东海岸序列
- 南天星位与南纬测定
- 新大陆论证
- 书信体航行记录
- 不该探索：
- No coast described without a latitude to anchor it
- No new continent claimed from a single landfall
- No letter distance trusted without a chart to check it
- No voyage argued in print that was never sailed
- Negative prompt: `No coast described without a latitude to anchor it, No new continent claimed from a single landfall, No letter distance trusted without a chart to check it, No voyage argued in print that was never sailed`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Amerigo Vespucci, a 2026 dispatch from an uncrewed survey ship argues from latitudes and star positions that the coast it found is a new passage, the voyage argued into print rather than only sailed.`
- 中文对照：亚美利哥·韦斯普奇风格：一艘无人测量船2026年发回的报告以纬度与星位论证它发现的海岸是一条新航道，航行不只航出来，还要写进报告里论证出来。
- Negative: `No coast described without a latitude to anchor it, No new continent claimed from a single landfall, No letter distance trusted without a chart to check it, No voyage argued in print that was never sailed`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
