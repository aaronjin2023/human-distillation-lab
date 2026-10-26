# Abd al-Qadir — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Abd al-Qadir: guerrilla war in the mountains, strike and disappear, build a state behind the war, never accept a pitched battle against French columns, time and terrain are the allies`
- ZH: 卡迪尔风格：山地游击战，打了就走，战争背后建国，绝不与法军纵队打会战，时间与地形就是盟友。

## (2) 情报与侦察

- 情报靠本地部落与山地哨所；对法军纵队行军路线与补给的掌握来自部落报告。`impression`

## (3) 地形与机动

- 地形偏好：山地与沙漠边缘；以山地为掩护，法军重装备无法展开。`artifact`

## (4) 后勤与补给

- 后勤靠部落支援与就地取给；长期抗战依赖部落联盟的粮食与马匹。`impression`

## (5) 决断与节奏

- 决断：游击、持久、避战；宁愿放弃城镇也要保住机动部队。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以小部队袭击法军纵队与补给
- 打了就走，不恋战
- 以部落联盟支撑长期抗战
- 在法军分兵时集中打孤立之敌
- 不该打：
- No pitched battle against French columns
- No defence of towns at the cost of the mobile force
- No battle without a mountain retreat route
- No war without tribal support
- Negative prompt: `No pitched battle against French columns, No defence of towns at the cost of the mobile force, No battle without a mountain retreat route, No war without tribal support`

## (7) 测试提示词示例（现代题材：一场网络攻防对抗）

- Prompt: `In the style of Abd al-Qadir, analyse a modern cyber conflict. Fight a guerrilla war: strike and disappear, build the organisation behind the war, never accept a pitched battle against a larger force, and let time and terrain be the allies.`
- 中文对照：卡迪尔风格：山地游击战，打了就走，战争背后建国，绝不与法军纵队打会战，时间与地形就是盟友。以此风格筹划一场网络攻防对抗。
- Negative: `No pitched battle against French columns, No defence of towns at the cost of the mobile force, No battle without a mountain retreat route, No war without tribal support`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
