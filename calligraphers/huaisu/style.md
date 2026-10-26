# Huaisu — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Huaisu: wild cursive, one continuous thread, circular turns like drifting silk, dry and wet ink in a single breath`
- ZH: 怀素风格：狂草一笔书，圆转连绵如游丝，枯润相间，一气呵成。

## (2) 笔法

- 中锋圆转，提按连绵；一笔书，笔画首尾相连，转折如游丝；枯笔与润笔相间，节奏一气呵成。`verbatim`（《自叙帖》摹本 / 争议真迹可见）
- 禁笔：他几乎不用的笔法——断笔的楷书结字、浓墨的滞重。

## (3) 结字与章法

- 结字大小参差，欹侧流转；章法行气连绵不绝，字行如游丝，疏密相间。`verbatim`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 墨色枯润相间，浓淡一幅之内多次转换；节奏连绵疾速，一气呵成。`verbatim`

## (5) 书体与取法

- 书体：狂草。唐狂草代表，与张旭并称“颠张醉素”；取法张旭而更圆转，后世狂草溯源于此。`impression`
- 演变：《自叙帖》真摹之争未定，无分期可言。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 一笔书的连绵圆转
- 如游丝般的牵丝
- 枯润相间的墨色
- 大小参差、欹侧流转的结字
- 一气呵成的疾速节奏
- 不该写：
- 断笔的楷书结字
- 浓墨的滞重
- 方折顿笔
- 端正划一
- 刻意装饰
- Negative prompt: `No disconnected regular-script characters, no heavy stagnant ink, no square turns, no uniform character size, no deliberate ornament`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Huaisu, wild cursive writing late night convenience store in Chinese characters, continuous flowing strokes, dry and wet ink contrast, circular turns, large empty space, one column, expressive`
- 中文对照：怀素风格：以狂草写“深夜便利店”条幅，笔画连绵圆转如游丝，枯润相间，一气呵成，留白疏朗。
- Negative: `No disconnected regular-script characters, no heavy stagnant ink, no square turns, no uniform character size, no deliberate ornament`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
