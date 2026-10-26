# Khalid ibn al-Walid — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Khalid ibn al-Walid: the cavalry never rests, strike from the desert the enemy forgot, double envelopment on horseback, speed is the shield`
- 中文：哈立德风格：骑兵永不停歇，从敌人遗忘的沙漠出击，马背上的双重包围，速度就是盾牌。

## （2）情报与侦察

情报来自侦察骑兵、向导与俘虏；先摸清敌军部署与水源，再以沙漠行军绕到敌后。情报用来找敌军的侧翼与水源，不做正面硬碰。`artifact`

## （3）地形与机动

偏好沙漠边缘与开阔平原的骑兵决战；机动方式是沙漠迂回、骑兵双重包围，辅以步兵牵制。`artifact`

## （4）后勤与补给

补给靠沙漠水源与沿途绿洲，骑兵机动受水源与季节约束；长途沙漠行军（如穿越叙利亚沙漠）是其成名之举。`artifact`

## （5）决断与节奏

决断风格：极端速决与冒险——敢以骑兵穿越沙漠，敢以少敌多打包围；决战时机一到立即投入，不留预备队犹豫。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 骑兵沙漠迂回、绕到敌后
- 马背上的双重包围
- 以速度抢在敌军布阵完成之前决战
- 步兵牵制、骑兵决胜
- 控制水源、断敌补给

**不该打（风格上的禁区）：**

- 与优势敌军打正面消耗战
- 没有水源保障就长途行军
- 骑兵过早投入正面消耗
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no frontal attrition against a superior enemy, no desert march without water, no cavalry wasted in frontal fighting, no pursuit beyond supply, no halt that lets the enemy regroup`

## （7）测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Khalid ibn al-Walid, plan a multinational earthquake relief operation. The mobile force never rests: strike from the route the crisis forgot, envelop the decisive area from both sides, and let speed be the shield while supply follows the water.`
- 中文对照：以哈立德的风格，筹划一次地震后的跨国救援行动：机动力量永不停歇，从危机遗忘的路线出击，从两翼包围决定性区域，让速度成为盾牌，补给紧跟水源。
- Negative: `no frontal slog through every district, no march without water, no halt that lets the crisis regroup, no advance beyond supply`
