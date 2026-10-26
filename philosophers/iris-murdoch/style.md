# Iris Murdoch — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Iris Murdoch: attention, the sovereignty of Good, unselfing, moral vision, no will-centred morality, no linguistic analysis that dissolves the Good`
- ZH: 默多克风格：注意，善的主权，自我消解，道德视域，拒绝以意志为中心的道德，拒绝用语言分析消解善。

## (2) 概念

- 注意（attention）：如实地看，是道德的起点；注意是慷慨而艰难的看。`artifact`（《主权善》）
- 善的主权（sovereignty of Good）：善是道德生活的实在中心，超越一切语言分析。`artifact`
- 自我消解（unselfing）：道德进步首先是自我的退位，而非意志的胜利。`artifact`
- 道德视域（moral vision）：人看到什么，决定了他能做什么；视域先于选择。`artifact`
- 幻想（fantasy）与现实：自我编织的幻想遮蔽现实；道德就是撕开幻想、如实地看。`artifact`
- 爱作为认识：爱不是情感，而是如实认识他者的方式。`impression`

## (3) 论证结构

小说式例子—概念重划—柏拉图式上升的三段式：先讲一个日常例子（婆婆如何重新看待儿媳），再以注意、幻想等概念重划道德问题，最后上升到善的主权。结论强度是视域性的：不是“应当如何”，而是“你看到了什么”。反例处理方式是再看一次——反例只说明看得还不够如实。`impression`

## (4) 修辞

文学化、意象、“看”的隐喻贯穿全书；语气温和而坚定，与读者的距离是邀你一起看，而非向你下命令。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：道德如何始于如实地看，而不是意志的胜利？
- 问题从哪里来：来自分析道德哲学的困境：语言分析与意志中心论都错失了道德生活的实在内容。；他把问题推向何处：把问题推向柏拉图式的善：道德哲学的中心不是选择，而是视域与注意。。

## (6) 该写什么 / 不该写什么

- 该写：
- 注意、善、自我消解、道德视域等概念群
- 以日常例子开篇，再重划概念
- 以善的主权收束
- 不该写：
- 以意志为中心的道德
- 没有注意的道德哲学
- 用语言分析消解善
- 安慰性的幻想
- Negative prompt: `No will-centred morality, no moral philosophy without attention, no linguistic analysis that dissolves the Good, no consoling fantasy`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Iris Murdoch, a person at a self-checkout machine notices one item was not scanned. Do not begin with rules or willpower. Begin with attention: truly see the cashier, the other shoppers, the labour behind the goods. The mother-in-law who learns to see her daughter-in-law justly — that is the whole of morality. Unselfing, not will. The Good, not the rule.`
- 中文对照：默多克风格：一个人在自助结账机前发现一件商品没有扫上。不要从规则或意志力开始，而从注意开始：真正看见收银员、其他顾客、商品背后的劳动。那位学会公正地看待儿媳的婆婆——那就是道德的全部。自我消解，不是意志。善，不是规则。
- Negative: `No will-centred morality, no moral philosophy without attention, no linguistic analysis that dissolves the Good, no consoling fantasy`
- 检验点：是否以注意开篇而非以规则开篇；“看”的隐喻是否在场；结尾是否指向善而非指向意志的胜利。
