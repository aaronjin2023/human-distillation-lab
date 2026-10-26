# Zhuge Liang — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Zhuge Liang: plan first in the thatched cottage, win the map before the battle, strict law and careful logistics, never fight a battle the supply cannot support`
- 中文：诸葛亮风格：先在草庐中定下大计，战前先赢地图，严法与精细后勤，绝不打补给支撑不了的仗。

## （2）情报与侦察

情报来自斥候、降将与对天下大势的判断；先摸清天下三分、敌军部署与地形，再定隆中对。情报用来定战略，不用来打遭遇战。`artifact`

## （3）地形与机动

偏好山地隘口与河流渡口的防御与北伐；机动方式是步步为营、木牛流马转运，以稳取胜。`artifact`

## （4）后勤与补给

补给靠蜀汉屯田与木牛流马转运，北伐受秦岭粮道与季节约束；六出祁山皆因粮尽而还，后勤是其最大弱点。`artifact`

## （5）决断与节奏

决断风格：谨慎与坚持并用——隆中对定下三分天下，北伐六出祁山，知其不可为而为之；决战时机只选己方占优时。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 战前先定战略（隆中对）
- 步步为营、稳扎稳打
- 严法与精细后勤并用
- 以木牛流马保障粮道
- 只打补给支撑得了的仗

**不该打（风格上的禁区）：**

- 没有战略就出兵
- 没有粮道保障就北伐
- 与优势敌军打正面消耗战
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no campaign without a strategy, no northern expedition without a supply line, no frontal attrition against a superior enemy, no pursuit beyond supply, no battle the logistics cannot support`

## （7）测试提示词示例（现代题材：一次现代企业的长期战略规划）

- Prompt: `In the style of Zhuge Liang, plan a company's long-term strategy. Plan first in the cottage: win the map before the battle, advance step by step with strict law and careful logistics, and never fight a battle the supply cannot support.`
- 中文对照：以诸葛亮的风格，筹划一家企业的长期战略：先在草庐中定下大计，战前先赢地图，步步为营、严法与精细后勤并用，绝不打补给支撑不了的仗。
- Negative: `no campaign without a strategy, no advance without a supply line, no frontal price war, no battle the logistics cannot support`
