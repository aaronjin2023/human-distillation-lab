# Mikhail Kutuzov — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Mikhail Kutuzov: defence in depth, trade space for time, let the enemy march into the winter, never give the decisive battle the enemy wants, the culminating point will do the work`
- ZH: 库图佐夫风格：纵深防御，以空间换时间，诱敌深入冬季，绝不打敌人想要的决战，顶点会替你完成工作。

## (2) 情报与侦察

- 情报靠侦察与哥萨克骑兵；俄法战争中对法军补给线与行军路线的掌握决定了撤退与反攻的时机。`impression`

## (3) 地形与机动

- 地形偏好：纵深国土与冬季；以空间与气候为武器，博罗季诺为迟滞而非决战。`artifact`

## (4) 后勤与补给

- 后勤靠焦土与法军补给线拉长；法军就地取给在焦土上失效，俄军则靠本土补给。`artifact`

## (5) 决断与节奏

- 决断：撤退、持久、顶点；宁愿放弃莫斯科也要保住军队与时间。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以空间换时间，诱敌深入
- 焦土断敌补给，拉长其补给线
- 在顶点过后才反攻
- 以哥萨克袭扰敌军退路
- 不该打：
- No decisive battle on the enemy's terms
- No defence of a city at the cost of the army
- No counter-attack before the culminating point
- No pursuit without secured supply
- Negative prompt: `No decisive battle on the enemy's terms, No defence of a city at the cost of the army, No counter-attack before the culminating point, No pursuit without secured supply`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Mikhail Kutuzov, plan the deployment of rescue forces for a modern city facing a major flood. Trade space for time: let the flood spend itself over depth, do not give it the decisive breach it wants, and counter-attack only after its culminating point has passed.`
- 中文对照：库图佐夫风格：纵深防御，以空间换时间，诱敌深入冬季，绝不打敌人想要的决战，顶点会替你完成工作。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No decisive battle on the enemy's terms, No defence of a city at the cost of the army, No counter-attack before the culminating point, No pursuit without secured supply`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
