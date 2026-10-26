# Juan Sebastián Elcano — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Juan Sebastián Elcano: the return leg as the real voyage, one leaking ship across the Indian Ocean, no port of call for months, latitudes logged and the crew counted down, the circumnavigation finished by the man who did not start it`
- ZH: 胡安·塞巴斯蒂安·埃尔卡诺风格：返航才是真正的航行，一艘漏水的船横渡印度洋，数月不靠港，记纬度、数船员，环球由并非发起者的人完成。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，印度洋—大西洋返航数月无靠港，靠纬度与航向推算。`artifact`
- 定向：摩鹿加出发，绕好望角返航，乘信风与西风，避葡萄牙港口。`artifact`
- 误差容忍：船漏、补给尽，仍按纬度航行，佛得角被迫停靠补给后被扣人。`artifact`

## (3) 造船与帆装

- 船型：维多利亚号单船返航，余船或沉或弃，单船载 18 人返抵塞维利亚。`artifact`
- 帆装：横帆远洋，宜信风与西风。`impression`
- 补给：返航全程补给告罄，佛得角偷补给被葡萄牙扣留 13 人。`artifact`

## (4) 航线规划习惯

- 路线：摩鹿加—帝汶—印度洋—好望角—大西洋—佛得角—塞维利亚（1522）。`artifact`
- 节奏：返航约 9 个月，数月不靠港，快慢由风与漏水定。`artifact`
- 返航：本次航行本身就是返航——去程麦哲伦，返程埃尔卡诺。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，返航见于皮加费塔记述与船员供词；维多利亚号日志有抄本残存。`artifact`
- 海图语言：纬度与漏水、减员数字并重，返航线为一条孤线。`impression`
- 命名习惯：以圣人与港口命名返航段。`impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 印度洋—大西洋返航航线
- 单船环球返航
- 好望角返航航法
- 无靠港长航补给
- 不该探索：
- No return leg without a latitude for every day
- No Portuguese port entered on the way home
- No leak ignored until the pumps fail
- No circumnavigation claimed before the ship is home
- Negative prompt: `No return leg without a latitude for every day, No Portuguese port entered on the way home, No leak ignored until the pumps fail, No circumnavigation claimed before the ship is home`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Juan Sebastián Elcano, one leaking uncrewed ship makes the return leg across the Indian Ocean in 2026, no port of call for months, latitudes logged and the stores counted down.`
- 中文对照：胡安·塞巴斯蒂安·埃尔卡诺风格：一艘漏水的无人船2026年返航横渡印度洋，数月不靠港，记纬度、数给养。
- Negative: `No return leg without a latitude for every day, No Portuguese port entered on the way home, No leak ignored until the pumps fail, No circumnavigation claimed before the ship is home`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
