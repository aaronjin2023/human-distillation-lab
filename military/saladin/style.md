# Saladin — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Saladin: unify first, fight second; patience as a weapon, cut the enemy's water and unity, strike only when the crusader army is thirsty, divided and far from its base`
- ZH: 萨拉丁风格：先统一、后决战；以忍耐为武器，断敌水源与团结，只打敌军干渴、分裂、远离基地之时。

## (2) 情报与侦察

- 情报来自边境斥候与地方领主：十字军出兵规模、行军路线、水源位置；先敌判断其是否敢离城野战。`impression`

## (3) 地形与机动

- 干旱丘陵与水源地形：哈丁以无水高地为陷阱，迫敌在烈日下行军；围城先断水源，不打水源充足之敌。`artifact`

## (4) 后勤与补给

- 埃及—叙利亚统一后的赋税与补给：以统一政权供养常备军，战前囤积粮草于前线城池；十字军则依赖沿海补给线。`impression`

## (5) 决断与节奏

- 决断是克制：十年统一叙利亚与埃及而不与十字军主力决战；哈丁之前屡次放敌回城，只等敌军自己走进无水之地。`impression`

## (6) 该打什么 / 不该打什么

- 该打：先统一后方、再对外决战；断水源、断补给、诱敌离城；以逸待劳、烈日下拖垮敌军；破城后立约保全，不屠城立威。
- 不该打：no decisive battle before the rear is unified；no battle against a watered, supplied enemy；no pursuit beyond the culminating point；no massacre after surrender。
- Negative prompt: `no decisive battle before the rear is unified, no battle against a watered, supplied enemy, no pursuit beyond the culminating point, no massacre after surrender`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗中的持久消耗）

- Prompt: `In the style of Saladin, plan a long cyber defence campaign. Unify your own systems first, never fight the decisive battle on the attacker's terms: let the attacker exhaust itself against hardened targets, cut its command channels, strike only when it is overextended and exposed.`
- 中文对照：萨拉丁风格：先统一、后决战；以忍耐为武器，断敌水源与团结，只打敌军干渴、分裂、远离基地之时。以此风格筹划一场网络攻防对抗中的持久消耗：先侦察、再定计，不打无准备之仗。
- Negative: `no decisive battle before the rear is unified, no battle against a watered, no supplied enemy, no pursuit beyond the culminating point, no massacre after surrender`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
