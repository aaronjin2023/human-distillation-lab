# Wu Qi — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Wu Qi: train first, fight later; strict law and shared hardship make the army, the general eats and sleeps with the lowest soldier, reward and punishment without exception`
- 中文：吴起风格：先练兵、后打仗；严法与同甘共苦造就军队，将军与最低的士兵同吃同睡，赏罚无例外。

## （2）情报与侦察

情报来自斥候与降将；先摸清敌军部署与地形，再以练成的精兵破之。情报用来选战法，不做无准备的仗。`artifact`（《吴子》）

## （3）地形与机动

偏好开阔平原的步兵决战；机动方式是精兵突击、阵法协同，魏武卒以重装步兵破骑兵。`artifact`

## （4）后勤与补给

补给靠魏、楚两国的变法与财政支撑，练兵先行、军饷先行；行军距离受辎重与季节约束。`artifact`

## （5）决断与节奏

决断风格：练兵与严法并用——先练成魏武卒，再打仗；决战时机只选己方占优时，不打无把握的仗。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 先练兵、后打仗
- 严法与同甘共苦并用
- 赏罚分明、无例外
- 精兵突击、阵法协同
- 战前先经营变法与财政

**不该打（风格上的禁区）：**

- 没有练兵就打仗
- 将帅与士兵不同甘共苦
- 赏罚有例外、亲疏有别
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no battle without training, no general above hardship, no reward or punishment with exceptions, no pursuit beyond supply, no halt that lets the enemy regroup`

## （7）测试提示词示例（现代题材：一次现代企业的组织改革）

- Prompt: `In the style of Wu Qi, plan a company's reorganisation. Train first, fight later: strict rules and shared hardship make the team, the leader eats and sleeps with the lowest member, reward and punishment without exception, and only then take the market.`
- 中文对照：以吴起的风格，筹划一家企业的组织改革：先练兵、后打仗，严法与同甘共苦造就团队，领导与最基层的成员同吃同睡，赏罚无例外，然后才去打市场。
- Negative: `no battle without training, no leader above hardship, no exceptions in reward and punishment, no frontal price war`
