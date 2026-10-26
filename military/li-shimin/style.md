# Li Shimin — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Li Shimin: lead the charge yourself, win the decisive field battle and the war follows, use the enemy's own generals against him, speed and personal courage decide`
- 中文：李世民风格：亲自率军冲锋，赢下决定性野战、战争随之而定，用敌人的将领反过来打他，速度与个人勇气定胜负。

## （2）情报与侦察

情报来自斥候、降将与对敌军将领的了解；先摸清敌军部署与将领性格，再以野战破之。情报用来选决战点，不做围困。`artifact`

## （3）地形与机动

偏好开阔平原的野战决战；机动方式是亲自率精骑突击、直取敌帅，辅以步兵牵制。`artifact`

## （4）后勤与补给

补给靠唐朝根据地与沿途取给，野战受河流与季节约束；虎牢关以少敌多，是后勤与速度的极限。`artifact`

## （5）决断与节奏

决断风格：极端果断与冒险——亲自冲锋、身先士卒；决战时机一到立即投入，不留预备队犹豫。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 亲自率精骑突击、直取敌帅
- 以少敌多、野战决胜
- 用敌方降将反过来打敌军
- 以速度抢在敌军合流之前决战
- 战后立即招降、巩固战果

**不该打（风格上的禁区）：**

- 与优势敌军打正面消耗战
- 没有野战条件就围城硬耗
- 追击时脱离补给与主力
- 胜后滥杀、激起全境死战
- 把统帅本人置于无谓的险地而不留后手

**Negative prompt（可直接给文本模型）：**

`no frontal attrition, no siege without a field battle first, no pursuit beyond supply, no massacre after victory, no battle without personal leadership`

## （7）测试提示词示例（现代题材：一次现代企业的市场进入战）

- Prompt: `In the style of Li Shimin, plan a company's entry into a contested market. Lead the charge yourself: win the decisive field battle and the market follows, use the rival's own people against it, and let speed and personal courage decide.`
- 中文对照：以李世民的风格，筹划企业进入竞争激烈的市场：亲自率军冲锋，赢下决定性野战、市场随之而定，用对手的人反过来打对手，速度与个人勇气定胜负。
- Negative: `no frontal price war, no siege without a field battle, no pursuit beyond supply, no scorched earth after victory`
