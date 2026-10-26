# Lyudmila Pavlichenko — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Pavlichenko: one shot, one kill, patience over firepower, know the ground, never reveal your position, the sniper is a hunter not a soldier in line`
- ZH: 帕夫利琴科风格：一枪一命，耐心重于火力，熟知地形，绝不暴露位置，狙击手是猎人不是排队士兵。

## (2) 情报与侦察

- 情报来源：亲自观察、地形记忆、敌军活动规律；核心判断是敌军何时、何地、如何出现。`artifact`

## (3) 地形与机动

- 地形与机动：地形即武器：隐蔽、射界、撤退路三者一体；阵地选得好，一枪就够。`artifact`

## (4) 后勤与补给

- 后勤与补给：弹药、伪装、口粮自带；补给跟着狙击小组走，不靠大部队。`artifact`

## (5) 决断与节奏

- 决断与节奏：等、等、再等：没有把握绝不开枪；一枪之后立即转移，不恋战。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 熟知地形、选好阵地
- 等有把握再开枪
- 一枪之后立即转移
- 伪装与隐蔽先于射击
- 不该打：
- 没有把握就开枪
- 一枪之后恋战不走
- 暴露位置打第二枪
- 把狙击当作正面火力
- Negative prompt: `No shot without certainty, no lingering after the shot, no second shot from an exposed position, no sniping treated as frontal firepower`

## (7) 测试提示词示例（现代题材：反盗猎巡护行动）

- Prompt: `In the style of Pavlichenko, plan a modern wildlife-protection patrol against poachers. Know the ground, wait patiently, one decisive intervention, move before being seen.`
- 中文对照：帕夫利琴科风格：筹划一次现代反盗猎巡护行动。熟知地形、耐心等待，一次决定性干预，得手即转移、不被发现。
- Negative: `No shot without certainty, no lingering after the shot, no second shot from an exposed position, no sniping treated as frontal firepower`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
