# William Slim — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Slim: rebuild the army first, fight the battle the enemy wants last, logistics through jungle, morale is a weapon, turn defence into encirclement`
- ZH: 斯利姆风格：先重建军队，打敌人最不想打的仗，丛林后勤，士气就是武器，防御转包围。

## (2) 情报与侦察

- 情报来源：丛林侦察、空中侦察、敌补给状况；核心判断是敌补给何时断、我军何时能反攻。`artifact`

## (3) 地形与机动

- 地形与机动：丛林、河流、山地；机动靠空运与河流，不靠公路；英帕尔以守为攻、诱敌深入再包围。`artifact`

## (4) 后勤与补给

- 后勤与补给：空运补给是缅甸战场的命脉；补给跟着部队走，断了补给的敌军自会崩溃。`artifact`

## (5) 决断与节奏

- 决断与节奏：先重建、再决战：士气与训练不到位不打；诱敌深入、待其补给断绝再包围歼灭。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 先重建军队与士气
- 诱敌深入、待其补给断绝
- 空运补给先行
- 防御转包围、歼灭于退路
- 不该打：
- 士气未恢复就决战
- 正面硬碰敌军主力
- 没有空运补给就纵深追击
- 把丛林当作不可逾越的障碍
- Negative prompt: `No decisive battle before rebuilding morale, no frontal blow against the enemy main force, no deep pursuit without air supply, no jungle treated as impassable`

## (7) 测试提示词示例（现代题材：山体滑坡后偏远山区救援）

- Prompt: `In the style of Slim, plan a modern relief operation in a remote mountain region after a landslide. Rebuild the team first, supply by air, let the blocked roads wear the problem down, then move in to encircle the isolated villages with aid.`
- 中文对照：斯利姆风格：筹划一次山体滑坡后偏远山区的现代救援。先重建队伍，空运补给先行，让阻断的道路消耗问题，再进山包围式覆盖孤立村庄。
- Negative: `No decisive battle before rebuilding morale, no frontal blow against the enemy main force, no deep pursuit without air supply, no jungle treated as impassable`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
