# Xu Da — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Xu Da: steady advance, take the city by surrounding it not by storming it, the northern expedition is won by logistics and by never overreaching`
- 中文：徐达风格：稳步推进，以围城取城而非强攻，北伐是靠后勤、靠绝不冒进赢来的。

## （2）情报与侦察

情报来自斥候、降将与对元军部署的精通；先摸清元军部署与大都城防，再以北伐破之。情报用来选北伐路线，不做硬攻。`artifact`

## （3）地形与机动

偏好华北平原的稳步北伐；机动方式是分路并进、围而不攻，辅以骑兵追击。`artifact`

## （4）后勤与补给

补给靠明朝国力与沿途屯田，北伐距离受粮道与季节约束；稳步推进是其后勤的答案。`artifact`

## （5）决断与节奏

决断风格：稳健与果断并用——北伐元大都，一战而定；决战时机只选己方占优时，绝不冒进。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 稳步推进、分路并进
- 围而不攻、取城而不强攻
- 战前先经营粮道与屯田
- 只打己方占优的仗
- 战后立即招降、巩固战果

**不该打（风格上的禁区）：**

- 没有粮道保障就北伐
- 与元军打正面消耗战
- 围城强攻、徒增伤亡
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no northern expedition without supply, no frontal attrition, no storming a city that can be surrounded, no pursuit beyond supply, no overreaching`

## （7）测试提示词示例（现代题材：一次现代企业的市场进入战）

- Prompt: `In the style of Xu Da, plan a company's entry into a contested market. Advance steadily: take the city by surrounding it not by storming it, win by logistics and by never overreaching, and consolidate each gain before the next.`
- 中文对照：以徐达的风格，筹划企业进入竞争激烈的市场：稳步推进，以围城取城而非强攻，靠后勤、靠绝不冒进赢来，巩固每一步战果再走下一步。
- Negative: `no advance without supply, no frontal price war, no storming what can be surrounded, no overreaching`
