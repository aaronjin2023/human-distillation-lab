# Julius Caesar — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Julius Caesar: speed, speed, speed; write the war as you fight it, strike before the enemy is ready, clemency after victory is a weapon`
- 中文：恺撒风格：速度、速度、速度；一边打仗一边写战记，在敌人准备好之前就打，胜利后的宽容本身就是武器。

## （2）情报与侦察

情报来自侦察骑兵、俘虏、降将与高卢向导；先摸清敌军集结与地形，再以速度抢在敌军合流之前各个击破。情报用来抢时间，不做漫长围困。`artifact`

## （3）地形与机动

偏好河流渡口与开阔平原的速决战；机动方式是快速行军、分进合击、渡河奇袭，辅以围城工事（如阿莱西亚双重壁垒）。`artifact`

## （4）后勤与补给

补给靠就地取给与高卢同盟城市，快速行军受辎重与季节约束；阿莱西亚围城时以工事代补给线，内外夹击是最大风险。`artifact`

## （5）决断与节奏

决断风格：极端速决与冒险——渡过卢比孔河、追击庞培至希腊，决战时机一到立即投入；胜后以宽容收编降者。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 以速度抢在敌军合流之前各个击破
- 快速行军、渡河奇袭
- 围城时筑双重壁垒、内外兼顾
- 胜后以宽容收编降将降兵
- 边打边写战记、以文字巩固战果

**不该打（风格上的禁区）：**

- 打敌人准备好的正面消耗战
- 没有速度优势就硬打决战
- 围城时忽视外援反扑
- 胜后滥杀、激起全境死战
- 追击时脱离补给与主力

**Negative prompt（可直接给文本模型）：**

`no battle without speed, no frontal attrition on the enemy's terms, no siege that ignores relief forces, no massacre after victory, no pursuit beyond supply`

## （7）测试提示词示例（现代题材：一次现代企业的市场进入战）

- Prompt: `In the style of Julius Caesar, plan a company's entry into a contested market. Speed, speed, speed: strike before rivals can combine, cross the river before they are ready, build a double wall around the decisive city, and use clemency after victory to turn rivals into partners.`
- 中文对照：以恺撒的风格，筹划企业进入竞争激烈的市场：速度、速度、速度；在对手合流之前各个击破，在对方准备好之前渡河，以双重壁垒围住决定性城市，胜后以宽容把对手变成伙伴。
- Negative: `no slow frontal price war, no battle without speed, no siege that ignores relief, no scorched earth after victory`
