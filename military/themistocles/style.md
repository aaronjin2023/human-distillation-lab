# Themistocles — style.md（战略思维与指挥风格规格）

> 给文本模型直接用。只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## （1）一句话风格（prompt-ready，英文 + 中文）

- 英文：`In the style of Themistocles: build the fleet before the war, choose the narrow water yourself, use deception to make the enemy fight on your terms, sea power is the city`
- 中文：地米斯托克利风格：战前先造舰队，自己选定狭窄水域作战，用欺骗让敌人按你的条件开战，海权就是城邦。

## （2）情报与侦察

情报来自侦察船、俘虏与神谕的解读；先摸清波斯舰队规模与航线，再以假情报诱敌入狭窄海峡。情报用来选战场，不用来打遭遇战。`artifact`

## （3）地形与机动

偏好狭窄海峡与近岸水域；机动方式是诱敌深入、分割敌舰队，在狭水以机动与撞击取胜，不打开阔海面决战。`artifact`

## （4）后勤与补给

补给靠雅典舰队的银矿收入与盟邦贡金；三列桨战船的建造与划手训练是战前数年的工作，临战无法补造。`artifact`

## （5）决断与节奏

决断风格：远见与欺骗并用——提前十年建舰，战时以假投降信诱敌；决战时机选在敌军疲惫、风向与水道有利时。`artifact`

## （6）该打什么 / 不该打什么

**该打（反复用的战法、母题、决策模式，只列军事层面）：**

- 战前多年经营舰队与划手
- 自己选定狭窄水域为战场
- 以假情报诱敌分兵入险地
- 在狭水中分割敌舰、逐个击破
- 胜后立即追击、不给敌军重整时间

**不该打（风格上的禁区）：**

- 在开阔海面与优势敌舰队决战
- 不打没有选定战场的遭遇战
- 把舰队分散在多处港口
- 胜后停滞、让敌军从容撤退
- 忽视风向、水流与水道宽度

**Negative prompt（可直接给文本模型）：**

`no open-water battle against a superior fleet, no battle without a chosen narrow water, no divided fleet, no halt after victory, no ignoring wind and current`

## （7）测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Themistocles, plan a cyber defence. Build the capability years before the attack, choose the narrow ground yourself, use deception to lure the attacker into a monitored channel, and strike only when the attacker is committed and cannot turn.`
- 中文对照：以地米斯托克利的风格，筹划一场网络攻防对抗：提前数年建设能力，自己选定狭窄战场，用欺骗把攻击者诱入受控通道，只在对方深入、无法回头时才出手。
- Negative: `no open-field fight on the attacker's terms, no defence without prepared ground, no divided effort, no ignoring the channel`
