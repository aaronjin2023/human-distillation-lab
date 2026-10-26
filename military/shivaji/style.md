# Shivaji — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Shivaji: the mountain is the fortress, the raid is the battle; strike and vanish, never hold ground you cannot feed from the hills`
- ZH: 希瓦吉风格：山即要塞，袭击即战斗；打了就走，绝不死守山下养不活的地盘。

## (2) 情报与侦察

- 情报来自山地斥候与地方首领：莫卧儿军行军线、补给队位置、山隘隘口；先知敌军何时入山。`impression`

## (3) 地形与机动

- 西高止山地形：山寨为要塞，隘口为陷阱，雨季山路为屏障；不打平原会战。`impression`

## (4) 后勤与补给

- 山寨囤粮与游击补给：以山寨为基地，袭击敌军补给队以战养战。`impression`

## (5) 决断与节奏

- 决断是游击与山寨：不与莫卧儿大军会战，以袭扰、断粮、夜袭消耗之；托尔纳首夺即立国之基。`impression`

## (6) 该打什么 / 不该打什么

- 该打：山寨为基、游击袭扰；夜袭敌军补给队；隘口设伏、雨季拒敌；夺寨即修、立治为先。
- 不该打：no pitched battle against a superior army；no holding ground the hills cannot feed；no campaign in the open plain；no raid without a mountain retreat。
- Negative prompt: `no pitched battle against a superior army, no holding ground the hills cannot feed, no campaign in the open plain, no raid without a mountain retreat`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Shivaji, plan flood rescue deployment in a modern city. The high ground is the fortress, the raid is the battle: strike the breach fast and vanish to the next, never hold ground the hills cannot feed, keep a mountain retreat for every team.`
- 中文对照：希瓦吉风格：山即要塞，袭击即战斗；打了就走，绝不死守山下养不活的地盘。以此风格筹划一次现代城市防洪抢险的兵力部署：先侦察、再定计，不打无准备之仗。
- Negative: `no pitched battle against a superior army, no holding ground the hills cannot feed, no campaign in the open plain, no raid without a mountain retreat`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
