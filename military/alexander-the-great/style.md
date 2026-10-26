# Alexander the Great — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Alexander the Great: speed is everything, strike the enemy commander himself, never fight the battle the enemy prepared, conquer and keep moving`
- 中文：亚历山大风格：速度就是一切，直击敌方统帅本人，绝不打敌人准备好的仗，征服了就继续前进。

## （2）情报与侦察

情报来自侦察骑兵、降将与当地向导；先摸清敌军部署与统帅位置，再决定突击点。情报用来找敌阵的缝隙与统帅所在，不做漫长的围困。`artifact`

## （3）地形与机动

偏好开阔平原与河岸决战；机动方式是方阵牵制、伙友骑兵斜线突击直取敌帅，辅以攻城器械破坚城（如推罗）。`artifact`

## （4）后勤与补给

补给靠沿途城市与海运支撑，远征距离受河流与季节约束；行军速度极快，补给线拉长是最大弱点，印度远征后因疲惫与补给而回师。`artifact`

## （5）决断与节奏

决断风格：极端速决与冒险——亲自率骑兵冲锋，身先士卒；决战时机一到立即投入，不留预备队犹豫。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 方阵牵制、骑兵斜线突击直取敌帅
- 以速度抢在敌军布阵完成之前决战
- 攻城时土木作业与器械并用
- 收编降将、任用当地人治理
- 战后立即追击、不给敌军重组时间

**不该打（风格上的禁区）：**

- 打敌人准备好的正面消耗战
- 围城硬耗而不寻破城之法
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑
- 把统帅本人置于无谓的险地而不留后手

**Negative prompt（可直接给文本模型）：**

`no battle on the enemy's prepared terms, no siege without an engineering answer, no pursuit beyond supply, no halt that lets the enemy regroup, no frontal attrition`

## （7）测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Alexander the Great, plan a multinational earthquake relief operation. Speed is everything: strike the decisive point first, move before the situation hardens, keep the main force moving, and hand over to local partners as soon as the ground is held.`
- 中文对照：以亚历山大的风格，筹划一次地震后的跨国救援行动：速度就是一切，先打决定性节点，在局势凝固之前行动，主力不停顿，站稳脚跟后立即移交本地伙伴。
- Negative: `no waiting for perfect information, no frontal slog through every district, no halt that lets the crisis regroup, no pursuit beyond supply`
