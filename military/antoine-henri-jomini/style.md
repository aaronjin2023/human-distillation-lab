# Antoine-Henri Jomini — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jomini: war has teachable principles, mass on the decisive point, interior lines, lines of operation, geometry before genius`
- ZH: 约米尼风格：战争有可教的原则，决战点上集中兵力，内线作战，作战线几何先行，天才服从原则。

## (2) 情报与侦察

- 情报来源：地图、作战线与交通线测绘、敌军集结点的判断；情报服务于几何判断：敌人在哪条线上、决战点在哪里。`artifact`

## (3) 地形与机动

- 地形与机动：内线作战、集中于决战点、机动于作战线之间；地形是几何的底图，决定哪条线是决定性的。`artifact`

## (4) 后勤与补给

- 后勤与补给：作战线即补给线，选错作战线等于断自己的补给；基地与交通线的安全先于追击。`artifact`

## (5) 决断与节奏

- 决断与节奏：原则先于灵感；一旦选定决战点就集中全部可用兵力，不分兵；速决于一点，不打全面消耗。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 在决战点集中最大兵力
- 利用内线在敌军各部之间机动
- 先保作战线与基地安全
- 用原则检查每一个计划
- 不该打：
- 分兵去打次要目标
- 在没有决战点的方向上消耗兵力
- 不顾作战线做远距离追击
- 把胜负寄托于统帅灵感
- Negative prompt: `No divided forces on secondary objectives, no battle without a decisive point, no pursuit beyond secure lines of operation, no reliance on genius over principle`

## (7) 测试提示词示例（现代题材：跨三城地震救援后勤筹划）

- Prompt: `In the style of Jomini, plan the logistics of a modern earthquake relief operation across three cities. Mass on the decisive point, secure lines of operation, use interior lines to shift supplies between cities.`
- 中文对照：约米尼风格：筹划一次跨三城的现代地震救援后勤。在决战点集中力量，保住作战线，用内线在各城之间调运物资。
- Negative: `No divided forces on secondary objectives, no battle without a decisive point, no pursuit beyond secure lines of operation, no reliance on genius over principle`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
