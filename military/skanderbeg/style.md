# Skanderbeg — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Skanderbeg: mountain defence of a single fortress, small force holding against a large army, ambush on the march, raid the supply line, never accept a pitched battle you cannot win`
- ZH: 斯坎德培风格：以一座山地要塞抗衡大军，小部队坚守，行军途中设伏，袭扰补给线，绝不打赢不了的会战。

## (2) 情报与侦察

- 情报靠山地哨所与本地居民；熟悉奥斯曼军进军路线与季节，伏击多设在隘口与补给道上。`impression`

## (3) 地形与机动

- 地形偏好：山地要塞与隘口；克鲁亚居高临下，周围山道狭窄，大军无法展开。`artifact`

## (4) 后勤与补给

- 后勤靠要塞囤积与山地就地取给；长期抗战依赖威尼斯与那不勒斯的间歇援助，补给从不稳定。`artifact`

## (5) 决断与节奏

- 决断：持久、诱敌、避战；宁愿放弃平原也要保住克鲁亚，25年抗战以不败为胜。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 坚守克鲁亚要塞，诱敌围攻消耗
- 在山道隘口伏击敌军行军队
- 袭扰敌军补给线与孤立据点
- 以小部队机动牵制大军
- 不该打：
- No pitched battle on open plains
- No defence of indefensible lowland towns
- No pursuit into Ottoman territory
- No battle without a mountain retreat route
- Negative prompt: `No pitched battle on open plains, No defence of indefensible lowland towns, No pursuit into Ottoman territory, No battle without a mountain retreat route`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Skanderbeg, plan a cross-border earthquake relief operation. Hold one mountain hub as the base, send small mobile teams through the passes, ambush the bottlenecks of delay rather than fighting them head-on, and never commit all teams to one open route.`
- 中文对照：斯坎德培风格：以一座山地要塞抗衡大军，小部队坚守，行军途中设伏，袭扰补给线，绝不打赢不了的会战。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No pitched battle on open plains, No defence of indefensible lowland towns, No pursuit into Ottoman territory, No battle without a mountain retreat route`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
