# Gil Eanes — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gil Eanes: a coastal captain's breakthrough, small caravel hugging the shore until the cape, dead reckoning and compass, one bold offshore leg past the dreaded cape, plain log of soundings and landmarks`
- ZH: 吉尔·埃亚内斯风格：沿岸船长的突破，小卡拉维尔贴岸航行至海角，推测航法与罗盘，离岸一大段绕过可怖之角，测深与地标的朴素日志。

## (2) 导航方法

- 定位：推测航法（dead reckoning）为主，罗盘定航向，航速靠计程估算，纬度靠北极星高度。`impression`
- 定向：沿岸认岸——岬角、河口、沙洲为路标；博哈多尔角一带先贴岸、后离岸绕行。`artifact`
- 误差容忍：近岸误差以测深锤与目视修正，远洋段宁可多绕不冒险贴礁。`impression`

## (3) 造船与帆装

- 船型：卡拉维尔（caravel），小而灵活，三角帆宜抢风，宜沿岸探查。`artifact`
- 帆装：拉丁帆，逆风可抢风航行，是绕过博哈多尔角的关键。`impression`
- 补给：短程沿岸航行，淡水与食物按港口补给，不做远洋补给。`impression`

## (4) 航线规划习惯

- 路线：葡萄牙—摩洛哥沿岸—博哈多尔角，贴岸南下，绕角后返航；去程贴岸、绕角段离岸。`artifact`
- 节奏：短程试探，1433 年失败后 1434 年再试，一次突破即返航报信。`artifact`
- 返航：原路北返，带回“海角可绕”的结论与航路。`impression`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，事迹见于葡萄牙编年史（祖拉拉）；蒸馏以编年史所载航路为准。`artifact`
- 海图语言：地标与测深为主，博哈多尔角为关键路标。`impression`
- 命名习惯：以岬角与河口命名航段。`impression`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 博哈多尔角以南海岸
- 西非沿岸贴岸航线
- 卡拉维尔离岸绕角法
- 沿岸测深与认岸
- 不该探索：
- No open-ocean crossing without a landmark or sounding
- No cape rounded without first sounding the approach
- No return without a fix on the cape's position
- No claim of a sea route beyond the farthest sounding
- Negative prompt: `No open-ocean crossing without a landmark or sounding, No cape rounded without first sounding the approach, No return without a fix on the cape's position, No claim of a sea route beyond the farthest sounding`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Gil Eanes, a small uncrewed vessel hugs the shore in 2026 until the cape, dead reckoning and compass, one bold offshore leg past the dreaded cape, a plain log of soundings and landmarks.`
- 中文对照：吉尔·埃亚内斯风格：一艘小型无人船2026年贴岸航行至海角，推测航法与罗盘，离岸一大段绕过可怖之角，测深与地标的朴素日志。
- Negative: `No open-ocean crossing without a landmark or sounding, No cape rounded without first sounding the approach, No return without a fix on the cape's position, No claim of a sea route beyond the farthest sounding`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
