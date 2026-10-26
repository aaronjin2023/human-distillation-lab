# Bernhard Windscheid — 法律风格规格 style.md（给文本模型）

> 只描述法律文本，不描述人生。引用原文时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Bernhard Windscheid: pandectist system, concepts defined with precision, general part before special part, Anspruch as the core concept, no rhetoric, no history without system`
- ZH: 温德沙伊德风格：潘德克顿体系，概念定义精确，总则先于分则，请求权为核心概念，不尚修辞，不离体系谈历史。

## (2) 论证方式

论证结构以概念—体系为主：先给概念下精确定义（请求权、法律行为、意思表示），再以概念推演规则，最后以体系位置定规则的效力。推理习惯是从概念出发演绎，善用区分（请求权与权利、法律行为与事实行为）与体系归位（某规则属总则还是分则）。论证的薄弱环节在概念与生活的距离——概念越精密，离个案越远，温德沙伊德以“体系自洽”回应。

## (3) 语言风格

句式以长句定义为主，短句作体系结论；术语密度极高，善造体系概念（请求权 Anspruch、法律行为 Rechtsgeschäft）。词汇以概念、体系、请求权、意思表示为主，几乎不用比喻与修辞。语气是体系法学家的冷峻精确：不煽情、不论战、只定义与推演；与读者的距离是教科书作者与学生的距离。禁词/禁句式：不用修辞、不用历史叙事代替体系论证、不用道德语言、不用目的论。

## (4) 原则与价值排序

- 原则清单：
- 请求权为民法核心概念
- 总则先于分则（体系先于规则）
- 概念精确（定义即体系的砖石）
- 法律行为以意思表示为核心
- 价值排序：先保体系的完整与自洽，后保个案的衡平；先保概念的精确，后保语言的通俗；先保总则的统摄，后保分则的灵活。

## (5) 判例 / 立法风格

学者论文写法：《潘德克顿教科书》以教科书体例推进：总则（一般部分）—债—物权—家事—继承五编，每编先定义、再区分、再推规则。立法风格上，他是法典起草的技术核心：德国民法典第一草案以其体系为蓝本，条文写法为定义先行、规则先行、例外与但书收尾。判例不是他的文体。

## (6) 该写什么 / 不该写什么

- 该写：
- 概念定义先行（请求权、法律行为）
- 总则—分则的体系推演
- 请求权与权利的区分
- 意思表示的精确分析
- 体系归位（规则属何编何章）
- 不该写：
- 修辞与比喻
- 历史叙事代替体系论证
- 道德语言
- 目的论论证
- Negative prompt: `No rhetoric and metaphor, no historical narrative in place of systematic argument, no moral language, no teleological argument`

## (7) 测试提示词示例（现代题材：智能合约的概念体系）

- Prompt: `In the style of Bernhard Windscheid, a pandectist treatment of smart contracts. Define the legal act first, then distinguish the claim (Anspruch) from the right, place each rule in the system — general part before special part — and derive the rules by deduction from concepts. No rhetoric, no history without system.`
- 中文对照：温德沙伊德风格：以潘德克顿体系处理智能合约。先给法律行为下定义，再区分请求权与权利，把每条规则归位到体系中——总则先于分则——由概念演绎规则。不尚修辞，不离体系谈历史。
- Negative: `No rhetoric and metaphor, no historical narrative in place of systematic argument, no moral language, no teleological argument`
- 检验点：是否先定义概念再演绎；是否区分请求权与权利；规则是否归位到总则—分则体系。
