# Ouyang Xun — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Ouyang Xun: Tang regular script, steep and险峻, square turns, precise structure, danger resolved into stability`
- ZH: 欧阳询风格：唐楷险峻，方折分明，结字险中求稳，笔画精严。

## (2) 笔法

- 中锋方折，提按峻利；横画微仰，竖画挺劲；起笔藏锋而收笔分明，笔画如刀刻。`verbatim`（拓本可见）
- 禁笔：他几乎不用的笔法——狂草的连绵缠绕、圆转的柔媚。

## (3) 结字与章法

- 结字险中求稳：欹侧取势而重心不倒，左右结构紧收，中宫收紧而四肢开张。`verbatim`
- 幅式：碑刻竖列。

## (4) 墨色与节奏

- 拓本墨色浓黑，笔画精严；节奏一字一顿，方折处顿挫分明，庄重峻利。`verbatim`

## (5) 书体与取法

- 书体：楷书。初唐楷书四大家之一；取法北碑与二王而变之，后世楷法宗欧者众。`impression`
- 演变：传世皆为碑刻，无早中晚期墨迹可分；《九成宫》为晚年成熟之作，此说据碑刻年代，不作分期定论。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 险中求稳的欹侧结字
- 方折分明的峻利笔画
- 中宫收紧、四肢开张的结构
- 浓黑精严的拓本墨色
- 一字一顿的顿挫节奏
- 不该写：
- 狂草的连绵缠绕
- 圆转的柔媚
- 扁阔的汉隶波磔
- 秀媚活泼的笔意
- 浓艳装饰
- Negative prompt: `No cursive connections, no soft rounded turns, no clerical wave strokes, no slender delicate charm, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Ouyang Xun, Tang regular script carving modern Tokyo subway station names on a stone stele, steep daring structure resolved into stability, square turns, precise strokes, black rubbing ink`
- 中文对照：欧阳询风格：以唐楷刻现代东京地铁站名于碑，结字险中求稳，方折峻利，笔画精严。
- Negative: `No cursive connections, no soft rounded turns, no clerical wave strokes, no slender delicate charm, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
