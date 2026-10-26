# Belisarius — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Belisarius: win with few against many, discipline and deception over numbers, take the city with a trick not a siege, hold the walls and let the enemy break on them`
- 中文：贝利撒留风格：以少胜多，纪律与欺骗胜过数量，用计取城而非硬攻，守住城墙、让敌人在墙下撞碎。

## （2）情报与侦察

情报来自侦察骑兵、间谍与降将；先摸清敌军人数、补给与士气，再以少敌多设伏。情报用来以弱胜强，不做硬碰。`artifact`

## （3）地形与机动

偏好设防城市与开阔平原的机动战；机动方式是骑兵突袭、佯动诱敌、夜袭破城，守城时以城墙与工事消耗敌军。`artifact`

## （4）后勤与补给

补给靠海运与沿途城市，远征兵力常年不足；后勤受皇帝猜忌与援军不到的约束，以战养战是常态。`artifact`

## （5）决断与节奏

决断风格：谨慎与果断并用——兵力不足时绝不硬打，机会一到立即夜袭或突袭；守城时以静制动，耗尽敌军。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 以少敌多、纪律与欺骗胜过数量
- 夜袭与佯动破城
- 骑兵突袭、分割敌军
- 守城时以城墙与工事消耗敌军
- 战前先经营海运补给与同盟

**不该打（风格上的禁区）：**

- 以少敌多时打正面消耗战
- 没有补给与援军就远征
- 围城硬耗而不寻破城之计
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑

**Negative prompt（可直接给文本模型）：**

`no frontal attrition when outnumbered, no expedition without supply and allies, no siege without a trick, no pursuit beyond supply, no halt that lets the enemy regroup`

## （7）测试提示词示例（现代题材：一次小团队面对巨头的竞争）

- Prompt: `In the style of Belisarius, plan how a small team competes against a giant. Win with few against many: discipline and deception over numbers, take the decisive position with a trick not a siege, hold your ground and let the rival break on it.`
- 中文对照：以贝利撒留的风格，筹划小团队如何与巨头竞争：以少胜多，纪律与欺骗胜过数量，用计取下决定性位置而非硬攻，守住阵地、让对手在墙下撞碎。
- Negative: `no frontal attrition when outnumbered, no siege without a trick, no battle without supply, no staking everything on one throw`
