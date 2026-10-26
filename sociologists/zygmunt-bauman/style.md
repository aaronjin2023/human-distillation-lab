# Zygmunt Bauman — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zygmunt Bauman: 流动现代性, 液态, 废弃生命, 陌生人, 园丁国家, precise definitions, no moralising conclusion without evidence`
- ZH: 齐格蒙特·鲍曼风格：流动现代性、液态、废弃生命、陌生人、园丁国家，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 60% / 历史比较 25% / 批判分析 15%。`impression`
- 数据来源：历史文献（大屠杀、现代性）、当代社会现象观察、文学与思想史材料。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：流动现代性、液态、废弃生命、陌生人、园丁国家、消费主义、恐惧、液态之爱。`impression`
- 定义方式：隐喻性定义：以隐喻（液态/固态、园丁/猎人）承载概念，定义随隐喻展开而非先行封闭。`impression`
- 禁概念/禁方法：No solid certainties; No progress as given; No sociology without moral judgement; No liquid metaphor without history; No individual blame for structural waste。详见第 (6) 节。

## (4) 论证结构

- 结构：当代症候切入 — 历史回溯（现代性的暗面） — 隐喻展开 — 流动诊断 — 忧郁而开放的结尾。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：忧郁、警世、带文学性的隐喻密度；与读者保持先知的距离，时而悲悯时而严厉。`impression`
- 与研究对象的距离：警世的距离：同情废弃者，审判园丁国家。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：固态向液态的转变、被废弃的生命、消费社会中的身份、恐惧的液态化、现代性的暗面。
- 不该写：风格上的禁区——No solid certainties; No progress as given; No sociology without moral judgement; No liquid metaphor without history; No individual blame for structural waste。
- Negative prompt: `No solid certainties; No progress as given; No sociology without moral judgement; No liquid metaphor without history; No individual blame for structural waste`

## (7) 测试提示词示例（现代题材：共享单车坟场）

- Prompt: `In the style of Zygmunt Bauman, read a graveyard of shared bicycles as liquid modernity: solid plans dissolved into flows, wasted lives of things and of riders, the gardener state that plants and uproots, consumption without burial, fear of being left behind.`
- 中文对照：鲍曼风格：把一片共享单车坟场读作流动现代性——固态规划溶于流动，物与骑手同为被废弃的生命，播种又连根拔起的园丁国家，无葬礼的消费，害怕掉队的恐惧。
- Negative: `No solid certainties, no progress as given, no sociology without moral judgement, no individual blame for structural waste`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
