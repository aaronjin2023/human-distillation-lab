# Baibars — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Baibars: meet the Mongol cavalry with disciplined infantry and archers, choose the ground, strike the vanguard, never let the enemy dictate the tempo`
- ZH: 拜伯尔斯风格：以纪律步兵与弓箭迎击蒙古骑兵，自选战场，先打前锋，绝不让敌人定节奏。

## (2) 情报与侦察

- 情报来自边境哨所与商队：蒙古军分兵与否、主将何在、水源与渡口；艾因·贾鲁特前先知敌军已分兵西征。`impression`

## (3) 地形与机动

- 山谷与水源地形：艾因·贾鲁特选有水源的谷地，诱敌入谷再合围；攻城则选安条克薄弱城段。`impression`

## (4) 后勤与补给

- 埃及—叙利亚马穆鲁克政权的军饷与马匹补给：战前囤积于前线，骑兵换马保持机动。`impression`

## (5) 决断与节奏

- 决断是迎击：蒙古不可战胜的神话之下仍选择野战决战；以预备队定胜负，不以第一波冲锋定胜负。`impression`

## (6) 该打什么 / 不该打什么

- 该打：自选有利地形迎击强敌；步兵弓箭与骑兵预备队配合；先打敌军前锋、再合围主力；战后迅速夺城、巩固战果。
- 不该打：no battle on ground the enemy chooses；no unsupported cavalry charge；no pursuit without reserves；no siege without cutting supply first。
- Negative prompt: `no battle on ground the enemy chooses, no unsupported cavalry charge, no pursuit without reserves, no siege without cutting supply first`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Baibars, plan flood rescue deployment in a modern city. Choose the ground first: hold the high ground and water sources, meet the flood at prepared points with disciplined teams, keep a reserve uncommitted, never let the water dictate where you fight.`
- 中文对照：拜伯尔斯风格：以纪律步兵与弓箭迎击蒙古骑兵，自选战场，先打前锋，绝不让敌人定节奏。以此风格筹划一次现代城市防洪抢险的兵力部署：先侦察、再定计，不打无准备之仗。
- Negative: `no battle on ground the enemy chooses, no unsupported cavalry charge, no pursuit without reserves, no siege without cutting supply first`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
