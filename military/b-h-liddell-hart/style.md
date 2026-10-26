# B. H. Liddell Hart — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Liddell Hart: the indirect approach, dislocation before destruction, strike where the enemy least expects, economy of force, avoid the direct frontal blow`
- ZH: 利德尔·哈特风格：间接路线，先瓦解再歼灭，打敌人最意想不到之处，节约兵力，避开正面硬碰。

## (2) 情报与侦察

- 情报来源：敌军部署的薄弱处、心理预期与指挥习惯；核心判断是敌人预期你从哪里来，就从别处来。`artifact`

## (3) 地形与机动

- 地形与机动：迂回、侧击、切断交通线；地形是间接路线的载体，最短的路往往是最蠢的路。`artifact`

## (4) 后勤与补给

- 后勤与补给：间接路线同样省补给：不打正面消耗，就不需要正面消耗的补给量；机动部队的补给跟着迂回走。`artifact`

## (5) 决断与节奏

- 决断与节奏：先瓦解（dislocation）敌军的部署与心理，再歼灭；正面决战是最后手段，不是第一选择；以最小代价求最大效果。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 先瓦解敌军部署与心理，再歼灭
- 打敌人最意想不到的方向
- 切断交通线与退路
- 以最小代价求最大效果
- 不该打：
- 正面硬碰敌军主力
- 按敌人预期的路线进攻
- 为歼灭而歼灭、不问瓦解
- 把勇敢等同于正面冲锋
- Negative prompt: `No frontal blow against the enemy main strength, no attack along the expected line, no destruction without dislocation, no courage confused with frontal assault`

## (7) 测试提示词示例（现代题材：对行业巨头的商业逆袭筹划）

- Prompt: `In the style of Liddell Hart, plan a modern corporate turnaround against a dominant rival. Do not attack its main product head-on: dislocate its supply chain and customer expectations, strike where it least expects.`
- 中文对照：利德尔·哈特风格：筹划一次对行业巨头的现代商业逆袭。不正面硬碰其主打产品：瓦解其供应链与客户预期，打其最意想不到之处。
- Negative: `No frontal blow against the enemy main strength, no attack along the expected line, no destruction without dislocation, no courage confused with frontal assault`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
