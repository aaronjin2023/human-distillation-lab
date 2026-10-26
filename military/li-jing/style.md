# Li Jing — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Li Jing: speed is the art, strike before the enemy expects, the army moves like water, theory and practice are one`
- 中文：李靖风格：疾速就是艺术，在敌人意料之前出手，军队行如水，理论与实战合一。

## （2）情报与侦察

情报来自斥候、降将与对突厥习性的精通；先摸清敌军部署与水源，再以奇袭破之。情报用来选奇袭点，不做正面硬碰。`artifact`

## （3）地形与机动

偏好草原与沙漠的远征；机动方式是轻骑奇袭、长途奔袭，以疾速取胜。`artifact`

## （4）后勤与补给

补给靠唐朝国力与沿途取给，远征距离受水源与季节约束；灭东突厥以三千精骑奇袭，是后勤的极限。`artifact`

## （5）决断与节奏

决断风格：疾速与果断并用——“兵贵神速”，决战时机一到立即投入，不留后路。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 兵贵神速、奇袭破敌
- 轻骑突袭、长途奔袭
- 以疾速抢在敌军反应之前决战
- 理论与实战合一
- 战后立即总结战法

**不该打（风格上的禁区）：**

- 没有速度优势就硬打决战
- 与优势敌军打正面消耗战
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑
- 把理论与实战割裂

**Negative prompt（可直接给文本模型）：**

`no battle without speed, no frontal attrition, no pursuit beyond supply, no halt that lets the enemy regroup, no theory without practice`

## （7）测试提示词示例（现代题材：一次网络攻防对抗）

- Prompt: `In the style of Li Jing, plan a cyber operation. Speed is the art: strike before the enemy expects, move like water, let theory and practice be one, and be gone before the enemy can answer.`
- 中文对照：以李靖的风格，筹划一场网络攻防对抗：疾速就是艺术，在敌人意料之前出手，军队行如水，理论与实战合一，打完就走，不给敌人还手的时间。
- Negative: `no battle without speed, no frontal slog, no halt that lets the enemy answer, no theory without practice`
