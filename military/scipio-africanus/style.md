# Scipio Africanus — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Scipio Africanus: learn the enemy's art and turn it on him, refuse the battle he expects, train the army for the one battle that matters, win the war not the skirmish`
- 中文：西庇阿风格：学会敌人的打法再反过来用他，拒绝敌人期待的那场仗，为决定性一战练兵，要赢的是战争不是遭遇战。

## （2）情报与侦察

情报来自侦察骑兵、俘虏与对汉尼拔战法的长期研究；先摸清敌军布阵习惯，再以反习惯的部署破之。情报用来反制，不用来硬碰。`artifact`

## （3）地形与机动

偏好开阔平原的机动决战；机动方式是变阵破敌——伊利帕以反常规布阵包抄，扎马以骑兵与步兵协同破战象。`artifact`

## （4）后勤与补给

补给靠西班牙经营与海运，远征非洲前先经营基地与努米底亚同盟；行军距离受海运与季节约束。`artifact`

## （5）决断与节奏

决断风格：学习与耐心并用——在西班牙多年练兵、研究汉尼拔，决战时机只选己方占优时；不打无把握的遭遇战。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 研究敌方战法、反过来用他
- 以反常规布阵破敌方习惯
- 战前多年练兵、经营基地与同盟
- 骑兵与步兵协同、专破战象
- 只打决定性一战、不恋战小胜

**不该打（风格上的禁区）：**

- 按敌方习惯布阵、打他准备好的仗
- 没有练兵与基地就远征
- 骑兵过早投入正面消耗
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no battle on the enemy's expected terms, no expedition without training and a base, no cavalry wasted in frontal attrition, no pursuit beyond supply, no halt that lets the enemy regroup`

## （7）测试提示词示例（现代题材：一次网络攻防对抗）

- Prompt: `In the style of Scipio Africanus, plan a cyber defence against an attacker whose playbook you have studied. Refuse the battle the attacker expects, redeploy in a formation the attacker has never seen, train for the one decisive engagement, and win the campaign not the skirmish.`
- 中文对照：以西庇阿的风格，筹划一场网络攻防对抗：拒绝攻击者期待的那场仗，以对手从未见过的布阵反制，为决定性一战练兵，要赢的是整场战役不是一次遭遇战。
- Negative: `no battle on the attacker's terms, no defence without training and a base, no frontal attrition, no halt after the first win`
