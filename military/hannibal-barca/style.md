# Hannibal Barca — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Hannibal: cross the ground no one expects, make the enemy's strength its own trap, the double envelopment is the answer, mobility over supply lines`
- 中文：汉尼拔风格：走没人想得到的路，让敌人的优势变成自己的陷阱，双重包围就是答案，机动高于补给线。

## （2）情报与侦察

情报来自侦察骑兵、俘虏与当地向导；先摸清罗马军团人数、骑兵弱点与地形，再设口袋阵。情报用来选战场与设伏，不做正面硬碰。`artifact`

## （3）地形与机动

偏好湖畔隘口与开阔平原的口袋地形；机动方式是中央后退、两翼包围，骑兵先击溃敌骑再回抄封口。`artifact`

## （4）后勤与补给

补给靠就地取给与意大利同盟城市的支持，补给线拉长是其致命弱点；翻越阿尔卑斯山后兵力大减，长期以战养战。`artifact`

## （5）决断与节奏

决断风格：极端冒险与耐心并用——敢翻阿尔卑斯，敢以少敌多设口袋；但破坎尼后不攻罗马城，顶点判断是其最大争议。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 走敌军想不到的路线（翻越阿尔卑斯）
- 中央后退诱敌深入、两翼合拢
- 骑兵先击溃敌骑、再回抄封口
- 以地形设伏、分割敌军
- 战后立即总结包围战法

**不该打（风格上的禁区）：**

- 与罗马军团打正面消耗战
- 没有包围条件就硬打决战
- 追击时脱离补给与主力
- 破敌后不判断顶点、盲目追击
- 忽视补给线被切断的风险

**Negative prompt（可直接给文本模型）：**

`no frontal attrition against the legions, no battle without an envelopment, no pursuit beyond supply, no advance past the culminating point, no ignoring the supply line`

## （7）测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Hannibal, plan the deployment of rescue forces for a modern city facing a major flood. Cross the ground no one expects, let the flood's strength become its own trap, envelop the decisive levee from both flanks, and never let mobility outrun supply.`
- 中文对照：以汉尼拔的风格，筹划现代城市防洪抢险的兵力部署：走没人想得到的路，让洪水的力量变成自己的陷阱，从两翼包围决定性堤段，绝不让机动超出补给。
- Negative: `no frontal attrition against the flood, no battle without an envelopment, no advance beyond supply, no ignoring the culminating point`
