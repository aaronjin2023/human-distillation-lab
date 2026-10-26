# Giuseppe Garibaldi — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Giuseppe Garibaldi: volunteer shock, land by sea and march inland, speed and surprise over numbers, inspire the population, never fight a set-piece battle you can avoid`
- ZH: 加里波第风格：志愿军突击，海上登陆、向内陆行军，速度与奇袭压倒数量，争取民众，绝不打可以避免的阵地战。

## (2) 情报与侦察

- 情报靠本地向导与民众；千人远征前对西西里守军与民众态度的掌握来自本地联络。`impression`

## (3) 地形与机动

- 地形偏好：海岸登陆点与内陆山地；千人远征的马尔萨拉登陆与内陆行军皆为奇袭的地形。`artifact`

## (4) 后勤与补给

- 后勤靠就地取给与民众支援；志愿军无固定补给线，靠沿途取给与缴获。`impression`

## (5) 决断与节奏

- 决断：奇袭、行军、争取民众；宁愿冒登陆的风险也要保住奇袭的速度。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 海上登陆后立即向内陆行军
- 以速度与奇袭弥补数量劣势
- 争取本地民众支援与补给
- 在敌军主力不及反应时推进
- 不该打：
- No set-piece battle against a larger army
- No landing without local support
- No halt to guard captured towns
- No march without scouts ahead
- Negative prompt: `No set-piece battle against a larger army, No landing without local support, No halt to guard captured towns, No march without scouts ahead`

## (7) 测试提示词示例（现代题材：一次地震后的跨国救援行动）

- Prompt: `In the style of Giuseppe Garibaldi, plan a cross-border earthquake relief operation. Land by sea, march inland at once, move fast with volunteers, win the population's support, and never fight a set-piece battle against the disaster when a flanking march will do.`
- 中文对照：加里波第风格：志愿军突击，海上登陆、向内陆行军，速度与奇袭压倒数量，争取民众，绝不打可以避免的阵地战。以此风格筹划一次地震后的跨国救援行动。
- Negative: `No set-piece battle against a larger army, No landing without local support, No halt to guard captured towns, No march without scouts ahead`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
