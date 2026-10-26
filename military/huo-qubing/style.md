# Huo Qubing — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Huo Qubing: light cavalry, no baggage, live off the enemy, strike deep and fast and be gone before the enemy can answer`
- 中文：霍去病风格：轻骑、无辎重，因粮于敌，深入、快速，打完就走，不给敌人还手的时间。

## （2）情报与侦察

情报来自侦察骑兵与降将；先摸清匈奴王庭与水源，再以轻骑奇袭破之。情报用来选奇袭点，不做正面硬碰。`artifact`

## （3）地形与机动

偏好草原与沙漠的轻骑远征；机动方式是轻骑突袭、长途奔袭，因粮于敌。`artifact`

## （4）后勤与补给

补给靠因粮于敌，轻骑无辎重；远征距离受水源与敌军粮草约束，速度就是补给。`artifact`

## （5）决断与节奏

决断风格：极端速决与冒险——敢以轻骑深入两千里，敢以少敌多；决战时机一到立即投入，不留后路。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 轻骑突袭、长途奔袭
- 因粮于敌、无辎重
- 深入敌后、直取王庭
- 以速度抢在敌军反应之前决战
- 战后立即转移、不恋战

**不该打（风格上的禁区）：**

- 带辎重行军、拖慢速度
- 与匈奴打正面消耗战
- 没有因粮条件就深入
- 追击时脱离主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no baggage train, no frontal attrition on the steppe, no deep march without living off the enemy, no halt that lets the enemy answer, no pursuit beyond supply`

## （7）测试提示词示例（现代题材：一次网络攻防对抗）

- Prompt: `In the style of Huo Qubing, plan a cyber operation. Light force, no baggage: live off the enemy's own ground, strike deep and fast and be gone before the enemy can answer, and let speed be the supply.`
- 中文对照：以霍去病的风格，筹划一场网络攻防对抗：轻骑、无辎重，因粮于敌，深入、快速，打完就走，不给敌人还手的时间，速度就是补给。
- Negative: `no heavy baggage, no frontal slog, no halt that lets the enemy answer, no advance without living off the ground`
