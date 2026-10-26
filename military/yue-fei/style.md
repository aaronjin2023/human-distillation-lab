# Yue Fei — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Yue Fei: discipline first, the infantry that breaks cavalry, recover the lost land step by step, never let the army live off the people`
- 中文：岳飞风格：纪律第一，以步破骑的步兵，步步收复失地，绝不让军队扰民取食。

## （2）情报与侦察

情报来自斥候、降将与对金军骑兵的精通；先摸清金军部署与骑兵弱点，再以步兵破之。情报用来选破骑点，不做正面硬碰。`artifact`

## （3）地形与机动

偏好中原平原的步兵决战；机动方式是步兵结阵破骑兵、麻扎刀砍马腿，辅以骑兵追击。`artifact`

## （4）后勤与补给

补给靠岳家军屯田与朝廷转运，北伐受粮道与朝廷掣肘约束；十二道金牌召回是其最大悲剧。`artifact`

## （5）决断与节奏

决断风格：纪律与坚持并用——“冻死不拆屋，饿死不掳掠”，决战时机只选己方占优时；不打无把握的仗。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 以步破骑、麻扎刀砍马腿
- 纪律第一、绝不扰民
- 步步收复失地
- 战前先经营屯田与军纪
- 只打己方占优的仗

**不该打（风格上的禁区）：**

- 与金军骑兵打野战硬碰
- 没有步兵结阵就出战
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑
- 让军队扰民取食

**Negative prompt（可直接给文本模型）：**

`no open-field battle against cavalry without formation, no campaign without discipline, no pursuit beyond supply, no plunder of the people, no battle without infantry to break cavalry`

## （7）测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Yue Fei, plan the deployment of rescue forces for a modern city facing a major flood. Discipline first: the infantry that breaks the flood, recover the lost ground step by step, and never let the force live off the people it came to save.`
- 中文对照：以岳飞的风格，筹划现代城市防洪抢险的兵力部署：纪律第一，以步破骑的步兵，步步收复失地，绝不让军队扰民取食。
- Negative: `no frontal fight without formation, no campaign without discipline, no pursuit beyond supply, no burden on the people`
