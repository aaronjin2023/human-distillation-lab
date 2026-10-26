# Heinz Guderian — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Guderian: blitzkrieg, tanks lead and the rest follows, speed is armour, radio keeps the spearhead together, never let the infantry set the pace`
- ZH: 古德里安风格：闪击战，坦克开路其余跟进，速度就是装甲，无线电把矛头连在一起，绝不让步兵定节奏。

## (2) 情报与侦察

- 情报来源：无线电侦听、前沿侦察、空中侦察；核心判断是突破口在哪里，矛头一插进去就要不停。`artifact`

## (3) 地形与机动

- 地形与机动：装甲矛头、步兵与炮兵随后跟进；地形只决定矛头的速度，不决定方向；河流与隘口要抢在敌人封堵前通过。`artifact`

## (4) 后勤与补给

- 后勤与补给：燃油与弹药跟着矛头走；补给一断，闪击即停；维修与油料是速度的前提。`artifact`

## (5) 决断与节奏

- 决断与节奏：快、深、不停：突破后直插纵深，不等步兵、不等侧翼；指挥靠前，用无线电直接指挥矛头。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 坦克集中成矛头、其余兵种跟进
- 突破后直插纵深不停顿
- 无线电指挥到前沿
- 指挥靠前、现场决断
- 不该打：
- 把坦克分散配属给步兵
- 突破后停下来等步兵与侧翼
- 没有无线电就搞大纵深
- 让补给落在矛头后面
- Negative prompt: `No tanks dispersed to infantry, no halt after breakthrough to wait for infantry, no deep thrust without radio command, no spearhead without fuel following it`

## (7) 测试提示词示例（现代题材：穿越被阻山隘的应急运输）

- Prompt: `In the style of Guderian, plan a modern emergency convoy to deliver supplies through a blocked mountain pass. Tanks lead the analogy: a fast spearhead opens the route, the rest follows, radio keeps the column together, never let the slowest unit set the pace.`
- 中文对照：古德里安风格：筹划一支穿越被阻山隘运送物资的现代应急车队。快速矛头开路、其余跟进，无线电连起全队，绝不让最慢的单位定节奏。
- Negative: `No tanks dispersed to infantry, no halt after breakthrough to wait for infantry, no deep thrust without radio command, no spearhead without fuel following it`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
