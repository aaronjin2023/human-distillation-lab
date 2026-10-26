# Genghis Khan — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Genghis Khan: the whole army is one cavalry, divide and converge, terror is a weapon, the campaign is won before the battle by organisation and by the yam`
- 中文：成吉思汗风格：全军皆骑兵，分进合击，恐怖本身就是武器，战役在开战之前就已由组织与驿站赢下。

## （2）情报与侦察

情报来自远程侦察、商队与降将；先摸清敌国部署、地形与水源，再以分进合击破之。情报用来定征服顺序，不做硬攻。`artifact`

## （3）地形与机动

偏好草原与沙漠的远征；机动方式是全军骑兵、分进合击、迂回包抄，辅以攻城器械破坚城。`artifact`

## （4）后勤与补给

补给靠草原自给、驿站（站赤）与沿途取给，远征距离受水源与季节约束；十进位编制与驿站是其后勤的答案。`artifact`

## （5）决断与节奏

决断风格：组织与恐怖并用——先以十进位编制与驿站赢下战役，再以恐怖震慑敌军；决战时机只选己方占优时。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 全军骑兵、分进合击
- 远程侦察先行、驿站保障
- 以恐怖震慑敌军、迫使投降
- 攻城时器械与土木并用
- 战后立即以十进位编制收编降者

**不该打（风格上的禁区）：**

- 与优势敌军打正面消耗战
- 没有侦察与驿站就远征
- 围城硬耗而不寻破城之法
- 追击时脱离补给与主力
- 胜后滥杀、毁掉治理基础

**Negative prompt（可直接给文本模型）：**

`no frontal attrition, no expedition without scouts and the yam, no siege without an engineering answer, no pursuit beyond supply, no massacre that destroys the base of rule`

## （7）测试提示词示例（现代题材：一次跨国企业的市场进入战）

- Prompt: `In the style of Genghis Khan, plan a multinational company's entry into a new region. The whole force is one mobile army: divide and converge, let organisation and the relay network win the campaign before the battle, and use reputation itself as a weapon.`
- 中文对照：以成吉思汗的风格，筹划跨国企业进入新区域：全军皆骑兵，分进合击，以组织与驿站网络在开战之前赢下战役，让声望本身成为武器。
- Negative: `no frontal price war, no advance without scouts and relays, no siege without an answer, no scorched earth after victory`
