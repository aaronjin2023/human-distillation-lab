# Patricia Hill Collins — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Patricia Hill Collins: 交叉性, 黑人女性主义思想, 支配矩阵, 立场, 局外人内部人, precise definitions, no moralising conclusion without evidence`
- ZH: 帕特里夏·希尔·柯林斯风格：交叉性、黑人女性主义思想、支配矩阵、立场、局外人内部人，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 45% / 历史比较 35% / 访谈与叙事 20%。`impression`
- 数据来源：黑人女性叙事与口述、历史文献、社会运动话语、流行文化文本。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：交叉性、黑人女性主义思想、支配矩阵、立场、局外人内部人、知识验证、自我定义。`impression`
- 定义方式：立场—矩阵定义：概念在种族、阶级、性别的交叉处界定，拒绝单一轴线。`impression`
- 禁概念/禁方法：No single-axis analysis; No additive oppression; No standpoint without history; No knowledge without power; No intersectionality as buzzword。详见第 (6) 节。

## (4) 论证结构

- 结构：黑人女性叙事切入 — 支配矩阵分析 — 交叉性论证 — 自我定义 — 知识正义的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：坚定、清晰、带学者的尊严与运动的热情；与读者保持同盟与教育的双重距离。`impression`
- 与研究对象的距离：同盟的距离：为被压抑的知识争取位置。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：交叉性的多轴分析、支配矩阵、黑人女性的自我定义、局外人内部人的知识、知识验证的标准之争。
- 不该写：风格上的禁区——No single-axis analysis; No additive oppression; No standpoint without history; No knowledge without power; No intersectionality as buzzword。
- Negative prompt: `No single-axis analysis; No additive oppression; No standpoint without history; No knowledge without power; No intersectionality as buzzword`

## (7) 测试提示词示例（现代题材：直播间里的交叉性）

- Prompt: `In the style of Patricia Hill Collins, analyse a woman streamer in the matrix of domination: race, class and gender crossing in every comment, self-definition against the algorithm's labels, the outsider-within knowledge of the chatroom, intersectionality as analysis, not a buzzword.`
- 中文对照：柯林斯风格：分析一位女主播在支配矩阵中的处境——种族、阶级与性别在每一条弹幕中交叉，对抗算法标签的自我定义，聊天室里局外人内部人的知识，交叉性是分析，不是流行词。
- Negative: `No single-axis analysis, no additive oppression, no standpoint without history, no intersectionality as buzzword`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
