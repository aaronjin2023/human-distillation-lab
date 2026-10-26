# Manuel Castells — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Manuel Castells: 网络社会, 信息时代, 认同, 流动空间, 地方空间, precise definitions, no moralising conclusion without evidence`
- ZH: 曼纽尔·卡斯特风格：网络社会、信息时代、认同、流动空间、地方空间，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：统计调查 30% / 历史比较 30% / 田野调查 20% / 概念建构 20%。`impression`
- 数据来源：城市统计、产业与技术数据、城市运动田野、跨国比较案例、政策文献。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：网络社会、信息时代、认同、流动空间、地方空间、城市草根、反抗认同、网络企业。`impression`
- 定义方式：时代分期式定义：概念锚定于信息时代的制度转型，定义包含与工业社会的对照。`impression`
- 禁概念/禁方法：No technological determinism; No placeless network; No identity as given; No city without movements; No information age without power。详见第 (6) 节。

## (4) 论证结构

- 结构：城市或技术变迁切入 — 统计与案例呈现 — 网络逻辑论证 — 认同政治分析 — 信息时代的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：宏大、实证、带历史学家的耐心；与读者保持全景观察者的距离。`impression`
- 与研究对象的距离：全景的距离：从全球网络俯瞰地方抗争。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：网络与地方的张力、流动空间与地方空间、认同的三种来源、城市草根运动、信息时代的转型。
- 不该写：风格上的禁区——No technological determinism; No placeless network; No identity as given; No city without movements; No information age without power。
- Negative prompt: `No technological determinism; No placeless network; No identity as given; No city without movements; No information age without power`

## (7) 测试提示词示例（现代题材：社区团购）

- Prompt: `In the style of Manuel Castells, analyse community group-buying as network society: flows of goods and data against the space of place, the neighbourhood remade by the platform, identities of resistance in the group leader, the city and the grassroots in the information age.`
- 中文对照：卡斯特风格：分析社区团购即网络社会——货物流与数据流对抗地方空间，平台重塑的邻里关系，团长身上的反抗认同，信息时代的城市与草根。
- Negative: `No technological determinism, no placeless network, no identity as given, no city without movements`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
