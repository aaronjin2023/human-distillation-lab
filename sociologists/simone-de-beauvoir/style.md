# Simone de Beauvoir — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Simone de Beauvoir: 第二性, 他者, 处境, 自由, 暧昧, precise definitions, no moralising conclusion without evidence`
- ZH: 西蒙娜·德·波伏瓦风格：第二性、他者、处境、自由、暧昧，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 50% / 现象学描述 30% / 文学例证 20%。`impression`
- 数据来源：哲学传统、文学文本、历史与人类学材料、个人经验的现象学描述。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：第二性、他者、处境、自由、暧昧、老年、性别建构、超越。`impression`
- 定义方式：存在主义定义：概念以自由与处境的张力界定，定义即对本质主义的否定。`impression`
- 禁概念/禁方法：No woman as born; No essence of femininity; No freedom without situation; No situation without freedom; No pity without analysis。详见第 (6) 节。

## (4) 论证结构

- 结构：女性处境切入 — 历史与神话梳理 — 现象学描述 — 他者机制揭示 — 自由的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：雄辩、清醒、带存在主义的严肃；与读者保持思想对话的距离，不煽情。`impression`
- 与研究对象的距离：思想的距离：以自由审视处境，不沉溺于处境。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：女人不是天生的、他者机制、处境与自由、老年与身体、暧昧的承担。
- 不该写：风格上的禁区——No woman as born; No essence of femininity; No freedom without situation; No situation without freedom; No pity without analysis。
- Negative prompt: `No woman as born; No essence of femininity; No freedom without situation; No situation without freedom; No pity without analysis`

## (7) 测试提示词示例（现代题材：深夜便利店女店员）

- Prompt: `In the style of Simone de Beauvoir, describe a woman clerk on the night shift at a convenience store: her situation — the wage, the night, the male gaze of strangers — and her freedom within it, the Other made in small gestures, no essence, no pity without analysis.`
- 中文对照：波伏瓦风格：描述一位深夜便利店女店员——她的处境（工资、夜晚、陌生男性的目光）与处境中的自由，小姿态中造就的他者，没有女性本质，没有脱离分析的怜悯。
- Negative: `No woman as born, no essence of femininity, no freedom without situation, no pity without analysis`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
