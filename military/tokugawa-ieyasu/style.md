# Tokugawa Ieyasu — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Tokugawa Ieyasu: wait longer than any enemy; win the battle before it starts by winning the allies, then let the field decide in one day`
- ZH: 德川家康风格：比任何敌人都等得更久；战前先赢得盟友，战场一日定胜负。

## (2) 情报与侦察

- 情报来自外交与内应：西军诸将动向、小早川秀秋是否倒戈；关原前先知敌军内部有隙。`impression`

## (3) 地形与机动

- 平原决战地形：关原选开阔地，利于大军团展开与倒戈后的合围。`impression`

## (4) 后勤与补给

- 三河—关东领地经济：以忍耐积蓄实力，战前囤积粮草于前线。`impression`

## (5) 决断与节奏

- 决断是等待与倒戈：等秀吉死、等西军内部分裂，关原一日以小早川倒戈定胜负；战后分封立幕府。`impression`

## (6) 该打什么 / 不该打什么

- 该打：战前以外交分化敌军；等待敌军内部分裂；决战一日、倒戈定胜负；战后分封、立治为先。
- 不该打：no battle before the enemy is divided；no decisive battle without the defection secured；no pursuit that breaks your own coalition；no victory without a settlement after。
- Negative prompt: `no battle before the enemy is divided, no decisive battle without the defection secured, no pursuit that breaks your own coalition, no victory without a settlement after`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗中的持久消耗）

- Prompt: `In the style of Tokugawa Ieyasu, plan a long cyber defence campaign. Wait longer than any attacker: win the allies first, divide the attacking coalition before the battle, let one defection decide the day, never fight before the enemy is divided.`
- 中文对照：德川家康风格：比任何敌人都等得更久；战前先赢得盟友，战场一日定胜负。以此风格筹划一场网络攻防对抗中的持久消耗：先侦察、再定计，不打无准备之仗。
- Negative: `no battle before the enemy is divided, no decisive battle without the defection secured, no pursuit that breaks your own coalition, no victory without a settlement after`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
