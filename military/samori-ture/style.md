# Samori Ture — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Samori Ture: professional army on the European model, three mobile columns, scorched earth when the capital falls, move the whole empire east rather than surrender it`
- ZH: 萨莫里风格：按欧洲模式建职业军，三路机动纵队，首都失守即坚壁清野，整个帝国向东迁移也不投降。

## (2) 情报与侦察

- 情报靠侦察与商队；对法军纵队与英国武器禁运的掌握决定了东迁的时机。`impression`

## (3) 地形与机动

- 地形偏好：萨凡纳与森林边缘；以机动纵队在开阔地与森林间转移。`artifact`

## (4) 后勤与补给

- 后勤靠帝国税收与塞拉利昂武器贸易；英国断供后勤后东迁即失去武器来源。`artifact`

## (5) 决断与节奏

- 决断：机动、坚壁、东迁；宁愿放弃首都也要保住军队与帝国。`impression`

## (6) 该打什么 / 不该打什么

- 该打：
- 以三路机动纵队绕敌补给线
- 坚壁清野，断敌就地取给
- 首都失守即东迁重建第二帝国
- 以职业军纪律约束部队
- 不该打：
- No defence of a fixed capital at the cost of the army
- No battle against French artillery in the open
- No war without modern firearms supply
- No halt after losing the capital
- Negative prompt: `No defence of a fixed capital at the cost of the army, No battle against French artillery in the open, No war without modern firearms supply, No halt after losing the capital`

## (7) 测试提示词示例（现代题材：一次现代城市防洪抢险的兵力部署）

- Prompt: `In the style of Samori Ture, plan the deployment of rescue forces for a modern city facing a major flood. Use three mobile columns, scorch the ground behind you so the flood cannot use it, and move the whole operation east to rebuild rather than surrendering the hub.`
- 中文对照：萨莫里风格：按欧洲模式建职业军，三路机动纵队，首都失守即坚壁清野，整个帝国向东迁移也不投降。以此风格筹划一次现代城市防洪抢险的兵力部署。
- Negative: `No defence of a fixed capital at the cost of the army, No battle against French artillery in the open, No war without modern firearms supply, No halt after losing the capital`
- 检验点：情报、地形、后勤、决断四项是否按本人的方式展开；禁区写法是否出现。
