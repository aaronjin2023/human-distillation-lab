# Gebhard Leberecht von Blücher — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Gebhard Leberecht von Blücher: aggressive pursuit, march to the sound of the guns, never let a defeat stop the march, attack again the next day, the ally's battle is your battle`
- ZH: 布吕歇尔风格：积极追击，闻炮而进，一次失败不停行军，第二天再攻，盟友的战斗就是你的战斗。

## (2) 情报与侦察

- 情报靠侦察与盟军联络；滑铁卢前对威灵顿阵地与法军位置的掌握来自联军通信。`impression`

## (3) 地形与机动

- 地形偏好：开阔平原与雨后泥泞；滑铁卢的泥泞行军本身就是其决断的考验。`artifact`

## (4) 后勤与补给

- 后勤靠普鲁士本土与联军补给；利尼战败后仍能重整行军，靠的是分散补给与快速重组。`impression`

## (5) 决断与节奏

- 决断：进攻、追击、盟军协同；宁愿冒雨后行军的风险也要赶到盟友的战场。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 闻炮而进，向盟友战场行军
- 战败后立即重整，第二天再攻
- 以快速行军抢占决战时机
- 在敌军翼侧出现时立即冲击
- 不该打：
- No halt after a defeat
- No battle fought alone without allies
- No waiting for perfect weather or supply
- No pursuit without the ally in sight
- Negative prompt: `No halt after a defeat, No battle fought alone without allies, No waiting for perfect weather or supply, No pursuit without the ally in sight`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Gebhard Leberecht von Blücher, plan a cross-border earthquake relief operation. March to the sound of the guns: move toward the other team's battle even in the mud, regroup after a setback and attack the problem again the next day, and never fight alone.`
- 中文对照：布吕歇尔风格：积极追击，闻炮而进，一次失败不停行军，第二天再攻，盟友的战斗就是你的战斗。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No halt after a defeat, No battle fought alone without allies, No waiting for perfect weather or supply, No pursuit without the ally in sight`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
