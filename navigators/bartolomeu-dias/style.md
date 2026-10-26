# Bartolomeu Dias — 航海方法与探索风格规格 style.md（给文本/图像模型）

> 只描述航海方法与风格，不描述人生。引用日志原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bartolomeu Dias: a patient southward grind broken by one long storm-driven run offshore, the cape found only on the way back, plain log of latitudes and headlands, no triumph in the wording`
- ZH: 巴尔托洛梅乌·迪亚士风格：耐心南下磨出来的航行，一次风暴驱使的离岸长航，返航时才发现海角，纬度与岬角的朴素日志，措辞里没有凯旋。

## (2) 导航方法

- 定位：推测航法 + 纬度观测，南下至北极星没入地平线以下，靠南十字星定南纬。`artifact`
- 定向：沿岸南下，遇风暴离岸 13 日向南漂流，转向东行发现陆地在东——海角已过。`artifact`
- 误差容忍：风暴中不强行定位，漂流后再以纬度与海岸走向重定船位。`impression`

## (3) 造船与帆装

- 船型：两艘 50 吨卡拉维尔加一艘补给船，1487 年 8 月自里斯本出发。`artifact`
- 帆装：拉丁帆与横帆并用，风暴中降帆漂流。`impression`
- 补给：补给船随行至中途，返航时补给不足为折返原因之一。`artifact`

## (4) 航线规划习惯

- 路线：里斯本—西非沿岸—风暴离岸南漂—转向东行—莫塞尔湾—阿尔戈亚湾—返航绕过好望角。`artifact`
- 节奏：南下慢、风暴快、返航时才确认海角；全程约 16 个月。`artifact`
- 返航：船员疲惫、补给将尽，折返途中才绕过海角并命名“风暴角”，若昂二世改名“好望角”。`artifact`

## (5) 日志与海图语言

- 日志体例：无亲笔日志传世，航路见于编年史与若昂·德·巴罗斯《亚洲》；蒸馏以编年史航路为准。`artifact`
- 海图语言：纬度与岬角为主，海角位置为关键一笔。`impression`
- 命名习惯：初名“风暴角”，王改“好望角”——命名权在王不在船长。`artifact`

## (6) 该探索什么 / 不该探索什么

- 该探索：
- 好望角与南非东海岸
- 南大西洋风暴离岸航法
- 印度洋入口
- 南纬星象导航
- 不该探索：
- No cape claimed before it is rounded on the return leg
- No storm sailed through when drifting is survivable
- No southward push past the last supply ship
- No triumphal wording for a cape found by accident
- Negative prompt: `No cape claimed before it is rounded on the return leg, No storm sailed through when drifting is survivable, No southward push past the last supply ship, No triumphal wording for a cape found by accident`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Bartolomeu Dias, an uncrewed ship grinds south in 2026 and is driven offshore by one long storm, finding the cape only on the way back, its log a plain record of latitudes and headlands.`
- 中文对照：巴尔托洛梅乌·迪亚士风格：一艘无人船2026年耐心南下，被一场漫长风暴驱向离岸，返航时才发现海角，日志是纬度与岬角的朴素记录。
- Negative: `No cape claimed before it is rounded on the return leg, No storm sailed through when drifting is survivable, No southward push past the last supply ship, No triumphal wording for a cape found by accident`
- 检验点：导航方法是否可辨；航线规划习惯是否成立；禁区写法是否出现。
