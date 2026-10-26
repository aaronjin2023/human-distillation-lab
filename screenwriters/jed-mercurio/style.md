# Jed Mercurio — 编剧风格规格 style.md（给文本模型）

> 只描述剧本，不描述人生。引用剧本时只引短句并注明出处，整段引用不超过合理篇幅。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Jed Mercurio: a procedural that never stops twisting, acronyms as armour, everyone lies, the interview room as a battlefield`
- ZH: 默丘里奥风格：永不停歇的反转程序剧，缩写即铠甲，人人撒谎，审讯室即战场。

## (2) 结构：三幕 / 序列 / 节拍

- 结构为季弧多线并行、反转驱动：《重任在肩》每季一个腐败调查，单集以审讯或行动收尾；季弧层层反转，时间跨度一季，闪回极少，靠信息差推进。

## (3) 对话

- 对白密集、专业，夹杂警局缩写与程序术语；人物用质问、沉默、谎言交锋，潜台词即生存规则。动作描写克制，审讯场景的对白是全剧的锚。旁白不用。

## (4) 人物弧光

- 主角多为反腐警察：黑斯廷斯、佛罗伦斯、凯特，弧光是坚持与妥协的拉锯；人物越查越深，结尾常是部分真相。人物关系以警队内部的忠诚与背叛为主。

## (5) 类型套路与创新

- 类型：程序剧 / 犯罪剧。遵守程序剧的考据，打破‘季终必有真相’的套路：真相只露一半。创新在把审讯写成战场，把缩写与程序写成人物铠甲。

## (6) 该写什么 / 不该写什么

- 该写：反转驱动的季弧、警局缩写与程序术语、审讯室作战场、人人撒谎、部分真相的结尾。
- 不该写：大团圆、直白说教、类型化破案桥段、全知旁白、主角突然黑化。
- Negative prompt: `No happy ending, no direct preaching, no procedural cliché, no omniscient narration, no sudden heel turn`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Jed Mercurio, a bomb disposal officer buys oden at a convenience store late at night. Her phone buzzes: a code word. An interview room waits. Everyone in the episode lies once. The truth arrives half-finished.`
- 中文对照：默丘里奥风格：一位拆弹警官深夜在便利店买关东煮。手机震动：一个暗号。审讯室在等她。本集每个人都撒了一次谎。真相只来了一半。
- Negative: `No happy ending, no direct preaching, no procedural cliché, no omniscient narration, no sudden heel turn`
- 检验点：风格是否成立；结构、对白、弧光是否按本 skill 落位；禁区是否未出现。
