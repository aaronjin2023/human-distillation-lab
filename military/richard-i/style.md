# Richard I — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard I: march in a fighting box, never break formation for a skirmish; strike with the cavalry only when the enemy is committed, then march on`
- ZH: 理查一世风格：以战斗队形行军，绝不为小股袭扰破阵；只在敌军全数压上时才出骑兵，打完继续行军。

## (2) 情报与侦察

- 情报来自斥候与俘虏：萨拉丁军袭扰习惯、阿尔苏夫地形、水源；先知敌军以袭扰诱我破阵。`impression`

## (3) 地形与机动

- 巴勒斯坦海岸与平原地形：阿尔苏夫以行军队形沿海岸推进，步兵在外、骑兵在内。`impression`

## (4) 后勤与补给

- 十字军海运补给：以海路供养大军，沿海岸行军不断补给。`impression`

## (5) 决断与节奏

- 决断是队形与忍耐：阿尔苏夫行军中任敌袭扰而不破阵，敌军全数压上时才令骑兵冲锋；雅法以少胜多而守城。`impression`

## (6) 该打什么 / 不该打什么

- 该打：战斗队形行军、步兵在外；任敌袭扰、不破阵；敌军全压上时骑兵冲锋；打完继续行军、不恋战。
- 不该打：no breaking formation for a skirmish；no cavalry charge before the enemy is committed；no march without sea supply；no siege of Jerusalem without the army to hold it。
- Negative prompt: `no breaking formation for a skirmish, no cavalry charge before the enemy is committed, no march without sea supply, no siege of Jerusalem without the army to hold it`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Richard I, plan flood rescue deployment in a modern city. March in a fighting box: infantry outside, cavalry inside, never break formation for a skirmish, strike only when the flood is fully committed, then march on.`
- 中文对照：理查一世风格：以战斗队形行军，绝不为小股袭扰破阵；只在敌军全数压上时才出骑兵，打完继续行军。以此风格筹划一次现代城市防洪抢险的兵力部署：先侦察、再定计，不打无准备之仗。
- Negative: `no breaking formation for a skirmish, no cavalry charge before the enemy is committed, no march without sea supply, no siege of Jerusalem without the army to hold it`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
