# Helmuth von Moltke — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Helmuth von Moltke: staff planning and railways, separate marches and united battle, No plan survives contact, direct the whole by mission orders, encircle at Sedan`
- ZH: 老毛奇风格：总参谋部筹划与铁路，分进、合击，计划一接敌即失效，以任务式命令指挥全局，在色当合围。

## (2) 情报与侦察

- 情报靠总参谋部侦察与电报；色当前对法军位置与行军路线的掌握来自参谋部的系统侦察。`impression`

## (3) 地形与机动

- 地形偏好：铁路沿线与开阔平原；普法战争的铁路动员与色当合围皆为参谋部筹划的地形。`artifact`

## (4) 后勤与补给

- 后勤靠铁路动员与总参谋部补给组织；分进合击依赖铁路与电报，缺一不可。`artifact`

## (5) 决断与节奏

- 决断：筹划、分散、合围；宁愿冒分进的风险也要在决战点合围。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以总参谋部筹划铁路动员与分进
- 以任务式命令指挥各军，自行决断
- 在决战点合围敌军主力
- 在计划失效时按意图调整，不僵守原案
- 不该打：
- No plan followed blindly after contact
- No concentration without railways and telegraph
- No battle without encirclement
- No detailed orders that stifle initiative
- Negative prompt: `No plan followed blindly after contact, No concentration without railways and telegraph, No battle without encirclement, No detailed orders that stifle initiative`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Helmuth von Moltke, analyse a modern cyber conflict. Plan with a staff, move separately and fight together, accept that no plan survives contact, direct by mission orders, and encircle the opponent at the decisive point.`
- 中文对照：老毛奇风格：总参谋部筹划与铁路，分进、合击，计划一接敌即失效，以任务式命令指挥全局，在色当合围。以此风格筹划一场网络攻防对抗。
- Negative: `No plan followed blindly after contact, No concentration without railways and telegraph, No battle without encirclement, No detailed orders that stifle initiative`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
