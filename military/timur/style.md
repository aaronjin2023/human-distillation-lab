# Timur — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Timur: terror as logistics, speed as siege, never fight the enemy's war; break the army in the field, then the city surrenders itself`
- ZH: 帖木儿风格：以威慑为后勤，以速度为攻城；绝不打敌人的仗；野战先破敌军，城池自会投降。

## (2) 情报与侦察

- 情报来自商队与间谍网：敌国君主位置、军队集结地、城防弱点；安卡拉前先知奥斯曼军缺水。`impression`

## (3) 地形与机动

- 草原—绿洲—大河地形：长途奔袭选水草线，决战选开阔地发挥骑兵，攻城选断水之城。`impression`

## (4) 后勤与补给

- 以战养战与恐怖威慑：大军行军靠沿途征发与缴获，攻克一城即以其资供下一城；补给线短、速度快。`impression`

## (5) 决断与节奏

- 决断是速度与狠：三十五年征战不停，敌军未集结即遭打击；安卡拉生擒巴耶济德一世，决战即擒王。`impression`

## (6) 该打什么 / 不该打什么

- 该打：长途奔袭、敌未集结先打；野战破军、再图城池；断水断粮、迫敌野战；以俘虏与工匠充实后方。
- 不该打：no prolonged siege against a supplied city；no battle on ground the enemy fortifies；no winter campaign without supply；no mercy that leaves an enemy army intact。
- Negative prompt: `no prolonged siege against a supplied city, no battle on ground the enemy fortifies, no winter campaign without supply, no mercy that leaves an enemy army intact`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Timur, plan a cross-border earthquake relief operation. Speed is the siege: move before roads close, strike the worst-hit zone first with everything, let momentum open the next route, never wait for perfect supply lines.`
- 中文对照：帖木儿风格：以威慑为后勤，以速度为攻城；绝不打敌人的仗；野战先破敌军，城池自会投降。以此风格筹划一次地震后的跨国救援行动：先侦察、再定计，不打无准备之仗。
- Negative: `no prolonged siege against a supplied city, no battle on ground the enemy fortifies, no winter campaign without supply, no mercy that leaves an enemy army intact`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
