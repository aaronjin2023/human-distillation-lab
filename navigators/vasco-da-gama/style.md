# Vasco da Gama — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Vasco da Gama: a long offshore arc across the South Atlantic, no coast in sight for weeks, then the monsoon run to India, latitudes logged daily, a voyage planned as one great curve rather than a coastal crawl`
- ZH: 瓦斯科·达·伽马风格：南大西洋上一道漫长的离岸大弧，数周不见陆地，再乘季风直抵印度，每日记纬度，航行按一道大弧规划而非贴岸爬行。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，南大西洋大弧航行（volta）数周不见陆地，靠纬度与航向推算船位。`artifact`
- 定向：离岸大弧借东南信风南下，再乘西南季风横渡阿拉伯海至卡利卡特。`artifact`
- 误差容忍：长段无地标航行，误差以到岸后的纬度实测纠正；季风窗口错过即等。`impression`

## (3) 造船与帆装

- 船型：四船船队，旗舰圣加布里埃尔号等，卡拉克大帆船，远洋载货与武装并重。`artifact`
- 帆装：横帆为主，宜顺风远洋；大弧航行靠信风，不靠抢风。`impression`
- 补给：沿途莫桑比克、蒙巴萨、马林迪补给，马林迪得领航员指引横渡印度洋。`artifact`
- 防坏血病：首航坏血病严重，船员大量死亡，返航仅余半数——补给与卫生为硬教训。`artifact`

## (4) 航线规划习惯

- 路线：里斯本—佛得角—南大西洋大弧—好望角—莫桑比克—马林迪—季风横渡—卡利卡特（1498）。`artifact`
- 节奏：大弧段慢而稳，季风段快；去程约 10 个月，返程近一年。`artifact`
- 返航：逆季风返航，坏血病与风暴致船员锐减，圣拉斐尔号焚毁。`artifact`

## (5) 日志与海图语言

- 日志体例：首航日志有抄本传世（佚名《达·伽马首航日志》），逐日记纬度、风向与海岸。`artifact`
- 海图语言：纬度数字密集，海岸地名随航行逐段出现。`artifact`
- 命名习惯：以圣人名命名船只与登陆日。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 欧洲—印度直航
- 南大西洋大弧航法
- 季风横渡阿拉伯海
- 东非沿岸补给港序列
- 不该探索：
- No coastal crawl where a great offshore arc serves
- No monsoon crossing outside the monsoon window
- No port entered without sounding and a local pilot
- No return leg sailed without water and provisions counted
- Negative prompt: `No coastal crawl where a great offshore arc serves, No monsoon crossing outside the monsoon window, No port entered without sounding and a local pilot, No return leg sailed without water and provisions counted`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Vasco da Gama, an uncrewed cargo ship takes a long offshore arc across the South Atlantic in 2026, no coast in sight for weeks, then the monsoon run onward, latitudes logged daily.`
- 中文对照：瓦斯科·达·伽马风格：一艘无人货轮2026年在南大西洋上走一道漫长的离岸大弧，数周不见陆地，再乘季风继续前行，每日记纬度。
- Negative: `No coastal crawl where a great offshore arc serves, No monsoon crossing outside the monsoon window, No port entered without sounding and a local pilot, No return leg sailed without water and provisions counted`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
