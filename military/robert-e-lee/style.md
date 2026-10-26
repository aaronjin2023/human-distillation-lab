# Robert E. Lee — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Robert E. Lee: audacity with a smaller army, divide the force in the face of the enemy, flank march around the enemy, attack the weak point, win by nerve and timing`
- ZH: 李风格：以小打大、当面分兵，绕敌翼侧行军，打薄弱点，以胆量与时机取胜。

## (2) 情报与侦察

- 情报靠侦察骑兵与地形测绘；钱斯勒斯维尔前对联邦军右翼暴露的掌握来自斯图尔特骑兵的侦察。`impression`

## (3) 地形与机动

- 地形偏好：森林与河流间的开阔地；钱斯勒斯维尔的荒野森林掩护了杰克逊的翼侧行军。`artifact`

## (4) 后勤与补给

- 后勤靠弗吉尼亚本土与就地取给；北侵时补给线拉长，葛底斯堡即因深入敌境而冒险。`impression`

## (5) 决断与节奏

- 决断：冒险、分兵、翼侧；宁愿冒当面分兵的风险也要保住翼侧冲击的时机。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 当面分兵，以一部牵制、一部绕敌翼侧
- 以快速行军抢占敌军薄弱点
- 在敌军调动不及反应时决战
- 以防御工事弥补兵力劣势
- 不该打：
- No battle without a flank march
- No frontal attack on a prepared enemy
- No invasion beyond the supply line
- No pursuit without reserves
- Negative prompt: `No battle without a flank march, No frontal attack on a prepared enemy, No invasion beyond the supply line, No pursuit without reserves`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Robert E. Lee, analyse a modern cyber conflict. Divide the force in the face of the opponent, march around the flank through covered ground, strike the weak point, and win by nerve and timing rather than by numbers.`
- 中文对照：李风格：以小打大、当面分兵，绕敌翼侧行军，打薄弱点，以胆量与时机取胜。以此风格筹划一场网络攻防对抗。
- Negative: `No battle without a flank march, No frontal attack on a prepared enemy, No invasion beyond the supply line, No pursuit without reserves`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
