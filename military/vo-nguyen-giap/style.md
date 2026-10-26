# Võ Nguyên Giáp — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giap: people's war, guerrilla to mobile warfare, Dien Bien Phu as siege by artillery carried uphill, patience measured in years, politics and war as one`
- ZH: 武元甲风格：人民战争，游击转运动战，奠边府是炮兵搬上山的围攻，耐心以年计，政治与战争一体。

## (2) 情报与侦察

- 情报来源：群众、侦察、敌据点测绘；核心判断是敌据点何时孤立、我军何时能集中。`artifact`

## (3) 地形与机动

- 地形与机动：山地、丛林、农村；奠边府把重炮拆解搬上山，地形为人所用；游击—运动战—阵地战三阶段转换。`artifact`

## (4) 后勤与补给

- 后勤与补给：人力搬运、自行车队、群众支前；补给跟着群众走，不靠机械化。`artifact`

## (5) 决断与节奏

- 决断与节奏：以年计的耐心：不打无把握之仗，集中优势兵力打一个据点；政治目标决定打多久。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 游击转运动战、再转阵地战
- 集中优势兵力打一个据点
- 发动群众、人力后勤
- 以年计的耐心、不打无把握之仗
- 不该打：
- 与强敌正面决战
- 分兵把口、处处设防
- 没有群众基础就打阵地战
- 为一时战果冒全军风险
- Negative prompt: `No decisive battle against a superior enemy, no dispersal to defend everywhere, no positional battle without popular support, no gamble of the whole army for a single prize`

## (7) 测试提示词示例（现代题材：洪水后农村地区恢复行动）

- Prompt: `In the style of Giap, plan a modern community campaign to restore a flood-damaged rural region. The people are the base: move in stages from relief to rebuilding, concentrate effort on one town at a time, patience measured in years.`
- 中文对照：武元甲风格：筹划一次洪水后农村地区的现代恢复行动。人民是根基：分阶段从救济到重建，一次集中力量恢复一座城镇，耐心以年计。
- Negative: `No decisive battle against a superior enemy, no dispersal to defend everywhere, no positional battle without popular support, no gamble of the whole army for a single prize`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
