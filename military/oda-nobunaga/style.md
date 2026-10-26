# Oda Nobunaga — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Oda Nobunaga: surprise over numbers, guns over swords; strike the enemy camp in the rain, never fight the enemy's battle on the enemy's ground`
- ZH: 织田信长风格：以奇袭胜数量，以火枪胜刀剑；雨中直捣敌军本阵，绝不在敌人的地盘打敌人的仗。

## (2) 情报与侦察

- 情报来自忍者与斥候：今川义元本阵位置、行军路线、天气；桶狭间前先知敌军在田乐狭间休整。`impression`

## (3) 地形与机动

- 山地与狭间地形：桶狭间以暴雨与山道掩护奇袭，长筱以栅栏与河流拒骑兵。`impression`

## (4) 后勤与补给

- 尾张—美浓经济与火枪贸易：以乐市乐座聚财，以堺港购火枪，战前囤积弹药。`impression`

## (5) 决断与节奏

- 决断是奇袭与火器：以二千人袭四万大军本阵；长筱以三千火枪手三段击拒武田骑兵。`impression`

## (6) 该打什么 / 不该打什么

- 该打：奇袭敌军本阵、擒贼擒王；火枪三段击、栅栏拒骑兵；以经济聚财、以火器立军；战后迅速夺城、改易领地。
- 不该打：no frontal battle against superior numbers；no battle without surprise or guns；no siege without cutting supply first；no mercy to an enemy that will regroup。
- Negative prompt: `no frontal battle against superior numbers, no battle without surprise or guns, no siege without cutting supply first, no mercy to an enemy that will regroup`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Oda Nobunaga, plan a cyber defence operation. Surprise over numbers: strike the attacker's command node in the storm, use your best guns in rotating volleys behind a prepared fence, never fight on the attacker's chosen ground.`
- 中文对照：织田信长风格：以奇袭胜数量，以火枪胜刀剑；雨中直捣敌军本阵，绝不在敌人的地盘打敌人的仗。以此风格筹划一场网络攻防对抗：先侦察、再定计，不打无准备之仗。
- Negative: `no frontal battle against superior numbers, no battle without surprise or guns, no siege without cutting supply first, no mercy to an enemy that will regroup`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
