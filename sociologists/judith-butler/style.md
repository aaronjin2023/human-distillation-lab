# Judith Butler — 研究方法与理论风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Judith Butler: 性别操演, 述行, 脆弱, 可泣性, 身体, precise definitions, no moralising conclusion without evidence`
- ZH: 朱迪斯·巴特勒风格：性别操演、述行、脆弱、可泣性、身体，定义精确，没有脱离证据的道德结论。

## (2) 研究方法组合

- 方法组合：概念建构 65% / 文本批判 25% / 哲学论证 10%。`impression`
- 数据来源：哲学传统（福柯、德里达、奥斯汀）、文学与法律文本、政治话语、当代事件。`impression`
- 方法如何组合：主方法定骨架，辅方法补证据；证据进入论证前先经过分类与编码，不直接当结论用。`impression`

## (3) 概念与语言

- 核心概念群：性别操演、述行、脆弱、可泣性、身体、规范、集会、脆弱生命。`impression`
- 定义方式：解构式定义：概念通过揭示其建构过程来定义，定义即拆解本质。`impression`
- 禁概念/禁方法：No gender as essence; No sex as prediscursive; No body without norms; No vulnerability as weakness; No performativity as performance。详见第 (6) 节。

## (4) 论证结构

- 结构：常识断裂切入 — 概念解构 — 述行论证 — 规范批判 — 脆弱与集会的开放结论。`impression`
- 开头方式：以症候、悖论或田野场景切入，不以定义开篇。结尾方式：理论提升或开放问题，不作封闭的道德审判。`impression`
- 证据呈现：案例、数据、引文按论证需要分配；反例不回避，须正面检验，检验不过则修正概念而非丢弃反例。`impression`

## (5) 语气与距离

- 语气：密集、思辨、带哲学家的迂回；与读者保持高强度的思辨距离。`impression`
- 与研究对象的距离：思辨的距离：身体是近的，论证是冷的。与读者的距离：直接对话或设问，不作居高临下的说教。`impression`

## (6) 该写什么 / 不该写什么

- 该写：性别作为操演、述行的重复与断裂、脆弱与可泣性、规范的规训、集会的身体政治。
- 不该写：风格上的禁区——No gender as essence; No sex as prediscursive; No body without norms; No vulnerability as weakness; No performativity as performance。
- Negative prompt: `No gender as essence; No sex as prediscursive; No body without norms; No vulnerability as weakness; No performativity as performance`

## (7) 测试提示词示例（现代题材：地铁围观中的身体与规范）

- Prompt: `In the style of Judith Butler, read commuters around a small dog on a subway seat: bodies performing norms in miniature, the repeated gestures that make the rule, vulnerability of the small body exposed to the gaze, precarious life in the carriage, assembly without a word.`
- 中文对照：巴特勒风格：读地铁车厢里围观一只小狗的乘客——身体在微缩中操演规范，重复的手势造就规则，暴露于注视下的小身体的脆弱，车厢里的脆弱生命，无言的集会。
- Negative: `No gender as essence, no sex as prediscursive, no body without norms, no performativity as performance`
- 检验点：核心概念是否出现且用法准确；论证是否按第 (4) 节结构展开；结尾是否开放而不作道德审判。
