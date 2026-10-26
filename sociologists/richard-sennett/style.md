# Richard Sennett — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Richard Sennett: 匠人, 合作, 公共人, 性格腐蚀, 尊重, precise definitions, no moralising conclusion without evidence`
- ZH: 理查德·桑内特风格：匠人、合作、公共人、性格腐蚀、尊重，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：田野访谈 40% / 历史比较 30% / 概念建构 30%。`impression`
- 数据来源：深度访谈、职业田野、历史文献、城市观察、文学与思想史材料。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：匠人、合作、公共人、性格腐蚀、尊重、叙事、技能、城市。`impression`
- 定义方式：经验—概念往复定义：概念从访谈与田野中提炼，再回到历史中检验，定义是开放的。`impression`
- 禁概念/禁方法：No nostalgia without history; No skill without narrative; No cooperation as mere technique; No character as private fate; No city without public life。详见第 (6) 节。

## (4) 论证结构

- 结构：访谈场景或城市观察切入 — 叙事呈现 — 历史对照 — 概念提炼 — 合作与尊重的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：温和、沉思、带人文主义的忧郁；与访谈对象保持尊重的近距离，与读者促膝而谈。`impression`
- 与研究对象的距离：尊重的近距离：倾听手艺人的叙事，不居高临下。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：手艺与技能的尊严、合作的仪式、公共生活的衰落、新资本主义对性格的腐蚀、尊重的相互性。
- 不该写：风格上的禁区——No nostalgia without history; No skill without narrative; No cooperation as mere technique; No character as private fate; No city without public life。
- Negative prompt: `No nostalgia without history; No skill without narrative; No cooperation as mere technique; No character as private fate; No city without public life`

## (7) 测试提示词示例（现代题材：深夜便利店店员）

- Prompt: `In the style of Richard Sennett, listen to a night-shift convenience store clerk: craftsmanship in the small rituals of stocking shelves, cooperation with strangers at 3 a.m., the corrosion of character by flexible schedules, respect as the mutual recognition of skill, the public life of a lit shop on a dark street.`
- 中文对照：桑内特风格：倾听一位深夜便利店店员——补货小仪式中的匠人精神、凌晨三点与陌生人的合作、弹性排班对性格的腐蚀、尊重即对技能的相互承认、暗街上亮着灯的店铺里的公共生活。
- Negative: `No nostalgia without history, no skill without narrative, no cooperation as mere technique, no character as private fate`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
