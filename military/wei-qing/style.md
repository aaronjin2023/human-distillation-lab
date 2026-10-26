# Wei Qing — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Wei Qing: go deep and come back, the cavalry goes where the maps end, win by endurance and by knowing when to stop, the desert is crossed by preparation not by courage alone`
- 中文：卫青风格：深入而还，骑兵走到地图尽头，以耐力与知止取胜，沙漠是靠准备、不是只靠勇气穿越的。

## （2）情报与侦察

情报来自侦察骑兵、降将与匈奴向导；先摸清匈奴王庭位置与水源，再以远征破之。情报用来定远征路线，不做无准备的深入。`artifact`

## （3）地形与机动

偏好草原与沙漠边缘的远征；机动方式是骑兵分路并进、迂回包抄，辅以步兵与辎重协同。`artifact`

## （4）后勤与补给

补给靠汉朝国力与沿途水源，远征距离受水源与季节约束；漠北之战以十万骑兵远征，是后勤的极限。`artifact`

## （5）决断与节奏

决断风格：稳健与果断并用——七次出塞，深入而还；决战时机只选己方占优时，知止是其最大特点。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 骑兵分路并进、迂回包抄
- 远征前先经营水源与补给
- 深入而还、不恋战
- 以耐力消耗敌军
- 战后立即总结远征战法

**不该打（风格上的禁区）：**

- 没有水源与补给就深入沙漠
- 与匈奴打正面消耗战
- 追击时脱离补给与主力
- 胜后停滞、让敌军重组反扑
- 把全部骑兵押在一次决战上

**Negative prompt（可直接给文本模型）：**

`no deep march without water and supply, no frontal attrition on the steppe, no pursuit beyond supply, no halt that lets the enemy regroup, no staking the whole cavalry on one battle`

## （7）测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Wei Qing, plan a multinational earthquake relief operation. Go deep and come back: the mobile force goes where the maps end, win by endurance and by knowing when to stop, and cross the desert by preparation not by courage alone.`
- 中文对照：以卫青的风格，筹划一次地震后的跨国救援行动：深入而还，机动力量走到地图尽头，以耐力与知止取胜，穿越沙漠靠的是准备、不是只靠勇气。
- Negative: `no deep march without water and supply, no frontal slog, no pursuit beyond supply, no advance past the culminating point`
