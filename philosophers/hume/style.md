# David Hume — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of David Hume: impressions and ideas, custom not reason, scepticism with cheerfulness, elegant essayistic prose, no metaphysical dogma, no unexamined necessity`
- ZH: 休谟风格：印象与观念、习惯而非理性、愉快的怀疑主义、优雅的随笔散文、无形而上学独断、无未经审查的必然性。

## (2) 概念

- 印象与观念：观念是印象的微弱摹本
- 因果：恒常联结加习惯，非必然联系
- 自我：知觉的束，无固定自我
- 归纳问题：过去不能保证未来
- 同情：道德的基础

- 概念操作：新概念先定义、再区分、再举例、再以反例划界；概念边界模糊处是收紧还是保留张力，各家处理不同。`impression`

## (3) 论证结构

- 分解—追问—收束：先把概念分解为印象来源，找不到印象就宣布其为空洞；归纳问题上先承认理性无解，再以习惯与自然信念收束；论证以优雅的怀疑收尾，不以独断收尾。

## (4) 修辞

- 随笔体与对话体并用；长句优雅、节奏从容；爱用日常事例（台球、火与热）；语气愉快、温和，怀疑而不苦涩。

## (5) 问题意识

- 核心问题（一句话）：因果必然性从何而来？我们凭什么相信未来像过去？
- 问题来源：前人的未解处、时代的危机、概念的内在张力；他把问题推向何处，各家演变不同。`impression`

## (6) 该写什么 / 不该写什么

- 该写：
- 印象来源的追问
- 因果的习惯解释
- 归纳问题的提出
- 知觉束的自我观
- 愉快的怀疑收束
- 不该写：No necessary connection as observed fact, no metaphysical dogma, no rationalist deduction from pure reason, no moralising conclusion, no unexamined idea without an impression。
- Negative prompt: `No necessary connection as observed fact, no metaphysical dogma, no rationalist deduction from pure reason, no moralising conclusion, no unexamined idea without an impression`

## (7) 测试提示词示例（现代题材：自助结账机漏扫了一件商品，当事人是否该付款）

- Prompt: `In the style of David Hume, a person at a self-checkout machine notices one item was not scanned. impressions and ideas, custom not reason, scepticism with cheerfulness, elegant essayistic prose, no metaphysical dogma, no unexamined necessity`
- 中文对照：休谟风格：印象与观念、习惯而非理性、愉快的怀疑主义、优雅的随笔散文、无形而上学独断、无未经审查的必然性。自助结账机漏扫了一件商品，当事人是否该付款。
- Negative: `No necessary connection as observed fact, no metaphysical dogma, no rationalist deduction from pure reason, no moralising conclusion, no unexamined idea without an impression`
- 检验点：概念是否按本家方式引入；论证骨架是否成立；禁区写法是否出现。
