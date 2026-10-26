# Chu Suiliang — 书法风格规格 style.md（给图像模型）

> 只描述字，不描述人生。引用原帖时只引短句并注明出处。

## (1) 一句话风格（prompt-ready）

- EN: `In the style of Chu Suiliang: Tang regular script, slender and elegant, graceful turns, the most refined of the early Tang masters`
- ZH: 褚遂良风格：唐楷瘦劲清秀，转折灵动，为初唐四大家中最清秀一路。

## (2) 笔法

- 中锋为主，提按灵动；笔画瘦劲，起笔藏锋而收笔分明，转折圆转兼方，秀润而不弱。`verbatim`（拓本可见）
- 禁笔：他几乎不用的笔法——颜真卿的宽博厚重、欧阳询的险峻方折。

## (3) 结字与章法

- 结字瘦长清秀，欹侧灵动，左右结构开张而重心稳；章法行气疏朗秀润。`verbatim`
- 幅式：碑刻竖列。

## (4) 墨色与节奏

- 拓本墨色浓黑而笔画清秀；节奏从容灵动，一字一顿而气韵流动。`verbatim`

## (5) 书体与取法

- 书体：楷书、行书。初唐楷书四大家之一；师虞世南、欧阳询而变之，取法二王，后世学褚者众。`impression`
- 演变：传世皆为碑刻，无分期；《雁塔圣教序》为晚年成熟之作，此说据碑刻年代。`artifact`

## (6) 该写什么 / 不该写什么

- 该写：
- 瘦劲清秀的唐楷
- 灵动的转折
- 瘦长清秀的结字
- 疏朗秀润的章法
- 从容灵动的节奏
- 不该写：
- 颜真卿的宽博厚重
- 欧阳询的险峻方折
- 狂草的连绵
- 隶书的波磔
- 浓艳装饰
- Negative prompt: `No broad heavy strokes, no steep square turns, no wild-cursive tangling, no clerical wave strokes, no ornate decoration`

## (7) 测试提示词示例（现代题材）

- Prompt: `In the style of Chu Suiliang, Tang regular script carving modern Tokyo subway station names on a stone stele, slender elegant characters, graceful turns, calm refined spacing, black rubbing ink`
- 中文对照：褚遂良风格：以唐楷刻现代东京地铁站名于碑，结字瘦劲清秀，转折灵动，行列疏朗。
- Negative: `No broad heavy strokes, no steep square turns, no wild-cursive tangling, no clerical wave strokes, no ornate decoration`
- 检验点：笔法、结字、章法、墨色四项是否与上文一致；字形是否落入禁区清单。
