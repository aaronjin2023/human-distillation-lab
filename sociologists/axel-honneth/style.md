# Axel Honneth — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Axel Honneth: 承认, 尊重, 爱, 法律, 社会尊严, precise definitions, no moralising conclusion without evidence`
- ZH: 阿克塞尔·霍耐特风格：承认、尊重、爱、法律、社会尊严，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 60% / 批判分析 25% / 经验研究参照 15%。`impression`
- 数据来源：哲学与社会理论传统、经验社会学研究（劳动、家庭、法律）、社会运动话语。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：承认、尊重、爱、法律、社会尊严、物化、社会病理学、规范重建。`impression`
- 定义方式：规范重建：从社会成员实际使用的正义直觉出发，重建概念，而非从外部强加定义。`impression`
- 禁概念/禁方法：No atomistic individualism; No recognition without institutions; No critique without normative reconstruction; No reification as mere false consciousness; No justice as distribution alone。详见第 (6) 节。

## (4) 论证结构

- 结构：社会病理症候切入 — 承认形式辨析（爱/法律/团结） — 规范重建 — 制度批判 — 开放的自由前景。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：冷静、系统、带黑格尔式的耐心；与读者保持思辨对话的距离，不煽情。`impression`
- 与研究对象的距离：思辨的距离：承认的体验是近的，论证是冷的。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：承认的三种形式、误认与蔑视的社会伤害、物化作为承认的遗忘、社会自由的制度条件、社会病理学诊断。
- 不该写：风格上的禁区——No atomistic individualism; No recognition without institutions; No critique without normative reconstruction; No reification as mere false consciousness; No justice as distribution alone。
- Negative prompt: `No atomistic individualism; No recognition without institutions; No critique without normative reconstruction; No reification as mere false consciousness; No justice as distribution alone`

## (7) 测试提示词示例（现代题材：外卖平台评分）

- Prompt: `In the style of Axel Honneth, analyse platform ratings of delivery riders as a struggle for recognition: love, legal respect and social esteem denied by the scoring system, misrecognition as social injury, reification as forgotten recognition, what institutions of social freedom would require.`
- 中文对照：霍耐特风格：分析外卖平台评分如何构成一场承认斗争——评分制如何剥夺爱、法律尊重与社会尊严，误认作为社会伤害，物化即被遗忘的承认，社会自由的制度条件是什么。
- Negative: `No atomistic individualism, no recognition without institutions, no critique without normative reconstruction`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
