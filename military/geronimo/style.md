# Geronimo — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Geronimo: small-band guerrilla war in the mountains and desert, strike and vanish into the rocks, live off the land, never accept a battle against a large column, freedom of movement is survival`
- ZH: 杰罗尼莫风格：小股山地沙漠游击战，打了就消失在岩石间，就地取给，绝不与大纵队打会战，机动自由就是生存。

## (2) 情报与侦察

- 情报靠侦察与地形熟悉；对美军纵队行军路线与水源的掌握来自阿帕奇人的本地知识。`impression`

## (3) 地形与机动

- 地形偏好：西南山地与沙漠；以岩石与峡谷为掩护，美军大纵队无法展开。`artifact`

## (4) 后勤与补给

- 后勤靠就地取给与袭击补给；小股部队无固定补给线，靠沿途取给与缴获。`impression`

## (5) 决断与节奏

- 决断：游击、消失、持久；宁愿放弃定居也要保住机动自由。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以小股部队袭击美军纵队与补给
- 打了就消失在山地岩石间
- 就地取给，不带辎重
- 在美军分兵时集中打孤立之敌
- 不该打：
- No pitched battle against a large column
- No defence of a fixed camp at the cost of mobility
- No battle without a mountain retreat route
- No raid without scouts ahead
- Negative prompt: `No pitched battle against a large column, No defence of a fixed camp at the cost of mobility, No battle without a mountain retreat route, No raid without scouts ahead`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Geronimo, analyse a modern cyber conflict. Fight a small-band guerrilla war: strike and vanish, live off the land, never accept a battle against a large column, and treat freedom of movement as survival itself.`
- 中文对照：杰罗尼莫风格：小股山地沙漠游击战，打了就消失在岩石间，就地取给，绝不与大纵队打会战，机动自由就是生存。以此风格筹划一场网络攻防对抗。
- Negative: `No pitched battle against a large column, No defence of a fixed camp at the cost of mobility, No battle without a mountain retreat route, No raid without scouts ahead`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
