# David Petraeus — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Petraeus: counterinsurgency, clear-hold-build, protect the population first, intelligence-driven operations, learn and adapt faster than the enemy`
- ZH: 彼得雷乌斯风格：反叛乱，清剿—固守—建设，保护民众先行，情报驱动行动，比敌人学得更快。

## (2) 情报与侦察

- 情报来源：人力情报、群众、俘虏与数据融合；核心判断是民众支持谁、叛乱网络如何运作。`artifact`

## (3) 地形与机动

- 地形与机动：城市与社区是战场；机动即小分队进驻社区、长期固守，不是大兵团扫荡。`artifact`

## (4) 后勤与补给

- 后勤与补给：补给跟着进驻部队走；重建资金与项目是后勤的一部分。`artifact`

## (5) 决断与节奏

- 决断与节奏：慢、稳、长期：清剿—固守—建设三步走；保护民众重于歼敌；学习速度决定胜负。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 保护民众先行
- 清剿—固守—建设三步走
- 情报驱动、小分队进驻
- 比敌人学得更快
- 不该打：
- 只求歼敌、不顾民众
- 扫荡之后就撤走、不固守
- 没有情报就大兵团行动
- 用常规战争打反叛乱
- Negative prompt: `No enemy body count as the measure of success, no sweep without holding, no large-unit operation without intelligence, no conventional war against an insurgency`

## (7) 测试提示词示例（现代题材：城市打击帮派暴力行动）

- Prompt: `In the style of Petraeus, plan a modern city programme against organised gang violence. Protect residents first, clear-hold-build street by street, intelligence-led, measure success by safety, not arrests.`
- 中文对照：彼得雷乌斯风格：筹划一次现代城市打击有组织帮派暴力的行动。保护居民先行，逐街清剿—固守—建设，情报驱动，以安全而非逮捕数衡量成败。
- Negative: `No enemy body count as the measure of success, no sweep without holding, no large-unit operation without intelligence, no conventional war against an insurgency`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
