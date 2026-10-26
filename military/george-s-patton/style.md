# George S. Patton — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Patton: attack, attack, attack, speed is the weapon, never hold what you have gained, keep the enemy off balance`
- ZH: 巴顿风格：进攻、进攻、进攻，速度就是武器，绝不固守已得之地，让敌人始终失衡。

## (2) 情报与侦察

- 情报来源：前沿侦察、空中侦察、俘虏口供；核心判断是敌人在哪里动摇，就从哪里撕开。`artifact`

## (3) 地形与机动

- 地形与机动：装甲纵队快速纵深、两翼包抄；地形只决定速度，不决定是否进攻。`artifact`

## (4) 后勤与补给

- 后勤与补给：速度的代价是燃油；补给跟不上就停，但停是为了再进攻，不是为了防守。`artifact`

## (5) 决断与节奏

- 决断与节奏：不停进攻；宁可打错方向的进攻，也不坐等完美的计划；士气靠进攻维持。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 不停进攻、保持速度
- 装甲纵深、两翼包抄
- 让敌人始终失衡
- 靠前指挥、现场决断
- 不该打：
- 固守已得之地
- 等完美计划再进攻
- 没有速度的正面消耗
- 让补给短缺变成停滞的借口而不想办法
- Negative prompt: `No holding ground instead of attacking, no waiting for the perfect plan, no frontal attrition without speed, no halt treated as a defensive posture`

## (7) 测试提示词示例（现代题材：山火围堵行动）

- Prompt: `In the style of Patton, plan a modern wildfire containment operation. Attack the fire line continuously, keep crews moving along both flanks, never sit on a held line while the fire regroups.`
- 中文对照：巴顿风格：筹划一次现代山火围堵行动。持续进攻火线，两翼不停机动，绝不固守一条防线等火势重整。
- Negative: `No holding ground instead of attacking, no waiting for the perfect plan, no frontal attrition without speed, no halt treated as a defensive posture`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
