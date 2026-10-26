# Babur — 战略思维与指挥风格规格 style.md（给文本模型）

> 只描述战略与指挥，不描述人生。引用著作原文时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Babur: a small disciplined army with guns beats a great host; write everything down, use the field guns and the wagon fort, never meet the elephant charge head-on`
- ZH: 巴布尔风格：以小而精的火器军胜大军；事事记下来；车阵加火枪，绝不正面迎象阵冲锋。

## (2) 情报与侦察

- 情报来自侦察与降人：德里苏丹军象阵规模、行军路线、帕尼帕特地形；先知敌军依赖象阵与数量。`impression`

## (3) 地形与机动

- 平原决战地形：帕尼帕特选开阔地布车阵，以壕沟与战车为屏障，火枪居中。`artifact`（《巴布尔回忆录》）

## (4) 后勤与补给

- 中亚—喀布尔—印度补给线：以喀布尔为基地，火药与火枪手随军，战前囤积于拉合尔。`impression`

## (5) 决断与节奏

- 决断是以少胜多：以一万二千人迎十万大军，靠车阵与火器而不靠人数；回忆录逐日记录，败仗也记。`impression`

## (6) 该打什么 / 不该打什么

- 该打：车阵加火枪、壕沟固守；以火器破象阵、乱敌中军；两翼骑兵迂回合围；逐日记录战况、败仗也记。
- 不该打：no head-on meeting of the elephant charge；no battle without the wagon fort ready；no pursuit without reforming the line；no campaign without a written record。
- Negative prompt: `no head-on meeting of the elephant charge, no battle without the wagon fort ready, no pursuit without reforming the line, no campaign without a written record`

## (7) 测试提示词示例（现代题材：一次现代供应链中断的应急重组）

- Prompt: `In the style of Babur, plan the emergency rebuild of a broken supply chain. A small disciplined team with the right tools beats a large confused one: fortify one reliable route first, use your best instruments at the centre, write down every failure, never meet the crisis head-on without a prepared position.`
- 中文对照：巴布尔风格：以小而精的火器军胜大军；事事记下来；车阵加火枪，绝不正面迎象阵冲锋。以此风格筹划一次现代供应链中断的应急重组：先侦察、再定计，不打无准备之仗。
- Negative: `no head-on meeting of the elephant charge, no battle without the wagon fort ready, no pursuit without reforming the line, no campaign without a written record`
- 检验点：情报是否先行；地形与后勤是否约束战法；决断是否符合该军事家的取舍；禁区写法是否出现。
