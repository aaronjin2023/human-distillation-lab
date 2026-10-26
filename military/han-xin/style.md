# Han Xin — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Han Xin: use the ground the enemy thinks is death, back to the river and fight, the more desperate the position the sharper the army, win the war by winning the map`
- 中文：韩信风格：用敌人以为是死地的地形，背水一战，位置越绝望、军队越锋利，以赢地图来赢战争。

## （2）情报与侦察

情报来自斥候、降将与对地形的精通；先摸清敌军部署与地形，再以背水、奇袭破之。情报用来选绝地，不用来硬碰。`artifact`

## （3）地形与机动

偏好河流、隘口与绝地的机动战；机动方式是背水列阵、奇袭断后、分进合击，以地形逼出士气。`artifact`

## （4）后勤与补给

补给靠汉军后方转运与沿途取给，远征距离受河流与季节约束；明修栈道、暗度陈仓是其成名之举。`artifact`

## （5）决断与节奏

决断风格：极端冒险与精算并用——敢背水列阵，敢以少敌多；决战时机只选地形与士气同时占优时。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 背水列阵、以绝地逼出士气
- 明修栈道、暗度陈仓
- 奇袭断敌后路
- 分进合击、多路并进
- 战前先经营地图与补给

**不该打（风格上的禁区）：**

- 与优势敌军打正面消耗战
- 没有地形优势就硬打决战
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑
- 把全部兵力押在一次决战上

**Negative prompt（可直接给文本模型）：**

`no frontal attrition against a superior enemy, no battle without the ground, no pursuit beyond supply, no halt that lets the enemy regroup, no staking the whole army on one throw`

## （7）测试提示词示例（现代题材：一次现代企业的市场进入战）

- Prompt: `In the style of Han Xin, plan a company's entry into a contested market. Use the ground the rival thinks is death: back to the river and fight, let the desperate position sharpen the team, win the war by winning the map, and strike the rival's rear while it watches the front.`
- 中文对照：以韩信的风格，筹划企业进入竞争激烈的市场：用对手以为是死地的地形，背水一战，位置越绝望、团队越锋利，以赢地图来赢战争，在对手盯着正面时打它的后路。
- Negative: `no frontal price war, no battle without the ground, no pursuit beyond supply, no halt that lets the rival regroup`
