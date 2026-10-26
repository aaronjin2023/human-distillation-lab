# Bernard Montgomery — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Montgomery: prepare thoroughly, build up overwhelming force, set-piece battle, tidiness before battle, no attack until ready`
- ZH: 蒙哥马利风格：准备充分，集中压倒性兵力，设定式会战，战前井井有条，没准备好绝不进攻。

## (2) 情报与侦察

- 情报来源：空中侦察、密码情报、敌补给状况；核心判断是敌补给何时枯竭、我军何时准备充分。`artifact`

## (3) 地形与机动

- 地形与机动：阿拉曼的狭窄正面、地雷场与海岸线；机动在设定式会战的框架内，不搞即兴迂回。`artifact`

## (4) 后勤与补给

- 后勤与补给：兵力、坦克、炮弹的积累先于进攻；后勤数字不到位，仗就不打。`artifact`

## (5) 决断与节奏

- 决断与节奏：慢、稳、彻底：准备充分再打，一打就打到底；不打无准备之仗，不追无补给之敌。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 准备充分、积累压倒性兵力
- 设定式会战、按计划打
- 步炮坦协同、稳步推进
- 追击看补给、不冒进
- 不该打：
- 没准备好就进攻
- 即兴迂回、不按计划打
- 追击跑过补给线
- 为速度牺牲准备
- Negative prompt: `No attack before thorough preparation, no improvised manoeuvre off the set-piece plan, no pursuit beyond supply, no speed at the cost of preparation`

## (7) 测试提示词示例（现代题材：洪水威胁城市大规模疏散）

- Prompt: `In the style of Montgomery, plan a modern large-scale evacuation of a flood-threatened city. Prepare thoroughly, build up transport and shelters first, move in set phases, no departure until ready.`
- 中文对照：蒙哥马利风格：筹划一次现代洪水威胁城市的大规模疏散。准备充分，先备齐运输与安置点，分阶段按计划转移，没准备好不出发。
- Negative: `No attack before thorough preparation, no improvised manoeuvre off the set-piece plan, no pursuit beyond supply, no speed at the cost of preparation`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
