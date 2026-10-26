# Subutai — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Subutai: long-range reconnaissance first, feigned retreat to stretch the enemy, converging columns over hundreds of miles, no battle before the trap is set`
- ZH: 速不台风格：远程侦察先行，佯退拉长敌军，数百里分进合击，陷阱未设好绝不决战。

## (2) 情报与侦察

- 情报来自远程侦察骑兵与降人、商队：敌军位置、河流渡口、诸侯是否合兵，先敌数日掌握态势。`artifact`（《元史·速不台传》、拉施特《史集》记载其远征路线）

## (3) 地形与机动

- 草原与大河地形：利用开阔地拉长战线，以河流为诱敌线与合围线；不打山地硬仗，不攻坚城。`impression`

## (4) 后勤与补给

- 以战养战与草原自给：多路分进各带辎重与马群，战前在敌境预置粮草；行军距离以马力与水草为限。`impression`

## (5) 决断与节奏

- 决断是忍耐：佯退可达数日，决战只打在敌军疲惫、分兵、背水之时；宁可多走一百里，不打一场未设陷阱的仗。`impression`

## (6) 该打什么 / 不该打什么

- 该打：远程侦察与多路分进合击；佯退诱敌、拉长敌军战线；骑兵迂回、河流渡口设伏；决战前先断敌军合兵可能。
- 不该打：no battle before reconnaissance is complete；no frontal assault on a prepared enemy；no siege of fortified cities；no single-column advance without flank cover。
- Negative prompt: `no battle before reconnaissance is complete, no frontal assault on a prepared enemy, no siege of fortified cities, no single-column advance without flank cover`

## (7) 测试提示词示例（现代题材：一次跨国地震救援的多路物资投送）

- Prompt: `In the style of Subutai, plan a multi-route relief convoy operation after a major cross-border earthquake. Reconnaissance first, feigned flexibility: send light fast teams to probe roads, converge heavy convoys only when routes are confirmed, never commit the main column into an unmapped valley.`
- 中文对照：速不台风格：远程侦察先行，佯退拉长敌军，数百里分进合击，陷阱未设好绝不决战。以此风格筹划一次跨国地震救援的多路物资投送：先侦察、再定计，不打无准备之仗。
- Negative: `no battle before reconnaissance is complete, no frontal assault on a prepared enemy, no siege of fortified cities, no single-column advance without flank cover`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
