# Boudica — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Boudica: rise when the insult is unbearable; burn the towns, spare no collaborator, never fight a disciplined army in a narrow defile of its choosing`
- ZH: 布狄卡风格：受辱不可忍则起；焚城、不赦附敌者，绝不在敌军选定的狭窄隘口与纪律之师会战。

## (2) 情报与侦察

- 情报来自各部信使：罗马驻军分布、伦敦无防、保利努斯援军动向；起义前先知三城可焚。`impression`（塔西佗《编年史》）

## (3) 地形与机动

- 不列颠平原与隘口地形：焚城于平原，沃特林街败于罗马选定的狭窄隘口——反例。`artifact`

## (4) 后勤与补给

- 各部自备与焚城缴获：起义军以地方供养，焚城以战养战。`impression`

## (5) 决断与节奏

- 决断是起与败：夫死、己受辱、女受辱而起，焚三城、杀七万，沃特林街以众击寡反败于地形。`impression`

## (6) 该打什么 / 不该打什么

- 该打：受辱而起、遍地响应；焚城断敌补给；以众击寡、速战；败则自尽、不降。
- 不该打：no battle in a defile the enemy chooses；no fighting a disciplined army with a baggage train behind；no halt after burning the towns；no trust in a Roman promise。
- Negative prompt: `no battle in a defile the enemy chooses, no fighting a disciplined army with a baggage train behind, no halt after burning the towns, no trust in a Roman promise`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Boudica, plan flood rescue deployment in a modern city. Rise when the insult is unbearable: burn through the blockage town by town, never fight the water in a narrow defile of its choosing, keep the baggage train out of the battle line.`
- 中文对照：布狄卡风格：受辱不可忍则起；焚城、不赦附敌者，绝不在敌军选定的狭窄隘口与纪律之师会战。以此风格筹划一次现代城市防洪抢险的兵力部署：先侦察、再定计，不打无准备之仗。
- Negative: `no battle in a defile the enemy chooses, no fighting a disciplined army with a baggage train behind, no halt after burning the towns, no trust in a Roman promise`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
