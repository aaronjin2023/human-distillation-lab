# Erwin Rommel — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Rommel: speed and audacity, lead from the front, strike before the enemy is ready, use terrain and deception, never outrun supply`
- ZH: 隆美尔风格：速度与胆略，靠前指挥，敌未备而击之，善用地形与欺骗，绝不跑过补给。

## (2) 情报与侦察

- 情报来源：前沿侦察、无线电侦听、俘虏口供；核心判断是敌防线哪里薄、哪里还没准备好。`artifact`

## (3) 地形与机动

- 地形与机动：沙漠机动、迂回侧击、利用地形遮蔽；机动即生命，停下来就是死。`artifact`

## (4) 后勤与补给

- 后勤与补给：北非的教训是补给线决定一切；燃油与弹药跟不上，速度反成自杀。`artifact`

## (5) 决断与节奏

- 决断与节奏：快、险、靠前：亲临前沿看清战况再决断；追击要狠，但一过补给顶点即收。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 靠前指挥、亲临前沿
- 敌未备而击之
- 迂回侧击、不打正面
- 追击狠、但看补给顶点
- 不该打：
- 坐镇后方等报告再决断
- 正面硬碰已设防的阵地
- 追击跑过补给线
- 忽视地形与欺骗
- Negative prompt: `No command from the rear waiting for reports, no frontal assault on prepared positions, no pursuit beyond supply lines, no movement without deception and terrain`

## (7) 测试提示词示例（现代题材：穿越灾区的快速救援车队）

- Prompt: `In the style of Rommel, plan a modern rapid rescue convoy through a disaster zone. Lead from the front, move fast around the blocked roads, strike the gap before conditions worsen, stop at the supply limit.`
- 中文对照：隆美尔风格：筹划一支穿越灾区的现代快速救援车队。靠前指挥，绕开阻断路段快速机动，抢在局势恶化前打通缺口，到补给极限即收。
- Negative: `No command from the rear waiting for reports, no frontal assault on prepared positions, no pursuit beyond supply lines, no movement without deception and terrain`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
