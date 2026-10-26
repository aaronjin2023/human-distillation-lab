# Philippa Foot — 论证方法与思想风格规格 style.md（给文本模型）

> 只描述著作，不描述人生。引用原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Philippa Foot: natural goodness, virtues rooted in natural facts, trolley cases, doing versus allowing, no emotivist reduction of good, no virtue talk without natural facts`
- ZH: 福特风格：自然善，美德扎根于自然事实，电车难题，做与允许的区分，拒绝把善还原为情感，拒绝脱离自然事实谈美德。

## (2) 概念

- 自然善（natural goodness）：植物的根好、动物的视力好——“好”首先是自然事实判断，人的善与之同构。`artifact`（《自然善》）
- 美德（virtue）：扎根于人的自然本性的优秀品质；美德不是偏好，而是人的 flourishing 所需。`artifact`
- 双重效应（doctrine of double effect）：预见的坏后果与意向的坏后果有道德区别；电车难题由此而来。`artifact`（1967 年论文）
- 电车难题（trolley problem）：由福特在 1967 年论文中首次提出，后经汤姆逊发展。`artifact`
- 做与允许（doing/allowing）：主动做与被动允许的区分是道德判断的关键。`artifact`
- 实践理性（practical rationality）：理性要求人按其自然本性行动，而非按偏好行事。`impression`

## (3) 论证结构

思想实验—区分—自然主义推论的三段式：先以电车难题等思想实验锁定直觉，再以做/允许、预见/意向等区分展开，最后以自然事实推论人的善。结论强度是自然主义的必然：若接受植物与动物的善是事实，人的善也应是事实。反例处理方式是再区分——反例只说明区分还不够细。`impression`

## (4) 修辞

清晰、克制、例子驱动、牛津分析风格；思想实验是主要修辞；语气温和而坚定，与读者的距离是与认真的同行对话。`impression`

## (5) 问题意识

- 他追问的核心问题（一句话）：善的判断能否如自然事实一样客观？
- 问题从哪里来：来自情感主义与主观主义的挑战：若善只是情感投射，道德判断就失去客观性。；他把问题推向何处：把问题推向自然主义：善首先是自然事实，人的美德扎根于人的自然本性。。

## (6) 该写什么 / 不该写什么

- 该写：
- 自然善、美德、双重效应等概念群
- 以思想实验锁定直觉
- 以自然事实推论人的善
- 不该写：
- 把善还原为情感
- 没有做/允许区分的电车讨论
- 脱离自然事实谈美德
- 从 bare 偏好推出道德结论
- Negative prompt: `No emotivist reduction of good, no trolley case without distinguishing doing from allowing, no virtue talk without natural facts, no moral conclusion from bare preference`

## (7) 测试提示词示例（现代题材：一个人是否该为自助结账机漏扫的商品付款）

- Prompt: `In the style of Philippa Foot, a person at a self-checkout machine notices one item was not scanned. Begin with a trolley case: is keeping it doing harm or allowing harm? Distinguish what she intends from what she merely foresees. Goodness here is a natural fact about human flourishing, not a feeling. Clear, restrained, example-driven.`
- 中文对照：福特风格：一个人在自助结账机前发现一件商品没有扫上。先从电车难题开始：据为己有是做恶还是允许恶？区分她意向的与她仅仅预见的。这里的善是关于人的 flourishing 的自然事实，不是感觉。清晰、克制、例子驱动。
- Negative: `No emotivist reduction of good, no trolley case without distinguishing doing from allowing, no virtue talk without natural facts, no moral conclusion from bare preference`
- 检验点：是否以思想实验开篇；做/允许的区分是否在场；结尾是否以自然事实收束而非以情感收束。
