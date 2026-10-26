# Norman Schwarzkopf — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Schwarzkopf: joint operations, air power first then the great left hook, overwhelming force, deception and mass, end the war fast`
- ZH: 施瓦茨科普夫风格：联合作战，先空袭再大左勾拳，压倒性兵力，欺骗与集中，速战速决。

## (2) 情报与侦察

- 情报来源：卫星与空中侦察、电子侦察、敌部署测绘；核心判断是敌军主力在哪里、左勾拳的缺口在哪里。`artifact`

## (3) 地形与机动

- 地形与机动：沙漠大纵深迂回（左勾拳）、空地一体；机动即装甲纵队的沙漠穿越。`artifact`

## (4) 后勤与补给

- 后勤与补给：沙漠风暴的命脉是海运与空运的巨量补给；补给不到位，左勾拳打不出去。`artifact`

## (5) 决断与节奏

- 决断与节奏：先空袭、再地面：空中削弱敌军数周，地面左勾拳几天定局；压倒性兵力、不打势均力敌。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 空袭先行、削弱敌军
- 大纵深迂回（左勾拳）
- 联合作战、多军种一体
- 压倒性兵力、速决
- 不该打：
- 没有空中准备就地面进攻
- 正面硬碰敌军主力
- 各军种各打各的
- 把速决战拖成消耗战
- Negative prompt: `No ground offensive without air preparation, no frontal blow against the enemy main force, no service fighting alone, no quick war dragged into attrition`

## (7) 测试提示词示例（现代题材：封锁后重开港口的多国行动）

- Prompt: `In the style of Schwarzkopf, plan a modern multinational port-reopening operation after a blockade. Air and sea power first to clear the approaches, then a wide flanking move by land, overwhelming force, finish fast.`
- 中文对照：施瓦茨科普夫风格：筹划一次封锁后重开港口的现代多国行动。先以海空力量打通外围，再陆上大迂回，压倒性兵力、速战速决。
- Negative: `No ground offensive without air preparation, no frontal blow against the enemy main force, no service fighting alone, no quick war dragged into attrition`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
