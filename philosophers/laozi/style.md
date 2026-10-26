# Laozi — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Laozi: the dao that can be told is not the dao, reversal as method, water conquers stone, wu-wei as action, the sage hides his light`
- ZH: 老子风格：道可道，非常道，反者道之动，水胜石，无为而治，圣人藏其光。

## (2) 概念

- 道：不可言说、不可名状的本原
- 无为：不妄为，顺应自然而治
- 反：反者道之动，弱胜强、柔胜刚
- 水：至柔至善的象征

## (3) 论证结构

悖论—反转：先立一对立（有无、强弱、刚柔），再以‘反者道之动’反转其价值——弱者胜强者、无用者有用；论证不靠演绎，而靠悖论的顿悟与自然的例证（水、婴儿、木）。反例靠再反转化解——任何肯定都可再反转。

## (4) 修辞

格言体、韵文体；悖论、对仗、反问；善用自然意象（水、婴儿、谷、木）；语气玄远、平静、带反讽；与读者如隐者对求道者——不直说，只点拨。

## (5) 问题意识

人怎样才能不违背道？——无为、反转、像水一样。

## (6) 该写什么 / 不该写什么

- 该写：道不可言的开篇、有无强弱的反转、水与婴儿的意象、无为的收束。
- 不该写：体系化的定义、直线式的因果、积极有为的劝勉、对道的肯定描述。
- Negative prompt: `No systematic definitions, no linear causal argument, no exhortation to strive and achieve, no positive description of the dao`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Laozi, a person at a self-checkout notices one item was not scanned. The dao that can be told is not the dao, reversal as method, water conquers stone, wu-wei, no system, no positive description.`
- 中文对照：老子风格：自助结账机漏扫一件商品，该不该付款？道可道，非常道，反者道之动，水胜石，无为，不建体系，不给道下肯定定义。
- Negative: `No systematic definitions, no linear causal argument, no exhortation to strive and achieve, no positive description of the dao`
- 检验点：概念是否贴切；论证结构是否成立；修辞是否服务于论证而非独立成趣。
