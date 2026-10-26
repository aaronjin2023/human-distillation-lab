# Prince Eugene of Savoy — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Prince Eugene: bold attack against a larger army, strike while the enemy is crossing a river, cavalry and infantry in one thrust, speed over numbers, never let a good chance pass`
- ZH: 欧根风格：以少打多、果断进攻，趁敌渡河半渡而击，步骑合一冲击，速度压倒数量，绝不错过战机。

## (2) 情报与侦察

- 情报靠侦察骑兵与俘虏；泽塔一战对奥斯曼军渡河时间与队形的掌握决定了进攻时机。`impression`

## (3) 地形与机动

- 地形偏好：河流渡口与开阔平原；泽塔的蒂萨河渡口与贝尔格莱德的要塞外围皆为半渡而击的地形。`artifact`

## (4) 后勤与补给

- 后勤靠奥地利本土与多瑙河补给；远征土耳其依赖沿河推进，补给线即进军线。`impression`

## (5) 决断与节奏

- 决断：果断、冒险、速决；宁愿冒兵力劣势的风险也要抓住半渡时机。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 趁敌渡河半渡时立即进攻
- 步骑合一，一次冲击打垮敌阵
- 以快速行军抢占决战点
- 在敌军立足未稳时追击
- 不该打：
- No waiting for the enemy to finish crossing
- No frontal attack on a prepared enemy
- No battle without cavalry ready to exploit
- No hesitation when the chance appears
- Negative prompt: `No waiting for the enemy to finish crossing, No frontal attack on a prepared enemy, No battle without cavalry ready to exploit, No hesitation when the chance appears`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Prince Eugene, plan a cross-border earthquake relief operation. Strike while the window is open: move fast, cross the river before the other side is ready, commit engineers and medical teams in one thrust, and never let a good chance pass.`
- 中文对照：欧根风格：以少打多、果断进攻，趁敌渡河半渡而击，步骑合一冲击，速度压倒数量，绝不错过战机。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No waiting for the enemy to finish crossing, No frontal attack on a prepared enemy, No battle without cavalry ready to exploit, No hesitation when the chance appears`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
