# Turenne — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Turenne: manoeuvre before battle, win by marching, deceive with a feint, strike the supply line, avoid a frontal battle until the enemy is already beaten by movement`
- ZH: 蒂雷纳风格：战前先机动，以行军取胜，佯动欺敌，打补给线，直到敌人已被调动拖垮才打正面会战。

## (2) 情报与侦察

- 情报靠侦察骑兵与地形测绘；蒂尔克海姆前对孚日山地隘口与敌军补给线了如指掌。`impression`

## (3) 地形与机动

- 地形偏好：山地隘口与河流渡口；以地形掩护迂回，迫敌分兵。`artifact`

## (4) 后勤与补给

- 后勤靠就地取给与快速行军；冬季行军穿越孚日山地本身就是对补给能力的考验。`artifact`

## (5) 决断与节奏

- 决断：机动优于会战；宁愿多走路也要少打硬仗，决战只打已胜之仗。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以佯动与迂回调动敌军，分散其兵力
- 先打补给线与渡口，再打主力
- 利用山地与河流掩护行军
- 在敌军疲惫分散时才决战
- 不该打：
- No frontal battle against a concentrated enemy
- No attack without first manoeuvring the enemy out of position
- No winter campaign without secured supply
- No pursuit without a retreat route
- Negative prompt: `No frontal battle against a concentrated enemy, No attack without first manoeuvring the enemy out of position, No winter campaign without secured supply, No pursuit without a retreat route`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Turenne, analyse a modern cyber conflict. Win by manoeuvre before any direct clash: feint at one target, cut the supply line of the attack, use the terrain of the network to outflank, and only engage when the opponent is already dispersed and exhausted.`
- 中文对照：蒂雷纳风格：战前先机动，以行军取胜，佯动欺敌，打补给线，直到敌人已被调动拖垮才打正面会战。以此风格筹划一场网络攻防对抗。
- Negative: `No frontal battle against a concentrated enemy, No attack without first manoeuvring the enemy out of position, No winter campaign without secured supply, No pursuit without a retreat route`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
