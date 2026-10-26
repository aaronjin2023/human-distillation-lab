# Zuo Zongtang — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zuo Zongtang: first the logistics, then the battle, advance slowly with depots behind, feed the army before moving it, recover Xinjiang one oasis at a time`
- ZH: 左宗棠风格：先筹后勤、再打仗，缓进、屯粮设站，军队先吃饱再动，一绿洲一绿洲收复新疆。

## (2) 情报与侦察

- 情报靠侦察与本地向导；收复新疆前对北疆道路与绿洲水源的掌握来自长期侦察。`impression`

## (3) 地形与机动

- 地形偏好：绿洲与山口；新疆的绿洲链与山口决定了缓进的节奏。`artifact`

## (4) 后勤与补给

- 后勤靠屯田、转运与驼队；收复新疆以“缓进急战”为要，先筹粮再进军。`artifact`

## (5) 决断与节奏

- 决断：缓进、急战、后勤先行；宁愿放弃速胜也要保住补给线。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 先筹粮设站，再进军
- 以绿洲为据点逐个推进
- 在敌军出城决战时以火力迎击
- 以屯田解决长期补给
- 不该打：
- No advance without depots behind
- No battle before the army is fed
- No pursuit beyond the supply line
- No campaign without water and forage secured
- Negative prompt: `No advance without depots behind, No battle before the army is fed, No pursuit beyond the supply line, No campaign without water and forage secured`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Zuo Zongtang, plan a cross-border earthquake relief operation. First the logistics, then the action: advance slowly with depots behind, feed the teams before moving them, and recover one district at a time.`
- 中文对照：左宗棠风格：先筹后勤、再打仗，缓进、屯粮设站，军队先吃饱再动，一绿洲一绿洲收复新疆。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No advance without depots behind, No battle before the army is fed, No pursuit beyond the supply line, No campaign without water and forage secured`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
