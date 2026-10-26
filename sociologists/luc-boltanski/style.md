# Luc Boltanski — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Luc Boltanski: 辩护, 价值秩序, 批判社会学, 批判的社会学, 苦难, precise definitions, no moralising conclusion without evidence`
- ZH: 吕克·博尔坦斯基风格：辩护、价值秩序、批判社会学、批判的社会学、苦难，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：田野访谈 40% / 概念建构 40% / 历史比较 20%。`impression`
- 数据来源：争议与辩护的访谈记录、田野观察、管理文献、企业与媒体话语。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：辩护、价值秩序、批判社会学、批判的社会学、苦难、资本主义新精神、检验、行动者能力。`impression`
- 定义方式：行动者中心定义：概念从行动者实际使用的辩护语汇中提炼，拒绝社会学家的外部强加。`impression`
- 禁概念/禁方法：No critique from above; No actors without competence; No justification without a common good; No capitalism without its spirit; No sociology that silences actors。详见第 (6) 节。

## (4) 论证结构

- 结构：争议场景切入 — 辩护语汇记录 — 价值秩序辨析 — 检验分析 — 批判能力的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：细致、耐心、带法国实用社会学的冷静；与读者保持跟随行动者的距离。`impression`
- 与研究对象的距离：跟随的近距离：相信普通人会做社会学。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：争议中的辩护、价值秩序的冲突、检验的成败、批判的社会学、苦难的表达。
- 不该写：风格上的禁区——No critique from above; No actors without competence; No justification without a common good; No capitalism without its spirit; No sociology that silences actors。
- Negative prompt: `No critique from above; No actors without competence; No justification without a common good; No capitalism without its spirit; No sociology that silences actors`

## (7) 测试提示词示例（现代题材：直播带货翻车后的公开辩护）

- Prompt: `In the style of Luc Boltanski, follow a livestream scandal's public justifications: the host, the brand and the viewers each appeal to a different order of worth, tests succeed or fail, the sociology of critique watches ordinary people do sociology, no verdict from above.`
- 中文对照：博尔坦斯基风格：跟随一场直播翻车后的公开辩护——主播、品牌与观众各自诉诸不同的价值秩序，检验或成或败，批判的社会学看普通人如何做社会学，不作居高临下的裁决。
- Negative: `No critique from above, no actors without competence, no justification without a common good, no sociology that silences actors`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
