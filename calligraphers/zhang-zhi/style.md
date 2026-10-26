# Zhang Zhi — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhang Zhi: early cursive script, brisk abbreviated strokes, characters still separable, the bridge from clerical to cursive`
- ZH: 张芝风格：早期草书，简省疾书而字字可辨，隶草之间的桥梁。

## (2) 笔法

- 草书初成之笔：隶书波磔渐省，笔画简省连带初现；转折圆转，起收仍见隶意。`impression`（摹本与草书演变通说）
- 禁笔：他几乎不用的笔法——成熟今草的连绵缠绕、楷书的方折顿笔。

## (3) 结字与章法

- 结字仍近隶书扁阔，但笔画省减、字形欹侧初现；字与字之间偶有牵丝，尚未连绵。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 摹本墨色浓淡不一，不可据为作者原墨；节奏疾速简省，一字数笔而就。`artifact`

## (5) 书体与取法

- 书体：草书（章草、今草之祖）。被称为“草圣”，今草之祖；由章草脱隶入草，后世王羲之草书溯源于此。`impression`
- 演变：真迹已佚，无分期可言；所谓早期与晚期皆据摹本推测，不作定论。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 简省的草书笔画，隶意未尽脱
- 字字可辨、尚未连绵的字形
- 欹侧初现的结字
- 疾速简省的书写节奏
- 圆转的转折
- 不该写：
- 成熟今草的连绵缠绕
- 楷书的方折顿笔
- 隶书完整的波磔
- 狂草的放纵
- 浓艳装饰
- Negative prompt: `No continuous wild-cursive tangling, no regular-script square turns, no full clerical wave strokes, no unrestrained狂草 flourishes, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Zhang Zhi, early cursive script writing modern Tokyo subway station names, brisk abbreviated strokes, characters still separable, a bridge from clerical to cursive, fluid ink on paper`
- 中文对照：张芝风格：以早期草书写现代东京地铁站名，笔画简省疾书，字字可辨，隶意未尽，节奏明快。
- Negative: `No continuous wild-cursive tangling, no regular-script square turns, no full clerical wave strokes, no unrestrained狂草 flourishes, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
