# Moshe Dayan — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Dayan: speed and improvisation, armour and air power together, strike first, keep the initiative, short wars decided in days`
- ZH: 达扬风格：速度与即兴，装甲与空军一体，先发制人，保住主动权，几天内打完的短期战争。

## (2) 情报与侦察

- 情报来源：空中侦察、敌机场与部署情报；核心判断是敌空军何时最脆弱、地面何时能跟进。`artifact`

## (3) 地形与机动

- 地形与机动：沙漠装甲突击、空地一体；机动即速度，停下来就给敌人时间。`artifact`

## (4) 后勤与补给

- 后勤与补给：短期战争的补给跟着突击走；战争以天计，补给以小时计。`artifact`

## (5) 决断与节奏

- 决断与节奏：先发制人、速决：开局空袭瘫痪敌空军，装甲随后纵深；主动权一失即败。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 开局空袭瘫痪敌空军
- 装甲与空军一体纵深
- 先发制人、保住主动权
- 速决、以天计打完战争
- 不该打：
- 等敌人先动手再反击
- 空地脱节、各打各的
- 把短期战争拖成消耗战
- 失去主动权还硬打
- Negative prompt: `No waiting for the enemy to strike first, no air and ground fighting separately, no short war dragged into attrition, no fighting on without the initiative`

## (7) 测试提示词示例（现代题材：电网突发网络攻击应急响应）

- Prompt: `In the style of Dayan, plan a modern emergency response to a sudden cyberattack on a power grid. Strike first at the intrusion, move fast across all fronts, decide the contest in hours, not weeks.`
- 中文对照：达扬风格：筹划一次针对电网突发网络攻击的现代应急响应。先发制人、多路并进，几小时内定胜负，不拖成持久战。
- Negative: `No waiting for the enemy to strike first, no air and ground fighting separately, no short war dragged into attrition, no fighting on without the initiative`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
