# Fu Hao — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Fu Hao: campaign far and return, oracle first then march, the chariot and the foot soldier together, the queen who leads the army herself`
- 中文：妇好风格：远征而还，先占卜、后出兵，车兵与步兵并用，亲自率军出征的王后。

## （2）情报与侦察

情报来自占卜（甲骨文）与斥候回报；先占卜问吉凶、再出兵，情报用来定出征时机与方向。`artifact`（甲骨文与妇好墓）

## （3）地形与机动

偏好中原与北方边地的远征；机动方式是车兵突击、步兵跟进，分路合击方国。`artifact`

## （4）后勤与补给

补给靠商王朝的贡赋与沿途方国，远征距离受季节与方国态度约束；一次征伐可动员上万兵力。`artifact`

## （5）决断与节奏

决断风格：占卜与果断并用——大事先占卜，出兵后速决；不打无占卜、无准备的仗。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 大事先占卜、再出兵
- 车兵突击、步兵跟进
- 分路合击方国
- 远征而还、不恋战
- 战后以战利品与俘虏巩固王权

**不该打（风格上的禁区）：**

- 没有占卜与准备就出兵
- 远征时脱离补给与主力
- 追击时深入敌境而不留后路
- 胜后停滞、让方国重组反扑
- 把全部兵力押在一次决战上

**Negative prompt（可直接给文本模型）：**

`no campaign without divination and preparation, no expedition beyond supply, no pursuit without a way back, no staking the whole army on one battle, no halt that lets the enemy regroup`

## （7）测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Fu Hao, plan the deployment of rescue forces for a modern city facing a major flood. Consult the signs first, then march: chariots and foot soldiers together, strike from several roads at once, campaign far and return, never let the force outrun its supply.`
- 中文对照：以妇好的风格，筹划现代城市防洪抢险的兵力部署：先占卜、后出兵，车兵与步兵并用，多路合击，远征而还，绝不让兵力超出补给。
- Negative: `no campaign without preparation, no advance beyond supply, no pursuit without a way back, no staking everything on one throw`
