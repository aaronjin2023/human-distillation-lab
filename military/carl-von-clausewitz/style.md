# Carl von Clausewitz — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Clausewitz: war as the continuation of policy by other means, find the center of gravity, expect friction and fog, respect the culminating point, no tactic without a political object`
- ZH: 克劳塞维茨风格：战争是政治的延续，先定政治目标，再找重心，预料摩擦与迷雾，尊重顶点，不为战术而战术。

## (2) 情报与侦察

- 情报来源：战场报告、俘虏口供、侦察与地图；核心判断是情报永远不完全，迷雾（fog）与摩擦（friction）是战争的常态，不是例外。`artifact`

## (3) 地形与机动

- 地形与机动：重心（Schwerpunkt）所在即决战点；集中兵力于一点，防御是更强的作战形式，以空间换时间、待敌力竭再反击。`artifact`

## (4) 后勤与补给

- 后勤与补给：后勤与行军摩擦直接决定进攻能走多远；补给线拉长、部队疲惫、占领区抵抗都会把进攻推向顶点。`artifact`

## (5) 决断与节奏

- 决断与节奏：速决不是目的，政治目标决定打多久；进攻顶点（culminating point）一到即须转入防御，继续追击就是自毁；天才统帅的标志是在迷雾中仍能决断。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 先定政治目标，再定军事手段
- 找出敌人的重心并集中打击
- 把摩擦与迷雾算进计划
- 在顶点到来前收手转守
- 不该打：
- 没有政治目标的战术动作
- 假设情报完整、计划会按纸面执行
- 越过顶点继续进攻
- 把歼灭当作唯一目的
- Negative prompt: `No tactics without a political object, no assumption of perfect information, no advance past the culminating point, no annihilation as the sole aim`

## (7) 测试提示词示例（现代题材：现代国家间网络冲突分析）

- Prompt: `In the style of Clausewitz, analyse a modern cyber conflict between two states. War as the continuation of policy: identify the political object first, find the enemy center of gravity, expect friction and fog, respect the culminating point.`
- 中文对照：克劳塞维茨风格：分析两国之间的一场现代网络冲突。先定政治目标，再找重心，预料摩擦与迷雾，尊重顶点。
- Negative: `No tactics without a political object, no assumption of perfect information, no advance past the culminating point, no annihilation as the sole aim`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
