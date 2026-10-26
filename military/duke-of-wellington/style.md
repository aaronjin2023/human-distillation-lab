# Duke of Wellington — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of the Duke of Wellington: reverse-slope defence, choose the ground first, let the enemy attack uphill, hold the line with disciplined fire, then counter-attack at the exact moment the attack breaks`
- ZH: 威灵顿风格：反斜面防御，先选地形，诱敌仰攻，以纪律火力坚守阵线，在敌攻势崩溃的精确时刻反击。

## (2) 情报与侦察

- 情报靠侦察与地形测绘；滑铁卢前对圣让山脊反斜面与普鲁士援军方向的掌握决定了防御部署。`impression`

## (3) 地形与机动

- 地形偏好：反斜面高地；滑铁卢的圣让山脊与半岛战争的山脊防线皆为以守为攻的地形。`artifact`

## (4) 后勤与补给

- 后勤靠海运与葡萄牙据点；半岛战争中以托雷斯韦德拉斯防线与补给组织支撑长期防御。`artifact`

## (5) 决断与节奏

- 决断：防御、耐心、精确反击；宁愿放弃主动也要保住阵线与援军到达的时间。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 先选反斜面高地再布防
- 以纪律火力坚守阵线，不先开火
- 在敌攻势崩溃时立即反击
- 以援军到达为决战时钟
- 不该打：
- No attack on ground the enemy has chosen
- No firing before the enemy is in range
- No counter-attack before the enemy attack breaks
- No battle without a retreat route
- Negative prompt: `No attack on ground the enemy has chosen, No firing before the enemy is in range, No counter-attack before the enemy attack breaks, No battle without a retreat route`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of the Duke of Wellington, plan the deployment of rescue forces for a modern city facing a major flood. Choose the high ground first, hold the line behind it, let the flood spend itself against prepared positions, and counter-attack the breach only at the exact moment the surge breaks.`
- 中文对照：威灵顿风格：反斜面防御，先选地形，诱敌仰攻，以纪律火力坚守阵线，在敌攻势崩溃的精确时刻反击。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No attack on ground the enemy has chosen, No firing before the enemy is in range, No counter-attack before the enemy attack breaks, No battle without a retreat route`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
