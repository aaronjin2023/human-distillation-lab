# Duarte Pacheco Pereira — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Duarte Pacheco Pereira: a cosmographer's navigation, the Esmeraldo as a sailing manual written from experience, latitudes and magnetic variation measured, coasts described to be sailed again`
- ZH: 杜阿尔特·帕谢科·佩雷拉风格：宇宙志学者的航行，《埃斯梅拉达》是凭经验写成的航海手册，纬度与磁偏角实测，海岸写得能再航一次。

## (2) 导航方法

- 定位：纬度观测 + 磁偏角修正，《埃斯梅拉达》详载各地纬度与磁偏角。`artifact`
- 定向：大西洋与印度洋航路并重，巴西海岸与印度海岸分卷记。`artifact`
- 误差容忍：磁偏角逐地实测，不以一地之值推他地。`artifact`

## (3) 造船与帆装

- 船型：葡萄牙印度航线船队，卡拉克帆船，远洋与武装并重。`artifact`
- 帆装：横帆远洋，宜大弧与季风航行。`impression`
- 补给：印度航线逐站补给，巴西海岸为返航补给点。`impression`

## (4) 航线规划习惯

- 路线：里斯本—巴西—好望角—印度（科钦一带），印度洋沿岸作战与贸易。`artifact`
- 节奏：多次往返印度，航路志逐次修订。`impression`
- 返航：印度—好望角—巴西—里斯本，巴西海岸为返航标志。`artifact`

## (5) 日志与海图语言

- 日志体例：《埃斯梅拉达》为航海手册体——分卷记海岸、纬度、磁偏角、风向与港口。`artifact`
- 海图语言：数字密集，纬度与磁偏角为核心数据。`artifact`
- 命名习惯：以港口与河口命名航段，巴西海岸段尤详。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 巴西海岸
- 印度洋航路
- 磁偏角实测
- 航海手册编纂
- 不该探索：
- No latitude logged without a magnetic variation to go with it
- No coast described that cannot be sailed again from the text
- No single variation value applied to a whole ocean
- No sailing manual left unrevised after a new voyage
- Negative prompt: `No latitude logged without a magnetic variation to go with it, No coast described that cannot be sailed again from the text, No single variation value applied to a whole ocean, No sailing manual left unrevised after a new voyage`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Duarte Pacheco Pereira, an uncrewed survey ship writes its own sailing manual from experience in 2026, latitudes and magnetic variation measured, coasts described so they can be sailed again.`
- 中文对照：杜阿尔特·帕谢科·佩雷拉风格：一艘无人测量船2026年凭经验写成自己的航海手册，纬度与磁偏角实测，海岸写得能再航一次。
- Negative: `No latitude logged without a magnetic variation to go with it, No coast described that cannot be sailed again from the text, No single variation value applied to a whole ocean, No sailing manual left unrevised after a new voyage`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
