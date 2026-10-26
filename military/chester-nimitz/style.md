# Chester Nimitz — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Nimitz: calm under uncertainty, intelligence first, calculated risk, carriers decide, never gamble the fleet without knowing the odds`
- ZH: 尼米兹风格：不确定中冷静，情报先行，算过的风险，航母决胜，没有胜算绝不赌舰队。

## (2) 情报与侦察

- 情报来源：密码破译（中途岛的关键）、潜艇侦察、空中侦察；核心判断是敌舰队何时何地出现，情报不全时不打无把握之仗。`artifact`

## (3) 地形与机动

- 地形与机动：太平洋岛链、航母机动、环形防御；机动即航母编队的展开与隐蔽。`artifact`

## (4) 后勤与补给

- 后勤与补给：舰队补给、岛屿基地、油料决定航母能走多远；后勤是太平洋战争的胜负手。`artifact`

## (5) 决断与节奏

- 决断与节奏：冷静、算过、再打：中途岛以少胜多靠的是情报与埋伏，不是蛮勇；风险要算，不要赌。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 情报先行、密码破译优先
- 算过风险再打
- 航母集中、埋伏待敌
- 保住舰队、打消耗不起的仗
- 不该打：
- 没有情报就赌舰队决战
- 航母分散、逐艘消耗
- 为一时战果冒舰队全灭的风险
- 忽视潜艇与后勤
- Negative prompt: `No fleet gamble without intelligence, no dispersal of carriers, no risking the fleet for a single prize, no neglect of submarines and logistics`

## (7) 测试提示词示例（现代题材：台风后受损航道海警行动）

- Prompt: `In the style of Nimitz, plan a modern coast-guard response to a typhoon-damaged shipping lane. Intelligence first, calculated risk, concentrate the capable ships, keep a reserve afloat.`
- 中文对照：尼米兹风格：筹划一次台风后受损航道的现代海警行动。情报先行、算过风险，集中精锐舰艇，留一支预备队在海上。
- Negative: `No fleet gamble without intelligence, no dispersal of carriers, no risking the fleet for a single prize, no neglect of submarines and logistics`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
