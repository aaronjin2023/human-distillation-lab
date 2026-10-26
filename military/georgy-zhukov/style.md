# Georgy Zhukov — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhukov: mass, depth and reserves, hold then strike, commit the reserve at the decisive moment, accept losses to break the enemy, never waste the counteroffensive`
- ZH: 朱可夫风格：数量、纵深与预备队，先顶住再反击，决战时刻投入预备队，承受损失也要打垮敌人，绝不浪费反攻。

## (2) 情报与侦察

- 情报来源：前线侦察、航空侦察、俘虏与密码情报；核心判断是敌主攻方向与进攻顶点何时到来。`artifact`

## (3) 地形与机动

- 地形与机动：纵深防御、两翼包围、预备队纵深配置；城市与河流是消耗敌人的磨盘，机动留给反攻。`artifact`

## (4) 后勤与补给

- 后勤与补给：以空间与人力换时间，后方动员与铁路决定反攻能走多远；补给跟着预备队走。`artifact`

## (5) 决断与节奏

- 决断与节奏：先顶住、再反击；预备队不到决战时刻不动，一动即定胜负；宁要反攻的彻底，不求前线的体面。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 纵深防御消耗敌人
- 预备队捏在手里到决战时刻
- 两翼包围、合围歼敌
- 反攻一发动就打到底
- 不该打：
- 前线寸土不让、预备队提前打光
- 没有预备队就发动反攻
- 追击越过补给与顶点
- 为保全面子打消耗战
- Negative prompt: `No holding every inch at the cost of reserves, no counteroffensive without a reserve, no pursuit past supply and the culminating point, no attrition for the sake of face`

## (7) 测试提示词示例（现代题材：城市抵御特大山火）

- Prompt: `In the style of Zhukov, plan a modern city defence against a major wildfire. Hold the inner lines, wear the fire down, keep a reserve crew uncommitted until the wind turns, then strike along both flanks.`
- 中文对照：朱可夫风格：筹划一次现代城市抵御特大山火的防御。守住内线、消耗火势，预备队捏到风向转变再投入，两翼合围。
- Negative: `No holding every inch at the cost of reserves, no counteroffensive without a reserve, no pursuit past supply and the culminating point, no attrition for the sake of face`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
