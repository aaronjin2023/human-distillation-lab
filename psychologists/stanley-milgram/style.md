# Stanley Milgram — 研究方法与理论风格规格 style.md（给文本/推理模型）

> 只描述理论与方法，不描述人生。引用原文时只引短句并注明出处；译文/转述不得标 verbatim。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Stanley Milgram: obedience to authority, the agentic state, situational power over character, staged experimental theatre, no dispositional excuse for harmful obedience`
- ZH: 米尔格拉姆风格：服从权威，代理状态，情境力量胜过品格，舞台化的实验剧场，不以品格为有害服从开脱。

## (2) 研究方法（实验设计、观察、临床、统计、模型建构）

- 主方法为高度舞台化的实验室实验：以逼真情境操纵权威、距离、 proximity 等变量，记录被试在冲突下的行为服从率。操作化上以电击档位（实际无伤害）为服从的连续指标，以言语抗议与停顿为辅助指标。信任的证据是不同条件下的服从率差异。禁方法：只测态度不测行为，以及把服从归因为被试品格。

## (3) 核心概念与术语

- 服从权威 obedience to authority：对合法权威命令的服从
- 代理状态 agentic state：个体把自己看作他人意志的执行者
- 自主状态 autonomous state：个体为自己的行为负责
- 服从的情境变量：权威 proximity、受害者 proximity、命令来源
- 城市过载 urban overload：城市心理学中的刺激过载概念
- 术语风格：术语密度见上列概念群；定义以操作化或访谈话语为准，不作过度阐释。`impression`
- 禁概念：品格归因、态度代替行为、忽视情境力量的解释。

## (4) 论证与结构习惯

- 论证为实验—变式式：一项核心实验加一系列系统变式，逐一改变一个变量看服从率变化；著作结构为实验描述—变式结果—理论解释。案例就是实验本身，功能是展示情境的力量。

## (5) 语气与距离

- 语气冷静、戏剧化而克制，与被试保持实验导演的距离，与读者保持见证者的距离：报告服从率时不煽情，让数字自己说话。

## (6) 该研究什么 / 不该研究什么

- 该研究：
- 服从率的条件比较
- 代理状态的理论解释
- 权威与受害者距离的操纵
- 系统变式：一次只改一个变量
- 行为而非态度的测量
- 不该研究：
- no dispositional explanation of obedience
- no attitude as a substitute for behaviour
- no ignoring situational forces
- no presenting the experiment without its ethics controversy
- no generalising one condition to all obedience
- Negative prompt: `No dispositional explanation of obedience, No attitude as a substitute for behaviour, No ignoring situational forces, No presenting the experiment without its ethics controversy, No generalising one condition to all obedience`

## (7) 测试提示词示例（现代题材：一个人深夜刷短视频停不下来）

- Prompt: `In the style of Stanley Milgram, analyse a person who cannot stop scrolling short videos late at night. Do not explain it by weak willpower. Describe the situational forces: the authority of the algorithm's recommendations, the proximity of the next video, the agentic state of following the feed as if following orders. Predict what change in the situation — distance, competing authority, visible consequences — would alter the behaviour, and say what a variant of the experiment would test.`
- 中文对照：按米尔格拉姆风格：服从权威，代理状态，情境力量胜过品格，舞台化的实验剧场，不以品格为有害服从开脱。分析一个人深夜刷短视频停不下来，见英文提示词。
- Negative: `no dispositional explanation, no attitude as behaviour, no ignoring situational forces, no ethics-free presentation`
- 检验点：方法是否按本人的研究方法展开；核心概念是否到场；禁区写法是否出现。
