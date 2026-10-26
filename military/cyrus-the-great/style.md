# Cyrus the Great — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Cyrus the Great: win by tolerance and speed, absorb the enemy army into your own, strike the capital before the coalition forms, govern the conquered as subjects not slaves`
- 中文：居鲁士风格：以宽容与速度取胜，收编敌军为己用，在联盟成形之前直取首都，把被征服者当作臣民而非奴隶来治理。

## （2）情报与侦察

情报来自使节、商队与被征服地的投诚者；先摸清诸国联盟的动向与君主的性格，再决定先打谁。情报用来分化联盟：对愿降者许以宽容，对顽抗者示以速决。`artifact`

## （3）地形与机动

偏好开阔平原与河流渡口的决战；机动方式是多路并进、直取首都，骑兵与步兵协同，攻城时用水攻与土木作业（如引开幼发拉底河）。`artifact`

## （4）后勤与补给

补给靠沿途城市投诚后的就地取给与王室驿道；远征前先经营基地与盟友，行军距离受河流与季节约束，攻城器械随军携带。`impression`（学界共识：波斯驿道与补给组织）

## （5）决断与节奏

决断风格：速决与宽容并用，冒险倾向中等——敢于以少敌多打决战，但不打无把握的消耗战；破城后立即停手转向治理，不追杀残敌。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 多路并进直取敌首都
- 收编降军与降将为己用
- 对投降城市许以宽容与自治
- 以骑兵机动配合步兵决战
- 攻城时用水攻、土木作业绕开城墙

**不该打（风格上的禁区）：**

- 围城硬耗而不寻他法
- 屠城立威、激起全境死战
- 分兵去打互不相干的次要目标
- 破城后纵兵劫掠、毁掉治理基础
- 在联盟成形后再逐个硬打

**Negative prompt（可直接给文本模型）：**

`no prolonged siege without an alternative, no massacre of surrendered cities, no divided forces on unrelated targets, no plunder after victory, no battle after the coalition has formed`

## （7）测试提示词示例（现代题材：一次跨国企业的市场进入战）

- Prompt: `In the style of Cyrus the Great, plan a multinational company's entry into a new regional market. Win by tolerance and speed: absorb local partners instead of crushing them, strike the decisive city first, govern the acquired business as a partner not a conquest.`
- 中文对照：以居鲁士的风格，筹划一家跨国企业进入新区域市场：以宽容与速度取胜，收编本地伙伴而非压垮他们，先取决定性城市，把并购来的业务当作伙伴而非战利品来治理。
- Negative: `no scorched-earth price war, no plunder of the acquired team, no slow siege of every small competitor`
