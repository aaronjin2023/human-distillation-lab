# Li Mu — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Li Mu: defend by not fighting, let the enemy wear itself out on your walls, train in secret and strike once, the border is won by patience`
- 中文：李牧风格：以不战而守，让敌人在你的壁垒前耗尽自己，暗中练兵、一击致命，边防是靠耐心赢来的。

## （2）情报与侦察

情报来自边关斥候与匈奴降者；先摸清匈奴来犯路线与秦军部署，再以坚壁清野耗敌。情报用来守，不用来追。`artifact`

## （3）地形与机动

偏好边关隘口与长城一线的防御地形；机动方式是坚壁清野、诱敌深入、伏击合围，不打野战硬碰。`artifact`

## （4）后勤与补给

补给靠边关屯田与赵国后方转运，坚壁清野的前提是己方粮草充足、敌方无所得；长期防御受财政与朝廷猜忌约束。`artifact`

## （5）决断与节奏

决断风格：极端耐心——多年不战、暗中练兵，敌军轻视时一击歼灭；决战时机只选敌军疲惫轻敌时。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 坚壁清野、诱敌深入
- 暗中练兵、一击致命
- 以防御消耗敌军
- 边关屯田、自给自足
- 只打敌军轻敌疲惫时的仗

**不该打（风格上的禁区）：**

- 与敌军打野战硬碰
- 没有练兵与屯田就出战
- 追击时脱离边关与补给
- 胜后停滞、让敌军重组反扑
- 把边防兵力调去打内战

**Negative prompt（可直接给文本模型）：**

`no open-field battle on the enemy's terms, no campaign without training and farming, no pursuit beyond the border, no battle before the enemy is worn out, no stripping the border for civil war`

## （7）测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Li Mu, plan the defence of a modern city facing a major flood. Defend by not fighting the water head-on: let the flood wear itself out on your walls, train in secret and strike once at the decisive levee, and win the border by patience.`
- 中文对照：以李牧的风格，筹划现代城市防洪抢险：以不战而守，让洪水在壁垒前耗尽自己，暗中练兵、一击致命，在决定性堤段出手，边防是靠耐心赢来的。
- Negative: `no frontal fight against the flood, no campaign without preparation, no pursuit beyond the line, no battle before the enemy is worn out`
