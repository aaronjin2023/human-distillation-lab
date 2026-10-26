# Zhong Yao — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Zhong Yao: early regular script, flat and wide characters, restrained turns, the quiet ancestor of all later kai`
- ZH: 钟繇风格：早期楷书，结字扁阔，提按含蓄，为后世楷法之祖。

## (2) 笔法

- 楷书初成之笔：由隶入楷，波磔收敛为顿笔；提按含蓄，转折多圆少方，起收藏锋。`impression`（摹本与楷书演变通说）
- 禁笔：他几乎不用的笔法——成熟唐楷的方折峻利、隶书的波磔挑法。

## (3) 结字与章法

- 结字扁阔，横向取势，左右结构开张；字形平稳端正，欹侧极少。`impression`
- 幅式：卷 / 尺牍 / 册页，横卷为主，行列疏朗。

## (4) 墨色与节奏

- 摹本墨色不可据为原墨；节奏缓慢稳重，一字一顿，绝无连带。`artifact`

## (5) 书体与取法

- 书体：楷书（楷书之祖）。被称为“楷书之祖”；由汉隶脱化出楷书，王羲之父子楷法溯源于此。`impression`
- 演变：真迹已佚，无分期；《宣示表》等摹本风格一致，皆属后世摹写层。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 早期楷书的扁阔结字
- 含蓄的提按与圆转
- 藏锋起收，一字一顿
- 平稳端正、欹侧极少的字形
- 缓慢稳重的书写节奏
- 不该写：
- 成熟唐楷的方折峻利
- 隶书的波磔挑法
- 行草的连绵牵丝
- 险绝欹侧的取势
- 浓艳装饰
- Negative prompt: `No sharp Tang regular-script square turns, no clerical wave strokes, no running or cursive connections, no daring slanted compositions, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Zhong Yao, early regular script writing modern Tokyo subway station names, flat wide characters, restrained turns, quiet dignity, one deliberate pause per character, ink on paper`
- 中文对照：钟繇风格：以早期楷书写现代东京地铁站名，结字扁阔，提按含蓄，一字一顿，安静端正。
- Negative: `No sharp Tang regular-script square turns, no clerical wave strokes, no running or cursive connections, no daring slanted compositions, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
