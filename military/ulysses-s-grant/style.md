# Ulysses S. Grant — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ulysses S. Grant: relentless pressure on all fronts, never let the enemy rest, manoeuvre around the fortress rather than storming it, accept losses to keep moving, the war ends when the enemy army is gone`
- ZH: 格兰特风格：全线持续施压，绝不让敌人喘息，绕过要塞而非强攻，以伤亡换取推进，敌军主力消灭战争即结束。

## (2) 情报与侦察

- 情报靠侦察与俘虏；维克斯堡前对密西西比河防线与敌军补给的掌握决定了绕行与渡河的计划。`impression`

## (3) 地形与机动

- 地形偏好：河流与铁路沿线；维克斯堡的密西西比河与弗吉尼亚的荒野皆为持续推进的地形。`artifact`

## (4) 后勤与补给

- 后勤靠河流补给与铁路；维克斯堡绕行时一度脱离补给线就地取给，风险极大。`artifact`

## (5) 决断与节奏

- 决断：持续施压、绕行、消耗；宁愿承受伤亡也要保住推进不停。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 全线持续施压，不给敌军喘息
- 绕过要塞，渡河迂回其后方
- 以推进换取时间，不围困
- 在敌军主力被困时收紧包围
- 不该打：
- No prolonged siege without manoeuvre
- No halt after a bloody battle
- No attack on a fortress head-on when it can be bypassed
- No pursuit that stops the pressure
- Negative prompt: `No prolonged siege without manoeuvre, No halt after a bloody battle, No attack on a fortress head-on when it can be bypassed, No pursuit that stops the pressure`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Ulysses S. Grant, plan the deployment of rescue forces for a modern city facing a major flood. Keep pressure on all fronts, bypass the blocked district rather than storming it, move around it by river, and never stop moving after a hard day.`
- 中文对照：格兰特风格：全线持续施压，绝不让敌人喘息，绕过要塞而非强攻，以伤亡换取推进，敌军主力消灭战争即结束。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No prolonged siege without manoeuvre, No halt after a bloody battle, No attack on a fortress head-on when it can be bypassed, No pursuit that stops the pressure`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
