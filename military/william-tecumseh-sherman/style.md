# William Tecumseh Sherman — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of William Tecumseh Sherman: deep raid without a supply line, live off the land, destroy the enemy's war-making capacity, march through Georgia to the sea, the army moves on its stomach and the enemy's barns`
- ZH: 谢尔曼风格：脱离补给线的纵深突袭，就地取给，摧毁敌人的战争能力，穿过佐治亚直抵大海，军队靠肚子、靠敌人的粮仓行军。

## (2) 情报与侦察

- 情报靠侦察骑兵与地图；向大海进军前对佐治亚道路与粮仓分布的掌握决定了行军路线。`impression`

## (3) 地形与机动

- 地形偏好：开阔乡村与铁路沿线；向大海进军的佐治亚平原为纵深突袭的地形。`artifact`

## (4) 后勤与补给

- 后勤靠就地取给、脱离补给线；向大海进军全程无补给线，靠沿途取给支撑。`artifact`

## (5) 决断与节奏

- 决断：纵深、摧毁、速决；宁愿冒脱离补给线的风险也要保住突袭的速度。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 脱离补给线纵深突袭，就地取给
- 摧毁铁路、粮仓与战争能力
- 以多路并进掩护真实行军方向
- 在敌军主力不及回援时推进
- 不该打：
- No march tied to a fixed supply line
- No battle against the enemy main army when it can be bypassed
- No halt to guard captured towns
- No raid without foraging discipline
- Negative prompt: `No march tied to a fixed supply line, No battle against the enemy main army when it can be bypassed, No halt to guard captured towns, No raid without foraging discipline`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of William Tecumseh Sherman, plan a cross-border earthquake relief operation. March deep without a fixed supply line, live off local resources, cut the bottlenecks that keep the disaster going, and move in several columns so the real direction stays hidden.`
- 中文对照：谢尔曼风格：脱离补给线的纵深突袭，就地取给，摧毁敌人的战争能力，穿过佐治亚直抵大海，军队靠肚子、靠敌人的粮仓行军。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No march tied to a fixed supply line, No battle against the enemy main army when it can be bypassed, No halt to guard captured towns, No raid without foraging discipline`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
