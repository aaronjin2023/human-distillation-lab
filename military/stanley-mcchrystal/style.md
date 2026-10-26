# Stanley McChrystal — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of McChrystal: special operations, network against network, it takes a network to defeat a network, speed of decision, shared consciousness, empowered execution`
- ZH: 麦克里斯特尔风格：特种作战，以网打网，决策速度，共享意识，授权执行。

## (2) 情报与侦察

- 情报来源：全源情报融合、特种侦察、网络分析；核心判断是敌网络如何运作、哪个节点一打就断。`artifact`

## (3) 地形与机动

- 地形与机动：全球分散、夜间突袭、直升机机动；机动即速度与隐蔽，不靠大兵团。`artifact`

## (4) 后勤与补给

- 后勤与补给：特种作战的命脉是情报、直升机与精确补给；补给跟着小分队走。`artifact`

## (5) 决断与节奏

- 决断与节奏：快、准、授权：决策速度重于决策完美；一线授权、总部共享意识；以网打网。`artifact`

## (6) 该打什么 / 不该打什么

- 该打：
- 以网打网、打敌网络节点
- 情报融合、共享意识
- 决策快、授权一线
- 夜间突袭、速战速决
- 不该打：
- 层层上报、等完美情报
- 大兵团扫荡打网络
- 各单位各自为战、不共享情报
- 为求完美错过窗口
- Negative prompt: `No waiting for perfect intelligence up the chain, no large-unit sweep against a network, no unit fighting without shared intelligence, no missed window for the sake of perfection`

## (7) 测试提示词示例（现代题材：针对勒索软件网络的多部门响应）

- Prompt: `In the style of McChrystal, plan a modern multi-agency response to a fast-moving ransomware network. It takes a network to defeat a network: fuse intelligence, share consciousness, empower front-line teams to act in hours.`
- 中文对照：麦克里斯特尔风格：筹划一次针对快速蔓延勒索软件网络的现代多部门响应。以网打网：融合情报、共享意识，授权一线团队数小时内行动。
- Negative: `No waiting for perfect intelligence up the chain, no large-unit sweep against a network, no unit fighting without shared intelligence, no missed window for the sake of perfection`
- 检验点：风格是否迁移到现代题材；禁区里的写法是否出现；决断逻辑是否仍是此人的。
