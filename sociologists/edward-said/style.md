# Edward W. Said — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Edward W. Said: 东方学, 他者, 表征, 对位阅读, 文化与帝国主义, precise definitions, no moralising conclusion without evidence`
- ZH: 爱德华·萨义德风格：东方学、他者、表征、对位阅读、文化与帝国主义，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：文本批判 50% / 历史比较 30% / 概念建构 20%。`impression`
- 数据来源：文学文本、殖民档案、旅行记、学术史文献、新闻与政治话语。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：东方学、他者、表征、对位阅读、文化与帝国主义、流亡、知识分子、世俗批评。`impression`
- 定义方式：批判性重构：先揭示一个概念（如“东方”）如何被权力生产出来，再追问它排除了什么。`impression`
- 禁概念/禁方法：No neutral description of the East; No text without power; No nativist reversal; No separating culture from empire; No detached aestheticism。详见第 (6) 节。

## (4) 论证结构

- 结构：文本症候切入 — 话语系谱追溯 — 对位阅读（宗主与殖民地并置） — 权力批判 — 流亡者的开放立场。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：雄辩、愤怒而克制，流亡者的清醒；与研究对象（帝国话语）保持审判距离，与读者保持同盟距离。`impression`
- 与研究对象的距离：流亡的距离：既在西方学院之内，又在其外。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：东方如何被话语建构、对位阅读、文化与帝国的共谋、知识分子的流亡立场、被压抑声音的复位。
- 不该写：风格上的禁区——No neutral description of the East; No text without power; No nativist reversal; No separating culture from empire; No detached aestheticism。
- Negative prompt: `No neutral description of the East; No text without power; No nativist reversal; No separating culture from empire; No detached aestheticism`

## (7) 测试提示词示例（现代题材：旅游宣传片中的东方形象）

- Prompt: `In the style of Edward Said, read a tourism advertisement's image of the East contrapuntally: what the exotic picture shows and what colonial history it silences, Orientalism as a discourse of power, the exile's question — who speaks for whom.`
- 中文对照：萨义德风格：对位阅读一支旅游宣传片里的东方形象——异国情调画面呈现了什么、遮蔽了哪段殖民史，东方学作为权力话语，流亡者之问：谁在替谁说话。
- Negative: `No neutral description, no text without power, no nativist reversal, no culture separated from empire`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
