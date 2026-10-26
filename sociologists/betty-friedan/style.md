# Betty Friedan — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Betty Friedan: 女性的奥秘, 女性问题, 第二阶段, 自我实现, 家务, precise definitions, no moralising conclusion without evidence`
- ZH: 贝蒂·弗里丹风格：女性的奥秘、女性问题、第二阶段、自我实现、家务，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：访谈调查 40% / 概念建构 30% / 批判分析 30%。`impression`
- 数据来源：家庭主妇访谈、心理学与社会学文献、媒体话语、妇女运动材料。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：女性的奥秘、女性问题、第二阶段、自我实现、家务、性别角色、选择。`impression`
- 定义方式：问题化定义：先命名一个无名的问题（“没有名字的问题”），定义即命名。`impression`
- 禁概念/禁方法：No feminine mystique as nature; No fulfilment without choice; No second stage without men; No problem without a name; No liberation as private escape。详见第 (6) 节。

## (4) 论证结构

- 结构：访谈原声切入 — 问题命名 — 制度批判 — 自我实现的论证 — 第二阶段的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：直率、动员性强，带美国公共写作的清晰；与读者保持同盟的距离。`impression`
- 与研究对象的距离：同盟的距离：与家庭主妇站在一起，向社会发问。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：没有名字的问题、家务的隐形劳动、自我实现、第二阶段的男女重组、选择的政治。
- 不该写：风格上的禁区——No feminine mystique as nature; No fulfilment without choice; No second stage without men; No problem without a name; No liberation as private escape。
- Negative prompt: `No feminine mystique as nature; No fulfilment without choice; No second stage without men; No problem without a name; No liberation as private escape`

## (7) 测试提示词示例（现代题材：全职妈妈重返职场）

- Prompt: `In the style of Betty Friedan, name the problem of a full-time mother returning to work: the feminine mystique that called her home, the invisible labour no CV records, the second stage where men must also change, fulfilment as choice, not escape.`
- 中文对照：弗里丹风格：为一位重返职场的全职妈妈命名她的问题——把她唤回家的女性的奥秘、简历上不记录的隐形劳动、男人也必须改变的第二阶段，自我实现是选择，不是逃离。
- Negative: `No feminine mystique as nature, no fulfilment without choice, no second stage without men, no problem without a name`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
